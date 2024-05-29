import keyboard as keyb

# превращение первого параметра, во второй после нажатия пробела
keyb.add_abbreviation('fti', 'from tkinter import *')

# создание горячей клавиши, которая выполняет lambda функцию
keyb.add_hotkey('f + t', lambda: keyb.write('from tkinter import *'))
