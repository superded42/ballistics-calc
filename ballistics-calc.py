
import math
import plotext as plt
from termcolor import colored

print()
print('Баллистический калькулятор')
print()
print('Вам придется выяснить несколько характеристик')
g = 9.80665
S_x = float(input('Введите дальность полета в метрах. Измеряйте от основания механизма запуска: '))# Дальность найденная экспериментально
a = float(input('Введите угол наклона вектора начальной скорости в градусах: '))
a = math.radians(a)
h0 = float(input('Введите высоту, на которой находится механизм запуска: '))
l = float(input('Введите длину механизма запуска: '))
if l == 0:
    print(f'Нельзя на 0 делить')
    exit()
L_exp=S_x-l*math.cos(a)
v0_0 = (L_exp/math.cos(a))*math.sqrt(g/(2*(L_exp*math.tan(a)+h0+l*math.sin(a))))# Отправная скорость, найденная без силы сопротивления воздуха
t = L_exp/(v0_0*math.cos(a))# Теоретическое время полета
m = float(input('Введите массу снаряда в кг: '))
if m == 0:
    print('Нельзя на 0 делить')
    exit()
r = float(input('Введите радиус снаряда в м: '))
print()
trenie = int(input('В механизме присутствует трение: \n1 - да, \n0 - нет \nУкажите цифру: '))
if trenie == 1:
    mu = float(input('Укажите коэффициент трения (default - 0.15): ') or 0.15)
    F_trenie = mu*m*g*math.cos(a)
    print()
elif trenie == 0:
    F_trenie = 0
    print()
else:
    print('Неверные значения')
    exit()
print('Характеристики среды полета:')
tempC = float(input('Введите температуру воздуха в градусах Цельсия: '))
RH = float(input('Введите влажность воздуха в %: '))

#Вычисляем давление насыщенного пара в гПа по методу Ардена Бака
if tempC >= 0:
    E=6.1121*math.exp((17.502*tempC)/(240.97+tempC))
else:
    E=6.1115*math.exp((22.452*tempC)/(272.55+tempC))
E=E*100
e=E*RH/100 # Реальное давление пара

temp = tempC + 273.15 # Перевод температуры в Кельвины
rt_st = float(input('Введите атмосферное давление в мм рт. ст. : '))
print()

#================================================
# Учитываем скорость и направление ветра
nv = int(input('Укажите направление ветра: \n1. С\n2. С-В\n3. В\n4. Ю-В\n5. Ю\n6. Ю-З\n7. З\n8. С-З\nУкажите одну из 8 цифр: '))
print()

nb = int(input('Укажите направление запуска: \n1. С\n2. С-В\n3. В\n4. Ю-В\n5. Ю\n6. Ю-З\n7. З\n8. С-З\nУкажите одну из 8 цифр: '))
print()

w = float(input('Введите скорость ветра в м/с: '))
wx = 0 # скорость ветра в проеции на ОХ. Начальное условие
wz= 0 # скорость ветра в проекции на ОZ. Начальное условие
#Если северное направление компаса принять за направление ОХ, а восточное за нарпавление ОZ, движение ветра на восток меняет wz в положительном направлении, а на запад - в отрицательном и так далее в зависимости от направления броска
# Бросок на север
if nb == 1 and nv == 1:
    wx=-w
    wz=0
elif nb == 1 and nv == 2:
    wx=-w*math.cos(math.pi/4)
    wz=wx
elif nb == 1 and nv == 3:
    wx = 0
    wz = -w
elif nb == 1 and nv == 4:
    wx = w*math.cos(math.pi/4)
    wz = -wx
elif nb == 1 and nv == 5:
    wx = w
    wz = 0
elif nb == 1 and nv == 6:
    wx = w*math.cos(math.pi/4)
    wz = wx
elif nb == 1 and nv == 7:
    wx = 0
    wz = w
elif nb == 1 and nv == 8:
    wx = -w*math.cos(math.pi/4)
    wz = -wx

# Бросок на северо-восток
elif nb == 2 and nv == 1:
    wx = -w* math.cos(math.pi/4)
    wz = -wx
elif nb == 2 and nv == 2:
    wx = -w
    wz = 0 
elif nb == 2 and nv == 3:
    wx = -w*math.cos(math.pi/4)
    wz = wx
