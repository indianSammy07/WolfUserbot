import os
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd, get_readable_time as grt
from platform import python_version, uname
import time
from userbot import UpTime
from telethon import events, version

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet."
ALIVE_PIC = os.environ.get("ALIVE_PIC", None)
PLUSPIC = ALIVE_PIC

def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time
@borg.on(admin_cmd(pattern="alive"))
async def iamalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = alive.message
    uptime = grt((time.time() - UpTime))
    if alive.reply_to_msg_id:
        reply_to_id = await alive.get_reply_message()
        
    if PLUSPIC:
    	ALIVE = f"**MADE IN 🇮🇳 , MADE FOR 🐺** \n\n`◾ Telethon :` **{version.__version__}** \n`🔹 Python:` **{python_version()}** \n`🔸 Fork by:` @WolfUserBotOT \n`🔹 Bot creator:` [//•Wolf•UserBot•//](tg://user?id=1499383735)\n`🔸 Plus+ Uptime:` **{uptime}** \n`🔹 My owner:` **{DEFAULTUSER}**  \n`🔸 Join` @RkProjects `For Help` \n\n                      [Deploy✔️](https://heroku.com/deploy?template=https://github.com/indianSammy07/WolfUserbot)  \n\n   "
    	await borg.send_file(alive.chat_id, PLUSPIC, caption=ALIVE)
    	await alive.delete()
    else:
    	ALIVE = f"**MADE IN 🇮🇳 , MADE FOR 🐺** \n\n`◽ Telethon :` **{version.__version__}** \n`🔹 Python:` **{python_version()}** \n`🔸 Fork by:` @WolfUserBotOT \n`🔹 Bot creator:` [//•Wolf•UserBot•//](tg://user?id=1499383735)\n`🔸 Plus+ Uptime:` **{uptime}** \n`🔹 My owner:` **{DEFAULTUSER}**  \n`🔸 Join` @RkProjects `For Help` \n\n                      [Deploy✔️](https://heroku.com/deploy?template=https://github.com/indianSammy07/WolfUserbot)  \n\n   "
    	await alive.edit(f"{ALIVE}")

@borg.on(admin_cmd(pattern="sudoalive", allow_sudo=True))
async def iamalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = alive.message
    uptime = grt((time.time() - UpTime))
    if alive.reply_to_msg_id:
        reply_to_id = await alive.get_reply_message()
        
    if PLUSPIC:
    	ALIVE = f"**MADE IN 🇮🇳 , MADE FOR 🐺** \n\n`◾ Telethon :` **{version.__version__}** \n`🔹 Python:` **{python_version()}** \n`🔸 Fork by:` @WolfUserBotOT \n`🔹 Bot creator:` [//•Wolf•UserBot•//](tg://user?id=1499383735)\n`🔸 Plus+ Uptime:` **{uptime}** \n`🔹 My owner:` **{DEFAULTUSER}**  \n`🔸 Join` @RkProjects `For Help` \n\n                      [Deploy✔️](https://heroku.com/deploy?template=https://github.com/indianSammy07/WolfUserbot)  \n\n   "
    	await borg.send_file(alive.chat_id, PLUSPIC, caption=ALIVE)
    	await alive.delete()
    else:
    	ALIVE = f"**MADE IN 🇮🇳 , MADE FOR 🐺** \n\n`◽ Telethon :` **{version.__version__}** \n`🔹 Python:` **{python_version()}** \n`🔸 Fork by:` @WolfUserBotOT \n`🔹 Bot creator:` [//•Wolf•UserBot•//](tg://user?id=1499383735)\n`🔸 Plus+ Uptime:` **{uptime}** \n`🔹 My owner:` **{DEFAULTUSER}**  \n`🔸 Join` @RkProjects `For Help` \n\n                      [Deploy✔️](https://heroku.com/deploy?template=https://github.com/indianSammy07/WolfUserbot)  \n\n   "
    	await alive.reply(f"{ALIVE}")
