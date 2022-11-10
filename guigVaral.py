import PySimpleGUI as psg
from gVaral import gNorm,gPoisson

psg.theme('GrayGrayGray')

layout = [
    [psg.Text('¿Cuantas variables deseas generar?',font = 'Baskerville 20')],
    [psg.InputText(key = 'num')],
    [psg.Text('¿Que distribucion deseas generar? ',font = 'Baskerville 20')],
    [psg.Button('NORMAL',size = (15,1),key = 'normal',button_color = ('white','gray'))
    ,psg.Button('POISSON',size = (15,1),key = 'poisson',button_color = ('white','gray'))]
]

ventana = psg.Window('Simulacion', layout,enable_close_attempted_event = True)

while True:
    event, values = ventana.read()  # type: ignore
    if event in ('normal'):
        num = int(values['num'])
        n = [gNorm(10,6.5) for i in range(num)]
        with open("Dist.csv", 'w') as d:
            d.write("Normal, \n")
            for i in n:
                d.writelines(str(i) +", \n")
    elif event in ('poisson'):
        num = int(values['num'])
        p = [gPoisson(5) for i in range(num)]
        with open("Dist.csv", 'w') as d:
            d.write("Poisson, \n")
            for i in p:
                d.writelines(str(i) +", \n")
    break

ventana.close()