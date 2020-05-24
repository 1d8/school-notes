#include <stdio.h>


/* NOTE: THIS IS INACCURATE WHEN FINDING COVARIANCE, IT'S SUGGESTED TO USE THE
 * PYTHON SCRIPT INSTEAD */

int main()
{
	int x[] = {20, 22, 4.4};
	int y[] = {78, 73, 71};
	int x_deviation[3];
	int y_deviation[3];
	float x_mean = 15.5;
	float y_mean = 74;
	float deviationX = 0.0;
	float deviationY = 0.0;
	int sum;
	int multiplied_nums[3];
	int n;
	/* Calculating covariance for X */
	for ( int a=0; a < sizeof(x)/sizeof(x[0]); a++ ) 
	{
		deviationX = x[a] - x_mean;
		x_deviation[a] = deviationX;
		printf("X deviation: %d\n", x_deviation[a]);
	}
	/* Calculating covariance for Y */
	for ( int a=0; a < sizeof(y)/sizeof(y[0]); a++ )
	{
		deviationY = y[a] - y_mean;
		y_deviation[a] = deviationY;
		printf("Y deviation: %d\n", y_deviation[a]);
	}

	for ( int loop=0; loop < 3; loop++ )
	{
		multiplied_nums[loop] = x_deviation[loop] * y_deviation[loop];
	}
	sum = 0;
	for ( int loop=0; loop < sizeof(multiplied_nums)/sizeof(multiplied_nums[0]); loop++) 
	{
		sum = sum + multiplied_nums[loop];
	}
	printf("The sum of multiplying the values & adding together the sum : %d\n", sum);
	n = sizeof(multiplied_nums)/sizeof(multiplied_nums[0]);
	n = n - 1;
	printf("The covariance for X & Y is: %d\n", sum/n);
		
		

}
