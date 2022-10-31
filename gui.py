from cgitb import text
import PySimpleGUI as psg
from Pseudo import Pseudo

psg.theme('GrayGrayGray')
layout = [
    [psg.Text('Introduce los datos que deseas: ',font = 'Baskerville 20')],
    [psg.Text('Semilla: ',size = (15,1),font = 'TimesNewRoman 12'), psg.InputText(key = 'semilla')],
    [psg.Text('G: ',size = (15,1),font = 'TimesNewRoman 12'), psg.InputText(key = 'g')],
    [psg.Text('K: ',size = (15,1),font = 'TimesNewRoman 12'), psg.InputText(key = 'k')],
    [psg.Text('C: ',size = (15,1),font = 'TimesNewRoman 12'), psg.InputText(key = 'c')],
    [psg.Text('Alpha: ',size = (15,1),font = 'TimesNewRoman 12'), psg.InputText(key = 'alpha')],
    [psg.Button('Aceptar',size = (15,1),key = 'aceptar',button_color = ('white','gray')),
    psg.Button('Mostrar',size = (15,1),key = 'mostrar',button_color = ('white','gray')),
    psg.Button('Cerrar',size = (15,1),key = 'cerrar',button_color = ('white','gray')),],
    [psg.Text('Prueba de Medias:',size = (15,1),font = 'TimesNewRoman 12')], 
    [psg.Text('',size = (15,1),key = 'medias',font = 'TimesNewRoman 12',text_color = 'red')],
    [psg.Text('Prueba de Varianza:',size = (17,1),font = 'TimesNewRoman 12')], 
    [psg.Text('',size = (15,1),key = 'varianza',font = 'TimesNewRoman 12',text_color = 'red')],
    [psg.Text('Prueba de Independencia:',size = (20,1),font = 'TimesNewRoman 12')], 
    [psg.Text('',size = (15,1),key = 'independencia',font = 'TimesNewRoman 12',text_color = 'red')],
    [psg.Text('Prueba de Uniformidad:',size = (20,1),font = 'TimesNewRoman 12')], 
    [psg.Text('',size = (20,1),key = 'uniformidad',font = 'TimesNewRoman 12',text_color = 'red')],
    [psg.Text('Camiones',size = (20,1),font = 'TimesNewRoman 15')], 
    [psg.Text('# de trabajadores: ',size = (20,1),font = 'TimesNewRoman 12'), psg.InputText(key = 'trabajadores')], 
]

ventana = psg.Window('Simulacion', layout,enable_close_attempted_event = True)

while True:
    event, values = ventana.read()  # type: ignore
    if event in (psg.WINDOW_CLOSE_ATTEMPTED_EVENT,'cerrar'): 
        break
    elif event in ('aceptar'):
        x0 = int(values['semilla'])
        g = int(values['g'])
        k = int(values['k'])
        c = int(values['c'])
        alfa = float(values['alpha'])
        ntrabajadores = int(values['trabajadores'])
        break
    elif event in ('mostrar'):
        x0 = int(values['semilla'])
        g = int(values['g'])
        k = int(values['k'])
        c = int(values['c'])
        alfa = float(values['alpha'])
        o = Pseudo(x0, g, k, c)
        o.gLineal()
        if o.pMedias(alfa)[0] == True:
            ventana['medias'].update(o.pMedias(alfa)[0],text_color = 'green')
            print("Prueba de medias: \n" , o.pMedias(alfa)[1])
        else:
            ventana['medias'].update(o.pMedias(alfa)[0])
            print("Prueba de medias: \n" , o.pMedias(alfa)[1])
        if  o.pVarianza(alfa)[0] == True:
            ventana['varianza'].update(o.pVarianza(alfa)[0],text_color = 'green')
            print("\nPrueba de varianza: \n" ,o.pVarianza(alfa)[1])
        else:
            ventana['varianza'].update(o.pVarianza(alfa)[0])
            print("\nPrueba de varianza: \n" ,o.pVarianza(alfa)[1])
        if o.pUniformidad(alfa)[0] == True:
            ventana['uniformidad'].update(o.pUniformidad(alfa)[0],text_color = 'green')
            print("\nPrueba de uniformidad: \n" ,o.pUniformidad(alfa)[1])
        else:
            ventana['uniformidad'].update(o.pUniformidad(alfa)[0])
            print("\nPrueba de uniformidad: \n" ,o.pUniformidad(alfa)[1])
        if o.pIndependencia(alfa)[0] == True:
            ventana['independencia'].update(o.pIndependencia(alfa)[0],text_color = 'green')
            print("\nPrueba de independencia: \n" ,o.pIndependencia(alfa)[1])
        else:
            ventana['independencia'].update(o.pIndependencia(alfa)[0])
            print("\nPrueba de independencia: \n" ,o.pIndependencia(alfa)[1])

ventana.close()



