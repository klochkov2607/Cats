from tkinter import*
from PIL import Image, ImageTk#PIL, для работы с изображениями
import requests#для получения информации из интернета
from io import BytesIO#библиотека io import позволяет работать с вводом/выводом

from bottle import response


#информации, а BytesIO с двойничными единичками, ноликами, байтами


def load_image():
    try:
        response=requests.get(url)
#response - переводится ответ (делается запрос по ссылке, что в ответ возвращается в response)
        response.taise_for_status()#строчка для обработки исключений
        image_data=BytesIO(response.content)
#image_data (делаем изображение), в переменную кладем обработанное изображение
#сам контент этого ответа (сама картинка) будет преобразована с помощью BytesIO
        img=Image.open(image_data)
#img, локальная переменная (внутри функции), image_data, из библиотеки pillow
        return ImageTk.PhotoImage(img)#функция возвращвет Image картинку img, а дальше эту
#картинку положим в img=load_image(url) и это отобразится в метке label
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None




window.Tk()
window.title(text="Cats!")
window.geometry("600x480")
label=Label()
label.pack()

url="https://cataas.com/cat"
img=load_image(url)


if img:
    label.config(image=img)
    label.image=img#чтобы "сборщик мусора" не посчитал картинку таковым

window.mainloop()




