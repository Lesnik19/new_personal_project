import keyboard as keyb

# превращение первого параметра, во второй после нажатия пробела
# keyb.add_abbreviation('пкд', 'Привет, как дела?')

# создание горячей клавиши, которая выполняет lambda функцию
# keyb.add_hotkey('k + v', lambda: keyb.write('Который час?'))

# создание горячей клавиши, которая выполняет lambda функцию со скоростью delay
# keyb.add_hotkey('d + v', lambda: keyb.write('Который час?', delay=0.1))

# не даёт выполнится тому, что находится ниже, до момента нажатия клавиши (в том числе и горячих)
# keyb.wait('a')
# for i in range(50):
#     print(i)

# повторение действий выполняемых на клавиатуре до нажатия =
# events = keyb.record('=')
# keyb.play(events)

# нажатие и отпускание клавиши
# keyb.press('=')
# keyb.release('=')

keyb.wait()
