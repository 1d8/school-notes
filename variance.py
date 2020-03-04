mean = 6.2
nums = [9,7,4,2,8,7,6,7,8,3,4,7,8,7,5,6,7,3,7,9]
#this calculates the deviation, not the variance
#from here, you add up all the deviations & divide by (N-1) (where N = total number of  scores) to find the variance.
for i in nums:
    i = int(i)
    deviation = mean - i
    deviation = deviation**2
    print(deviation)
