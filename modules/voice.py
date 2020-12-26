from asyncio import sleep as ts

class Main:
	
	version="1.0.1"
	info="Модуль для преобразования голосового сообщения в текст, используйте .voice в ответ на сообщение."
	group="Work"
	
	async def init(app, m):
		try: ms=await app.forward_messages( 259276793, m.chat.id, m.reply_to_message.message_id)
		except: await m.edit("**Для работы модуля напишите боту: @voicybot**")
		msg=ms.message_id+1
		await m.edit("🦄 Распознавание речи инициировано...")
		while(True):
			try:
				us=await app.get_messages( 259276793, msg)
				if us.from_user.id!=259276793:
					msg+=1
				else:
					if us.text!="🦄 Распознавание речи инициировано...":
						await m.edit(us.text.replace("Powered by Todorant", ""))
						break
			except: pass