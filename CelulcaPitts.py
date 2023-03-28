import numpy as np

def compuerta(umbral):
    for i in range(0,4):
        activation = puerta(productos[i], umbral)
        print(f'Activacion: {activation}')
    print(' ')

table = np.array([
    [0,0], [0,1], [1,0], [1,1] 
])
pesos = np.array([9,2])
productos = table @ pesos
umbral = 9
print(f'productos: {productos}')
compuerta(umbral)

def puerta(dot: int, T: float) -> int:
    '''Salida del umbral'''
    if dot >= T:
        return 1
    else:
        return 0