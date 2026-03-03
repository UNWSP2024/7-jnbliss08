# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year,
# the average monthly rainfall, # and the months with the highest and lowest amounts.

import statistics

months = ('Jan','Feb','Mar','Apr','May','June','July','Aug','Sep','Oct','Nov','Dec')

RAINFALL = []

for month in months:
    RAINFALL.append(float(input(f'Enter inches of rainfall for {month}: ')))

total_rainfall = sum(RAINFALL)
average_rainfall = statistics.mean(RAINFALL)
max_rainfall = max(RAINFALL)
min_rainfall = min(RAINFALL)
max_month = RAINFALL.index(max_rainfall)
min_month = RAINFALL.index(min_rainfall)

print (f'Total rainfall is: {total_rainfall} inches')
print (f'Average rainfall is: {average_rainfall} inches')
print(f'Maximum rainfall is: {max_rainfall} inches in {months[max_month]}')
print(f'Minimum rainfall is: {min_rainfall} inches in {months[min_month]}')