# а) Сделать набросок дизайна программы в figma / paint для программы,
# которая делает запрос на сайт jsonplaceholder с определённым id.
# б) Разработать эту программу на библиотеке tkinter.
# в) Реализовать сохранение полученного объекта в папку.

import requests
import os
import json
from tkinter import Tk, Label, Button

# Напишем функцию, которая будет делать запрос на сайт jsonplaceholder, вытаскивать оттуда информацию и сохранять
# ее в виде json-файлов в отдельную папку, проще говоря повторим тот код, который писали в задаче 1 урока 24

def json_download():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    data = response.json()
    current_dir = os.getcwd()
    folder_name = 'JSON Folder'
    path = os.path.join(current_dir, folder_name)
    os.makedirs(path, exist_ok=True)
    for d in data:
        file_name = f'data_{d["id"]}.json'
        file_path = os.path.join(path, file_name)
        with open(file_path, 'w') as file:
            json.dump(d, file)

# Теперь напишем графический интерфейс для пользователя с текстом и с кнопкой, при нажатии которой выполнится 
# вышенаписанная функция

# Создадим окно - объект класса Tk
window = Tk()
# Зададим заголовок для этого окна
window.title('JSON download')
# Зададим какой-нибудь размер для окна
window.geometry('200x100')
# Создадим какую-нибудь бирку - текст внутри основного окна, зададим содержание текста, его стиль и размер шрифта
label = Label(window, text='Загрузка JSON', font=('Arial', 20))
# Поместим эту бирку внутри окна в левый верхний угол, то есть в самое начало 
label.grid(column=0, row=0)
# Теперь создадим кнопку внутри этого окна с названием и привяжем к ней выполнении функции json_download..
btn = Button(window, text='Загрузить', command=json_download)
# и поместим ее на следующую строку после бирки
btn.grid(column=0, row=1)
# Запустим открытие окна
window.mainloop()