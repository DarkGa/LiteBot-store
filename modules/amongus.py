from requests import get
from random import randint, choice
from PIL import Image, ImageFont, ImageDraw
from core.utils import utils
from textwrap import wrap

class Main:
	
	version="1.0.0"
	info="Модуль для определения предателя из игры AmongUs"
	group="Fun"
	
	async def init(app, m):
		
		url="https://raw.githubusercontent.com/KeyZenD/AmongUs/master/"

		await m.delete()
        
		if m.reply_to_message:
			img=get(url+str(randint(1, 12))+".png", stream=True).raw
			font_raw=get("https://raw.githubusercontent.com/onivim/oni2/master/assets/fonts/Inter-UI-Bold.ttf", stream=True).raw
			
			im2 = Image.open(img)
			im = Image.new('RGBA', (920, 500), color=(0,0,0,0))
			im.paste(im2, (30, 30), im2)
			draw_text = ImageDraw.Draw(im) 
			
			text=m.reply_to_message.from_user.first_name+f' {choice(["был", "не был"])} предателем'
			text_ = "\n".join(["\n".join(wrap(part, 13)) for part in text.split("\n")])
			
			draw_text.text(
					(400,10),
					text_,
					font=ImageFont.truetype(font_raw, 65),
					fill=('#000000')
			)
			im.save("test.png", "PNG")
			utils.bash("mv test.png test.webp")
			await m.reply_sticker("test.webp", reply_to_message_id=m.reply_to_message.message_id)
