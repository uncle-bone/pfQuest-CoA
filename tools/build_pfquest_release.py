#!/usr/bin/env python3
"""Rebuild pfQuest-CoA from its verified stable source ZIP plus local patches."""
from __future__ import annotations

import hashlib
import json
import pathlib
import re
import shutil
import urllib.request
import zipfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
CFG = json.loads((ROOT / ".release.json").read_text(encoding="utf-8"))
VERSION = CFG["version"]
STAGING = ROOT / "build" / "staging"
DIST = ROOT / "dist"


def replace_exact(path: pathlib.Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8-sig")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one patch target in {path}, found {count}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8", newline="")


def main() -> None:
    STAGING.mkdir(parents=True, exist_ok=True)
    DIST.mkdir(parents=True, exist_ok=True)
    source_zip = ROOT / "build" / "source.zip"
    urllib.request.urlretrieve(CFG["source_url"], source_zip)
    actual = hashlib.sha256(source_zip.read_bytes()).hexdigest()
    if actual.lower() != CFG["source_sha256"].lower():
        raise RuntimeError(f"Source ZIP checksum mismatch: {actual}")

    if STAGING.exists():
        shutil.rmtree(STAGING)
    STAGING.mkdir(parents=True)
    with zipfile.ZipFile(source_zip) as archive:
        for info in archive.infolist():
            target = (STAGING / info.filename).resolve()
            if STAGING.resolve() not in target.parents and target != STAGING.resolve():
                raise RuntimeError(f"Unsafe archive path: {info.filename}")
        if archive.testzip() is not None:
            raise RuntimeError("Source ZIP integrity check failed")
        archive.extractall(STAGING)

    sync = STAGING / "pfQuest" / "coa_sync.lua"
    replace_exact(
        sync,
        """ elseif event=='CHAT_MSG_CHANNEL' then
  local msg,sender,_,_,_,_,_,chIndex,chName=...
  if journal and channel and (tonumber(chIndex)==channel or (type(chName)=='string' and (chName:lower()=='coasync' or chName:lower():match('^%d+%. coasync$')))) then receive(msg,sender) end""",
        """ elseif event=='CHAT_MSG_CHANNEL' then
  local msg,sender,_,channelDisplay,_,_,_,chIndex,channelBaseName=...
  local function matchesChannelName(name)
   if type(name)~='string' then return false end
   name=name:gsub('^%s+',''):gsub('%s+$','')
   name=name:gsub('^%d+%.%s*','')
   return name:lower()==CHANNEL:lower()
  end
  local receivedIndex=tonumber(chIndex)
  if journal and channel and receivedIndex==channel and (matchesChannelName(channelBaseName) or matchesChannelName(channelDisplay)) then receive(msg,sender) end""",
    )
    replace_exact(
        sync,
        " if not channel or not journal.sharing then return false end\n if stats.peers==0 then return false end",
        " if not channel or not journal.sharing then return false end\n if stats.peers==0 and payload:sub(1,2)~='H|' then return false end",
    )
    replace_exact(
        sync,
        " if t-lastSend<10 or not channel or not journal.sharing or stats.peers==0 then return end",
        " if t-lastSend<10 or not channel or not journal.sharing then return end",
    )
    replace_exact(
        sync,
        "  -- Solo clients remain silent: no Hello or bucket broadcasts without peers.\n  nextHello=t+600+math.random(1,120)\n  if stats.peers>0 then send('H|'..BASE..'|'..(keys and #keys or 0));lastSend=t end",
        "  -- Send periodic HELLO even with no known peers so matching clients can bootstrap.\n  nextHello=t+600+math.random(1,120)\n  if send('H|'..BASE..'|'..(keys and #keys or 0)) then lastSend=t end",
    )
    replace_exact(
        sync,
        " elseif #queue>0 then\n  local item=table.remove(queue,1);queued[item.key]=nil;send(item.payload);lastSend=t",
        " elseif #queue>0 and stats.peers>0 then\n  local item=table.remove(queue,1);queued[item.key]=nil;send(item.payload);lastSend=t",
    )
    replace_exact(
        sync,
        "  local n=math.min(tonumber(GetNumQuestLogEntries()) or 0,100)",
        "  local questCount=GetNumQuestLogEntries()\n  local n=math.min(tonumber(questCount) or 0,100)",
    )
    version_label = VERSION.removeprefix("v")
    replace_exact(
        sync,
        "title:SetPoint('TOP',gui,'TOP',0,-18);title:SetText('pfQuest-CoA v1.0.15 | CoASync')",
        f"title:SetPoint('TOP',gui,'TOP',0,-18);title:SetText('pfQuest-CoA v{version_label} | CoASync')",
    )
    replace_exact(
        sync,
        "title:SetPoint('TOPLEFT',self,'TOPLEFT',16,-16);title:SetText('pfQuest-CoA v1.0.15 - CoASync sharing')",
        f"title:SetPoint('TOPLEFT',self,'TOPLEFT',16,-16);title:SetText('pfQuest-CoA v{version_label} - CoASync sharing')",
    )
    sync_text = sync.read_text(encoding="utf-8-sig")
    if f"pfQuest-CoA v{version_label}" not in sync_text or "pfQuest-CoA v1.0.15" in sync_text:
        raise RuntimeError("CoASync pane title version labels were not updated")

    for folder in CFG["folders"]:
        addon = STAGING / folder
        if not addon.is_dir():
            raise RuntimeError(f"Missing addon folder: {folder}")
        tocs = list(addon.glob("*.toc"))
        if not tocs:
            raise RuntimeError(f"Missing TOC: {folder}")
        for toc in tocs:
            text = toc.read_text(encoding="utf-8-sig")
            text, count = re.subn(
                r"(?m)^## Version: .*$",
                f"## Version: {VERSION.removeprefix('v')}",
                text,
            )
            if count:
                toc.write_text(text, encoding="utf-8", newline="")
            for raw in text.splitlines():
                line = raw.strip()
                if not line or line.startswith("#"):
                    continue
                if not (addon / line.replace("\\", "/")).is_file():
                    raise RuntimeError(f"Missing TOC reference: {toc}: {line}")

    output = DIST / f"pfQuest-CoA-{VERSION}.zip"
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for folder in CFG["folders"]:
            for path in sorted((STAGING / folder).rglob("*")):
                if path.is_file() and path.name not in (".DS_Store", "Thumbs.db"):
                    archive.write(path, path.relative_to(STAGING).as_posix())
    with zipfile.ZipFile(output) as archive:
        if archive.testzip() is not None:
            raise RuntimeError("Built ZIP integrity check failed")
        names = archive.namelist()
        for folder in CFG["folders"]:
            if not any(name.startswith(folder + "/") for name in names):
                raise RuntimeError(f"Built ZIP is missing {folder}/")
    print(
        f"Built {output} ({output.stat().st_size} bytes), "
        f"SHA-256 {hashlib.sha256(output.read_bytes()).hexdigest()}"
    )


if __name__ == "__main__":
    main()
