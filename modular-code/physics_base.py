import math

# Вся базовая физика
def fizika(inp, g, koef, C, R, Mo, Mh):
    S_x= inp['S_x']
    a=inp['a']
    h0=inp['h0']
    l=inp['l']
    m=inp['m']
    r=inp['r']
    trenie=inp['trenie']
    tempC=inp['tempC']
    RH=inp['RH']
    rt_st=inp['rt_st']
    nv=inp['nv']
    nb=inp['nb']
    w=inp['w']
    wx=inp['wx']
    wz=inp['wz']

    L_exp=S_x-l*math.cos(a)
    v0_0 = (L_exp/math.cos(a))*math.sqrt(g/(2*(L_exp*math.tan(a)+h0+l*math.sin(a))))#
    t = L_exp/(v0_0*math.cos(a))# Теоретическое время полета

    #Вычисление beta
    #Вычисляем давление насыщенного пара в гПа по методу Ардена Бака
    if tempC >= 0:
        E=6.1121*math.exp((17.502*tempC)/(240.97+tempC))
    else:
        E=6.1115*math.exp((22.452*tempC)/(272.55+tempC))
    E=E*100
    e=E*RH/100 # Реальное давление пара
    temp = tempC + 273.15 # Перевод температуры в Кельвины
    p = rt_st*koef # Перевод мм рт. ст. в Па
    rho = ((p-e)*Mo+e*Mh)/(R*temp) # Плотность воздуха
    #Главное в блоке
    beta= C*rho*math.pi*r**2/(4)
    return{
            'L_exp':L_exp,
            'v0_0':v0_0,
            't':t,
            'beta':beta,
            'rho':rho
            }


