import math
import numpy as np
import matplotlib.pyplot as plt
import random
## Free fall
def excersice_1(*highs):
    g = 9.80665 # m/s^2
    
    plt.xlabel('Time (s)')
    plt.ylabel('High (m)')
    plt.title('Free fall')
    plt.grid()
    max_high = max(highs)
    max_time = math.sqrt(2 * max_high / 9.80665)
    plt.axis([0, max_time + 1, 0, max_high + 10])
    
    results = []
    for high in highs:
        t = math.sqrt(2 * high / g)
        speed = g * t
        plt.plot(t, high, 'ro') # ro = red circle
        #assign the exact value of the point as a label
        plt.text(t, high, '({:.3f} s, {:.3f} m, {:.3f} m/s)'.format(t, high, speed))
        results.append((t, high, speed))
    
    plt.show()
    return results

## example
#print(excersice_1(9.8, 20, 50, 100, 250)) # No define the number of points from 1 to unlimited

## Converter km/h to m/s and vice versa
def excersice_2(*duple):
    data = []
    for d in duple:
        if d[1] == 'km/h':
            # Original in km/h, convert to m/s and mph
            data.append([d[0], d[0] * 1000 / 3600, d[0] * 0.621371])
        elif d[1] == 'm/s':
            # Original in m/s, convert to km/h and mph
            data.append([d[0] * 3.6, d[0], d[0] * 2.23694])
        elif d[1] == 'mph':
            # Original in mph, convert to km/h and m/s
            data.append([d[0] * 1.60934, d[0] * 0.44704, d[0]])
    
    col_labels = ['km/h', 'm/s', 'mph']
    
    # Format data for better readability
    formatted_data = []
    for row in data:
        formatted_data.append([f"{val:.2f}" for val in row])
    
    # Set background color
    colors = []
    for _ in range(len(data)):
        colors.append([['lightgreen', 'white', 'white'][i] for i in range(len(col_labels))])
    
    plt.figure(figsize=(8, 4))
    plt.table(cellText=formatted_data, colLabels=col_labels, loc='center', cellColours=colors)
    
    plt.axis('off')
    plt.title('Speed Conversion Table')
    plt.tight_layout()
    plt.show()
    
    return formatted_data

## example
#print(excersice_2((100, 'km/h'), (27, 'm/s'), (50, 'km/h'), (13, 'm/s'), (60, 'mph')))

## Movement MUR
def excersice_3(*data): # data = (vi, a, t)
    results = []
    for d in data:
        vi, a, t = d
        vf = vi + a * t
        s = vi * t + 0.5 * a * t ** 2
        results.append((vi, a, t, vf, s))
    
    col_labels = ['vi (m/s)', 'a (m/s^2)', 't (s)', 'vf (m/s)', 's (m)']
    
    # Format data for better readability
    formatted_data = []
    for row in results:
        formatted_data.append([f"{val:.2f}" for val in row])
    
    plt.figure(figsize=(10, 4))
    plt.table(cellText=formatted_data, colLabels=col_labels, loc='center')
    
    plt.axis('off')
    plt.title('Movement MUR Table')
    plt.tight_layout()
    plt.show()

    return results

## example
#print(excersice_3((10, 2, 5), (15, 3, 3), (20, 4, 2), (25, 5, 1), (30, 6, 0.5)))

## Vector sum
def excersice_4(vec_1, vec_2):
    if len(vec_1) != len(vec_2):
        return 'The vectors must have the same length'
    else:
        result = [vec_1[i] + vec_2[i] for i in range(len(vec_1))]
        return f"Vectores: {vec_1}  :  {vec_2} \nResultado: {result}"
    
## example
#print(excersice_4([1, 2, 3], [4, 5, 6]))
#print(excersice_4([1, 2, 3], [4, 5, 6, 7]))
#print(excersice_4([3, 4], [ 6, 7]))
        
## scalar product betweeb two vectors and angle
def excersice_5(vec_1, vec_2):
    if len(vec_1) != len(vec_2):
        return 'The vectors must have the same length'
    else:
        scalar_product = sum([vec_1[i] * vec_2[i] for i in range(len(vec_1))])
        norm_1 = math.sqrt(sum([val ** 2 for val in vec_1]))
        norm_2 = math.sqrt(sum([val ** 2 for val in vec_2]))
        angle = math.acos(scalar_product / (norm_1 * norm_2))
        return f"Vectores: {vec_1}  :  {vec_2} \nProducto escalar: {scalar_product} \nÁngulo: {angle:.2f} rad ({math.degrees(angle):.2f}°)"

def deg_to_rad(deg):
    return deg * math.pi / 180
