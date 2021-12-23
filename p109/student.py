import pandas as pd
import statistics
import csv

df=pd.read_csv("StudentsPerformance.csv")
height_list=df["math score"].tolist()

#calculating the mean and standerd dviation
mean=sum(height_list)/len(height_list)
std_deviation=statistics.stdev(height_list)
median=statistics.median(height_list)
mode=statistics.mode(height_list)

print("Mean of this data is "+str(mean))
print("Std deviation of this data is "+str(std_deviation))
print("Mode of this data is "+str(mode))
print("Median of this data is "+str(median))


#finding first standerd deviation start and end values, second standerd deviation start and end values
first_std_deviation_start, first_std_deviation_end=mean-std_deviation,mean+std_deviation
second_std_deviation_start, second_std_deviation_end=mean-(2*std_deviation),mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end=mean-(3*std_deviation),mean+(3*std_deviation)

list_of_data_within_1_std_deviation = [result for result in height_list if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in height_list if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in height_list if result > third_std_deviation_start and result < third_std_deviation_end]

print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(height_list)))
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(height_list)))
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(height_list)))

