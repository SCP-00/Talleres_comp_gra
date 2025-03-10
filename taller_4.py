import numpy as np

def create_one_dimensional_array():
    array_1 = np.arange(1, 11)
    print("1) One-Dimensional Array:", array_1)

def create_two_dimensional_matrix():
    matrix_2d = np.arange(1, 10).reshape(3, 3)
    print("\n2) Two-Dimensional Matrix:\n", matrix_2d)

def sum_two_arrays():
    array_2 = np.arange(1, 6)
    sum_array = array_2 + array_2
    print("\n3) Sum of Two Arrays:", sum_array)

def exponential_of_array():
    array_2 = np.arange(1, 6)
    exp_array = np.exp(array_2)
    print("\n4) Exponential of Array:", exp_array)

def even_elements_of_array():
    array_1 = np.arange(1, 11)
    even_array = array_1[array_1 % 2 == 0]
    print("\n5) Even Elements of Array:", even_array)

def create_random_array():
    random_array = np.random.rand(10)
    print("\n6) Random Array:", random_array)

def mean_of_array():
    array_3 = np.arange(1, 6)
    mean_value = np.mean(array_3)
    print("\n7) Mean of Array:", mean_value)

def array_with_constant_value():
    array_4 = np.full(5, 7)
    print("\n8) Array with Constant Value:", array_4)

def sum_with_broadcasting():
    array_5 = np.arange(1, 3+1)
    array_6 = np.arange(4, 6+1)
    sum_broadcast_array = array_5 + array_6
    print("\n9) Sum with Broadcasting:", sum_broadcast_array)

def create_two_dimensional_array_2():
    array_7 = np.arange(1, 7).reshape(2, 3)
    print("\n10) Two-Dimensional Array:\n", array_7)

def main_menu():
    while True:
        print("\nMenu:")
        print("1) Create One-Dimensional Array")
        print("2) Create Two-Dimensional Matrix")
        print("3) Sum of Two Arrays")
        print("4) Exponential of Array")
        print("5) Even Elements of Array")
        print("6) Create Random Array")
        print("7) Mean of Array")
        print("8) Array with Constant Value")
        print("9) Sum with Broadcasting")
        print("10) Create Two-Dimensional Array")
        print("0) Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_one_dimensional_array()
        elif choice == '2':
            create_two_dimensional_matrix()
        elif choice == '3':
            sum_two_arrays()
        elif choice == '4':
            exponential_of_array()
        elif choice == '5':
            even_elements_of_array()
        elif choice == '6':
            create_random_array()
        elif choice == '7':
            mean_of_array()
        elif choice == '8':
            array_with_constant_value()
        elif choice == '9':
            sum_with_broadcasting()
        elif choice == '10':
            create_two_dimensional_array_2()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
