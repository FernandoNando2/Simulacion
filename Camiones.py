import Transformada as ti
from funciones import leer
import statistics as sts
import datetime
from gui import ntrabajadores


# Ejercicio camiones
l = leer('Numeros.csv') # Lista de numeros
t = open("tiCamiones.csv", "r")
with open("Camiones.csv", "w") as f:
    pass

# Condiciones iniciales
'''
    Equipo: 3 personas
    Turno: 8 horas
    Horario: 11:00 pm - 07:30 am
    Comida: 03:00 am . 03:30 am
    Nota: Se termina de descargar el camion y despues se toman alimentos si es que el camion se descarga durante el horario de la comida
'''
horaInicio = datetime.datetime(100, 1, 1, 23, 0)
horaFin = datetime.datetime(100, 1, 2, 7, 30)
horaComida = datetime.datetime(100, 1, 2, 3, 0)
horaFinComida = datetime.datetime(100, 1, 2, 3, 30)
CostEsperaCamion = 100
Salario, CostoNormal = 25, 0
TiempoExtra, CostoExtra = 37.5, 0
CostoAlmacen = 500
CostTotal = 0


# Almacenar las tablas de probabilidades.
a, b = ti.leerTi(t)  # Numero de camiones en espera antes de abrir
c, d = ti.leerTi(t)  # Tiempo de entre llegadas
e, o = ti.leerTi(t)  # Tiempo de servicio (3 personas)
g, h = ti.leerTi(t)  # Tiempo de servicio (4 personas)
i, j = ti.leerTi(t)  # Tiempo de servicio (5 personas)
m, n = ti.leerTi(t)  # Tiempo de servicio (6 personas)

if ntrabajadores == 3:
    t1, t2 = e, o
elif ntrabajadores == 4:
    t1, t2 = g, h
elif ntrabajadores == 5:
    t1, t2 = i, j
else:
    t1, t2 = m, n

f = open("Camiones.csv", "a")


# Simulación del ejercicio

