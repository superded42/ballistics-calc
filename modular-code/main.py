# Главный код модуля

import math
import plotext as plt
from termcolor import colored
from data import data_entry
from physics_base import fizika
from wind import windout
from rk4 import rk4f
from rk4 import finrk
from charts import graf

# Константы
g = 9.80665
Mo = 28.9644 * 10**(-3)
Mh = 18.0152 * 10**(-3)
R = 8.31446261815324
C = 0.47
koef = 101325 / 760

print()
print('Баллистический калькулятор')
print()
print('Вам придется выяснить несколько характеристик')

inp = data_entry(g)
fiz = fizika(inp, g, koef, C, R, Mo, Mh)
wxz = windout(inp)

beta = fiz['beta']
G = int(input('Учитываем сопротивление воздуха? 1 - да, 0 - нет: '))
if G == 0:
    beta = 0
print()
print()
a = inp['a']

# Метод бисекции
L_calc = 0
L_calc_prev = 0
v_min = fiz['v0_0']
v_max = fiz['v0_0'] * 1.3
dt = 0.0001

max_iter = 500
iter_count = 0
while abs(L_calc - fiz['L_exp']) > 0.01:
    iter_count += 1
    if iter_count > max_iter:
        print('Ошибка: бесконечный цикл')
        exit()

    v_mid = (v_min + v_max) / 2
    if v_mid > 2000:
        print(f'Ошибка: получается слишком большая начальная скорость ({v_mid:.1f} м/с)')
        exit()

    t = 0
    x = 0
    z = 0
    y_max = 0
    t_ymax = 0
    y = inp['h0'] + inp['l'] * math.sin(a)
    vx = v_mid * math.cos(a)
    vy = v_mid * math.sin(a)
    vz = 0

    #Подруб Рунге-Кутты
    rk = rk4f(x, y, z, y_max, t_ymax, vx, vy, vz, g, dt, beta, inp, wxz)
    L_calc = math.sqrt(rk['x']**2 + rk['z']**2)

    if abs(L_calc - L_calc_prev) < 1e-6 and iter_count > 5:
        print('Ошибка: нереальные значения')
        exit()
    L_calc_prev = L_calc

    if L_calc < fiz['L_exp']:
        v_min = v_mid
    if L_calc > fiz['L_exp']:
        v_max = v_mid

v0 = v_mid

# Финальный прогон
t = 0
x = 0
z = 0
y = inp['h0'] + inp['l'] * math.sin(a)
y_max = y
t_ymax = 0
vx = v0 * math.cos(a)
vy = v0 * math.sin(a)
vz = 0

times, heights, speed, Kin, Pot, Meh, vg, vv, lp, Fsv, lz, vp = [], [], [], [], [], [], [], [], [], [], [], []

next_target = 0.0000000000000000000000000000001
last_recorder = 0

rk = finrk(x, y, z, y_max, t_ymax, vx, vy, vz, g, dt, beta, inp, wxz,
           next_target, last_recorder, times, heights, speed, Kin, Pot, Meh,
           vg, vv, lp, Fsv, lz, vp)

y_max = rk['y_max']
t_ymax = rk['t_ymax']
vx_last = rk['vx']
vy_last = rk['vy']
vz_last = rk['vz']
v_last = math.sqrt(rk['vx']**2 + rk['vy']**2 + rk['vz']**2)
a_last = abs(math.degrees(math.atan2(rk['vy'], rk['vx'])))

# Добавляем точку падения
times.append(rk['t'])
heights.append(0.0)
speed.append(0.0)
vg.append(0.0)
vv.append(0.0)
vp.append(0.0)
lp.append(rk['x'])
lz.append(rk['z'])
Kin.append(0.0)
Pot.append(0.0)
Meh.append(0.0)

T_full = rk['t']
L_calc = math.sqrt(rk['x']**2 + rk['z']**2)

# Отображение графиков
graf(times, heights, speed, vg, vv, vp, lp, lz, Kin, Pot, Meh, Fsv)

# Вывод результатов
print(f"В момент времени {T_full:.4f} c:")
print('Горизонтальная скорость: 0 м/с')
print('Вертикальная скорость: 0 м/с')
print('Скорость поперечного движения : 0 м/с')
print('Модуль реальной скорости: 0 м/с')
print('Высота: 0 м')
print(f"Заданная дальность полета от основания механизма запуска: {inp['S_x']} м")
print(f"Перемещение снаряда вдоль запуска: {rk['x']:.4f} м")
if rk['z'] > 0:
    print(f"Смещение вправо из-за поперечного ветра: {rk['z']:.4f} м")
elif rk['z'] == 0:
    print('Нет смещения в сторону')
else:
    print(f"Смещение влево из-за поперечного ветра: {abs(rk['z']):.4f} м")
print(f"Реальное перемещение снаряда: {math.sqrt(rk['x']**2 + rk['z']**2):.4f} м")
print('Кинетическая энергия: 0 Дж')
print('Потенциальная энергия: 0 Дж')
print('Полная механическая энергия: 0 Дж')
print()
print()

print(f"Плотность воздуха составила: {fiz['rho']:.4f} кг/м^3")
print()

F = inp['m'] * v0**2 / (2 * inp['l']) + inp['m'] * g * math.sin(a) + beta * v0**2 + inp['F_trenie']

print(f"{inp['F_trenie']:.4f} Н - модуль силы трения механизма")
print(f"{T_full:.4f} с - полное время полета")
print(f"{t_ymax:.4f} с - время подъема до максимальной высоты")
print(f"{y_max:.4f} м - максимальная высота")
if G == 0:
    print(f"{fiz['v0_0']:.4f} м/с - реальная начальная скорость")
else:
    print(f"{v0:.4f} м/с - реальная начальная скорость")
print(f"{v_last:.4f} м/с - модуль скорости при ударе о землю")
print(f"{a_last:.4f} градусов - угол при ударе о землю")
print()

if len(Meh) >= 2:
    E_n = Meh[0]
    E_k = Meh[-2]
    E_r = E_n - E_k
    E_rp = (E_r / E_n) * 100

    if E_r > 0:
        print(colored(f'Потеря полной механической энергии за полет: {E_r:.4f} Дж', 'yellow'))
        print(colored(f'Относительная потеря полной механической энергии за полет: {E_rp:.4f} %', 'yellow'))
    elif E_r < 0:
        print(colored(f'Дополнительное приобретение энергии: {-E_r:.4f} Дж', 'yellow'))
        print(colored(f'Относительное приобретение энергии {-E_rp:.4f} %', 'yellow'))
    elif E_r == 0:
        print(colored('Нет потерь энергии', 'yellow'))
    print()

print(colored(f"{F:.4f} Н - сила запуска", 'yellow'))

input('Для выхода нажмите Enter: ')
