import math
import sympy as sp # Import sympy library to use symbolic mathematics
def excersice_1():
    #Science calculator
    print("Science calculator")
    print("1. Sum\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponentiation\n6. Square root\n7. Logarithm\n8. Sine\n9. Cosine\n10. Tangent\n11. Cotangent\n12. Secant\n13. Cosecant\n14. Factorial\n15. Exit")
    option = int(input("Choose an option: "))
    menu = True
    while menu:
        if option == 1:
            print("Sum")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(f"The sum of {num1} and {num2} is: {num1 + num2}")
            option = int(input("Choose an option: "))
        elif option == 2:
            print("Subtraction")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(f"The subtraction of {num1} and {num2} is: {num1 - num2}")
            option = int(input("Choose an option: "))
        elif option == 3:
            print("Multiplication")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(f"The multiplication of {num1} and {num2} is: {num1 * num2}")
            option = int(input("Choose an option: "))
        elif option == 4:
            print("Division")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(f"The division of {num1} and {num2} is: {num1 / num2}")
            option = int(input("Choose an option: "))
        elif option == 5:
            print("Exponentiation")
            num1 = float(input("Enter the base: "))
            num2 = float(input("Enter the exponent: "))
            print(f"{num1} raised to the power of {num2} is: {num1 ** num2}")
            option = int(input("Choose an option: "))
        elif option == 6:
            print("Square root")
            num1 = float(input("Enter the number: "))
            print(f"The square root of {num1} is: {math.sqrt(num1)}")
            option = int(input("Choose an option: "))
        elif option == 7:
            print("Logarithm")
            num1 = float(input("Enter the number: "))
            print(f"The logarithm of {num1} is: {math.log(num1)}")
            option = int(input("Choose an option: "))
        elif option == 8:
            print("Sine")
            num1 = float(input("Enter the angle in degrees: "))
            print(f"The sine of {num1} degrees is: {math.sin(math.radians(num1))}")
            option = int(input("Choose an option: "))
        elif option == 9:
            print("Cosine")
            num1 = float(input("Enter the angle in degrees: "))
            print(f"The cosine of {num1} degrees is: {math.cos(math.radians(num1))}")
            option = int(input("Choose an option: "))
        elif option == 10:
            print("Tangent")
            num1 = float(input("Enter the angle in degrees: "))
            print(f"The tangent of {num1} degrees is: {math.tan(math.radians(num1))}")
            option = int(input("Choose an option: "))
        elif option == 11:
            print("Cotangent")
            num1 = float(input("Enter the angle in degrees: "))
            print(f"The cotangent of {num1} degrees is: {1 / math.tan(math.radians(num1))}")
            option = int(input("Choose an option: "))
        elif option == 12:
            print("Secant")
            num1 = float(input("Enter the angle in degrees: "))
            print(f"The secant of {num1} degrees is: {1 / math.cos(math.radians(num1))}")
            option = int(input("Choose an option: "))
        elif option == 13:
            print("Cosecant")
            num1 = float(input("Enter the angle in degrees: "))
            print(f"The cosecant of {num1} degrees is: {1 / math.sin(math.radians(num1))}")
            option = int(input("Choose an option: "))
        elif option == 14:
            print("Factorial")
            num1 = int(input("Enter the number: "))
            print(f"The factorial of {num1} is: {math.factorial(num1)}")
            option = int(input("Choose an option: "))
        elif option == 15:
            print("Goodbye")
            menu = False
        else:
            print("Invalid option")
            option = int(input("Choose an option: "))
    return