for i in range(10):

    f.write(
        "#pse,Numero camion,#pse,Hora de llegada,Hora de entrada a descarga,#pse,Tiempo de descarga,Hora de salida del camion,Tiempo de espera\n")


    horaAct = horaInicio
    horaSalida = 0
    totalEsp = datetime.datetime(100, 1, 1, 0, 0)
    comieron = False
    CostEspera = 0
    CostoNormal, CostoExtra, CostTotal = 0, 0, 0
    CostoAlm = 0


    # Verificar el primer camion en ingresar al almacen.
    pse = round(l.pop(0), 4)
    numCamiones = int(ti.gTi(a, b, pse)) # Simular el numero de camiones en cola antes de que abra el negocio.
    f.write(f"{pse},{numCamiones},")

    if numCamiones == 0:
        pse = round(l.pop(0), 4)
        horaLleg = horaAct + \
            datetime.timedelta(minutes=ti.gTi(c, d, pse))
        horaAct = horaLleg
    else:
        pse = 'N/A'
        horaLleg = horaAct

    horaEntrada = horaLleg
    f.write(
        f"{pse},{horaLleg.time().isoformat('minutes')},{horaEntrada.time().isoformat('minutes')},")

    pse = round(l.pop(0), 4)
    tiempoDescarga = ti.gTi(t1, t2, pse)

    horaSalida = horaEntrada + \
        datetime.timedelta(minutes=tiempoDescarga)

    tiempoEsp = horaEntrada - \
        datetime.timedelta(hours=horaLleg.time().hour,
                            minutes=horaLleg.time().minute)
    totalEsp = totalEsp + datetime.timedelta(
        hours=tiempoEsp.time().hour, minutes=tiempoEsp.time().minute)  

    f.write(f"{pse},{tiempoDescarga},{horaSalida.time().isoformat('minutes')},{tiempoEsp.time().isoformat('minutes')}\n")


    if (numCamiones > 1): # En caso de que haya camiones en espera.
        for i in range(numCamiones - 1):
            horaEntrada = horaSalida
            f.write(
                f",,N/A,{horaInicio.time().isoformat('minutes')},{horaEntrada.time().isoformat('minutes')},")

            pse = round(l.pop(0), 4)
            tiempoDescarga = ti.gTi(t1, t2, pse)

            horaSalida = horaEntrada + \
                datetime.timedelta(minutes=tiempoDescarga)

            tiempoEsp = horaEntrada - \
                datetime.timedelta(hours=horaLleg.time().hour,
                                    minutes=horaLleg.time().minute)

            totalEsp = totalEsp + datetime.timedelta(
                hours=tiempoEsp.time().hour, minutes=tiempoEsp.time().minute)  

            f.write(f"{pse},{tiempoDescarga},{horaSalida.time().isoformat('minutes')},{tiempoEsp.time().isoformat('minutes')}\n")


    # Simular el resto de los camiones.
    while True:
        pse = round(l.pop(0), 4)
        horaLleg = horaAct + \
            datetime.timedelta(minutes=ti.gTi(c, d, pse))
        horaAct = horaLleg

        if horaAct > horaFin:
            f.write(
            f"****,****,{pse},{horaLleg.time().isoformat('minutes')},****,****,****,****,****")
            break

        if (horaSalida >= horaComida) & (comieron == False):  
            if horaSalida >= horaFinComida:
                rango = horaFinComida - horaComida
                horaSalida = horaSalida + rango
            else:
                horaSalida = horaFinComida
            comieron = True

        if horaSalida <= horaLleg: 
            horaEntrada = horaLleg
        else:
            horaEntrada = horaSalida 

        f.write(
            f",,{pse},{horaLleg.time().isoformat('minutes')},{horaEntrada.time().isoformat('minutes')},")
        pse = round(l.pop(0), 4)
        tiempoDescarga = ti.gTi(e, o, pse)
        horaSalida = horaEntrada + \
            datetime.timedelta(minutes=tiempoDescarga)
        tiempoEsp = horaEntrada - \
            datetime.timedelta(hours=horaLleg.time().hour,
                            minutes=horaLleg.time().minute) 
        totalEsp = totalEsp + datetime.timedelta(
            hours=tiempoEsp.time().hour, minutes=tiempoEsp.time().minute)
        f.write(f"{pse},{tiempoDescarga},{horaSalida.time().isoformat('minutes')},{tiempoEsp.time().isoformat('minutes')}\n")


    # Calcular el costo total.
    #print(f"Tiempo de espera: {totalEsp.time()}")
    CostEspera = (totalEsp.time().hour +
                        totalEsp.time().minute / 60) * CostEsperaCamion
    CostTotal += CostEspera
    #print(f"Costo de espera del camion: ${CostEspera}")

    horario = datetime.datetime(100, 1, 1)
    horario += horaFin - horaInicio
    CostoNormal = horario.time().hour * ntrabajadores * Salario
    CostTotal += CostoNormal
    #print(f"Costo tiempo normal operadores: ${CostoNormal}")

    if horaSalida > horaFin:
        rango = horaSalida - horaFin
        CostoExtra = datetime.datetime(100,1,1)
        CostoExtra += rango
        CostoExtra = CostoExtra.time().hour + CostoExtra.time().minute / 60 
        CostoExtra = CostoExtra * ntrabajadores * TiempoExtra 
        CostTotal += CostoExtra
        #print(f"Costo tiempo extra operadores: ${CostoExtra}")

    horario = datetime.datetime(100,1,1)
    horario += horaSalida - horaInicio
    horario = horario.time().hour + horario.time().minute / 60
    CostoAlm = horario * CostoAlmacen
    CostTotal += CostoAlm
    CostTotal = round(CostTotal, 3)
    #print(f"Costo disponibilidad del almacen: ${CostoAlm}")
    #print(f"Costo total: ${CostTotal}")

    f.write(f"\nCosto Total,${CostTotal}\n,\n")
