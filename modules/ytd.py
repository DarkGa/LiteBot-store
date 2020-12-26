import os
import sys
try: from pytube import YouTube
except: os.system("pip3 install pytube")

class Main:
	
	version="1.0.1"
	info="Загрузка и конвертация видео с ютуба в музыку, используйте .ytd в ответ на ссылку, либо .ytd link для прямой загрузки."
	group="YouTube-utils"
	
	async def init(app, m):
		
		try: sys.modules["pytube"]
		except: await m.edit("**Для работы перезапустите самого бота.**"); return 
		
		argc=m.text.split()
		
		if len(argc)==1:
			if m.reply_to_message:
				await m.edit("```Скачиваем...```")
				d=m.message_id
				yt=YouTube(m.reply_to_message.text)
				t=yt.streams.filter(only_audio=True).all()
				t[0].download("tmp")
				music=os.listdir("tmp")
				os.system(f'mv "tmp/{music[0]}" "tmp/{music[0][:-1]}3"')
				await m.edit("```Отправляем...```")
				await m.reply_audio("tmp/"+music[0][:-1]+"3", caption="**Powered by [LiteBot](https://github.com/DarkGa/LiteBot)**", reply_to_message_id=m.reply_to_message.message_id)
				await m.delete()
				os.system("rm -rf tmp")
			else: await m.edit("**Для справки отправте** '```.help ytd```'.")
		else:
			await m.edit("```Скачиваем...```")
			yt=YouTube(argc[1])
			t=yt.streams.filter(only_audio=True).all()
			t[0].download("tmp")
			music=os.listdir("tmp")
			os.system(f'mv "tmp/{music[0]}" "tmp/{music[0][:-1]}3"')
			await m.edit("```Отправляем...```")
			await app.send_audio(m.chat.id, "tmp/"+music[0][:-1]+"3", caption="**Powered by [LiteBot](https://github.com/DarkGa/LiteBot)**")
			await m.delete()
			os.system("rm -rf tmp")
	