def excersice_1_2():
    #Solve the expression
    x = sp.symbols('x')
    y = sp.symbols('y')
    z = sp.symbols('z')
    print("Calculate expressions as derivatives, integrals, limits,cuadratic, simply, etc.")
    print("1. Derivative\n2. Integral\n3. Limit\n4. Simplify\n5. Factor\n6. Expand\n7. Quadratic\n8. Exit")
    option = int(input("Choose an option: "))
    menu = True
    while menu:
        if option == 1:
            print("Derivative")
            expression = input("Enter the expression: ")
            print(f"The derivative of {expression} is: {sp.diff(expression, x)}")
            option = int(input("Choose an option: "))
        elif option == 2:
            print("Integral")
            expression = input("Enter the expression: ")
            print(f"The integral of {expression} is: {sp.integrate(expression, x)}")
            option = int(input("Choose an option: "))
        elif option == 3:
            print("Limit")
            expression = input("Enter the expression: ")
            print(f"The limit of {expression} is: {sp.limit(expression, x, 0)}")
            option = int(input("Choose an option: "))
        elif option == 4:
            print("Simplify")
            expression = input("Enter the expression: ")
            print(f"The simplified expression is: {sp.simplify(expression)}")
            option = int(input("Choose an option: "))
        elif option == 5:
            print("Factor")
            expression = input("Enter the expression: ")
            print(f"The factor of the expression is: {sp.factor(expression)}")
            option = int(input("Choose an option: "))
        elif option == 6:
            print("Expand")
            expression = input("Enter the expression: ")
            print(f"The expanded expression is: {sp.expand(expression)}")
            option = int(input("Choose an option: "))
        elif option == 7:
            print("Quadratic")
            a = float(input("Enter the value of a: "))
            b = float(input("Enter the value of b: "))
            c = float(input("Enter the value of c: "))
            print(f"The solutions of the quadratic equation are: {sp.solve(a*x**2 + b*x + c, x)}")
            option = int(input("Choose an option: "))
        elif option == 8:
            print("Goodbye")
            menu = False
        else:
            print("Invalid option")
            option = int(input("Choose an option: "))
    return

def excersice_2(*lists):
    result = []
    for list_i in lists:
        list_aux = []
        for element in list_i:
            if element % 2 == 0:
                list_aux.append(element)
        result.append(list_aux)
    return f"New list: {result}"

## example
#list1 = [1, 2, 3, 4, 5, 6]
#list2 = [7, 8, 9, 10, 11, 12]
#print(excersice_2(list1, list2))

def excersice_3(*lists):
    result = []
    for list_i in lists:
        list_aux = list(map(lambda x: x * 9/5 + 32, list_i))
        result.append(list_aux)
    return f"New list: {result}"

## example
#list1 = [0, 10, 20, 30, 40, 50]

def excersice_4(grades: list):
    for grade in grades:
        if grade.between(0, 59):
            print(f"{grade} is F")
        elif grade.between(60, 69):
            print(f"{grade} is D")
        elif grade.between(70, 79):
            print(f"{grade} is C")
        elif grade.between(80, 89):
            print(f"{grade} is B")
        elif grade.between(90, 100):
            print(f"{grade} is A")
        else:
            print("Invalid grade")
    return f"Grades: {grades}"
#print(excersice_4([50, 60, 70, 80, 90, 100, 110]))

def exercise_5(*txt):
    words = {}
    for text in txt:
        for word in text.split():
            word = word.lower()
            word = word.strip(".,")
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
    return words

def excerise_6(list, element):
    for i in range(len(list)):
        if list[i] == element:
            return i
    return -1

def excersice_7(*txt): #no es un compilador, por lo tanto no tiene analisis semantico para comprobar si los parentesis estan bien cerrados,
    #por lo tanto se asume que si hay un parentesis de cierre sin uno de apertura, no esta bien cerrado. Sin importar el orden.
    words = {}
    round_brackets = 0
    square_brackets = 0
    curly_brackets = 0
    for text in txt:
        for word in text:
            if word == "(":
                round_brackets += 1
            elif word == ")":
                round_brackets -= 1
            if round_brackets < 0:
                return False
            elif word == "[":
                square_brackets += 1
            elif word == "]":
                square_brackets -= 1
            if square_brackets < 0:
                return False
            elif word == "{":
                curly_brackets += 1
            elif word == "}":
                curly_brackets -= 1
            if curly_brackets < 0:
                return False
    print(f"Round brackets: {round_brackets}\nSquare brackets: {square_brackets}\nCurly brackets: {curly_brackets}")
    if round_brackets == 0 and square_brackets == 0 and curly_brackets == 0:
        return True
    return False

