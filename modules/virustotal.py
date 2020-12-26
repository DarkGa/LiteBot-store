import requests
from core.utils import utils
import os

class Main:
	
	version="1.0.0"
	info="Модуль для проверки файла через апи VirusTotal."
	group="Security"
	data=["token"]
	
	async def init(app, m):
		
		try: token=utils.db.select("virustotal", "token")[0]
		except: token=False
		
		if token:
			if m.reply_to_message:
				file_info = m.reply_to_message.document.file_id
				await m.edit("```Скачиваем...```")
				downloaded_file = await app.download_media(file_info, file_name="tmp")
				src = "downloads/tmp"
				url = 'https://www.virustotal.com/vtapi/v2/file/scan'
				params = {'apikey': token}
				files = {'file': ("tmp", open(src, 'rb'))}
				await m.edit("```Отправляем...```")
				response = requests.post(url, files=files, params=params)
				await m.edit("```Получаем хеш...```")
				json_scan = response.json()
				hash = json_scan['resource']
				url = 'https://www.virustotal.com/vtapi/v2/file/report'
				params = {'apikey': token, 'resource': hash}
				await m.edit("```Получаем результаты...```")
				response = requests.get(url, params=params)
				json_scan = response.json()
				await m.edit("```Готовим отчет...```")
				try: dr=json_scan['scans']['DrWeb']['result']
				except: dr="*Ничего*"
				try: malv=json_scan['scans']['Malwarebytes']['result']
				except: malv="*Ничего*"
				try: kasp=json_scan['scans']['Kaspersky']['result']
				except: kasp="*Ничего*"
				try: hou=json_scan['positives']
				except: hou="Нету"
				os.system("rm -rf downloads/tmp")
				
				if 1==1:
					if hou==0 or hou=="None" or hou==None: await m.edit("Файл полностью безопасен✅")
					else:
						antivirus=["Malwarebytes ", "Dr.Web ", "Kaspersky ", "Всего угроз "]
						check=[malv, dr, kasp, hou]
						message="""Отчет о файле:"""
						for i in range(4):
							if check[i]!=None and check[i]!="None": message+=f"""\n\n**{antivirus[i]}** - ```{check[i]}```"""
						await m.edit(message)
			else: await m.edit("И что проверять? (ответь на сообщение с файлом)")
		else: await m.edit("Для работы требуется токен, получить его можно [тут](https://www.virustotal.com/gui/join-us), настроить его можно в веб панели бота.")