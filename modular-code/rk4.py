import math

def rk4f(x, y, z, y_max, t_ymax, vx, vy, vz, g, dt, beta, inp, wxz):
    t = 0
    wx = wxz['wx']
    wz = wxz['wz']
    m = inp['m']

    while y > 0:
        ux1 = vx - wx
        uy1 = vy
        uz1 = vz - wz
        u1 = math.sqrt(ux1**2 + uy1**2 + uz1**2)
        ax1 = -(beta / (m / 2)) * u1 * ux1
        ay1 = -g - (beta / (m / 2)) * u1 * uy1
        az1 = -(beta / (m / 2)) * u1 * uz1

        k1_vx = ax1 * dt
        k1_vy = ay1 * dt
        k1_vz = az1 * dt
        k1_x = vx * dt
        k1_y = vy * dt
        k1_z = vz * dt

        vx_mid = vx + 0.5 * k1_vx
        vy_mid = vy + 0.5 * k1_vy
        vz_mid = vz + 0.5 * k1_vz
        x_mid = x + 0.5 * k1_x
        y_mid = y + 0.5 * k1_y
        z_mid = z + 0.5 * k1_z

        ux2 = vx_mid - wx
        uy2 = vy_mid
        uz2 = vz_mid - wz
        u2 = math.sqrt(ux2**2 + uy2**2 + uz2**2)
        ax2 = -(beta / (m / 2)) * u2 * ux2
        ay2 = -g - (beta / (m / 2)) * u2 * uy2
        az2 = -(beta / (m / 2)) * u2 * uz2

        k2_vx = ax2 * dt
        k2_vy = ay2 * dt
        k2_vz = az2 * dt
        k2_x = vx_mid * dt
        k2_y = vy_mid * dt
        k2_z = vz_mid * dt

        vx_mid = vx + 0.5 * k2_vx
        vy_mid = vy + 0.5 * k2_vy
        vz_mid = vz + 0.5 * k2_vz
        x_mid = x + 0.5 * k2_x
        y_mid = y + 0.5 * k2_y
        z_mid = z + 0.5 * k2_z

        ux3 = vx_mid - wx
        uy3 = vy_mid
        uz3 = vz_mid - wz
        u3 = math.sqrt(ux3**2 + uy3**2 + uz3**2)
        ax3 = -(beta / (m / 2)) * u3 * ux3
        ay3 = -g - (beta / (m / 2)) * u3 * uy3
        az3 = -(beta / (m / 2)) * u3 * uz3

        k3_vx = ax3 * dt
        k3_vy = ay3 * dt
        k3_vz = az3 * dt
        k3_x = vx_mid * dt
        k3_y = vy_mid * dt
        k3_z = vz_mid * dt

        vx_end = vx + k3_vx
        vy_end = vy + k3_vy
        vz_end = vz + k3_vz
        x_end = x + k3_x
        y_end = y + k3_y
        z_end = z + k3_z

        ux4 = vx_end - wx
        uy4 = vy_end
        uz4 = vz_end - wz
        u4 = math.sqrt(ux4**2 + uy4**2 + uz4**2)
        ax4 = -(beta / (m / 2)) * u4 * ux4
        ay4 = -g - (beta / (m / 2)) * u4 * uy4
        az4 = -(beta / (m / 2)) * u4 * uz4

        k4_vx = ax4 * dt
        k4_vy = ay4 * dt
        k4_vz = az4 * dt
        k4_x = vx_end * dt
        k4_y = vy_end * dt
        k4_z = vz_end * dt

        vx = vx + (k1_vx + 2*k2_vx + 2*k3_vx + k4_vx) / 6
        vy = vy + (k1_vy + 2*k2_vy + 2*k3_vy + k4_vy) / 6
        vz = vz + (k1_vz + 2*k2_vz + 2*k3_vz + k4_vz) / 6
        x = x + (k1_x + 2*k2_x + 2*k3_x + k4_x) / 6
        y = y + (k1_y + 2*k2_y + 2*k3_y + k4_y) / 6
        z = z + (k1_z + 2*k2_z + 2*k3_z + k4_z) / 6
        t = t + dt

    return {
        'vx': vx,
        'vy': vy,
        'vz': vz,
        'x': x,
        'y': y,
        'z': z,
        't': t
    }


