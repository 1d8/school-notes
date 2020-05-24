# for vars x & y, fill these w/your data

x = [20, 22, 4.4]
y = [78, 73, 71]
x_deviation = []
y_deviation = []
x_mean = 15.5
y_mean = 74

#IF YOU"RE FINDING VARIANCE, UNCOMMENT THE DEVIATION=DEVIATION**2 LINES
# finding deviations for x
#If you're attempting to find covariance, comment out the deviation = deviation ** 2 part on both the x loop & y loop
for i in x:
	deviation = i - x_mean
	#deviation = deviation ** 2
	x_deviation.append(deviation)
print("x deviations:", x_deviation)
# finding deviations for y
for i in y:
	deviation = i - y_mean
	#deviation = deviation ** 2
	y_deviation.append(deviation)
print("y deviations", y_deviation)
#covariation
# Change the range int according to the length of the X & Y values, this will iterate through the multiplication part 
# of the equation 25 times in order to multiply every number, then it adds them to the Z variable
multiplied_num = []
for i in range(3):
	number = x_deviation[i] * y_deviation[i]
	multiplied_num.append(number)
z = sum(multiplied_num)
print("adding up all the values after multiplying them gets:", z)
n = len(x) - 1
covariance = z/n
print("Your covariance is:", covariance)
