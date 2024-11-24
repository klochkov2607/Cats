from tkinter import*
from PIL import Image, ImageTk#PIL, для работы с изображениями
import requests#для получения информации из интернета
from io import BytesIO#библиотека io import позволяет работать с вводом/выводом
#информации, а BytesIO с двойничными единичками, ноликами, байтами


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




