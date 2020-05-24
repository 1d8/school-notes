# for vars x & y, fill these w/your data

x = []
y = []
x_deviation = []
y_deviation = []
x_mean = 12.56
y_mean = 2.04

## Variance Section

# finding variance for x
#If you're attempting to find covariance, comment out the deviation = deviation ** 2 part on both the x loop & y loop
for i in x:
	deviation = i - x_mean
	deviation = deviation ** 2
	x_deviation.append(deviation)

#prints the sum for your x variance, then you divide by N-1
z = sum(x_deviation)
print(z)

# finding variance for y
for i in y:
	deviation = i - y_mean
	deviation = deviation ** 2
	y_deviation.append(deviation)

#prints the sum for your y variance, then you divide by N-1
z = sum(y_deviation)
print(z)


## Covariance
multiplied_num = []
#Make sure to comment out the deviation**2 parts of the code above if you're attempting to find the covariance
# Change the range int according to the length of the X & Y values, this will iterate through the multiplication part 
# of the equation 25 times in order to multiply every number, then it adds them to the Z variable
#for i in range(25):
#	number = x_deviation[i] * y_deviation[i]
#	multiplied_num.append(number)

# prints sum for your x & y covariance, then you divide by N-1
#z = sum(multiplied_num)
#print(z)

### by the population size (N) - 1
