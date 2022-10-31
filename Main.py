from gui import ventana
import Dados
import Camiones

if __name__ == "__main__":
    Dados.leer("Numeros.csv")
    ventana.read()
    Camiones.leer("Camiones.csv")