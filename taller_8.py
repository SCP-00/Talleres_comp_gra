import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

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

def ejercicio_2():
    matriz = np.ones((10,11,3)) # matriz de tamaño 10x11
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
    plt.title('Imagen con escala de grises')
    plt.show()

def ejercicio_3():
    utp = mpimg.imread('C:\\Users\\andyh\\Documents\\Computacion_grafica\\Codigo\\UTP.jpg')
    
    plt.figure(figsize=(10, 5))  # Adjust figure size as needed

    plt.subplot(1, 2, 1)  # 1 row, 2 columns, first subplot
    plt.imshow(utp)
    plt.title('Original')

    plt.subplot(1, 2, 2)  # 1 row, 2 columns, second subplot
    plt.imshow(1 - utp)
    plt.title('Inverted')

    plt.tight_layout()  # Adjust layout to prevent overlapping titles
    plt.show()

def ejercicio_4(capa_de_color):
    utp = mpimg.imread('C:\\Users\\andyh\\Documents\\Computacion_grafica\\Codigo\\UTP.jpg')
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
        case _:
            raise ValueError('Canal de color invalido')
    plt.show()

def ejercicio_5():
    utp = mpimg.imread('C:\\Users\\andyh\\Documents\\Computacion_grafica\\Codigo\\UTP.jpg')
    red_channel = utp[:, :, 0]
    green_channel = utp[:, :, 1]
    blue_channel = utp[:, :, 2]
    
    reconstructed_image = np.stack((red_channel, green_channel, blue_channel), axis=2)
    
    plt.imshow(reconstructed_image)
    plt.title('Reconstructed Image')
    plt.show()

def fusionar_imagenes(img1, img2):
    return ((img1 / 2 + img2 / 2).astype(np.uint8))

def fusionar_imagenes_ecualizadas(img1, img2):
    img1_eq = (img1 - img1.min()) / (img1.max() - img1.min()) * 255
    img2_eq = (img2 - img2.min()) / (img2.max() - img2.min()) * 255
    return (fusionar_imagenes(img1_eq.astype(np.uint8), img2_eq.astype(np.uint8)))

def ecualizar_imagen(img, factor):
    img_eq = (img - img.min()) / (img.max() - img.min()) * factor
    return (img_eq.astype(np.uint8))

def promedio_imagen(img):
    return (np.mean(img, axis=2).astype(np.uint8))

def escala_grises_promedio(img):
    gray = np.mean(img, axis=2)
    return (np.stack((gray, gray, gray), axis=2).astype(np.uint8))

def escala_grises_luminosidad(img):
    gray = 0.21 * img[:, :, 0] + 0.72 * img[:, :, 1] + 0.07 * img[:, :, 2]
    return (np.stack((gray, gray, gray), axis=2).astype(np.uint8))

def escala_grises_midgray(img):
    gray = (img[:, :, 0] + img[:, :, 1] + img[:, :, 2]) / 3
    return (np.stack((gray, gray, gray), axis=2).astype(np.uint8))

def ejercicio_6():
    img1 = mpimg.imread('C:\\Users\\andyh\\Documents\\Computacion_grafica\\Codigo\\UTP.jpg')
    img2 = mpimg.imread('C:\\Users\\andyh\\Documents\\Computacion_grafica\\Codigo\\Fries.jpg')
    
    # Resize img2 to match the size of img1
    img2 = np.array(Image.fromarray(img2).resize((img1.shape[1], img1.shape[0])))
    
    fusion = fusionar_imagenes(img1, img2)
    fusion_eq = fusionar_imagenes_ecualizadas(img1, img2)
    img_eq = ecualizar_imagen(img1, 255)
    img_promedio = promedio_imagen(img1)
    img_gris_promedio = escala_grises_promedio(img1)
    img_gris_luminosidad = escala_grises_luminosidad(img1)
    img_gris_midgray = escala_grises_midgray(img1)
    
    plt.figure(figsize=(15, 10))
    
    plt.subplot(2, 4, 1)
    plt.imshow(fusion)
    plt.title('Fusion sin ecualizar')
    
    plt.subplot(2, 4, 2)
    plt.imshow(fusion_eq)
    plt.title('Fusion ecualizada')
    
    plt.subplot(2, 4, 3)
    plt.imshow(img_eq)
    plt.title('Imagen ecualizada')
    
    plt.subplot(2, 4, 4)
    plt.imshow(img_promedio, cmap='gray')
    plt.title('Promedio')
    
    plt.subplot(2, 4, 5)
    plt.imshow(img_gris_promedio)
    plt.title('Escala de grises (Promedio)')
    
    plt.subplot(2, 4, 6)
    plt.imshow(img_gris_luminosidad)
    plt.title('Escala de grises (Luminosidad)')
    
    plt.subplot(2, 4, 7)
    plt.imshow(img_gris_midgray)
    plt.title('Escala de grises (Midgray)')
    
    plt.tight_layout()
    plt.show()

def menu():
    while True:
        print("\nSeleccione una opción:")
        print("1. Ejercicio 1")
        print("2. Ejercicio 2")
        print("3. Ejercicio 3")
        print("4. Ejercicio 4")
        print("5. Ejercicio 5")
        print("6. Ejercicio 6")
        print("0. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            ejercicio_1()
        elif opcion == "2":
            ejercicio_2()
        elif opcion == "3":
            ejercicio_3()
        elif opcion == "4":
            capa = int(input("Ingrese el número de la capa de color (0-5): "))
            ejercicio_4(capa)
        elif opcion == "5":
            ejercicio_5()
        elif opcion == "6":
            ejercicio_6()
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
