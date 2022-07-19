"""тестовый вариант c ползунком"""
import tkinter
from PIL import Image, ImageTk
from aboba_finish import mainfunc
from tkinter import Tk, BOTH, IntVar, LEFT, HORIZONTAL, IntVar
from tkinter.ttk import Frame, Label, Scale, Style


class App:
    """основной класс"""

    def __init__(self):
        self.root = tkinter.Tk()

        # создаем рабочую область
        self.frame = tkinter.Frame(self.root)
        self.frame.grid()

        # Добавим метку
        self.label_r = tkinter.Label(self.frame, text="                      ползунок наклона лучей", anchor='w').grid(row=0, column=0)
        self.label_y = tkinter.Label(self.frame, text="    ползунок наклона жёлтой зеркала", anchor='w').grid(row=1, column=0)
        self.label_b = tkinter.Label(self.frame, text="      ползунок наклона синей зеркала", anchor='w').grid(row=2, column=0)
        self.label_a = tkinter.Label(self.frame, text="ползунок наклона всей конструкции", anchor='w').grid(row=3, column=0)

        # label показывающий градусы ползунка лучей
        self.label_rays = tkinter.Label(self.frame, text=2)
        self.label_yellow = tkinter.Label(self.frame, text=0)
        self.label_blue = tkinter.Label(self.frame, text=0)
        self.label_all = tkinter.Label(self.frame, text=0)
        self.label_p = tkinter.Label(self.frame, text='Количество падающих лучей на понель = 0')
        self.label_o = tkinter.Label(self.frame, text='Количество падающих лучей отраженных от зеркал = 0')
        self.label_rays.grid(row=0, column=5)
        self.label_yellow.grid(row=1, column=5)
        self.label_blue.grid(row=2, column=5)
        self.label_all.grid(row=3, column=5)
        self.label_p.grid(row=4, column=0)
        self.label_o.grid(row=5, column=0)

        # фотография по умолчанию
        self.image = Image.open("saved_figure.jpg")
        self.photo = ImageTk.PhotoImage(self.image)

        # добавляем ползунок для изменения наклона лучей
        self.v_rays = IntVar()
        self.v_yellow = IntVar()
        self.v_blue = IntVar()
        self.v_all = IntVar()
        self.scale_rays = Scale(self.frame, variable=self.v_rays, from_=2, to=179, orient=HORIZONTAL, command=self.rays_scale)
        self.scale_yellow = Scale(self.frame, variable=self.v_yellow, from_=0, to=179, orient=HORIZONTAL, command=self.yellow_scale)
        self.scale_blue = Scale(self.frame, variable=self.v_blue, from_=0, to=179, orient=HORIZONTAL, command=self.blue_scale)
        self.scale_all = Scale(self.frame, variable=self.v_all, from_=0, to=360, orient=HORIZONTAL, command=self.all_scale)
        self.scale_rays.grid(row=0, column=4)
        self.scale_yellow.grid(row=1, column=4)
        self.scale_blue.grid(row=2, column=4)
        self.scale_all.grid(row=3, column=4)

        # Добавим изображение
        self.canvas = tkinter.Canvas(self.root, height=600, width=700)
        self.c_image = self.canvas.create_image(0, 0, anchor='nw', image=self.photo)
        self.canvas.grid(row=4, column=0)
        self.root.mainloop()

    def create_scale_label(self, name_label: str, row: int):
        """метод для создания ползунка и label"""
        pass

    def my_event_handler(self, val_rays, val_yellow, val_blue, val_all):
        if val_rays == 0 or val_rays == 1:
            val_rays = 2
        print(val_rays, val_yellow, val_blue, val_all)

        print("my_event_handler")
        q = mainfunc(val_rays, val_yellow, val_blue, val_all)
        self.label_p.config(text='Количество падающих лучей на понель = ' + str(q[0]))
        self.label_o.config(text='Количество падающих лучей отраженных от зеркал = ' + str(q[1]))
        self.image = Image.open("saved_figure.jpg")
        self.photo = ImageTk.PhotoImage(self.image)
        self.c_image = self.canvas.create_image(0, 0, anchor='nw', image=self.photo)
        self.canvas.grid(row=2, column=0)

    def rays_scale(self, val: str):
        val = round(float(val))
        self.label_rays.config(text=str(val))
        self.my_event_handler(val_rays=val, val_yellow=round(self.v_yellow.get()), val_blue=round(self.v_blue.get()), val_all=round(self.v_all.get()))

    def yellow_scale(self, val: str):
        val = round(float(val))
        self.label_yellow.config(text=str(val))
        self.my_event_handler(val_rays=round(self.v_rays.get()), val_yellow=val, val_blue=round(self.v_blue.get()), val_all=round(self.v_all.get()))

    def blue_scale(self, val: str):
        val = round(float(val))
        self.label_blue.config(text=str(val))
        self.my_event_handler(val_rays=round(self.v_rays.get()), val_yellow=round(self.v_yellow.get()), val_blue=val, val_all=round(self.v_all.get()))

    def all_scale(self, val: str):
        val = round(float(val))
        self.label_all.config(text=str(val))
        self.my_event_handler(val_rays=round(self.v_rays.get()), val_yellow=round(self.v_yellow.get()), val_blue=round(self.v_blue.get()), val_all=val)


app = App()