elif nb == 2 and nv == 4:
    wx = 0
    wz = -w
elif nb == 2 and nv == 5:
    wx = w*math.cos(math.pi/4)
    wz = -wx
elif nb == 2 and nv == 6:
    wx = w
    wz = 0
elif nb == 2 and nv == 7:
    wx = w*math.cos(math.pi/4)
    wz = wx
elif nb == 2 and nv == 8:
    wx = 0
    wz = w

# Бросок на восток
elif nb == 3 and nv == 1:
    wx =0
    wz = w
elif nb == 3 and nv == 2:
    wx = -w*math.cos(math.pi/4)
    wz = -wx
elif nb == 3 and nv == 3:
    wx = -w
    wz = 0
elif nb == 3 and nv == 4:
    wx = -w*math.cos(math.pi/4)
    wz = wx
elif nb == 3 and nv == 5:
    wx = 0
    wz = -w
elif nb == 3 and nv == 6:
    wx = w*math.cos(math.pi/4)
    wz = -wx
elif nb == 3 and nv == 7:
    wx = w
    wz = 0
elif nb == 3 and nv == 8:
    wx = w*math.cos(math.pi/4)
    wz = wx

# Бросок на юго-восток
elif nb == 4 and nv == 1:
    wx = w*math.cos(math.pi/4)
    wz = wx
elif nb == 4 and nv == 2:
    wx = 0
    wz = w
elif nb == 4 and nv == 3:
    wx = -w*math.cos(math.pi/4)
    wz = -wx
elif nb == 4 and nv == 4:
    wx = -w
    wz = 0
elif nb == 4 and nv == 5:
    wx = -w*math.cos(math.pi/4)
    wz = wx
elif nb == 4 and nv == 6:
    wx = 0
    wz = -w
elif nb == 4 and nv == 7:
    wx = w*math.cos(math.pi/4)
    wz = -wx
elif nb == 4 and nv == 8:
    wx = w
    wz = 0 

# Бросок на юг
elif nb == 5 and nv == 1:
    wx = w
    wz = 0 
elif nb == 5 and nv == 2:
    wx = w*math.cos(math.pi/4)
    wz = wx
elif nb == 5 and nv == 3:
    wx = 0
    wz = w
elif nb == 5 and nv == 4:
    wx = -w*math.cos(math.pi/4)
    wz = -wx
elif nb == 5 and nv == 5:
    wx = - w
    wz = 0
elif nb == 5 and nv == 6:
    wx = -w*math.cos(math.pi/4)
    wz = wx
elif nb == 5 and nv == 7:
    wx = 0
    wz = -w
elif nb == 5 and nv == 8:
    wx = w*math.cos(math.pi/4)
    wz = -wx

# Бросок на юго-запад
elif nb == 6 and nv == 1:
    wx = w*math.cos(math.pi/4)
    wz = -wx
elif nb == 6 and nv == 2:
    wx = w
    wz = 0
elif nb == 6 and nv == 3:
    wx = w*math.cos(math.pi/4)
    wz = wx
elif nb == 6 and nv == 4:
    wx = 0
    wz = w
elif nb == 6 and nv == 5:
    wx = -w*math.cos(math.pi/4)
    wz = -wx
elif nb == 6 and nv == 6:
    wx = -w 
    wz = 0
elif nb == 6 and nv == 7:
    wx = -w*math.cos(math.pi/4)
    wz = wx
elif nb == 6 and nv == 8:
    wx = 0
    wz = -w

# Бросок на запад
elif nb == 7 and nv == 1:
    wx = 0
    wz = -w
elif nb == 7 and nv == 2:
    wx = w*math.cos(math.pi/4)
    wz = -wx
elif nb == 7 and nv == 3: 
    wx = w
    wz = 0
elif nb == 7 and nv == 4:
    wx = w*math.cos(math.pi/4)
    wz = wx
elif nb == 7 and nv == 5:
    wx = 0
    wz = w
elif nb == 7 and nv == 6:
    wx = -w*math.cos(math.pi/4)
    wz = -wx
elif nb == 7 and nv == 7:
    wx = -w
    wz = 0
elif nb == 7 and nv == 8:
    wx = -w*math.cos(math.pi/4)
    wz = wx

