import numpy as np

def create_vector_a():
    global A
    A = np.array([2, 3, 5, 1, 4, 7, 9, 8, 6, 10])
    print("Vector A:", A)

def create_vector_b():
    global B
    B = np.arange(11, 21)
    print("Vector B:", B)

def concatenate_vectors():
    try:
        global C
        C = np.concatenate((A, B))
        print("Vector C:", C)
    except NameError:
        print("Create A and B first.")

def find_minimum():
    try:
        print("Min C:", np.min(C))
    except NameError:
        print("Create C first.")

def find_maximum():
    try:
        print("Max C:", np.max(C))
    except NameError:
        print("Create C first.")

def find_length():
    try:
        print("Length C:", len(C))
    except NameError:
        print("Create C first.")

def calculate_average():
    try:
        print("Average C:", np.mean(C))
    except NameError:
        print("Create C first.")

def calculate_median():
    try:
        print("Median C:", np.median(C))
    except NameError:
        print("Create C first.")

def calculate_sum():
    try:
        print("Sum C:", np.sum(C))
    except NameError:
        print("Create C first.")

def create_vector_d():
    try:
        global D
        D = C[C > 5]
        print("Vector D (C > 5):", D)
    except NameError:
        print("Create C first.")

def create_vector_e():
    try:
        global E
        E = C[(C > 5) & (C < 15)]
        print("Vector E (5 < C < 15):", E)
    except NameError:
        print("Create C first.")

def change_elements():
    try:
        C[C == 5] = '7'
        C[C == 15] = '7'
        print("C with 5/15 changed to '7':", C)
    except NameError:
        print("Create C first.")

def sort_vector():
    try:
        print("Sorted C:", np.sort(C))
    except NameError:
        print("Create C first.")

def multiply_vector():
    try:
        print("C * 10:", C * 10)
    except NameError:
        print("Create C first.")

def change_elements_range():
    try:
        C[5:8] = [60, 70, 80]
        print("C with elements 6-8 changed:", C)
    except NameError:
        print("Create C first.")

def change_elements_range_2():
    try:
        C[13:16] = [140, 150, 160]
        print("C with elements 14-16 changed:", C)
    except NameError:
        print("Create C first.")

def main_menu():
    options = {
        '1': ("Create vector A", create_vector_a),
        '2': ("Create vector B", create_vector_b),
        '3': ("Concatenate A and B into C", concatenate_vectors),
        '4': ("Find min of C", find_minimum),
        '5': ("Find max of C", find_maximum),
        '6': ("Find length of C", find_length),
        '7': ("Calculate average of C", calculate_average),
        '8': ("Calculate median of C", calculate_median),
        '9': ("Calculate sum of C", calculate_sum),
        '10': ("Create D (elements of C > 5)", create_vector_d),
        '11': ("Create E (5 < C < 15)", create_vector_e),
        '12': ("Change 5/15 of C to '7'", change_elements),
        '13': ("Sort C", sort_vector),
        '14': ("Multiply C by 10", multiply_vector),
        '15': ("Change elements 6-8 of C", change_elements_range),
        '16': ("Change elements 14-16 of C", change_elements_range_2),
        '0': ("Exit", None)
    }

    while True:
        print("\nNumPy Array Workshop")
        for key, (description, _) in options.items():
            print(f"{key}. {description}")

        choice = input("Enter your choice: ")

        if choice in options:
            if choice == '0':
                print("Exiting.")
                break
            else:
                options[choice][1]()
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()
