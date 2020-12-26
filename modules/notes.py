import os

class Main:
	
	version="1.0.0"
	info="Модуль для создания/чтения ваших заметок, испооьзуйте .notes для просмотра, .notes Моя заметка для создания заметки."
	group="Work"
	
	async def init(app, m):
		
		if len(m.text)<=7:
			if os.path.exists("notes.txt"):
				notes=open("notes.txt", "r")
				text_notes=notes.read()
				if len(text_notes)==0:
					await m.edit('''
**Ваши заметки:**

( пусто )
					''')
				else:
					msg=''
					for note in text_notes.split('\n'):
					  if len(note)!=0:
					    msg+=f'**• {note}**\n'
					await m.edit(f'''
__**Ваши заметки:**__

{msg}
					''')
				notes.close()
			else:
				await m.edit('''
**Ваши заметки:**

( пусто )
					''')
		
		else:
			try: notes=open("notes.txt", "a")
			except: notes=open("notes.txt", "w")
			notes.write(f'{m.text.replace(".notes ", "")}\n')
			await m.edit('**Заметка добавлена в блокнот, для просмотра заметок отправте ```.notes```**')
			notes.close()
			text_notes.close()