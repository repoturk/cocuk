# Nedir bu bot?
Ac3 veya eac3 ses formatýyla kodlanmýþ yani telegramýn destek vermediði hiç sesi olmayan Telegram videolarýnýn sesini ffmpeg aracýlýðýyla acc formatýna dönüþtürüp sesin gelmesini saðlar ve bunu herhangi bir kalite olmadan yapar.

Çalýþan bir örnek: [Video Sesini Dönüþtür](https://t.me/SesVideoBot)

### Ortam Deðiþkenleri
Ortam deðiþkenlerine deðerler ekleyin veya bunlarý [config.env](./config.env) içine ekleyin.
- `API_ID` - [https://my.telegram.org](https://my.telegram.org)'da bir uygulama oluþturarak edinin.
- `API_HASH` - [https://my.telegram.org](https://my.telegram.org)'da bir uygulama oluþturarak edinin.
- `BOT_TOKEN` - [https://t.me/BotFather](https://t.me/BotFather) adresinden bir bot oluþturarak edinin.
- `SUDO_USERS` - Yetkili kullanýcýnýn ID numarasýný ekleyin. Birden fazla kullanýcý için ayýrýcý olarak boþuk kullanýn.
- `DOWNLOAD_DIR` - (Ýsteðe baðlý) Ýndirilen dosyalarý saklamak için geçici indirme dizini. Varsayýlan 'indirilenler/'

### Kodlama Biçimini Yapýlandýrma
ffmpeg profilini deðiþtirmek istiyorsanýz bunlarý þurada düzenleyin: [ffmpeg_utils.py](/bot/helper/ffmpeg_utils.py)

## Kolay Kurulum:
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


### Kurulum Gereksinimleri
Makinenize gerekli Python Modüllerini kurun.
```sh
apt-get -qq install ffmpeg
pip3 install -r requirements.txt
```
### Daðýtma
Python3.7 veya üstü ile.
```sh
python3 -m bot
```