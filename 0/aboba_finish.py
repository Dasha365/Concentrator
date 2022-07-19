import time
import math
import numpy as np
import matplotlib.pyplot as plt


def mainfunc(val_rays: int, val_yellow: int, val_blue: int, val_all: int):
    rays = 0
    rays_out_mirror = 0

    #  Р¤СѓРЅРєС†РёСЏ РіСЂР°С„РёС‡РµСЃРєРѕРіРѕ РїСЂРµРґСЃС‚Р°РІР»РµРЅРёСЏ РґРІСѓРјРµСЂРЅРѕРіРѕ РјР°СЃСЃРёРІР°
    def show_2d_array(array, min_val=-4, max_val=3):
        plt.pcolormesh(array, cmap='rainbow', vmin=min_val,
                       vmax=max_val)  # Р—Р°РґР°С‘Рј РёРјСЏ РѕР±СЉРµРєС‚Р° РґР»СЏ РІС‹РІРѕРґР° (РїРµСЂРІРѕРµ РІ СЃРєРѕР±РєР°С…) Рё С†РІРµС‚РѕРІСѓСЋ РіР°РјРјСѓ
        plt.xlabel('y')
        plt.ylabel('x')
        # plt.show()
        plt.savefig('saved_figure.jpg')

    # РїР°РЅРµР»СЊ
    def panel(x3_right, y3_right, alpha_panel):
        counter3 = 0
        x3_left = x3_right
        y3_left = y3_right
        while counter3 <= length3:
            try:
                x3_right += h * math.sin(alpha_panel)
                y3_right += h * math.cos(alpha_panel)
                for j in range(0, 8):  # С‚РѕР»С‰РёРЅР° РїР°РЅРµР»Рё
                    array[round(x3_right) + j, round(y3_right) + j] = 2
                x3_left -= h * math.sin(alpha_panel)
                y3_left -= h * math.cos(alpha_panel)
                for j in range(0, 8):
                    array[round(x3_left) + j, round(y3_left) + j] = 2
                counter3 += h
            except IndexError:
                break

    # Р¶РµР»С‚РѕРµ Р·РµСЂРєР°Р»Рѕ
    def mirror(x0_right, y0_right, alpha_mirror):
        counter = 0
        x0_left = x0_right
        y0_left = y0_right
        while counter <= length:
            try:
                x0_right += h * math.sin(alpha_mirror)
                y0_right += h * math.cos(alpha_mirror)
                for j in range(0, 8):  # С‚РѕР»С‰РёРЅР° Р·РµСЂРєР°Р»Р°
                    array[round(x0_right) + j, round(y0_right) + j] = 1
                x0_left -= h * math.sin(alpha_mirror)
                y0_left -= h * math.cos(alpha_mirror)
                for j in range(0, 8):
                    array[round(x0_left) + j, round(y0_left) + j] = 1
                counter += h
            except IndexError:
                break

    # СЃРёРЅРµРµ Р·РµСЂРєР°Р»Рѕ
    def mirror_l(x0_right_l, y0_right_l, alpha_mirror_l):
        counter_l = 0
        x0_left_l = x0_right_l
        y0_left_l = y0_right_l
        while counter_l <= length:
            try:
                x0_right_l += h * math.sin(alpha_mirror_l)
                y0_right_l += h * math.cos(alpha_mirror_l)
                for j in range(0, 8):  # С‚РѕР»С‰РёРЅР° Р·РµСЂРєР°Р»Р°
                    array[round(x0_right_l) + j, round(y0_right_l) + j] = -3
                x0_left_l -= h * math.sin(alpha_mirror_l)
                y0_left_l -= h * math.cos(alpha_mirror_l)
                for j in range(0, 8):
                    array[round(x0_left_l) + j, round(y0_left_l) + j] = -3
                counter_l += h
            except IndexError:
                break

    # С„СѓРЅРєС†РёСЏ Р»СѓС‡РµР№ РїР°РґРµРЅРёСЏ
    def padenie(xp, yp, b_rad):
        x1_pad = xp
        y1_pad = yp
        while True:
            if x1_pad <= 0 or x1_pad >= n - 1 or y1_pad <= 0 or y1_pad >= n - 1:
                break
            x1_pad += h * math.sin(b_rad)
            y1_pad += h * math.cos(b_rad)
            if array[round(x1_pad), round(y1_pad)] == 1:
                q = 1
                otr(x1_pad, y1_pad, q)
                break
            if array[round(x1_pad), round(y1_pad)] == -3:
                q = 1
                otr_l(x1_pad, y1_pad, q)
                break
            if array[round(x1_pad), round(y1_pad)] == 2:
                nonlocal rays
                rays += 1
                break
            else:
                array[round(x1_pad), round(y1_pad)] = -4

    # С„СѓРЅРєС†РёСЏ Р»СѓС‡РµР№ РѕС‚СЂР°Р¶РµРЅРёСЏ РѕС‚ Р¶РµР»С‚РѕРіРѕ Р·РµСЂРєР°Р»Р°
    def otr(x1_pad, y1_pad, q):
        while q <= 3:
            try:
                x1_pad += h * math.sin(gamma)
                y1_pad += h * math.cos(gamma)
                if array[round(x1_pad), round(y1_pad)] == 2:
                    nonlocal rays_out_mirror
                    rays_out_mirror += 1
                    break
                if array[round(x1_pad), round(y1_pad)] == -3:
                    break
                if y1_pad <= 0 or y1_pad >= n or x1_pad <= 0 or y1_pad >= n:
                    break
                else:
                    if array[round(x1_pad), round(y1_pad)] == 1 or array[round(x1_pad), round(y1_pad)] == -3:
                        q += 1
                    array[round(x1_pad), round(y1_pad)] = -2
            except IndexError:
                break

    # С„СѓРЅРєС†РёСЏ Р»СѓС‡РµР№ РѕС‚СЂР°Р¶РµРЅРёСЏ РѕС‚ СЃРёРЅРµРіРѕ Р·РµСЂРєР°Р»Р°
    def otr_l(x1_pad, y1_pad, q):
        nonlocal rays_out_mirror
        while q <= 3:
            try:
                x1_pad += h * math.sin(gamma_l)
                y1_pad += h * math.cos(gamma_l)
                if array[round(x1_pad), round(y1_pad)] == 2:
                    rays_out_mirror += 1
                    break
                if array[round(x1_pad), round(y1_pad)] == 1:
                    break
                if y1_pad <= 0 or y1_pad >= n or x1_pad <= 0 or y1_pad >= n:
                    break
                else:
                    if array[round(x1_pad), round(y1_pad)] == -3:
                        q += 1
                    array[round(x1_pad), round(y1_pad)] = -2
            except IndexError:
                break

    n = 500  # СЂР°Р·РјРµСЂ РїРѕР»СЏ
    array = np.zeros((n, n))

    h = 0.45  # С€Р°Рі РїРёРєСЃРµР»РµР№
    length = 60  # РґР»РёРЅР° Р·РµСЂРєР°Р»Р°
    counter_l = 0  # СЃС‡РµС‚С‡РёРє
    x0_right = n / 5  # РєРѕРѕСЂРґРёРЅР°С‚С‹ Р¶РµР»С‚РѕРіРѕ Р·РµСЂРєР°Р»Р°
    y0_right = n / 4
    x0_left = n / 5  # РєРѕРѕСЂРґРёРЅР°С‚С‹ СЃРёРЅРµРіРѕ Р·РµСЂРєР°Р»Р°
    y0_left = 3 * n / 4

    alpha_degr = val_all  # угол поворота вей конструкции

    # РїРѕРІРѕСЂРѕС‚ РєРѕРЅСЃС‚СЂСѓРєС†РёРё
    c_x = n / 2
    c_y = n / 2

    alpha = alpha_degr * math.pi / 180
    x0_right_new = (-(math.sin(alpha) * (y0_right - n / 2)) + (math.cos(alpha) * (x0_right - n / 2))) - n / 2
    y0_right_new = ((math.cos(alpha) * (y0_right - n / 2)) + (math.sin(alpha) * (x0_right - n / 2))) - n / 2
    x0_left_new = (-(math.sin(alpha) * (y0_left - n / 2)) + (math.cos(alpha) * (x0_left - n / 2))) - n / 2
    y0_left_new = ((math.cos(alpha) * (y0_left - n / 2)) + (math.sin(alpha) * (x0_left - n / 2))) - n / 2

    x0_right = x0_right_new
    y0_right = y0_right_new
    x0_left = x0_left_new
    y0_left = y0_left_new

    # Р·РµСЂРєР°Р»Р°
    alpha_deg = val_yellow  # угол наклона жёлтого зеркала
    alpha_mirror = alpha_deg * math.pi / 180 - alpha  # СѓРіРѕР» Р¶РµР»С‚РѕРіРѕ Р·РµСЂРєР°Р»Р° Рє РіРѕСЂРёР·РѕРЅС‚Сѓ РІ СЂР°РґРёР°РЅР°С…
    alpha_deg_l = val_blue  # угол наклона синего зеркала
    alpha_mirror_l = alpha_deg_l * math.pi / 180 - alpha  # СѓРіРѕР» СЃРёРЅРµРіРѕ Р·РµСЂРєР°Р»Р° Рє РіРѕСЂРёР·РѕРЅС‚Сѓ РІ СЂР°РґРёР°РЅР°С…

    # РїР°РЅРµР»СЊ
    x3_right = 4 * n / 5
    y3_right = n / 2
    x3_right_new = (-(math.sin(alpha) * (y3_right - n / 2)) + (math.cos(alpha) * (x3_right - n / 2))) - n / 2
    y3_right_new = ((math.cos(alpha) * (y3_right - n / 2)) + (math.sin(alpha) * (x3_right - n / 2))) - n / 2
    x3_right = x3_right_new
    y3_right = y3_right_new
    counter3 = 0
    length3 = 60  # РґР»РёРЅР° РїР°РЅРµР»Рё
    sigma_panel = 180  # СѓРіРѕР» РїР°РЅРµР»Рё Рє РіРѕСЂРёР·РѕРЅС‚Сѓ РІ РіСЂР°РґСѓСЃР°С…
    alpha_panel = sigma_panel * math.pi / 180 - alpha  # СѓРіРѕР» РїР°РЅРµР»Рё Рє РіРѕСЂРёР·РѕРЅС‚Сѓ РІ СЂР°РґРёР°РЅР°С…

    panel(x3_right, y3_right, alpha_panel)

    # Р»СѓС‡Рё
    b = val_rays  # угл падения лучей горизонта
    b = 360 - b
    b_rad = b * math.pi / 180  # СѓРіРѕР» Р»СѓС‡Р° Рє РіРѕСЂРёР·РѕРЅС‚Сѓ РІ СЂР°РґРёР°РЅР°С…
    pad = (math.pi / 180) + b_rad - alpha_mirror  # СѓРіРѕР» РїР°РґРµРЅРёСЏ РІ СЂР°РґРёР°РЅР°С…
    counter = 0
    gamma = 2 * alpha_mirror - b_rad  # СѓРіРѕР» РѕС‚СЂР°Р¶РµРЅРёСЏ РІ РіСЂР°РґСѓСЃР°С…
    gamma_l = 2 * alpha_mirror_l - b_rad  # СѓРіРѕР» РѕС‚СЂР°Р¶РµРЅРёСЏ РІ СЂР°РґРёР°РЅР°С…

    mirror(x0_right, y0_right, alpha_mirror)
    mirror_l(x0_left, y0_left, alpha_mirror_l)

    # РЅРµСЃРєРѕР»СЊРєРѕ Р»СѓС‡РµР№
    if b == 270:
        step = 15
        step = round(step / abs(math.sin(b_rad)))
        for i in range(0, n, step):  # Р—Р°РїРѕР»РЅРµРЅРёРµ РІРµСЂС…Р° Р»СѓС‡Р°РјРё
            padenie(n - 2, i, b_rad)
    elif b < 270:
        step = 20
        if 225 < b:
            step = round(step / abs(math.sin(b_rad)))
            for i in range(0, n, round(step * abs(
                    1 * (math.tan(b_rad))))):  # Р—Р°РїРѕР»РЅРµРЅРёРµ Р»РµРІРѕРіРѕ Р±РѕРєР° Р»СѓС‡Р°РјРё
                padenie(i, n - 2, b_rad)
            for i in range(0, n,
                           round(step * abs(1 * math.sin(b_rad)))):  # Р—Р°РїРѕР»РЅРµРЅРёРµ РІРµСЂС…Р° Р»СѓС‡Р°РјРё
                padenie(n - 2, i, b_rad)
        else:
            step = round(step / abs(math.tan(b_rad)))
            for i in range(0, n, round(step * abs(
                    math.tan(b_rad)))):  # Р—Р°РїРѕР»РЅРµРЅРёРµ РїСЂР°РІРѕРіРѕ Р±РѕРєР° Р»СѓС‡Р°РјРё
                padenie(i, n - 2, b_rad)
            for i in range(0, n, round(step * abs(math.cos(b_rad)))):  # Р—Р°РїРѕР»РЅРµРЅРёРµ РІРµСЂС…Р° Р»СѓС‡Р°РјРё
                padenie(n - 2, i, b_rad)
    elif b > 270:
        step = 20
        if b > 315:
            step = round(step * abs(math.sin(b_rad)))
            for i in range(0, n, round(step * abs(
                    (1 / (math.tan(b_rad)))))):  # Р—Р°РїРѕР»РЅРµРЅРёРµ Р»РµРІРѕРіРѕ Р±РѕРєР° Р»СѓС‡Р°РјРё
                padenie(i, 1, b_rad)
            for i in range(0, n, round(step * abs(
                    (1 / math.sin(b_rad))) ** 2)):  # Р—Р°РїРѕР»РЅРµРЅРёРµ РІРµСЂС…Р° Р»СѓС‡Р°РјРё
                padenie(n - 2, i, b_rad)
        else:
            step = round(step * abs(math.sin(b_rad)))
            for i in range(0, n, round(step * abs(
                    (math.tan(b_rad))))):  # Р—Р°РїРѕР»РЅРµРЅРёРµ Р»РµРІРѕРіРѕ Р±РѕРєР° Р»СѓС‡Р°РјРё
                padenie(i, 1, b_rad)
            for i in range(0, n, round(step / abs(math.sin(b_rad)))):  # Р—Р°РїРѕР»РЅРµРЅРёРµ РІРµСЂС…Р° Р»СѓС‡Р°РјРё
                padenie(n - 2, i, b_rad)

    plt.figure(figsize=(5, 5))  # СЂР°Р·РјРµСЂ РїРѕР»СЏ РІ РґСЋР№РјР°С…
    show_2d_array(array)
    return rays, rays_out_mirror


if __name__ == '__main__':
    mainfunc(30, 80, 70, 0)
