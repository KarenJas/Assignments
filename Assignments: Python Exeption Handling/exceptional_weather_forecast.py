'''1. Exceptional Weather Forecast'''

#Task 1: Start
while True :
    try :
        temp = int(input('enter the temperature in fahrenheits: '))
    except ValueError:
        print('This is not a number. Please input an integer. ')
        break
    else:
        print(f"temp: {temp}")    
        break

#Task 2: Temperature Conversion
def fahrenheit_celsius():
    temperature = float(input('temperature in fahrenheit: '))
    # TEST TYPE ERROR: temperature = input('temperature in fahrenheit: ')
    try:
        celsius = (temperature - 32) * 5/9
    except ZeroDivisionError:
        print('Cant devide by 0')
    except OverflowError:
        print('Number is too high')
    except TypeError:
        print('Oh no you have a type error :(')
##Task 3: User Experience    
    else:
        print(f'Temperature in Celsius: {celsius: .2f}')
    finally:
        print('Thanks For Using The App :) ')

fahrenheit_celsius()






