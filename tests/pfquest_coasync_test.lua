-- Lua 5.1 regression test for pfQuest-CoA's WoW 3.3.5a channel receive path.
local frame = { events = {}, scripts = {} }
function frame:RegisterEvent(name) self.events[name] = true end
function frame:SetScript(name, fn) self.scripts[name] = fn end
CreateFrame = function() return frame end
GetTime = function() return 100 end
GetChannelName = function(name) assert(name == "CoASync"); return 6, "CoASync" end
GetChannelList = function() return 6, "CoASync" end
UnitName = function() return "LocalPlayer" end
GetRealmName = function() return "LocalRealm" end
date = function() return "00:00:00" end
time = function() return 100 end

local source = arg[1] or "build/staging/pfQuest/coa_sync.lua"
dofile(source)
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
print("pfQuest-CoA channel receive regression passed: valid messages counted; invalid channel identities ignored.")
