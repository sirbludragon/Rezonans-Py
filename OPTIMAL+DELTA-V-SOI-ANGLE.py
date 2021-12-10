import math
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.offsetbox import AnchoredText

#DODOTAKOWA FUNKCJIA 4 SATELITY ZAMIAST CO OKRES WYRZUCAC CO 4 OKRESY CZYLI JAKBY DLA 16 SATELIT DLA OSZCZEDNOSCI DELTA V W SATELECIE DOCELOWYM (NIE CHODZI O RAKIETE NOSNA)

def main():
    # name = [0name  1mass    2radius  3period axis 4height of atm/obstacle  5semi-ajor axis  6synchronous 7orbital period[days]  8type  9color(hex)  10mass of central body]
    kerbin = ['kerbin', 5.2915158 * pow(10, 22), 600000, 5.98594444444, 70000, 13599840256, 2863330, 426.090046296, 'planet', '#1F618D', 1.7565459 * pow(10, 28)]
    duna = ['duna', 4.5154270 * pow(10, 21), 320000, 18.19941666667, 50000, 20726155264, 2880000, 801.638888889, 'planet', '#CB4335', 1.7565459 * pow(10, 28)]
    eve = ['eve', 1.2243980 * pow(10, 23), 700000, 22.36111111, 90000, 9832684544, 10328470, 261.944212963, 'planet', '#8E44AD', 1.7565459 * pow(10, 28)]
    jool = ['jool', 4.2332127 * pow(10, 24), 6000000, 10, 200000, 68773560320, 15010460, 4845.43666667, 'planet', '#5CDC02', 1.7565459 * pow(10, 28)]
    eeloo = ['eeloo', 1.1149224 * pow(10, 21), 210000, 5.40555555556, 4000, 90118820000, 683690, 7268.15037037, 'planet', '#D7DBDD', 1.7565459 * pow(10, 28)]
    dres = ['dres', 3.2190937 * pow(10, 20), 138000, 9.66666666667, 6000, 40839348203, 732240, 2217.27143519, 'planet', '#797D7F', 1.7565459 * pow(10, 28)]
    moho = ['moho', 2.5263314 * pow(10, 21), 250000, 336.111111111, 7000, 5263138304, 18173170, 102.581203704, 'planet', '#DDB668', 1.7565459 * pow(10, 28)]
    gilly = ['gilly', 1.2420363 * pow(10, 17), 13000, 7.84861111111, 6000, 31500000, 42140, 261.944212963, 'moon', '#EDBB99', 1.2243980 * pow(10, 23)]
    mun = ['mun', 9.7599066 * pow(10, 20), 200000, 38.6067777778, 7100, 12000000, 2970560, 426.090046296, 'moon', '#626567', 5.2915158 * pow(10, 22)]
    minmus = ['minmus', 2.6457580 * pow(10, 19), 60000, 11.2222222222, 6000, 47000000, 357940, 426.090046296, 'moon', '#ABEBC6', 5.2915158 * pow(10, 22)]
    ike = ['ike', 2.7821615 * pow(10, 20), 130000, 18.1994166667, 13000, 3200000, 1133900, 801.638888889, 'moon', '#616A6B', 4.5154270 * pow(10, 21)]
    laythe = ['laythe', 2.9397311 * pow(10, 22), 500000, 14.7169166667, 50000, 27184000, 4686320, 4845.43666667, 'moon', '#2E86C1', 4.2332127 * pow(10, 24)]
    vall = ['vall', 3.1087655 * pow(10, 21), 300000, 29.4339166667, 8000, 43152000, 3593200, 4845.43666667, 'moon', '#85C1E9', 4.2332127 * pow(10, 24)]
    tylo = ['tylo', 4.2332127 * pow(10, 22), 600000, 58.8684444444, 12000, 68500000, 14157880, 4845.43666667, 'moon', '#BDC3C7', 4.2332127 * pow(10, 24)]
    kerbol = ['kerbol', 1.7565459 * pow(10, 28), 261600000, 20, 1500, 0, 1508045290, 1, 'star', '#F4D03F', 0]
    bop = ['bop', 3.7261090 * pow(10, 19), 65000, 151.252055556, 12000, 128500000, 2588170, 4845.43666667, 'moon', '#B98A2E', 4.2332127 * pow(10, 24)]
    pol = ['pol', 1.0813507 * pow(10, 19), 44000, 250.5285, 5000, 179890000, 2415080, 4845.43666667, 'moon', '#CEB337', 4.2332127 * pow(10, 24)]
    earth = ['Earth', 5.97219* pow(10, 24), 6371000, 23.934472222222222, 300000, 149598023e+3, 35786000, 365.256363004,'planet','#1F618D',1.98847 * pow(10, 30)]

    xlist = []
    ylist = []
    listr = []
    listv = []

    constant_G = 6.67 * pow(10, -11)
    constant_pi = math.pi
    x0 = 0
    y0 = 0
    c = 10000

    list = []
    list.append(kerbin)
    list.append(duna)
    list.append(eve)
    list.append(jool)
    list.append(eeloo)
    list.append(dres)
    list.append(moho)
    list.append(gilly)
    list.append(mun)
    list.append(minmus)
    list.append(ike)
    list.append(laythe)
    list.append(vall)
    list.append(tylo)
    list.append(kerbol)
    list.append(bop)
    list.append(pol)
    list.append(earth)

    name = input('Enter the name of planet: ')
    found = False

    for element in list:
        if element[0].upper() == name.upper():

            found = True

            SOI = ((element[5]*((element[1] / (element[10])) ** (2/5)))-element[2])
            if SOI == 0:
                print('\nSOI of kerbol is infinite\n')
            else:
                print('\nSOI of ' + name, 'is equal to =', SOI, 'meters\n')

            if element[8] == 'planet':
                RATIO=element[5]/kerbin[5]
                AVG=(1+RATIO)/2
                P=AVG**(3/2)
                P1=P*kerbin[7]
                DEGS=360/element[7]
                HP1=P1/2
                DEG=HP1*DEGS
                ANGLE=180-DEG
                print('Angle bettewen kerbin and',element[0],'at launch time should be',ANGLE,'degrees','\n')

            print('If you want the orbit to have a rotation period of your choice, enter: 1 ')
            print('If you want the orbit to have the selected height, enter: 2')
            print('If you want the orbit to have lowest height for network on the chosen number of satellites, enter: 3')
            print('If you want the orbit to be synchronous orbit, enter: 4','\n')
            variable=int(input('Please select a variant: '))
            print('You have selected variant number '+ str(variable))

            if variable == 1:

                print('Rotation time of ' + name, 'around its axis: ' + str(element[3]), 'hours')
                period = float(input('Enter the target satellites rotation period: '))
                print('The specified period of satellites rotation: ' + str(period))

                result_period = pow(period * 60 * 60, 2)
                result_constant = (element[1] * constant_G)
                A = (result_period * result_constant / (4 * pow(constant_pi, 2)))

                A3 = (pow(A, (1 / 3)) - (element[2]))
                A3R = (pow(A, (1 / 3)))
                print('The height of the circular orbit is:', (round(A3)),'meters above sea level')
                if A3 > SOI:
                    print('Height of circular orbit is out of SOI')
                satellite = int(input('How many satellites do you want to orbit: '))
                print('the number of entered satellites:' + str(satellite))
                result_constant2 = (pow(period * 60 * 60 * (satellite - 1), 2) / pow(satellite, 2))
                Ax = (result_constant2 * result_constant / (4 * pow(constant_pi, 2)))
                Ax3R = (pow(Ax, (1 / 3)))
                pe = (((2 * Ax3R) - A3R) - (element[2]))
                if pe>=element[4]:
                    print('Initial orbit perigee:', round(pe), 'meters above sea leve')
                    if pe > SOI:
                        print('Perigee of orbit is out of SOI')
                    r = (A3 + element[2])
                    a = (((A3 + pe) / 2) + element[2])
                    v = (((constant_G * element[1]) * ((2 / r) - (1 / a))) ** 0.5)
                    pe1 = (pe + element[2])
                    v_1 = (((constant_G * element[1]) * ((2 / pe1) - (1 / a))) ** 0.5)
                    v_2 = (((constant_G * element[1])/r)**0.5)
                    print('delta-v required =',abs(v-v_2))
                else:
                    result_constant2 = (pow(period * 60 * 60 * (satellite + 1), 2) / pow(satellite, 2))
                    Ax = (result_constant2 * result_constant / (4 * pow(constant_pi, 2)))
                    Ax3R = (pow(Ax, (1 / 3)))
                    pe = (((2 * Ax3R) - A3R) - (element[2]))
                    print('Initial orbit apogee:', round(pe), 'meters above sea leve')
                    if pe > SOI:
                        print('Apogee of orbit is out of SOI')
                    r = (A3 + element[2])
                    a = (((A3 + pe) / 2) + element[2])
                    v = (((constant_G * element[1]) * ((2 / r) - (1 / a))) ** 0.5)
                    pe1 = (pe + element[2])
                    v_1 = (((constant_G * element[1]) * ((2 / pe1) - (1 / a))) ** 0.5)
                    v_2 = (((constant_G * element[1])/r)**0.5)
                    print('delta-v required =',abs(v-v_2))

            elif variable == 2:
                print('Rotation time of ' + name, 'around its axis: ' + str(element[3]), 'hours')
                A3 = float(input('Enter the target orbit altitude for the satellites in meters: '))
                result_constant = (element[1] * constant_G)
                period = (((4 * pow(constant_pi, 2)) * (pow((A3+(element[2])), 3))) / (result_constant)) # T^2
                A3R = ((A3) + (element[2]))
                print('The height of the circular orbit is:', (round(A3)),'meters above sea level')
                if A3 > SOI:
                    print('Height of circular orbit is out of SOI')
                satellite = int(input('How many satellites do you want to orbit: '))
                print('the number of entered satellites:' + str(satellite))
                result_constant2 = (((period * pow((satellite - 1), 2))/(pow(satellite, 2))))
                Ax = ((result_constant2 * result_constant)/(4 * pow(constant_pi, 2)))
                Ax3R = (pow(Ax, (1 / 3)))
                pe = (((2 * Ax3R) - A3R) - (element[2]))
                if pe>=element[4]:
                    print('Initial orbit perigee:', round(pe), 'meters above sea leve')
                    if pe > SOI:
                        print('Perigee of orbit is out of SOI')
                    r = (A3 + element[2])
                    a = (((A3 + pe) / 2) + element[2])
                    v = (((constant_G * element[1]) * ((2 / r) - (1 / a))) ** 0.5)
                    pe1 = (pe + element[2])
                    v_1 = (((constant_G * element[1]) * ((2 / pe1) - (1 / a))) ** 0.5)
                    v_2 = (((constant_G * element[1])/r)**0.5)
                    print('delta-v required =',abs(v-v_2))
                else:
                    result_constant2 = (((period * pow((satellite+1), 2)) / (pow(satellite, 2))))
                    Ax = ((result_constant2 * result_constant) / (4 * pow(constant_pi, 2)))
                    Ax3R = (pow(Ax, (1 / 3)))
                    pe = (((2 * Ax3R) - A3R) - (element[2]))
                    print('Initial orbit apogee:', round(pe), 'meters above sea leve')
                    if pe > SOI:
                        print('Apogee of orbit is out of SOI')
                    r = (A3 + element[2])
                    a = (((A3 + pe) / 2) + element[2])
                    v = (((constant_G * element[1]) * ((2 / r) - (1 / a))) ** 0.5)
                    pe1 = (pe + element[2])
                    v_1 = (((constant_G * element[1]) * ((2 / pe1) - (1 / a))) ** 0.5)
                    v_2 = (((constant_G * element[1])/r)**0.5)
                    print('delta-v required =',abs(v-v_2))

            elif variable == 3:
                print('Rotation time of ' + name, 'around its axis: ' + str(element[3]), 'hours')
                result_constant = (element[1] * constant_G)
                satellite = int(input('How many satellites do you want to orbit: '))
                print('the number of entered satellites:' + str(satellite))
                angle_degree = (90-((((satellite-2)*180))/(2*satellite)))
                angle_radian = ((angle_degree*2*constant_pi)/(360))
                A3 = ((element[2]/(math.cos(angle_radian)))-element[2])
                period = (((4 * pow(constant_pi, 2)) * (pow((A3 + (element[2])), 3))) / (result_constant))  # T^2
                if A3 >=element[4] and satellite >2:
                    A3R = ((A3) + (element[2]))
                    result_constant2 = (((period * pow((satellite-1), 2)) / (pow(satellite, 2))))
                    Ax = ((result_constant2 * result_constant) / (4 * pow(constant_pi, 2)))
                    Ax3R = (pow(Ax, (1 / 3)))
                    pe = (((2 * Ax3R) - A3R) - (element[2]))
                    if pe >=element[4]:
                        print('The height of the circular orbit and the apogee of the initial orbit is:', (round(A3)),'meters above sea level')
                        if A3 > SOI:
                            print('Height of circular orbit is out of SOI')
                        print('Initial orbit perigee:', round(pe), 'meters above sea level',(element[4]))
                        if pe > SOI:
                            print('Perigee of orbit is out of SOI')
                        r = (A3 + element[2])
                        a = (((A3 + pe) / 2) + element[2])
                        v = (((constant_G * element[1]) * ((2 / r) - (1 / a))) ** 0.5)
                        pe1 = (pe + element[2])
                        v_1 = (((constant_G * element[1]) * ((2 / pe1) - (1 / a))) ** 0.5)
                        v_2 = (((constant_G * element[1]) / r) ** 0.5)
                        print('delta-v required =',abs(v-v_2))
                    else:
                        A3R = ((A3) + (element[2]))
                        result_constant2 = (((period * pow((satellite+1), 2)) / (pow(satellite, 2))))
                        Ax = ((result_constant2 * result_constant) / (4 * pow(constant_pi, 2)))
                        Ax3R = (pow(Ax, (1 / 3)))
                        pe = (((2 * Ax3R) - A3R) - (element[2]))
                        print('The height of the circular orbit and the perigee of the initial orbit is:', (round(A3)),'meters above sea level')
                        if A3 > SOI:
                            print('Height of circular orbit is out of SOI')
                        print('Initial orbit apogee:', round(pe), 'meters above sea leve')
                        if pe > SOI:
                            print('Apogee of orbit is out of SOI')
                        r = (A3 + element[2])
                        a = (((A3 + pe) / 2) + element[2])
                        v = (((constant_G * element[1]) * ((2 / r) - (1 / a))) ** 0.5)
                        pe1 = (pe + element[2])
                        v_1 = (((constant_G * element[1]) * ((2 / pe1) - (1 / a))) ** 0.5)
                        v_2 = (((constant_G * element[1])/r)**0.5)
                        print('delta-v required =',abs(v-v_2))
                else:
                    print('Wrong number of satellites to make perfect network select fewer/more satellites',)
                    exit()

            elif variable == 4:
                if element[6]<SOI:
                    print('Rotation time of ' + name, 'around its axis: ' + str(element[3]), 'hours')
                    A3 =(element[6])
                    print('Height of synchronous orbit: ' + str(A3))
                    result_constant = (element[1] * constant_G)
                    period = (((4 * pow(constant_pi, 2)) * (pow((A3+(element[2])), 3))) / (result_constant)) # T^2
                    A3R = ((A3) + (element[2]))
                    print('The height of the circular orbit is:', (round(A3)),'meters above sea level')
                    satellite = int(input('How many satellites do you want to orbit: '))
                    print('the number of entered satellites:' + str(satellite))
                    result_constant2 = (((period * pow((satellite - 1), 2))/(pow(satellite, 2))))
                    Ax = ((result_constant2 * result_constant)/(4 * pow(constant_pi, 2)))
                    Ax3R = (pow(Ax, (1 / 3)))
                    pe = (((2 * Ax3R) - A3R) - (element[2]))
                    if pe>=element[4]:
                        print('Initial orbit perigee:', round(pe), 'meters above sea leve')
                        if pe > SOI:
                            print('Perigee of orbit is out of SOI')
                        r = (A3 + element[2])
                        a = (((A3 + pe) / 2) + element[2])
                        v = (((constant_G * element[1]) * ((2 / r) - (1 / a))) ** 0.5)
                        pe1 = (pe + element[2])
                        v_1 = (((constant_G * element[1]) * ((2 / pe1) - (1 / a))) ** 0.5)
                        v_2 = (((constant_G * element[1]) / r) ** 0.5)
                        print('delta-v required =',abs(v-v_2))
                    else:
                        result_constant2 = (((period * pow((satellite+1), 2)) / (pow(satellite, 2))))
                        Ax = ((result_constant2 * result_constant) / (4 * pow(constant_pi, 2)))
                        Ax3R = (pow(Ax, (1 / 3)))
                        pe = (((2 * Ax3R) - A3R) - (element[2]))
                        print('Initial orbit apogee:', round(pe), 'meters above sea leve')
                        if pe > SOI:
                            print('Apogee of orbit is out of SOI')
                        r = (A3 + element[2])
                        a = (((A3 + pe) / 2) + element[2])
                        v = (((constant_G * element[1]) * ((2 / r) - (1 / a))) ** 0.5)
                        pe1 = (pe + element[2])
                        v_1 = (((constant_G * element[1]) * ((2 / pe1) - (1 / a))) ** 0.5)
                        v_2 = (((constant_G * element[1]) / r) ** 0.5)
                        print('delta-a required =',abs(v-v_2))
                else:
                    print('Height of synchronous orbit is out of SOI')
            else:
                print('you have selected a variant that does not exist')
                exit()
            #v-velocity on perigee(eliptical)  v_1-velocity on apogee(eliptical)  v_2-velocity on final orbit
            if variable >=1 and variable<=4:

                plt.subplot(1, 2, 2)
                if pe<=A3:
                    sub_orbit = (A3-pe)/1000
                    for k in range(0, 1000 + 1):
                        r = pe + (k * sub_orbit)
                        listr.append(r)
                        v1 = (((constant_G * element[1]) * ((2 / (r + element[2])) - (1 / a))) ** 0.5)
                        listv.append(v1)
                else:
                    sub_orbit = (pe - A3)/1000
                    for k in range(0, 1000 + 1):
                        r = A3 + (k * sub_orbit)
                        listr.append(r)
                        v1 = (((constant_G * element[1]) * ((2 / (r + element[2])) - (1 / a))) ** 0.5)
                        listv.append(v1)
                plt.plot(listr, listv)
                plt.xlabel('Height (m)')
                plt.title('Velocity on an elliptical orbit',fontsize=20)
                plt.ylabel  ('Velocity (m/s)')

                ax = plt.subplot(1, 2, 1,aspect='equal')
                ellipse = Ellipse((x0, -(((A3+((pe)-A3))/2)-0.5*(A3))), 2 * (((pe+element[2])*(A3+element[2]))**0.5), (2 * ((A3+((pe)-A3)/2))+2*element[2]), fill=False,
                              linestyle='--',color='b',label='Hohmann transfer')
                ax.add_artist(ellipse)
                if pe>A3:
                    circle1 = plt.Circle((x0, y0), A3+element[2], fill=False, label=('Perigee = ' + str(round(A3)) + ' m.'))
                    ax.add_artist(circle1)
                    circle2 = plt.Circle((x0, y0), pe+element[2], fill=False, label=('Apogee = ' + str(round(pe)) + ' m.'))
                    ax.add_artist(circle2)
                elif pe<A3:
                    circle1 = plt.Circle((x0, y0), A3+element[2], fill=False, label=('Apogee = ' + str(round(A3)) + ' m.'))
                    ax.add_artist(circle1)
                    circle2 = plt.Circle((x0, y0), pe+element[2], fill=False, label=('Perigee = ' + str(round(pe)) + ' m.'))
                    ax.add_artist(circle2)

                circle3 = plt.Circle((x0, y0), element[2],fill=True,color=element[9])
                ax.add_artist(circle3)

                circle4 = plt.Circle((x0, y0), (SOI+element[2]), fill=False,linestyle='--',color='r', label=('SOI = ' + str(round(SOI)) + ' m.'))
                ax.add_artist(circle4)

                circle5 = plt.Circle((x0, y0), 0, fill=False,color='black', label = ('Δ-v= ' + str(abs((round((v - v_2) * math.pow(10, 2)) / math.pow(10, 2)))) + ' m/s'))
                ax.add_artist(circle2)

                DEG = 360 / satellite
                for n in range(0, satellite + 1):

                    Deg = 90 - n * DEG
                    Rad = (Deg * math.pi / 180)
                    a = (math.tan(Rad))

                    if Deg >= -90 and Deg <= 90:
                        x = ((((A3+element[2]) ** 2) / ((a ** 2) + 1)) ** 0.5)
                    else:
                        x = -((((A3+element[2]) ** 2) / ((a ** 2) + 1)) ** 0.5)
                    if (a >= 100000 or a <= -100000):
                        a = 0

                    x_floor = round(x * math.pow(10, 14)) / math.pow(10, 14)

                    y = ((((A3+element[2]) ** 2) - (x_floor ** 2)) ** 0.5)
                    if Deg >= -180 and Deg <= 0:
                        y = -((((A3+element[2]) ** 2) - (x_floor ** 2)) ** 0.5)
                    y_floor = round(y * math.pow(10, 13)) / math.pow(10, 13)
                    ylist.append(y_floor)
                    xlist.append(x_floor)
                plt.plot(xlist, ylist, '--g*', mew=2, mec='red')
                if pe<=A3:
                    pe=A3
                legenda = plt.legend(handles=[circle1,circle2,circle5], loc=2)
                ax = plt.gca().add_artist(legenda)
                plt.legend(handles=[ellipse, circle4], loc=1)
                plt.xlim(-1.3*(pe+element[2]), 1.3*(pe+element[2]))
                plt.ylim(-1.3*(pe+element[2]), 1.3*(pe+element[2]))
                plt.xlabel('Distance(m)')
                plt.ylabel('Distance(m)')
                plt.title(label=('Orbit around '+str(element[0]).title()),fontsize=20)
                plt.show()
    if found == False:

        print('There is no such element')

main()