# Бросок на северо-запад
elif nb == 8 and nv == 1:
    wx = -w*math.cos(math.pi/4)
    wz = wx
elif nb == 8 and nv == 2:
    wx = 0
    wz = -w
elif nb == 8 and nv == 3:
    wx = w*math.cos(math.pi/4)
    wz = -wx
elif nb == 8 and nv == 4:
    wx = w
    wz = 0
elif nb == 8 and nv == 5:
    wx = w*math.cos(math.pi/4)
    wz = wx
elif nb == 8 and nv == 6:
    wx = 0
    wz = w
elif nb == 8 and nv == 7:
    wx = -w*math.cos(math.pi/4)
    wz = -wx
elif nb == 8 and nv == 8:
    wx = -w
    wz = 0
else:
    print('Неверные значения ввода сторон света')
    exit()
#================================================

koef = 101325/760 # Коэффициент перевода мм рт. ст. в Па
p = rt_st*koef # Перевод мм рт. ст. в Па

Mo = 28.9644*10**(-3) # молярная масса воздуха
Mh = 18.0152*10**(-3) # молярная масса водяного пара
R = 8.31446261815324 # Универсальная газовая постоянная
C = 0.47 # Коэффициент лобового столкновения
rho = ((p-e)*Mo+e*Mh)/(R*temp) # Плотность воздуха
beta= C*rho*math.pi*r**2/(4)

print()
print('Для чистоты эксперимента запуск должен совершаться методом толкания ядра')
print()

# Теоретические характеристики
y = h0 + l*math.sin(a) +v0_0*math.sin(a)*t - g*t**2/2
D = (2*v0_0*math.sin(a))**2 + 4*g*2*(h0+l*math.sin(a))
tao = (2*v0_0*math.sin(a)+math.sqrt(D))/(2*g) - (math.sqrt(D))/(2*g)
H = h0 +l*math.sin(a) + v0_0*math.sin(a)*tao - g*tao**2/2

G = int(input('Учитываем сопротивление воздуха? 1 - да, 0 - нет: '))
if G == 0:
    beta=0
print()
print()

times, heights, speed, Kin, Pot, Meh, vg, vv, lp, Fsv, lz, vp = [], [], [], [], [], [], [], [], [], [], [], []# Команда задает массивы


# Метод бисекции
L_calc = 0
L_calc_prev = 0
v_min = v0_0
v_max = v0_0*1.3
dt = 0.0001

max_iter = 500
iter_count=0
while abs(L_calc-L_exp)>0.01:
    iter_count +=1
    if iter_count > max_iter:
        print('Ошибка: бесконечный цикл')
        exit()

    #1. Формула нахождения оптимальной реальной скорости
    v_mid = (v_min+ v_max)/2
    if v_mid > 2000:
        print(f'Ошибка: получается слишком большая начальная скорость ({v_mid:.1f} м/с)')
        exit()

    t=0
    x=0
    z=0
    y_max=0
    t_ymax=0
    y=h0+l*math.sin(a)
    vx=v_mid*math.cos(a)
    vy=v_mid*math.sin(a)
    vz=0
    
    #2. Численный полет по методу Эйлера
#    while y > 0:
#        ux=vx-wx # скорость снаряда по Х относительно воздуха
#        uy=vy # скорость снаряда по У относитльно воздуха
#        uz=vz-wz
#        u=math.sqrt(ux**2+uy**2+uz**2)
#        v=math.sqrt(vx**2+vy**2+vz**2)
#        ax=-(beta/(m/2))*u*ux
#        ay=-g-(beta/(m/2))*u*uy
#        az=-(beta/(m/2))*u*uz

