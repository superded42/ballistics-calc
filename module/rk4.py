import math

#Блок симуляции полета методом Эйлера и Рунге-Кутты
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
def rk4f(x, y, z, y_max, t_ymax, vx, vy, vz, g, dt, beta, inp, wxz):
    t=0
    wx=wxz['wx']
    wz=wxz['wz']
    m=inp['m']
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
    return{
            'vx':vx,
            'vy':vy,
            'vz':vz,
            'x':x,
            'y':y,
            'z':z,
            't':t
            }
#Функция финального прогона
def finrk(x, y, z, y_max, t_ymax, vx, vy, vz, g, dt, beta, inp, wxz, next_target, last_recorder, times, heights, speed, Kin, Pot, Meh, vg, vv, lp, Fsv, lz, vp):

    t=0
    wx=wxz['wx']
    wz=wxz['wz']
    m=inp['m']

    next_target = 0.0
    last_recorder=-1.0

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
    if rk['y'] > y_max:
        y_max=rk['y']
        t_ymax=rk['t']

    #Найдем характеристики балистики в целочисленные моменты времени при движении
    if t>= next_target and next_target > last_recorder and y > 0:
        last_recorder = t
        next_target= next_target + 1.0

        ux=rk['vx']-wxz['wx']
        uy=rk['vy']
        uz=rk['vz']-wxz['wz']

        # Блок показывает, как изменяется сила сопротивления воздуха в разные моменты времени
        F_svx=beta*math.sqrt(ux**2+uy**2+uz**2)*ux
        F_svy=beta*math.sqrt(ux**2+uy**2+uz**2)*uy
        F_svz=beta*math.sqrt(ux**2+uy**2+uz**2)*uz
        F_sv=math.sqrt(F_svx**2+F_svy**2+F_svz**2)

        v = math.sqrt(rk['vx']**2+rk['vy']**2+rk['vz']**2)


        # Определяем массивы
        times.append(rk['t'])
        heights.append(rk['y'])
        speed.append(v)
        Kin.append(inp['m']*(rk['vx']**2+rk['vy']**2+rk['vz']**2)/2)
        Pot.append(inp['m']*g*rk['y'])
        Meh.append(inp['m']*g*rk['y']+inp['m']*(rk['vx']**2+rk['vy']**2+rk['vz']**2)/2)
        vg.append(rk['vx'])
        vv.append(rk['vy'])
        vp.append(rk['vz'])
        lp.append(rk['x'])
        lz.append(rk['z'])
        Fsv.append(F_sv)

            
        print(f'В момент времени {rk['t']:.4f} c:')  # печатаем текущее время
        print(f'Горизонтальная скорость снаряда: {rk['vx']:.4f} м/с')
        print(f'Вертикальная скорость снаряда: {rk['vy']:.4f} м/с')
        print(f'Скорость поперечного движения: {rk['vz']:.4f} м/с')
        print(f'Модуль реальной скорости: {math.sqrt(rk['vx']**2+rk['vy']**2+rk['vz']**2):.4f} м/с')
        print(f'Угол наклона реальной скорости снаряда к горизонту: {abs(math.degrees(math.atan2(rk['vy'], rk['vx']))):.4f}')
        print(f'Высота: {y:.4f} м')
        print(f'Перемещение вдоль запуска: {rk['x']:.4f} м')
        if z > 0:
            print(f'Смещение вправо из-за поперечного ветра: {rk['z']:.4f} м')
        elif z == 0 :
            print(f'Нет смещения в сторону')
        else:
            print(f'Смещение влево из-за поперечного ветра: {abs(rk['z']):.4f} м')
        print(f'Реальное перемещение: {math.sqrt(rk['x']**2+rk['z']**2):.4f} м')
        print(f'Кинетическая энергия: {inp['m']*(rk['vx']**2+rk['vy']**2+rk['vz']**2)/2:.4f} Дж')
        print(f'Потенциальная энергия: {inp['m']*g*rk['y']:.4f} Дж')
        print(f'Полная механическая энергия: {inp['m']*(rk['vx']**2+rk['vy']**2+rk['vz']**2)/2+inp['m']*g*rk['y']:.4f} Дж')
        print(f'Модуль силы сопротивления воздуха: {F_sv:.4f} Н')
        print()
        print()
    return{
            'vx':vx,
            'vy':vy,
            'vz':vz,
            'x':x,
            'y':y,
            'z':z,
            't':t,
            'times':times,
            'heights':heights,
            'speed':speed,
            'Kin':Kin,
            'Pot':Pot,
            'Meh':Meh,
            'vg':vg,
            'vv':vv,
            'vp':vp,
            'lp':lp,
            'lz':lz,
            'Fsv':Fsv,
            'y_max':y_max,
            't_ymax':t_ymax
            }

