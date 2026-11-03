-- Lua 5.1 regression test for pfQuest-CoA's WoW 3.3.5a channel receive path.
local function newFrame()
  local f = { events = {}, scripts = {} }
  function f:RegisterEvent(name) self.events[name] = true end
  function f:SetScript(name, fn) self.scripts[name] = fn end
  function f:CreateFontString() return setmetatable({}, {__index=function() return function() end end}) end
  function f:SetPoint() end
  function f:SetWidth() end
  function f:SetHeight() end
  function f:SetText() end
  function f:SetChecked() end
  function f:GetChecked() return false end
  function f:CreateTexture() return setmetatable({}, {__index=function() return function() end end}) end
  return f
end
local frames = {}
CreateFrame = function()
  local f = newFrame()
  frames[#frames + 1] = f
  return f
end
local frame
SlashCmdList = {}
local now = 100
GetTime = function() return now end
GetChannelName = function(name) assert(name == "CoASync"); return 6, "CoASync" end
GetChannelList = function() return 6, "CoASync" end
UnitName = function() return "LocalPlayer" end
GetRealmName = function() return "LocalRealm" end
date = function() return "00:00:00" end
time = function() return 100 end
math.randomseed(1)
UnitAffectingCombat = function() return false end
GetFramerate = function() return 60 end
GetNumQuestLogEntries = function() return 0 end
local sent = {}
SendChatMessage = function(message, _, _, channel)
  assert(channel == 6, "bootstrap HELLO used the wrong channel number")
  sent[#sent + 1] = message
end

local source = arg[1] or "build/staging/pfQuest/coa_sync.lua"
dofile(source)
frame = frames[1]
local onEvent = assert(frame.scripts.OnEvent, "coa_sync.lua did not register OnEvent")
onEvent(frame, "PLAYER_LOGIN")

local hello = "PFQ6:H:pfQuest-CoA-v4:12"
local function message(sender, display, index, base)
  onEvent(frame, "CHAT_MSG_CHANNEL", hello, sender, "COMMON", display, nil, nil, nil, index, base)
end

message("PeerOne-Realm", "6. CoASync", 6, "CoASync")
assert(pfQuestCoA_Learned.received == 1, "valid decorated CoASync message was not counted")
assert(pfQuestCoA_Learned.peers["PeerOne-Realm"] ~= nil, "valid sender was not recorded as a peer")

message("PeerTwo-Realm", "CoASync", 6, "CoASync")
assert(pfQuestCoA_Learned.received == 2, "valid plain CoASync message was not counted")
assert(pfQuestCoA_Learned.peers["PeerTwo-Realm"] ~= nil, "plain-name sender was not recorded as a peer")

message("WrongName-Realm", "6. General", 6, "General")
message("WrongIndex-Realm", "7. CoASync", 7, "CoASync")
message("MissingIndex-Realm", "6. CoASync", nil, "CoASync")
assert(pfQuestCoA_Learned.received == 2, "invalid channel identity was accepted")
assert(pfQuestCoA_Learned.peers["WrongName-Realm"] == nil, "wrong channel created a peer")
assert(pfQuestCoA_Learned.peers["WrongIndex-Realm"] == nil, "wrong local number created a peer")
assert(pfQuestCoA_Learned.peers["MissingIndex-Realm"] == nil, "missing local number created a peer")

-- A fresh client has no peers. It must still send HELLO or two fresh clients
-- can never discover one another (the previous implementation deadlocked).
pfQuestCoA_Learned.peers = {}
now = 140
frame.scripts.OnUpdate(frame, 0.25)
assert(#sent > 0 and sent[1]:match("^PFQ6:H:pfQuest%-CoA%-v4:"), "solo client did not send its bootstrap HELLO")

-- Quest lifecycle categories must remain separate natural identifiers.
assert(pfQuestCoA_RecordDiscovery("Q", 70001), "quest-accepted record was not stored")
assert(pfQuestCoA_RecordDiscovery("C", 70001), "quest-complete record collided with accepted record")
assert(pfQuestCoA_Learned.records["Q:70001"] and pfQuestCoA_Learned.records["C:70001"], "category-specific quest IDs were not preserved")
print("pfQuest-CoA channel receive regression passed: valid messages counted; invalid channel identities ignored.")
