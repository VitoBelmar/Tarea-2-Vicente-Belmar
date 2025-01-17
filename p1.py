# -*- coding: utf-8 -*-
"""p1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10iBToxTY5re7rarZze3cwmq_PJkqb4aA
"""

#p1.py
import sys
from read import read
from plot import plot1D, plot2D
import matplotlib.pyplot as plt

def main():
    # Comprobar que se pasaron los argumentos necesarios
    if len(sys.argv) != 3:
        print("Uso: python p1.py 'archivo.csv' 'out.png'")
        sys.exit(1)

    archivo_csv = sys.argv[1]
    archivo_salida = sys.argv[2]

    # Leer datos con la función read
    primera_columna, columnas_restantes = read(archivo_csv)

    # Verificar si es un gráfico 1D o 2D
    if len(columnas_restantes) == 1:
        # Gráfico 1D
        y = columnas_restantes[0]
        plot1D(primera_columna, y, "Tiempo", "Posición en Y")
    elif len(columnas_restantes) == 2:
        # Gráfico 2D
        x, y = columnas_restantes
        plot2D(x, y, primera_columna, "Posición en X", "Posición en Y")
    else:
        print("El archivo CSV debe tener dos o tres columnas.")
        sys.exit(1)

    # Guardar gráfico en archivo de salida
    plt.savefig(archivo_salida)
    print(f"Gráfico guardado en '{archivo_salida}'")

if __name__ == "__main__":
    main()