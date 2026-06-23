import math

#Блок про ветер
def windout(inp):
    w=inp['w']
    wx=inp['wx']
    wz=inp['wz']
    nb=inp['nb']
    nv=inp['nv']
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
    return{
            'wx':wx,
            'wz':wz
            }
        
