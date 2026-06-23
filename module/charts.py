#Блок про графики
import plotext as plt

def graf(times, heights, speed, vg, vv, vp, lp, lz, Kin, Pot, Meh, Fsv):
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
    plt.title("Vx - кр, Vy - зел, Vz - син, |V| - оранж (м/с)")
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
        
