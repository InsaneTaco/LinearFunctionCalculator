#y = mx + b
while True:
    print('Call a function. Type h for list of commands.')
    command = input('>').lower()
    
    #displays all commands
    if command == 'h':
        print('''Available commands:
    y - calculates y-intercept using one point and slope
    yy - calculates y-intercept using two points
    x - calulates x-intercept using one point and slope
    xx - calculates x-intercept using two points
    m - slope calculator from two points''')
    
    #y-intercept calculator - uses coordinates and slope to find y-intercept
    elif command == 'y':
        x_value = input('x value: ')
        y_value = input('y value: ')
        slope = input('slope: ')
        #b = y - mx
        y_intercept = float(y_value) - (float(slope) * float(x_value))
        print(f'y-intercept: 0, {y_intercept}')

    #y intercept calculator - uses two points, finds slope, then uses to find y-intercept
    elif command == 'yy':
        x_value1 = input('x value1: ')
        y_value1 = input('y value1: ')
        x_value2 = input('x value2: ')
        y_value2 = input('y value2: ')
        #finds slope
        rise = float(y_value2) - float(y_value1)
        run = float(x_value2) - float(x_value1)
        slope = rise / run
        #uses first point and slope to find y intercept
        #b = y - mx
        y_intercept = float(y_value1) - (float(slope) * float(x_value1))
        print(f'y-intercept: 0, {y_intercept}')
        print(f'slope: {slope}')

    #x-intercept calculator - uses coordinates and slope to find x-intercept
    elif command == 'x':
        x_value = input('x_value: ')
        y_value = input('y_value: ')
        slope = input('slope: ')
        #x-intercept = x - (my)
        x_intercept = float(x_value) - (float(slope) * float(y_value))
        print(f'x-intercept: {x_intercept}, 0')

    #x intercept calculator - uses two points, finds slope, then uses to find x-intercept
    elif command == 'xx':
        x_value1 = input('x value1: ')
        y_value1 = input('y value1: ')
        x_value2 = input('x value2: ')
        y_value2 = input('y value2: ')
        #finds slope
        rise = float(y_value2) - float(y_value1)
        run = float(x_value2) - float(x_value1)
        slope = rise / run
        #uses first point and slope to find y intercept
        #x-intercept = x - (my)
        x_intercept = float(x_value1) - (float(slope) * float(y_value1))
        print(f'y-intercept: {x_intercept}, 0')
        print(f'slope: {slope}')

    #slope calculator uses two coordinates to calculate
    elif command == 'm':
        x_value1 = input('first coordinate x-value: ')
        y_value1 = input('first coordinate y-value: ')
        x_value2 = input('second coordinate x-value: ')
        y_value2 = input('second coordinate y-value: ')
        #slope formula: (y2 - y1) / (x2 - x1)
        rise = float(y_value2) - float(y_value1)
        run = float(x_value2) - float(x_value1)
        slope = rise / run
        print(f'Slope: {slope}')
    
    #program quitter
    elif command == 'quit' or command == 'q':
        print('bye bye')
        break

    #if beginning command is not one of the options
    else:
        print("That's not a command. Try typing h for command list.")