def finrk(x, y, z, y_max, t_ymax, vx, vy, vz, g, dt, beta, inp, wxz,
          next_target, last_recorder, times, heights, speed, Kin, Pot, Meh,
          vg, vv, lp, Fsv, lz, vp):
    t = 0
    wx = wxz['wx']
    wz = wxz['wz']
    m = inp['m']

    while y > 0:
        ux1 = vx - wx
        uy1 = vy
        uz1 = vz - wz
        u1 = math.sqrt(ux1**2 + uy1**2 + uz1**2)
        ax1 = -(beta / (m / 2)) * u1 * ux1
        ay1 = -g - (beta / (m / 2)) * u1 * uy1
        az1 = -(beta / (m / 2)) * u1 * uz1

        k1_vx = ax1 * dt
        k1_vy = ay1 * dt
        k1_vz = az1 * dt
        k1_x = vx * dt
        k1_y = vy * dt
        k1_z = vz * dt

        vx_mid = vx + 0.5 * k1_vx
        vy_mid = vy + 0.5 * k1_vy
        vz_mid = vz + 0.5 * k1_vz
        x_mid = x + 0.5 * k1_x
        y_mid = y + 0.5 * k1_y
        z_mid = z + 0.5 * k1_z

        ux2 = vx_mid - wx
        uy2 = vy_mid
        uz2 = vz_mid - wz
        u2 = math.sqrt(ux2**2 + uy2**2 + uz2**2)
        ax2 = -(beta / (m / 2)) * u2 * ux2
        ay2 = -g - (beta / (m / 2)) * u2 * uy2
        az2 = -(beta / (m / 2)) * u2 * uz2

        k2_vx = ax2 * dt
        k2_vy = ay2 * dt
        k2_vz = az2 * dt
        k2_x = vx_mid * dt
        k2_y = vy_mid * dt
        k2_z = vz_mid * dt

        vx_mid = vx + 0.5 * k2_vx
        vy_mid = vy + 0.5 * k2_vy
        vz_mid = vz + 0.5 * k2_vz
        x_mid = x + 0.5 * k2_x
        y_mid = y + 0.5 * k2_y
        z_mid = z + 0.5 * k2_z

        ux3 = vx_mid - wx
        uy3 = vy_mid
        uz3 = vz_mid - wz
        u3 = math.sqrt(ux3**2 + uy3**2 + uz3**2)
        ax3 = -(beta / (m / 2)) * u3 * ux3
        ay3 = -g - (beta / (m / 2)) * u3 * uy3
        az3 = -(beta / (m / 2)) * u3 * uz3

        k3_vx = ax3 * dt
        k3_vy = ay3 * dt
        k3_vz = az3 * dt
        k3_x = vx_mid * dt
        k3_y = vy_mid * dt
        k3_z = vz_mid * dt

        vx_end = vx + k3_vx
        vy_end = vy + k3_vy
        vz_end = vz + k3_vz
        x_end = x + k3_x
        y_end = y + k3_y
        z_end = z + k3_z

        ux4 = vx_end - wx
        uy4 = vy_end
        uz4 = vz_end - wz
        u4 = math.sqrt(ux4**2 + uy4**2 + uz4**2)
        ax4 = -(beta / (m / 2)) * u4 * ux4
        ay4 = -g - (beta / (m / 2)) * u4 * uy4
        az4 = -(beta / (m / 2)) * u4 * uz4

        k4_vx = ax4 * dt
        k4_vy = ay4 * dt
        k4_vz = az4 * dt
        k4_x = vx_end * dt
        k4_y = vy_end * dt
        k4_z = vz_end * dt

        vx = vx + (k1_vx + 2*k2_vx + 2*k3_vx + k4_vx) / 6
        vy = vy + (k1_vy + 2*k2_vy + 2*k3_vy + k4_vy) / 6
        vz = vz + (k1_vz + 2*k2_vz + 2*k3_vz + k4_vz) / 6
        x = x + (k1_x + 2*k2_x + 2*k3_x + k4_x) / 6
        y = y + (k1_y + 2*k2_y + 2*k3_y + k4_y) / 6
        z = z + (k1_z + 2*k2_z + 2*k3_z + k4_z) / 6
        t = t + dt

        # обновление максимума высоты
        if y > y_max:
            y_max = y
            t_ymax = t

        # запись в целочисленные моменты времени
        if t >= next_target and next_target > last_recorder and y > 0:
            last_recorder = t
            next_target = next_target + 1.0

            ux = vx - wx
            uy = vy
            uz = vz - wz
            u = math.sqrt(ux**2 + uy**2 + uz**2)

            # сила сопротивления = 2 * beta * u^2 (по модулю)
            F_svx=beta*math.sqrt(ux**2+uy**2+uz**2)*ux
            F_svy=beta*math.sqrt(ux**2+uy**2+uz**2)*uy
            F_svz=beta*math.sqrt(ux**2+uy**2+uz**2)*uz
            F_sv = math.sqrt(F_svx**2 + F_svy**2 + F_svz**2)

            v = math.sqrt(vx**2 + vy**2 + vz**2)

            times.append(t)
            heights.append(y)
            speed.append(v)
            Kin.append(m * (vx**2 + vy**2 + vz**2) / 2)
            Pot.append(m * g * y)
            Meh.append(m * g * y + m * (vx**2 + vy**2 + vz**2) / 2)
            vg.append(vx)
            vv.append(vy)
            vp.append(vz)
            lp.append(x)
            lz.append(z)
            Fsv.append(F_sv)

            print(f"В момент времени {t:.4f} c:")
            print(f"Горизонтальная скорость снаряда: {vx:.4f} м/с")
            print(f"Вертикальная скорость снаряда: {vy:.4f} м/с")
            print(f"Скорость поперечного движения: {vz:.4f} м/с")
            print(f"Модуль реальной скорости: {math.sqrt(vx**2 + vy**2 + vz**2):.4f} м/с")
            print(f"Угол наклона реальной скорости снаряда к горизонту: {abs(math.degrees(math.atan2(vy, vx))):.4f}")
            print(f"Высота: {y:.4f} м")
            print(f"Перемещение вдоль запуска: {x:.4f} м")
            if z > 0:
                print(f"Смещение вправо из-за поперечного ветра: {z:.4f} м")
            elif z == 0:
                print("Нет смещения в сторону")
            else:
                print(f"Смещение влево из-за поперечного ветра: {abs(z):.4f} м")
            print(f"Реальное перемещение: {math.sqrt(x**2 + z**2):.4f} м")
            print(f"Кинетическая энергия: {m * (vx**2 + vy**2 + vz**2) / 2:.4f} Дж")
            print(f"Потенциальная энергия: {m * g * y:.4f} Дж")
            print(f"Полная механическая энергия: {m * g * y + m * (vx**2 + vy**2 + vz**2) / 2:.4f} Дж")
            print(f"Модуль силы сопротивления воздуха: {F_sv:.4f} Н")
            print()
            print()

    return {
        'vx': vx,
        'vy': vy,
        'vz': vz,
        'x': x,
        'y': y,
        'z': z,
        't': t,
        'times': times,
        'heights': heights,
        'speed': speed,
        'Kin': Kin,
        'Pot': Pot,
        'Meh': Meh,
        'vg': vg,
        'vv': vv,
        'vp': vp,
        'lp': lp,
        'lz': lz,
        'Fsv': Fsv,
        'y_max': y_max,
        't_ymax': t_ymax
    }
