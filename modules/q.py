from asyncio import sleep as ts

class Main:
	
	version="1.0.0"
	info="Модуль для создания цитаты в виде стикера, используйте .q в ответ на сообщение."
	group="Quotes"
	
	async def init(app, m):
		try: ms=await app.forward_messages( 1031952739, m.chat.id, m.reply_to_message.message_id)
		except: await m.edit("**Для работы модуля напишите боту: @QuotLyBot**")
		msg=ms.message_id+1
		await m.delete()
		
		while(True):
			us=await app.get_messages( 1031952739, msg)
			try:
				if us.from_user.id!=1031952739:
					msg+=1
				else:
					await app.download_media(us.sticker.file_id, file_name="tmp.webp")
					await m.reply_sticker("downloads/tmp.webp", reply_to_message_id=m.reply_to_message.message_id)
					break
			except:
				pass