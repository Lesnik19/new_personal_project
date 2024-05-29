from tkinter import *
import math
from random import *


class Draw_image:
    def __init__(self, change_time):
        # создание окна с именем win
        self.win = Tk()
        # присвоение окну названия
        self.win.title('Остров мечты')
        # присвоение окну размера
        self.win.geometry('800x600')
        # присвоение запрета на изменение высоты и ширины окна
        self.win.resizable(height=False, width=False)
        # создание в окне холста синего цвета по умолчанию
        self.canvas = Canvas(self.win, background='blue', width=800, height=600)
        # сохранение периодичности изменения изображения на холсте
        self.change_time = change_time
        # вызов функции для отрисовки изображения
        self.__move()
        # открытие и удерживание в открытом состоянии окна
        self.win.mainloop()

    def __draw_sol(self, x_center, y_center, radius, num_ray):
        height_ray = randint(55, 80)
        # присваивание окну имя с
        c = self.canvas
        # создание круга
        c.create_oval(x_center - radius, y_center - radius, x_center + radius, y_center + radius,
                      fill='yellow', outline='yellow')
        step_angle = 2 * math.pi/num_ray
        delta_angle = 2 * math.pi/(num_ray * 5)
        for i in range(0, num_ray):
            angle = step_angle * i
            angle_p = angle + delta_angle
            angle_m = angle - delta_angle
            start_x = int(x_center + radius * math.cos(angle))
            start_y = int(y_center + radius * math.sin(angle))
            end_x_p = int(x_center + (radius+height_ray) * math.cos(angle_p))
            end_y_p = int(y_center + (radius+height_ray) * math.sin(angle_p))
            end_x_m = int(x_center + (radius + height_ray) * math.cos(angle_m))
            end_y_m = int(y_center + (radius + height_ray) * math.sin(angle_m))
            c.create_polygon(start_x, start_y, end_x_p, end_y_p, end_x_m, end_y_m, fill='yellow')

    def __draw_palm(self):
        # присваивание окну имя с
        c = self.canvas
        # установка цвета листвы пальмы
        color_sheet = '#047a33'
        # цикл
        for i in range(0, 10):
            c.create_arc(150 - 4 * i, 550 - 23 * i, 200 - 6 * i, 600 - 23 * i, start=int(0 + 1.5 * i),
                    extent=int(180 + 1.5 * i), outline='black', fill='#85640c', width=2)
            c.create_arc(300 + 6 * i, 550 - 23 * i, 350 + 4 * i, 600 - 23 * i, start=int(0 - 1.5 * i),
                         extent=int(180 - 1.5 * i), outline='black', fill='#85640c', width=2)

        points_sheet = [40, 6, 20, 10, 26, 18, 17, 24, 19, 26,
                        9, 35, 15, 36, 10, 55, 18, 45, 25, 51,
                        27, 40, 34, 45, 32, 30, 39, 35, 38, 27,
                        41, 25, 37, 16, 38, 12, 41, 11]
        points_sheet_u = [52, 18, 50, 14, 49, 12, 37, 12, 30, 14,
                          22, 18, 15, 23, 10, 30, 5, 37, 18, 28,
                          20, 32, 30, 24, 31, 30, 42, 22, 44, 26]
        points_s1, points_s2, points_s3, points_s4 = [], [], [], []
        for i in range(len(points_sheet)):
            points_sheet[i] = int(points_sheet[i]*2.5)
            if i % 2 != 0:
                points_s1.append(points_sheet[i] + 330+randint(-2, +2))
                points_s2.append(points_s1[i])
            else:
                points_s1.append(points_sheet[i] + 25)
                points_s2.append(50-points_s1[i]+210)
        for i in range(len(points_sheet_u)):
            points_sheet_u[i] = int(points_sheet_u[i]*2.5)
            if i % 2 != 0:
                points_s3.append(points_sheet_u[i] + 300+randint(-2, +2))
                points_s4.append(points_s3[i])
            else:
                points_s3.append(points_sheet_u[i])
                points_s4.append(50-points_s3[i]+210)
        c.create_polygon(points_s1, fill=color_sheet, outline='black')
        c.create_polygon(points_s2, fill=color_sheet, outline='black')
        c.create_polygon(points_s3, fill=color_sheet, outline='black')
        c.create_polygon(points_s4, fill=color_sheet, outline='black')
        for n in range(1, 5):
            points_work = eval('points_s'+str(n))
            for i in range(len(points_work)):
                if i % 2 == 0:
                    points_work[i] += 240
        c.create_polygon(points_s1, fill=color_sheet, outline='black')
        c.create_polygon(points_s2, fill=color_sheet, outline='black')
        c.create_polygon(points_s3, fill=color_sheet, outline='black')
        c.create_polygon(points_s4, fill=color_sheet, outline='black')

    def __draw_fon(self):
        # присваивание окну имя с
        c = self.canvas
        # установка цвета песка
        color_sand = '#ebe38f'
        # создание песчаной части остова
        c.create_arc(-200, 400, 600, 1000, start=0,
                     extent=180, outline=color_sand, fill=color_sand)

        # создание зелёной части острова
        c.create_arc(-10, 500, 450, 800, start=0,
                     extent=180, outline='green', fill='green')

    def __draw_cloud(self):
        # присваивание окну имя с
        c = self.canvas
        # установка цвета облака
        color_cloud = '#27f5f5'
        points_cloud = [26, 29, 25, 26, 27, 23, 30, 22, 33, 24, 37, 20, 39, 19,
                        44, 18, 47, 20, 49, 18, 52, 17, 56, 16, 59, 18, 62, 21,
                        66, 19, 69, 21, 72, 24, 75, 26, 73, 29, 75, 30, 76, 33,
                        73, 36, 70, 36, 67, 35, 66, 38, 65, 40, 61, 40, 58, 39,
                        56, 37, 55, 39, 53, 42, 51, 43, 48, 43, 46, 42, 43, 39,
                        41, 41, 39, 43, 35, 44, 32, 44, 31, 42, 30, 39, 27, 39,
                        24, 38, 23, 35, 24, 30]
        points_cl1, points_cl2, points_cl3 = [], [], []
        k1, k2, k3 = 2.3, 2.6, 1.9
        for i in range(len(points_cloud)):
            if i % 2 != 0:
                points_cl1.append(int(points_cloud[i] * k1) + randint(-2, +2))
                points_cl2.append(int(points_cloud[i] * k2) + 70 + randint(-2, +2))
                points_cl3.append(int(points_cloud[i] * k3) - 10 + randint(-2, +2))
            else:
                points_cl1.append(int(points_cloud[i] * k1) + randint(-2, +2))
                points_cl2.append(int(points_cloud[i] * k2) + randint(-2, +2) + 130)
                points_cl3.append(int(points_cloud[i] * k3) + randint(-2, +2) + 260)
        c.create_polygon(points_cl1, fill=color_cloud, smooth=False)
        c.create_polygon(points_cl2, fill=color_cloud, smooth=False)
        c.create_polygon(points_cl3, fill=color_cloud, smooth=False)

    def __move(self):
        # очистка окна от всех объектов
        self.canvas.delete('all')
        # отрисовка острова (песка и земли)
        self.__draw_fon()

        # отрисовка солнца
        self.__draw_sol(600, 150, 50, 10)
        # отрисовка пальм
        self.__draw_palm()
        # отрисовка облаков
        self.__draw_cloud()
        # вывод холста на экран
        self.canvas.pack()
        # запуск метода одновременно с командой mainloop
        # (это буквально решение ВСЕХ (ну почти всех) ПРОБЛЕМ в tkinter)
        self.win.after(self.change_time, self.__move)


# Создаем экземпляр класса с заданной периодичностью изменения картинки
my_image = Draw_image(200)
