
import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions
from uniborg.util import admin_cmd
import asyncio
import shutil 
import random, re



FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

#Add telegraph media links of profile pics that are to be used
TELEGRAPH_MEDIA_LINKS = ["https://telegra.ph/file/2bc2e85fb6b256efc4088.jpg",
                         "https://telegra.ph/file/443fff8a7db51d390e1a7.jpg",
                         "https://telegra.ph/file/e49bbb9e21383f8231d85.jpg",
                         "https://telegra.ph/file/d6875213197a9d93ff181.jpg",
                         "https://telegra.ph/file/ec7da24872002e75e6af8.jpg",
                         "https://telegra.ph/file/468a2af386d10cd45df8f.jpg",
                         "https://telegra.ph/file/59c7ce59289d80f1fe830.jpg"
                        ]
@borg.on(admin_cmd(pattern="thordp ?(.*)"))
async def autopic(event):
    while True:
        piclink = random.randint(0, len(TELEGRAPH_MEDIA_LINKS) - 1)
        AUTOPP = TELEGRAPH_MEDIA_LINKS[piclink]
        downloaded_file_name = "./ravana/original_pic.png"
        downloader = SmartDL(AUTOPP, downloaded_file_name, progress_bar=True)
        downloader.start(blocking=False)
        photo = "photo_pfp.png"
        while not downloader.isFinished():
            place_holder = None
    
    
        shutil.copy(downloaded_file_name, photo)
        im = Image.open(photo)
        current_time = datetime.now().strftime("@MrSemmy \n \nTime: %H:%M:%S \nDate: %d/%m/%y")
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 30)
        drawn_text.text((30, 50), current_time, font=fnt, fill=(102, 209, 52))
        img.save(photo)
        file = await event.client.upload_file(photo)  # pylint:disable=E0602
        try:
            await event.client(functions.photos.DeletePhotosRequest(await event.client.get_profile_photos("me", limit=1)))
            await event.client(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
                file
            ))
            os.remove(photo)
            
            await asyncio.sleep(600)
        except:
            return