#        vx=vx+ax*dt
#        vy=vy+ay*dt
#        vz=vz+az*dt
#        x=x+vx*dt
#        y=y+vy*dt
#        z=z+vz*dt
#        t=t+dt 

    #2.1 Метод Рунге-Кутты
    while y > 0:
        # Шаг 1: k1 в начале шага
        ux1=vx-wx
        uy1=vy
        uz1=vz-wz
        u1=math.sqrt(ux1**2+uy1**2+uz1**2)
        ax1=-(beta/(m/2))*u1*ux1
        ay1=-g-(beta/(m/2))*u1*uy1
        az1=-(beta/(m/2))*u1*uz1

        k1_vx=ax1*dt
        k1_vy=ay1*dt
        k1_vz=az1*dt
        k1_x=vx*dt
        k1_y=vy*dt
        k1_z=vz*dt

        #шаг 2:k2  в середине шага, используя k1
        vx_mid=vx+0.5*k1_vx
        vy_mid=vy+0.5*k1_vy
        vz_mid=vz+0.5*k1_vz
        x_mid=x+0.5*k1_x
        y_mid=y+0.5*k1_y
        z_mid=z+0.5*k1_z

        ux2 = vx_mid-wx
        uy2=vy_mid
        uz2=vz_mid-wz
        u2=math.sqrt(ux2**2+uy2**2+uz2**2)
        ax2=-(beta/(m/2))*u2*ux2
        ay2=-g-(beta/(m/2))*u2*uy2
        az2=-(beta/(m/2))*u2*uz2

        k2_vx=ax2*dt
        k2_vy=ay2*dt
        k2_vz=az2*dt
        k2_x=vx_mid*dt
        k2_y=vy_mid*dt
        k2_z=vz_mid*dt

        #Шаг 3: k3 опять в середине, используя k2
        vx_mid = vx+0.5*k2_vx
        vy_mid=vy+0.5*k2_vy
        vz_mid=vz+0.5*k2_vz
        x_mid=x+0.5*k2_x
        y_mid=y+0.5*k2_y
        z_mid=z+0.5*k2_z

        ux3=vx_mid-wx
        uy3=vy_mid
        uz3=vz_mid-wz
        u3=math.sqrt(ux3**2+uy3**2+uz3**2)
        ax3=-(beta/(m/2))*u3*ux3
        ay3=-g-(beta/(m/2))*u3*uy3
        az3=-(beta/(m/2))*u3*uz3

        k3_vx=ax3*dt
        k3_vy=ay3*dt
        k3_vz=az3*dt
        k3_x=vx_mid*dt
        k3_y=vy_mid*dt
        k3_z=vz_mid*dt

        #Шаг 4: k4 в конце, используя k3
        vx_end=vx+k3_vx
        vy_end=vy+k3_vy
        vz_end=vz+k3_vz
        x_end=x+k3_x
        y_end=y+k3_y
        z_end=z+k3_z

        ux4=vx_end-wx
        uy4=vy_end
        uz4=vz_end-wz
        u4=math.sqrt(ux4**2+uy4**2+uz4**2)
        ax4=-(beta/(m/2))*u4*ux4
        ay4=-g-(beta/(m/2))*u4*uy4
        az4=-(beta/(m/2))*u4*uz4

        k4_vx=ax4*dt
        k4_vy=ay4*dt
        k4_vz=az4*dt
        k4_x=vx_end*dt
        k4_y=vy_end*dt
        k4_z=vz_end*dt

        #Финальное обновление (усреднение с весами 1,2,2,1)
        vx=vx+(k1_vx+2*k2_vx+2*k3_vx+k4_vx)/6
        vy=vy+(k1_vy+2*k2_vy+2*k3_vy+k4_vy)/6
        vz=vz+(k1_vz+2*k2_vz+2*k3_vz+k4_vz)/6
        x=x+(k1_x+2*k2_x+2*k3_x+k4_x)/6
        y=y+(k1_y+2*k2_y+2*k3_y+k4_y)/6
        z=z+(k1_z+2*k2_z+2*k3_z+k4_z)/6
        t=t+dt

    L_calc=x

    # Защита от зацикливания
    if abs(L_calc - L_calc_prev) < 1e-6 and iter_count>5:
        print('Ошибка: нереальные значения')
        exit()
    L_calc_prev=L_calc

    if L_calc < L_exp:
        v_min = v_mid
    if L_calc > L_exp:
        v_max = v_mid
v0=v_mid # Реальная начальная скорость
T_full=t # Реальное время полета




#=============================================
# Финальный прогон с найденным v0:
t = 0
x = 0
z = 0
y= h0+ l*math.sin(a)
y_max = y
t_ymax = 0
vx = v0*math.cos(a)
vy = v0*math.sin(a)
vz=0

next_target = 0.0000000000000000000000000000001
last_recorder = 0

