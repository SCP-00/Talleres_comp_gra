import numpy as np
import matplotlib.pyplot as plt
'''
cyan,blanco,rojo,
magenta,gris,verde,
amarillo, negro, azul

'''
def ejercicio_1():
    matriz = np.ones((3,3,3))
    matriz[0,0,0] = 0
    matriz[1,0,1] = 0
    matriz[2,0,2] = 0

    matriz[1,1,:] = 0.5
    matriz[2,1,:] = 0

    matriz[0,2,1] = matriz[0,2,2] = 0
    matriz[1,2,0] = matriz[1,2,2] = 0
    matriz[2,2,0] = matriz[2,2,1] = 0

    plt.imshow(matriz)
    plt.show()
#ejercicio_1()
def ejercicio_2():

    matriz = np.ones((10,11,3)) # matriz de tamaño 11x11
    matriz[7:,0,:] = 0.93
    matriz[7:,1,:] = 0.9
    matriz[7:,2,:] = 0.8
    matriz[7:,3,:] = 0.7
    matriz[7:,4,:] = 0.6
    matriz[7:,5,:] = 0.5
    matriz[7:,6,:] = 0.4
    matriz[7:,7,:] = 0.3
    matriz[7:,8,:] = 0.2
    matriz[7:,9,:] = 0.1
    matriz[7:,10,:] = 0
    
    matriz[:7,0,:] = int('98',16)/255,int('98',16)/255,int('00',16)/255
    matriz[:7,1:3,:] = int('00',16)/255,int('98',16)/255,int('98',16)/255
    matriz[:7,3:5,:] = int('00',16)/255,int('98',16)/255,int('00',16)/255
    matriz[:7,5:7,:] = int('98',16)/255,int('00',16)/255,int('98',16)/255
    matriz[:7,7:9,:] = int('98',16)/255,int('00',16)/255,int('00',16)/255
    matriz[:7,9:11,:] = int('00',16)/255,int('00',16)/255,int('98',16)/255
    

    plt.imshow(matriz)
    plt.__name__ = '"Imagen con escala de grises"'
    plt.show()

#ejercicio_2()

def ejercicio_3(): #invertir una imagen y mostar la original a la izquierda
    utp = plt.imread('UTP.jpg')
    
    plt.figure(figsize=(10, 5))  # Adjust figure size as needed

    plt.subplot(1, 2, 1)  # 1 row, 2 columns, first subplot
    plt.imshow(utp)
    plt.title('Original')

    plt.subplot(1, 2, 2)  # 1 row, 2 columns, second subplot
    plt.imshow(1 - utp)
    plt.title('Inverted')

    plt.tight_layout()  # Adjust layout to prevent overlapping titles
    plt.show()
#ejercicio_3()

def ejercicio_4(capa_de_color):
    utp = plt.imread('UTP.jpg')
    match capa_de_color:
        case 0:
            plt.imshow(utp[:, :, 0], cmap='Reds')
            plt.title('Red channel')
        case 1:
            plt.imshow(utp[:, :, 1], cmap='Greens')
            plt.title('Green channel')
        case 2:
            plt.imshow(utp[:, :, 2], cmap='Blues')
            plt.title('Blue channel')
        case 3: #magenta
            utp_copy = utp.copy()
            utp_copy[:, :, 1] = 0  # Set green channel to 0
            plt.imshow(utp_copy)
            plt.title('Magenta channel')
        case 4: #cyan
            utp_copy = utp.copy()
            utp_copy[:, :, 0] = 0  # Set red channel to 0
            plt.imshow(utp_copy)
            plt.title('Cyan channel')
        case 5: #amarillo
            utp_copy = utp.copy()
            utp_copy[:, :, 2] = 0  # Set blue channel to 0
            plt.imshow(utp_copy)
            plt.title('Yellow channel')
        case default:
            raise ValueError('Canal de color invalido')
    plt.show()

#ejercicio_4(0)
#ejercicio_4(1)
#ejercicio_4(2)
#ejercicio_4(3)
#ejercicio_4(4)
#ejercicio_4(5)

def ejercicio_5(): # Reconstruir el color de una imagen con la suma de sus 3 capas
    utp = plt.imread('UTP.jpg')
    
ejercicio_5()