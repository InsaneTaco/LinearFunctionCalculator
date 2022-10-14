#y = mx + b
#asks for command
while True:
    print('''Run a command. Type h and enter for help.''')
    command = input().lower()
    
    #displays all commands for help
    if command == 'h':
        print('''
    Available commands:
    1 - type in one point and slope, and it will display all information.
    2 - type in two points, and it will display all information.
    ''')


    #calculator that uses one point and slope
    elif command == '1':
        x_value = input('x value: ')
        y_value = input('y value: ')
        slope = input('slope: ')

        #calculates y-intercept
        #b = y - mx
        y_intercept = float(y_value) - (float(slope) * float(x_value))
        #calculates x-intercept
        #x-intercept = x - (my)
        x_intercept = float(x_value) - (float(slope) * float(y_value))
        
        #prints the equation
        #changes the plus or minus sign depending if slope is positive or negative
        if y_intercept < 0:
            print(f'''
    y = {slope}x {y_intercept}''')
        else:
            print(f'''
    y = {slope}x + {y_intercept}''')

        #prints the y-intercept, x-intercept, and slope
        print(f'''    y-intercept: 0, {y_intercept}
    x-intercept: {x_intercept}, 0
    Slope: {slope}
    ''')


    #y intercept calculator - uses two points, finds slope, then uses to find y-intercept
    elif command == '2':
        x_value1 = input('x-value1: ')
        y_value1 = input('y-value1: ')
        x_value2 = input('x-value2: ')
        y_value2 = input('y-value2: ')

        #calculates slope
        rise = float(y_value2) - float(y_value1)
        run = float(x_value2) - float(x_value1)
        slope = rise / run
    
        #calculates y-intercept
        #b = y - mx
        y_intercept = float(y_value1) - (float(slope) * float(x_value1))
        #calculates x-intercept
        #x-intercept = x - (my)
        x_intercept = float(x_value1) - (float(slope) * float(y_value1))
        
        #prints the equation
        #changes the plus or minus sign depending if slope is positive or negative
        if y_intercept < 0:
            print(f'''
    y = {slope}x {y_intercept}''')
        else:
            print(f'''
    y = {slope}x + {y_intercept}''')

        #prints the y-intercept, x-intercept, and slope
        print(f'''    y-intercept: 0, {y_intercept}
    x-intercept: {x_intercept}, 0
    Slope: {slope}
    ''')
    

    #program quitter
    elif command == 'quit' or command == 'q':
        print('bye bye')
        break

    #if beginning command is not one of the options
    else:
        print("That's not a command. Try typing h and hit enter for help.")
