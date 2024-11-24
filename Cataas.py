from tkinter import*
from PIL import Image, ImageTk#PIL, для работы с изображениями
import requests#для получения информации из интернета
from io import BytesIO#библиотека io import позволяет работать с вводом/выводом
#информации, а BytesIO с двойничными единичками, ноликами, байтами


def load_image(url):
    try:
        response=requests.get(url)
#response - переводится ответ (делается запрос по ссылке, что в ответ возвращается в response)
        response.raise_for_status()#строчка для обработки исключений
        image_data=BytesIO(response.content)
#image_data (делаем изображение), в переменную кладем обработанное изображение
#сам контент этого ответа (сама картинка) будет преобразована с помощью BytesIO
        img=Image.open(image_data)
#img, локальная переменная (внутри функции), image_data, из библиотеки pillow
        return ImageTk.PhotoImage(img)#функция возвращает Image картинку img, а дальше эту
#картинку положим в img=load_image(url) и это отобразится в метке label
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None


def set_image():#отдельная функция, вызывающая load_image и устанавливать изображение в метку
    img=load_image(url)

    if img:
        label.config(image=img)  # устанавливаем картинку на метку
        label.image = img  # чтобы "сборщик мусора" не посчитал картинку таковым


window.Tk()
window.title(text="Cats!")
window.geometry("600x480")
label=Label()
label.pack()

update_button=Button(text="Обновить", command=set_image)
update_button.pack()

url="https://cataas.com/cat"

set_image()#когда запускаем первый раз функция должна быть вызвана, чтобы появилась первая
#картинка при запуске проекта

window.mainloop()




