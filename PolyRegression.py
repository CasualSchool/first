from __future__ import print_function
import numpy
import matplotlib.pyplot as plt

angles = [-40, -20, 0, 20,40,60,80]
average = [61,177.33,296.33,680.33,651,534.67,24.67]

polyInput = numpy.polyfit(angles, average, 2)
equation = numpy.poly1d(polyInput)
print (equation)
x2 = numpy.arange(-40,90)
yfit = numpy.polyval(polyInput,x2)

while True:
    try:
        angleInput = raw_input("Please enter a valid angle or enter q to quit: ")
        print (equation(int(angleInput)))
        plt.plot(angles, average, label='Points')
        plt.plot(x2,yfit,label='Fit')
        plt.show()
    except ValueError:
        if angleInput == 'q':
            break
        print ("Angle is invalid.")
        continue

