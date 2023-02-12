from tkinter import *  # Імпортування головної бібліотеки Tkinter

mein = Tk()  # Створення основний клас застосунку Tkinter.
mein.config(bg='RED', relief=RIDGE, bd=15, height=500, width=500)  #Відповідає за вигляд вікна, RIDGE - вигляді хребта
# bg колір фону
# bd ширина рамки

mein.title('Добрий день!')  # Назва вікна
title = Label(text='Текст', bg='RED', font=10)  # Робить текст
title.pack() # Створює текст
bth = Button(text='Kопка', bg='Green') # Робить кнопку
bth.pack() # Створює кнопку

mein.mainloop()  # Запуск вікна на виконання



