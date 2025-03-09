import numpy as np

def exercise_1():
    """Array Creation and Properties"""
    arr = np.array(range(1, 11))
    arr = arr.reshape(2, 5)
    print("Array:\n", arr)
    print("Shape:", arr.shape)
    print("Size:", arr.size)
    print("Dimensions:", arr.ndim)

def exercise_2():
    """Basic Operations"""
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print("Sum:", a + b)
    print("Subtraction:", a - b)
    print("Element-wise product:", a * b)
    print("Sum of elements in a:", np.sum(a))

def exercise_3():
    """Indexing and Slicing"""
    data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    print("Fifth element:", data[4])
    print("Subsection from the third to the seventh element:", data[2:7])

def exercise_4():
    """Broadcasting and Universal Functions"""
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("A + 10:\n", A + 10)
    print("Square root of A:\n", np.sqrt(A))

def exercise_5():
    """Shape Manipulation and Linear Algebra"""
    M = np.array([[1, 2], [3, 4], [5, 6]])
    M = M.reshape(3, 2)
    print("M:\n", M)
    print("Dot product of M and M.T:\n", np.dot(M, M.T))

def exercise_6():
    """Working with Missing Data"""
    data = np.array([1, 2, np.nan, 4, 5, np.nan, 7, 8, 9, 10])
    data = np.nan_to_num(data, nan=0)
    print("Array with NaN replaced by 0:\n", data)
    print("Mean of the array:", np.mean(data))

def menu():
    """Interactive menu"""
    while True:
        print("\n--- Menu ---")
        print("1. Exercise 1: Array Creation and Properties")
        print("2. Exercise 2: Basic Operations")
        print("3. Exercise 3: Indexing and Slicing")
        print("4. Exercise 4: Broadcasting and Universal Functions")
        print("5. Exercise 5: Shape Manipulation and Linear Algebra")
        print("6. Exercise 6: Working with Missing Data")
        print("7. Exercise 7: Saving and Loading Arrays")
        print("0. Exit")

        option = input("Select an exercise: ")

        if option == '1':
            exercise_1()
        elif option == '2':
            exercise_2()
        elif option == '3':
            exercise_3()
        elif option == '4':
            exercise_4()
        elif option == '5':
            exercise_5()
        elif option == '6':
            exercise_6()
        elif option == '0':
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    menu()
