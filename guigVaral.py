import PySimpleGUI as psg
from gVaral import gNorm,gPoisson

psg.theme('GrayGrayGray')

layout = [
    [psg.Text('¿Que distribucion deseas generar? ',font = 'Baskerville 20'), psg.InputText(key = 'dist')],
    [psg.Button('Aceptar',size = (15,1),key = 'aceptar',button_color = ('white','gray'))]
]

ventana = psg.Window('Simulacion', layout,enable_close_attempted_event = True)

while True:
    event, values = ventana.read()  # type: ignore
    if event in ('aceptar'):
        dist = values['dist']
        if dist == "Normal" or dist == "normal":
            n = [gNorm(10,6.5) for i in range(100)]
            with open("Dist.csv", 'w') as d:
                d.write("Normal, \n")
                for i in n:
                    d.writelines(str(i) +", \n")
        elif dist == "Poisson" or dist == "poisson":
            p = [gPoisson(5) for i in range(100)]
            with open("Dist.csv", 'w') as d:
                d.write("Poisson, \n")
                for i in p:
                    d.writelines(str(i) +", \n")
    break

ventana.close()