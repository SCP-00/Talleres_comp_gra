import numpy as np
#1)-------------------------------------------------------------------------------------------#
def create_vector_a():
    global A
    A = np.array([2, 3, 5, 1, 4, 7, 9, 8, 6, 10])
    print("Vector A:", A)
    return A

#2)-------------------------------------------------------------------------------------------#
def create_vector_b():
    global B
    B = np.arange(11, 21)
    print("Vector B:", B)
    return B

#3)-------------------------------------------------------------------------------------------#
def concatenate_vectors(*vectors):
    global C
    C = np.concatenate(vectors)
    print("Vector C (A + B):", C)
    return C

#4)-------------------------------------------------------------------------------------------#
def find_minimum():
    try:
        print("Min C:", np.min(C))
        return np.min(C)
    except NameError:
        print("Create C first.")

#5)-------------------------------------------------------------------------------------------#
def find_maximum():
    try:
        print("Max C:", np.max(C))
        return np.max(C)
    except NameError:
        print("Create C first.")

#6)-------------------------------------------------------------------------------------------#
def find_length():
    try:
        print("Length C:", len(C))
        return len(C)
    except NameError:
        print("Create C first.")

#7)-------------------------------------------------------------------------------------------#
def calculate_average():
    try:
        print("Average C:", sum(C) / len(C))
        return (sum(C) / len(C))
    except NameError:
        print("Create C first.")

#8)-------------------------------------------------------------------------------------------#
def calculate_mean():
    try:
        print("Mean C:", np.mean(C))
        return np.mean(C)
    except NameError:
        print("Create C first.")

#9)-------------------------------------------------------------------------------------------#
def calculate_median():
    try:
        print("Median C:", np.median(C))
        return np.median(C)
    except NameError:
        print("Create C first.")

#10)-------------------------------------------------------------------------------------------#
def calculate_sum():
    try:
        print("Sum C:", np.sum(C))
        return np.sum(C)
    except NameError:
        print("Create C first.")

#11)-------------------------------------------------------------------------------------------#
def create_vector_d():
    try:
        global D
        D = C[C > 5]
        print("Vector D (C > 5):", D)
        return D
    except NameError:
        print("Create C first.")

#12)-------------------------------------------------------------------------------------------#
def create_vector_e():
    try:
        global E
        E = C[(C > 5) & (C < 15)]
        print("Vector E (5 < C < 15):", E)
        return E
    except NameError:
        print("Create C first.")

#13)-------------------------------------------------------------------------------------------#
def change_elements():
    try:
        C[C == 5] = '7'
        C[C == 15] = '7'
        print("C with 5/15 changed to '7':", C)
        return C
    except NameError:
        print("Create C first.")

#14)-------------------------------------------------------------------------------------------#
def vector_mode():
    try:
        print("Mode C:", np.argmax(np.bincount(C)))
        return np.argmax(np.bincount(C))
    except NameError:
        print("Create C first.")

#15)-------------------------------------------------------------------------------------------#
def sort_vector():
    try:
        print("Sorted C:", np.sort(C))
        return np.sort(C)
    except NameError:
        print("Create C first.")

#16)-------------------------------------------------------------------------------------------#
def multiply_vector():
    try:
        C *= 10
        print("C * 10:", C)
        return C
    except NameError:
        print("Create C first.")

#17)-------------------------------------------------------------------------------------------#
def change_elements_range():
    try:
        C[5:8] = [60, 70, 80]
        print("C with elements 6-8 changed:", C)
        return C
    except NameError:
        print("Create C first.")

#18)-------------------------------------------------------------------------------------------#
def change_elements_range_2():
    try:
        C[13:16] = [140, 150, 160]
        print("C with elements 14-16 changed:", C)
        return C
    except NameError:
        print("Create C first.")

def menu():
    print("1. Create vector A")
    print("2. Create vector B")
    print("3. Concatenate vectors A and B")
    print("4. Find minimum value in C")
    print("5. Find maximum value in C")
    print("6. Find length of C")
    print("7. Calculate average of C")
    print("8. Calculate mean of C")
    print("9. Calculate median of C")
    print("10. Calculate sum of C")
    print("11. Create vector D (C > 5)")
    print("12. Create vector E (5 < C < 15)")
    print("13. Change elements 5 and 15 to 7")
    print("14. Find mode of C")
    print("15. Sort vector C")
    print("16. Multiply vector C by 10")
    print("17. Change elements 6-8 to 60, 70, 80")
    print("18. Change elements 14-16 to 140, 150, 160")
    print("0. Exit")
    option = int(input("Select an option: "))
    return option

def main():
    while True:
        option = menu()
        match option:
            case 1:
                create_vector_a()
            case 2:
                create_vector_b()
            case 3:
                concatenate_vectors(A, B)
            case 4:
                find_minimum()
            case 5:
                find_maximum()
            case 6:
                find_length()
            case 7:
                calculate_average()
            case 8:
                calculate_mean()
            case 9:
                calculate_median()
            case 10:
                calculate_sum()
            case 11:
                create_vector_d()
            case 12:
                create_vector_e()
            case 13:
                change_elements()
            case 14:
                vector_mode()
            case 15:
                sort_vector()
            case 16:
                multiply_vector()
            case 17:
                change_elements_range()
            case 18:
                change_elements_range_2()
            case 0:
                break
            case _:
                print("Invalid option")
if __name__ == '__main__':
    main()