## projectile launch
def excersice_6(v0, angle):
    g = 9.80665  # m/s^2
    angle_rad = deg_to_rad(angle)
    
    # Calculate key parameters
    t_flight = 2 * v0 * math.sin(angle_rad) / g
    max_height = (v0 ** 2) * (math.sin(angle_rad) ** 2) / (2 * g)
    max_distance = (v0 ** 2) * math.sin(2 * angle_rad) / g
    
    # Create points for the trajectory
    t_points = np.linspace(0, t_flight, 100)
    x_points = v0 * np.cos(angle_rad) * t_points
    y_points = v0 * np.sin(angle_rad) * t_points - 0.5 * g * t_points**2
    
    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(x_points, y_points)
    plt.grid(True)
    plt.xlabel('Distance (m)')
    plt.ylabel('Height (m)')
    plt.title(f'Projectile Motion (v₀={v0} m/s, angle={angle}°)')
    
    # Add annotations
    # Initial velocity vector
    plt.arrow(0, 0, v0*math.cos(angle_rad)/2, v0*math.sin(angle_rad)/2, 
              head_width=max_height/20, head_length=max_height/10, fc='blue', ec='blue')
    plt.text(v0*math.cos(angle_rad)/4, v0*math.sin(angle_rad)/4 + max_height/10, 
             f'{v0} m/s', color='blue')
    
    # Max height
    plt.plot([max_distance/2], [max_height], 'ro')
    plt.vlines(max_distance/2, 0, max_height, linestyles='dashed', colors='red')
    plt.text(max_distance/2 + max_distance/40, max_height*0.8, f'Max height: {max_height:.2f} m', color='red')
    
    # Max distance
    plt.plot([max_distance], [0], 'go')
    plt.text(max_distance*0.8, max_height/10, f'δ_x: {max_distance:.2f} m', color='green')
    
    # Time
    plt.text(max_distance/3, max_height/3, f'Time: {t_flight:.2f} s', 
             bbox=dict(facecolor='white', alpha=0.5))
    
    plt.axis([0, max_distance*1.1, 0, max_height*1.2])
    plt.show()
    
    return f"Time: {t_flight:.2f} s\nMax height: {max_height:.2f} m\nMax distance: {max_distance:.2f} m"

## example
#print(excersice_6(200, 60))


def menu():
    default_option = int(input("Use default values? (1: Yes, 0: No): "))
    if default_option == 0:
        option = int(input('Select an option:\n1. Free fall\n2. Speed conversion\n3. Movement MUR\n4. Vector sum\n5. Scalar product between two vectors and angle\n6. Projectile launch\n'))
        match option:
            case 1:
                highs = []
                n = int(input('Enter the number of points: '))
                for i in range(n):
                    high = float(input(f'Enter the height of point {i + 1}: '))
                    highs.append(high)
                excersice_1(*highs)
            case 2:
                data = []
                n = int(input('Enter the number of data: '))
                for i in range(n):
                    speed = float(input(f'Enter the speed of point {i + 1}: '))
                    unit = input(f'Enter the unit of point {i + 1} (km/h, m/s, mph): ')
                    data.append((speed, unit))
                excersice_2(*data)
            case 3:
                data = []
                n = int(input('Enter the number of data: '))
                for i in range(n):
                    vi = float(input(f'Enter the initial velocity of point {i + 1}: '))
                    a = float(input(f'Enter the acceleration of point {i + 1}: '))
                    t = float(input(f'Enter the time of point {i + 1}: '))
                    data.append((vi, a, t))
                excersice_3(*data)
            case 4:
                vec_1 = []
                vec_2 = []
                n = int(input('Enter the number of elements of the vectors: '))
                for i in range(n):
                    elem = float(input(f'Enter the element {i + 1} of vector 1: '))
                    vec_1.append(elem)
                for i in range(n):
                    elem = float(input(f'Enter the element {i + 1} of vector 2: '))
                    vec_2.append(elem)
                print(excersice_4(vec_1, vec_2))
            case 5:
                vec_1 = []
                vec_2 = []
                n = int(input('Enter the number of elements of the vectors: '))
                for i in range(n):
                    elem = float(input(f'Enter the element {i + 1} of vector 1: '))
                    vec_1.append(elem)
                for i in range(n):
                    elem = float(input(f'Enter the element {i + 1} of vector 2: '))
                    vec_2.append(elem)
                print(excersice_5(vec_1, vec_2))
            case 6:
                v0 = float(input('Enter initial velocity (m/s): '))
                angle = float(input('Enter angle (degrees): '))
                print(excersice_6(v0, angle))
            case _:
                print('Invalid option')
    else:
        option = int(input('Select an option:\n1. Free fall\n2. Speed conversion\n3. Movement MUR\n4. Vector sum\n5. Scalar product between two vectors and angle\n6. Projectile launch\n'))
        match option:
            case 1:
                excersice_1(9.8, 20, 50, 100, 250)
            case 2:
                excersice_2((100, 'km/h'), (27, 'm/s'), (50, 'km/h'), (13, 'm/s'), (60, 'mph'))
            case 3:
                excersice_3((10, 2, 5), (15, 3, 3), (20, 4, 2), (25, 5, 1), (30, 6, 0.5))
            case 4:
                print(excersice_4([1, 2, 3], [4, 5, 6]))
            case 5:
                print(excersice_5([1, 2, 3], [4, 5, 6]))
            case 6:
                print(excersice_6(200, 60))
            case _:
                print('Invalid option')
    
    return int(input("Do you want to continue? (1: Yes, 0: No): "))

if __name__ == '__main__':
    continue_option = 1
    while continue_option == 1:
        continue_option = menu()