#Метод Эйлера
#while y > 0:
#    ux=vx-wx
#    uy=vy
#    uz=vz-wz
#    u=math.sqrt(ux**2+uy**2+uz**2)
#    v=math.sqrt(vx**2+vy**2+vz**2)
#    ax=-(beta/(m/2))*u*ux
#    ay=-g-(beta/(m/2))*u*uy
#    az=-(beta/(m/2))*u*uz

#    vx = vx + ax*dt
#    vy = vy + ay*dt
#    vz = vz + az*dt
#    x = x + vx*dt
#    y = y + vy*dt
#    z = z + vz*dt
#    t = t + dt


#Метод Рунге-Кутты
while y > 0:
    # Шаг 1: k1 в начале шага
    ux1=vx-wx
    uy1=vy
    uz1=vz-wz
    u1=math.sqrt(ux1**2+uy1**2+uz1**2)
    ax1=-(beta/(m/2))*u1*ux1
    ay1=-g-(beta/(m/2))*u1*uy1
    az1=-(beta/(m/2))*u1*uz1

    k1_vx=ax1*dt
    k1_vy=ay1*dt
    k1_vz=az1*dt
    k1_x=vx*dt
    k1_y=vy*dt
    k1_z=vz*dt

    #шаг 2:k2  в середине шага, используя k1
    vx_mid=vx+0.5*k1_vx
    vy_mid=vy+0.5*k1_vy
    vz_mid=vz+0.5*k1_vz
    x_mid=x+0.5*k1_x
    y_mid=y+0.5*k1_y
    z_mid=z+0.5*k1_z

    ux2 = vx_mid-wx
    uy2=vy_mid
    uz2=vz_mid-wz
    u2=math.sqrt(ux2**2+uy2**2+uz2**2)
    ax2=-(beta/(m/2))*u2*ux2
    ay2=-g-(beta/(m/2))*u2*uy2
    az2=-(beta/(m/2))*u2*uz2

    k2_vx=ax2*dt
    k2_vy=ay2*dt
    k2_vz=az2*dt
    k2_x=vx_mid*dt
    k2_y=vy_mid*dt
    k2_z=vz_mid*dt

    #Шаг 3: k3 опять в середине, используя k2
    vx_mid = vx+0.5*k2_vx
    vy_mid=vy+0.5*k2_vy
    vz_mid=vz+0.5*k2_vz
    x_mid=x+0.5*k2_x
    y_mid=y+0.5*k2_y
    z_mid=z+0.5*k2_z

    ux3=vx_mid-wx
    uy3=vy_mid
    uz3=vz_mid-wz
    u3=math.sqrt(ux3**2+uy3**2+uz3**2)
    ax3=-(beta/(m/2))*u3*ux3
    ay3=-g-(beta/(m/2))*u3*uy3
    az3=-(beta/(m/2))*u3*uz3

    k3_vx=ax3*dt
    k3_vy=ay3*dt
    k3_vz=az3*dt
    k3_x=vx_mid*dt
    k3_y=vy_mid*dt
    k3_z=vz_mid*dt

    #Шаг 4: k4 в конце, используя k3
    vx_end=vx+k3_vx
    vy_end=vy+k3_vy
    vz_end=vz+k3_vz
    x_end=x+k3_x
    y_end=y+k3_y
    z_end=z+k3_z

    ux4=vx_end-wx
    uy4=vy_end
    uz4=vz_end-wz
    u4=math.sqrt(ux4**2+uy4**2+uz4**2)
    ax4=-(beta/(m/2))*u4*ux4
    ay4=-g-(beta/(m/2))*u4*uy4
    az4=-(beta/(m/2))*u4*uz4

    k4_vx=ax4*dt
    k4_vy=ay4*dt
    k4_vz=az4*dt
    k4_x=vx_end*dt
    k4_y=vy_end*dt
    k4_z=vz_end*dt

    #Финальное обновление (усреднение с весами 1,2,2,1)
    vx=vx+(k1_vx+2*k2_vx+2*k3_vx+k4_vx)/6
    vy=vy+(k1_vy+2*k2_vy+2*k3_vy+k4_vy)/6
    vz=vz+(k1_vz+2*k2_vz+2*k3_vz+k4_vz)/6
    x=x+(k1_x+2*k2_x+2*k3_x+k4_x)/6
    y=y+(k1_y+2*k2_y+2*k3_y+k4_y)/6
    z=z+(k1_z+2*k2_z+2*k3_z+k4_z)/6
    t=t+dt


    # Максимум высоты
    if y > y_max:
        y_max=y
        t_ymax=t

    #Найдем характеристики балистики в целочисленные моменты времени при движении
    if t>= next_target and next_target > last_recorder and y > 0:
        last_recorder = t
        next_target= next_target + 1.0

        ux=vx-wx
        uy=vy
        uz=vz-wz

        # Блок показывает, как изменяется сила сопротивления воздуха в разные моменты времени
        F_svx=beta*math.sqrt(ux**2+uy**2+uz**2)*ux
        F_svy=beta*math.sqrt(ux**2+uy**2+uz**2)*uy
        F_svz=beta*math.sqrt(ux**2+uy**2+uz**2)*uz
        F_sv=math.sqrt(F_svx**2+F_svy**2+F_svz**2)

        v = math.sqrt(vx**2+vy**2+vz**2)


        # Определяем массивы
        times.append(t)
        heights.append(y)
        speed.append(v)
        Kin.append(m*(vx**2+vy**2+vz**2)/2)
        Pot.append(m*g*y)
        Meh.append(m*g*y+m*(vx**2+vy**2+vz**2)/2)
        vg.append(vx)
        vv.append(vy)
        vp.append(vz)
        lp.append(x)
        lz.append(z)
        Fsv.append(F_sv)

            
        print(f'В момент времени {t:.4f} c:')  # печатаем текущее время
        print(f'Горизонтальная скорость снаряда: {vx:.4f} м/с')
        print(f'Вертикальная скорость снаряда: {vy:.4f} м/с')
        print(f'Модуль реальной скорости: {math.sqrt(vx**2+vy**2+vz**2):.4f} м/с')
        print(f'Угол наклона реальной скорости снаряда к горизонту: {abs(math.degrees(math.atan2(vy, vx))):.4f}')
        print(f'Высота: {y:.4f} м')
        print(f'Реальное горизонтальное перемещение снаряда: {x:.4f} м')
        if z > 0:
            print(f'Смещение вправо из-за поперечного ветра: {z:.4f} м')
        elif z == 0 :
            print(f'Нет смещения в сторону')
        else:
            print(f'Смещение влево из-за поперечного ветра: {abs(z):.4f} м')
        print(f'Кинетическая энергия: {m*(vx**2+vy**2+vz**2)/2:.4f} Дж')
        print(f'Потенциальная энергия: {m*g*y:.4f} Дж')
        print(f'Полная механическая энергия: {m*(vx**2+vy**2+vz**2)/2+m*g*y:.4f} Дж')
        print(f'Модуль силы сопротивления воздуха: {F_sv:.4f} Н')
        print()
        print()