#print(excersice_7("()[]{}", "([{}])", "(["))

def excersice_8(register:list):
        if type(register) != list or len(register) == 0:
            return None
        for register_i in register:
         if type(register_i) != tuple and len(register_i) != 2:
             return False
         #sort first by age and then by name (name, age)
         sorted_register = sorted(register, key=lambda x: (x[1], x[0]))
        return sorted_register
#print(excersice_8([("Juan", 25), ("Maria", 30), ("Pedro", 20), ("Ana", 25)])))

def excersice_9():
    import random
    import string
    password = ""
    while True:
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(12, 16)))
        if not any(c.isdigit() for c in password):
            continue
        if not any(c.isupper() for c in password):
            continue
        if not any(c.islower() for c in password):
            continue
        if "_" in password:
            continue
        break
    return password
#print(excersice_9())


def excersice_10():
    contacts = {}
    def add_contact(name, phone):
        contacts[name] = phone
        return contacts
    def search_contact(name):
        if name in contacts:
            return f"{name}: {contacts[name]}"
        return "Contact not found"
    def delete_contact(name):
        if name in contacts:
            del contacts[name]
            return contacts
        return "Contact not found"
    def show_contacts():
        return contacts
    print("Phonebook")
    print("1. Add contact\n2. Search contact\n3. Delete contact\n4. Show contacts\n5. Exit")
    option = int(input("Choose an option: "))
    menu = True
    while menu:
        if option == 1:
            print("Add contact")
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            print(add_contact(name, phone))
            option = int(input("Choose an option: "))
        elif option == 2:
            print("Search contact")
            name = input("Enter the name: ")
            print(search_contact(name))
            option = int(input("Choose an option: "))
        elif option == 3:
            print("Delete contact")
            name = input("Enter the name: ")
            print(delete_contact(name))
            option = int(input("Choose an option: "))
        elif option == 4:
            print("Show contacts")
            print(show_contacts())
            option = int(input("Choose an option: "))
        elif option == 5:
            print("Goodbye")
            menu = False
        else:
            print("Invalid option")
            option = int(input("Choose an option: "))
    return

def menu():
    print("1. Exercise 1\n2. Exercise 1.2\n3. Exercise 2\n4. Exercise 3\n5. Exercise 4\n6. Exercise 5\n7. Exercise 6\n8. Exercise 7\n9. Exercise 8\n10. Exercise 9\n11. Exercise 10\n12. Exit")
    option = int(input("Choose an option: "))
    while option != 11:
        if option == 1:
            excersice_1()
        elif option == 2:
            excersice_1_2()
        elif option == 3:
            list1 = [1, 2, 3, 4, 5, 6]
            list2 = [7, 8, 9, 10, 11, 12]
            print(excersice_2(list1, list2))
        elif option == 4:
            list1 = [0, 10, 20, 30, 40, 50]
            print(excersice_3(list1))
        elif option == 5:
            print(excersice_4([50, 60, 70, 80, 90, 100, 110]))
        elif option == 6:
            print(exercise_5("Hello world", "Python is awesome", "Python is easy", "Python is fun"))
        elif option == 7:
            print(excerise_6([1, 2, 3, 4, 5, 6], 4))
        elif option == 8:
            print(excersice_7("()[]{}", "([{}])", "([")) 
        elif option == 9:
            print(excersice_8([("Juan", 25), ("Maria", 30), ("Pedro", 20), ("Ana", 25)]))
        elif option == 10:
            excersice_10()
        elif option == 11:
            print("Goodbye")
            break
        else:
            print("Invalid option")
            option = int(input("Choose an option: "))
    return

if __name__ == "__main__":
    menu()
