import os
import time
from bot import data, download_dir
from pyrogram.types import Message
from .ffmpeg import encode, get_thumbnail, get_duration, get_width_height
from bot.progress import progress_for_pyrogram

def on_task_complete():
    del data[0]
    if len(data) > 0:
      add_task(data[0])

def add_task(message: Message):
    try:
      c_time = time.time()
      msg = message.reply_text("```Video Yükleniyor...```", quote=True)
      filepath = message.download(
                file_name=download_dir,
                progress=progress_for_pyrogram,
                progress_args=(
                   "İndiriliyor...",
                    msg,
                    c_time
                ))
      msg.edit("```Video Kodlanıyor...```")
      new_file = encode(filepath)
      if new_file:
        msg.edit("```Video Kodlandı, Metadata Veriler Alınıyor...```")
        duration = get_duration(new_file)
        thumb = get_thumbnail(new_file, download_dir, duration / 4)
        width, height = get_width_height(new_file)
        msg.edit("```Video yükleniyor...```")
        message.reply_video(
                new_file, 
                quote=True, 
                supports_streaming=True, 
                thumb=thumb, 
                duration=duration, 
                width=width, 
                height=height,
                progress=progress_for_pyrogram,
                progress_args=(
                    "Yükleniyor...",
                    msg,
                    c_time
                ))
        os.remove(new_file)
        os.remove(thumb)
        msg.edit("```Video Başarıyla Kodlandı.```")
      else:
        msg.edit("```Dosyanızı kodlarken bir şeyler ters gitti.```")
        os.remove(filepath)
    except Exception as e:
      msg.edit(f"```{e}```")
    on_task_complete()