vx_last = vx #Скорость перед падением по оси Х
vy_last = vy #Скорость перед падением по оси У
vz_last = vz #Скорость перед падением по оси Z
v_last = math.sqrt(vx**2+vy**2+vz**2) #Модуль реальной скорости перед падением
a_last = abs(math.degrees(math.atan2(vy, vx))) #Угол к горизонту в момент падения


# Добавляем точку падения
times.append(t)
heights.append(0.0)
speed.append(0.0)
vg.append(0.0)
vv.append(0.0)
vp.append(0.0)
lp.append(x)
lz.append(z)
Kin.append(0.0)
Pot.append(0.0)
Meh.append(0.0)

T_full = t
L_calc = x

# Создаем графики c plotext
# График траектория h(l)
plt.theme("dark") # Темная тема
plt.plot(lp, heights, marker='dot', color='orange') # Задаем аргумент и функцию. marker - отрисовка на графике. color - цвет
plt.title("Y")# Название графика
plt.xlabel("X")# Название оси Х

plt.plotsize(80, 30)# Размер графика в терминале
plt.show() # Показать график

plt.clf() # Очищение памяти plotext от первого графика

print()
print()
# z(x)
plt.theme("dark")
plt.plot(lp, lz, marker='dot', color='orange')
plt.title("Z")
plt.xlabel("X")
plt.plotsize(80, 30)
plt.show()
plt.clf()
print()
print()

