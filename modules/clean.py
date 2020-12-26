class Main:
	
	version="1.0.0"
	info='''Модуль для очистки группы от удаленных аккаунтов, принимает следующие аргументы scan|del
	
scan - подсчет удаленных аккаунтов
del - очистка группы от удаленных аккаунтов'''
	group="Admins"
	
	async def init(app, m):
		
		argc=m.text.split()
		
		if len(argc)!=1:
			if m.chat.type=="group" or m.chat.type=="supergroup":
				users=[u.user.id for u in await app.get_chat_members(m.chat.id) if u.user.is_deleted]
				if argc[1]=="scan":
					if len(users)==0: await m.edit("**В чате отсутствуют удаленные аккаунты**")
					else: await m.edit(f"**В чате обнаруженно {len(users)} удаленных аккаунтов**")
				elif argc[1]=="del":
					for user in users:
						try: await app.kick_chat_member(m.chat.id, user)
						except: await m.edit("**Не достаточно прав!**"); return
					await m.edit(f"Было забанено {len(users)} удаленных аккаунтов")
				else: await m.edit("Для справки отправте ```.help clean```")
			else: await m.edit("**Доступно только в группах!**")
		else: await m.edit("Для справки отправте ```.help clean```")
						
							
							
							