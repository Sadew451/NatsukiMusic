# EzilaXMusic (Telegram bot project )
# Copyright (C) 2021  Sadew Jayasekara

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
from EzilaXMusicV1.config import SOURCE_CODE
from EzilaXMusicV1.config import ASSISTANT_NAME
from EzilaXMusicV1.config import PROJECT_NAME
from EzilaXMusicV1.config import SUPPORT_GROUP
from EzilaXMusicV1.config import UPDATES_CHANNEL
class Messages():
      START_MSG = "**❤️ 𝙃𝙚𝙡𝙡𝙤 ❤️ 👋 [{}](tg://user?id={})!**\n\n🤖 𝓘 𝓪𝓶 𝓪𝓷 𝓪𝓭𝓿𝓪𝓷𝓬𝓮𝓭 𝓫𝓸𝓽 𝓬𝓻𝓮𝓪𝓽𝓮𝓭 𝓯𝓸𝓻 𝓹𝓵𝓪𝔂𝓲𝓷𝓰 𝓶𝓾𝓼𝓲𝓬 𝓲𝓷 𝓽𝓱𝓮 𝓿𝓸𝓲𝓬𝓮 𝓬𝓱𝓪𝓽𝓼 𝓸𝓯 𝓣𝓮𝓵𝓮𝓰𝓻𝓪𝓶 𝓖𝓻𝓸𝓾𝓹𝓼 & 𝓒𝓱𝓪𝓷𝓷𝓮𝓵𝓼❤️.\n\n✅ 𝓢𝓮𝓷𝓭 𝓶𝓮 /help 𝓯𝓸𝓻 𝓶𝓸𝓻𝓮 𝓲𝓷𝓯𝓸
."
      HELP_MSG = [
        ".",
f"""
**ℍ𝕖𝕪 👋 𝕎𝕖𝕝𝕔𝕠𝕞𝕖 𝕓𝕒𝕔𝕜 𝕥𝕠 {PROJECT_NAME}

⚪️ {PROJECT_NAME} c𝕒𝕟 𝕡𝕝𝕒𝕪 𝕞𝕦𝕤𝕚𝕔 𝕚𝕟 𝕪𝕠𝕦𝕣 𝕘𝕣𝕠𝕦𝕡'𝕤 𝕧𝕠𝕚𝕔𝕖 𝕔𝕙𝕒𝕥 𝕒𝕤 𝕨𝕖𝕝𝕝 𝕒𝕤 𝕔𝕙𝕒𝕟𝕟𝕖𝕝 𝕧𝕠𝕚𝕔𝕖 𝕔𝕙𝕒𝕥𝕤

⚪️ 𝔸𝕤𝕤𝕚𝕤𝕥𝕒𝕟𝕥 𝕟𝕒𝕞𝕖>> @{ASSISTANT_NAME}\n\nℂ𝕝𝕚𝕔𝕜 𝕟𝕖𝕩𝕥 𝕗𝕠𝕣 𝕚𝕟𝕤𝕥𝕣𝕦𝕔𝕥𝕚𝕠𝕟𝕤**
""",

f"""
**Setting up**

1) Make bot admin (Group and in channel if use cplay)
2) Start a voice chat
3) Try /play [song name] for the first time by an admin
*) If userbot joined enjoy music, If not add @{ASSISTANT_NAME} to your group and retry

**For Channel Music Play**
1) Make me admin of your channel 
2) Send /userbotjoinchannel in linked group
3) Now send commands in linked group

**Commands**

**=>> Song Playing 🎧**

- /play: Play the requestd song
- /play [yt url] : Play the given yt url
- /play [reply yo audio]: Play replied audio
- /dplay: Play song via deezer
- /splay: Play song via jio saavn
- /ytplay: Directly play song via Youtube Music

**=>> Playback ⏯**

- /player: Open Settings menu of player
- /skip: Skips the current track
- /pause: Pause track
- /resume: Resumes the paused track
- /end: Stops media playback
- /current: Shows the current Playing track
- /playlist: Shows playlist

*Player cmd and all other cmds except /play, /current  and /playlist  are only for admins of the group.
""",
        
f"""
**=>> Channel Music Play 🛠**

⚪️ For linked group admins only:

- /cplay [song name] - play song you requested
- /cdplay [song name] - play song you requested via deezer
- /csplay [song name] - play song you requested via jio saavn
- /cplaylist - Show now playing list
- /cccurrent - Show now playing
- /cplayer - open music player settings panel
- /cpause - pause song play
- /cresume - resume song play
- /cskip - play next song
- /cend - stop music play
- /userbotjoinchannel - invite assistant to your chat

channel is also can be used instead of c ( /cplay = /channelplay )

⚪️ If you donlt like to play in linked group:

1) Get your channel ID.
2) Create a group with tittle: Channel Music: your_channel_id
3) Add bot as Channel admin with full perms
4) Add @{ASSISTANT_NAME} to the channel as an admin.
5) Simply send commands in your group.
""",

f"""
**=>> More tools 🧑‍🔧**

- /musicplayer [on/off]: Enable/Disable Music player
- /admincache: Updates admin info of your group. Try if bot isn't recognize admin
- /userbotjoin: Invite @{ASSISTANT_NAME} Userbot to your chat

**=>> Commands for Sudo Users ⚔️**

 - /userbotleaveall - remove assistant from all chats
 - /gcast <reply to message> - globally brodcast replied message to all chats
 - /pmpermit [on/off] - enable/disable pmpermit message
*Sudo Users can execute any command in any groups

"""
      ]