# График h(T)и l(T)
plt.theme("dark")
plt.plot(times, heights, marker='dot', color='red')
plt.plot(times, lp, marker='dot', color='green')
plt.title("Высота - красный, Sx - зеленый (м)")
plt.xlabel("Момент времени (с)")
plt.plotsize(80, 30)
plt.show()
plt.clf()
print()
print()

# График vx(T), vy(T), vz(T) и |v|(T)
plt.theme("dark")
plt.plot(times, vg, marker='dot', color='red')# график горизонтальной скорости
plt.plot(times, vv, marker='dot', color='green')# график вертикальной скорости
plt.plot(times, speed, marker='dot', color='orange')
plt.plot(times, vp, marker='dot', color='blue') # график поперечной скорости
plt.title("\nVx - красный, Vy - зеленый, Vz - синий, |V| - оранжевый (м/с)")
plt.xlabel("Момент времени (с)")
plt.plotsize(80, 30)
plt.show()
plt.clf()
print()
print()

# График v(T)
plt.theme("dark")
plt.plot(times, speed, marker='dot', color='orange')
plt.title("Модуль реальной мгновенной скорости (м/с)")
plt.xlabel("Момент времени (с)")
plt.plotsize(80, 30)
plt.show()
plt.clf()
print()
print()

# График Ek, Ep, Em от времени
plt.theme("dark")
plt.plot(times, Kin, marker='dot', color='blue')
plt.plot(times, Pot, marker='dot', color='white')
plt.plot(times, Meh, marker='dot', color='green')
plt.title('Ек - синий, Еп - белый, Ем - зеленый (Дж)')
plt.xlabel('Момент времени (с)')
plt.plotsize(80, 30)
plt.show()
plt.clf()
print()
print()

# График модуля силы сопротивления воздуха от вермени
plt.theme("dark")
plt.plot(times, Fsv, marker='dot', color='orange')
plt.title('Модуль силы сопротивления воздуха (Н)')
plt.xlabel('Момент вермени (c)')
plt.plotsize(80, 30)
plt.show()
print()
print()


# Пропишем характеристики балистики при остановке снаряда
print(f'В момент времени {T_full:.4f} c:')
print('Горизонтальная скорость: 0 м/с')
print('Вертикальная скорость: 0 м/с')
print('Модуль реальной скорости: 0 м/с')
print('Высота: 0 м')
print(f'Заданная дальность полета от основания механизма запуска: {S_x} м')
print(f'Реальное горизонтальное перемещение снаряда: {x:.4f} м')
if z > 0:
    print(f'Смещение вправо из-за поперечного ветра: {z:.4f} м')
elif z == 0:
    print('Нет смещения в сторону')
else:
    print(f'Смещение влево из-за поперечного ветра: {abs(z):.4f} м')
print('Кинетическая энергия:0 Дж')
print('Потенциальная энергия: 0 Дж')
print('Полная механическая энергия: 0 Дж')
print()
print()


print(f'Плотность воздуха составила: {rho:.4f} кг/м^3')
print()
# Подставляем найденное значение v0 в формулу силы:
F = m*v0**2/(2*l)+m*g*math.sin(a)+beta*v0**2+F_trenie

print(f'{F_trenie:.4f} Н - модуль силы трения механизма')
print(f'{T_full:.4f} с - полное время полета')
print(f'{t_ymax:.4f} с - время подъема до максимальной высоты')
print(f'{y_max:.4f} м - максимальная высота')
if G == 0:
    print(f'{v0_0:.4f} м/с - реальная начальная скорость')
else:
    print(f'{v0:.4f} м/с - реальная начальная скорость')
print(f'{v_last:.4f} м/с - модуль скорости при ударе о землю')
print(f'{a_last:.4f} градусов - угол при ударе о землю')
print()

# Находим потерю полной механической энергии
if len(Meh)>=2:
    E_n=Meh[0]
    E_k=Meh[-2]
    E_r=E_n-E_k
    E_rp=(E_r/E_n)*100

    print(colored(f'Потеря полной механической энергии за полет: {E_r:.4f} Дж','yellow'))
    print(colored(f'Относительная потеря полной механической энергии за полет: {E_rp:.4f} %','yellow'))

    print()

print(colored(f'{F:.4f} Н - сила запуска','yellow'))

