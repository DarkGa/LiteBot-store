from core.utils import utils
import requests

class Main:
	
	version="1.0.0"
	info="Удаление фона на заданной картинке."
	group="Work"
	data=["token"]
	
	async def init(app, m):
		
		try: token=utils.db.select("nobg", "token")[0]
		except: token=False
		
		if token:
			if m.reply_to_message:
				await m.edit("__Скачиваем…__")
				await app.download_media(m.reply_to_message, file_name="tmp.png")
				
				await m.edit("__Шаманим…__")
				response = requests.post(
				    'https://api.remove.bg/v1.0/removebg',
				    files={'image_file': open('downloads/tmp.png', 'rb')},
				    data={'size': 'auto'},
				    headers={'X-Api-Key': token},
				)
				
				await m.edit("__Отправляем…__")
				if response.status_code == requests.codes.ok:
					with open('no-bg.png', 'wb') as out:
						out.write(response.content)
						await m.delete()
						await m.reply_document(document="no-bg.png", caption="**Powered by [LiteBot](https://github.com/DarkGa/LiteBot)**", reply_to_message_id=m.reply_to_message.message_id)
				else:
					await m.edit(f"Error: {response.status_code} {response.text}")
			else: await m.edit("И что обрабатывать? (ответь на сообщение с картинкой)")
		else: await m.edit("Для работы требуется токен, получить его можно [тут](https://www.remove.bg/dashboard#api-key), настроить его можно в веб панели бота.")


 