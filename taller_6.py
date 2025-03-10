import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
#1)------------------------------------------------------------------------#
def crear_y_manipular_arrays():
    A = np.arange(1, 16).reshape(3, 5)
    print("Array A:\n", A)
    return A

#2)------------------------------------------------------------------------#
def operaciones_basicas(A):
    suma_A = np.sum(A)
    media_A = np.mean(A)
    producto_A = np.prod(A)
    print("\nSuma de A:", suma_A)
    print("Media de A:", media_A)
    print("Producto de A:", producto_A)

#3)------------------------------------------------------------------------#
def acceso_y_slicing(A):
    elementos_seleccionados = A[1, 1:3]
    print("\nElementos seleccionados de A:", elementos_seleccionados)

#4)------------------------------------------------------------------------#
def indexacion_booleana(A):
    B = A[A > 7]
    print("\nArray B (elementos de A mayores que 7):\n", B)

#5)------------------------------------------------------------------------#
def algebra_lineal():
    C = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    try:
        determinante_C = np.linalg.det(C)
        inversa_C = np.linalg.inv(C)
        print("\nMatriz C:\n", C)
        print("Determinante de C:", determinante_C)
        print("Inversa de C:\n", inversa_C)
    except np.linalg.LinAlgError:
        print("\nMatriz C:\n", C)
        print("La matriz C no tiene inversa (es singular).")

#6)------------------------------------------------------------------------#
def estadisticas_numpy():
    D = np.random.rand(100)
    maximo_D = np.max(D)
    minimo_D = np.min(D)
    media_D = np.mean(D)
    desviacion_estandar_D = np.std(D)
    print("\nValor máximo de D:", maximo_D)
    print("Valor mínimo de D:", minimo_D)
    print("Media de D:", media_D)
    print("Desviación estándar de D:", desviacion_estandar_D)
    return D

#7)------------------------------------------------------------------------#
def grafico_basico(): #graficar seno y coseno en el intervalo [-2π, 2π]
    x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
    seno = np.sin(x)
    coseno = np.cos(x)

    plt.figure(figsize=(8, 6))
    plt.plot(x, seno, label='Seno', color='blue', linestyle='-', linewidth=2)
    plt.plot(x, coseno, label='Coseno', color='red', linestyle='--', linewidth=2)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfico de Seno y Coseno')
    plt.legend()
    plt.grid(True)
    plt.show()
#8)------------------------------------------------------------------------#
def graficos_dispersion(D):
    indices = np.arange(len(D))
    plt.figure(figsize=(8, 6))
    plt.scatter(indices, D, alpha=0.7)
    plt.xlabel('Índice')
    plt.ylabel('Valor')
    plt.title('Gráfico de Dispersión de D')
    plt.grid(True)
    plt.show()

#9)------------------------------------------------------------------------#
def histogramas(D):
    plt.figure(figsize=(8, 6))
    plt.hist(D, bins=30, color='skyblue', edgecolor='black')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de D')
    plt.grid(True)
    plt.show()

#10)------------------------------------------------------------------------#
def manipulacion_imagenes():
    try:
        img = mpimg.imread('C:\\Users\\andyh\\Documents\\Computacion_grafica\\Codigo\\Fries.jpg')
        img_gris = np.mean(img, axis=2)

        plt.figure(figsize=(10, 5))

        plt.subplot(1, 2, 1)
        plt.imshow(img)
        plt.title('Imagen Original')
        plt.axis('off')

        plt.subplot(1, 2, 2)
        plt.imshow(img_gris, cmap='gray')
        plt.title('Imagen en Escala de Grises')
        plt.axis('off')

        plt.show()
    except FileNotFoundError:
        print("\nError: No se encontró la imagen 'Fries.jpg'.")
    except Exception as e:
        print(f"\nSe produjo un error al procesar la imagen: {e}")

#---------------------------------------------------------------------------#
def menu():
    while True:
        print("\nMenú:")
        print("1. Creación y Manipulación de Arrays")
        print("2. Operaciones Básicas")
        print("3. Acceso y Slicing")
        print("4. Indexación Booleana")
        print("5. Álgebra Lineal")
        print("6. Estadísticas con NumPy")
        print("7. Gráfico Básico")
        print("8. Gráficos de Dispersión")
        print("9. Histogramas")
        print("10. Manipulación de Imágenes con Matplotlib")
        print("11. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            A = crear_y_manipular_arrays()
        elif opcion == '2':
            operaciones_basicas(A)
        elif opcion == '3':
            acceso_y_slicing(A)
        elif opcion == '4':
            indexacion_booleana(A)
        elif opcion == '5':
            algebra_lineal()
        elif opcion == '6':
            D = estadisticas_numpy()
        elif opcion == '7':
            grafico_basico()
        elif opcion == '8':
            graficos_dispersion(D)
        elif opcion == '9':
            histogramas(D)
        elif opcion == '10':
            manipulacion_imagenes()
        elif opcion == '11':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
