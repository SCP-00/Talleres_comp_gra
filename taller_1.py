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
        return result
    
## example
#print(excersice_4([1, 2, 3], [4, 5, 6]))
print(excersice_4([1, 2, 3], [4, 5, 6, 7]))
#print(excersice_4([3, 4], [ 6, 7]))
        
    