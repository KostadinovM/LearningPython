import statistics                       #as s - if uncomment 'as s', the library 
                                        #can be referenced using 's'. Ex: s.mean(example_list)
#from statistics import variance        #if we do this, its not necesery to even write s or statistics
                                        #Ex: variance(example_list)
#from statistics import variance as     #Ex: v(example_list)
#from statistics import mean as m, variance as v  #For multiple imports
#from statistics import *               #Import all of them.


example_list = [1,5,2,3,6,9,12,53,123,54,34,21]

x = statistics.mean(example_list)       #mean of a list of numbers
y = statistics.median(example_list)     #median of a list of numbers
z = statistics.stdev(example_list)      #standard deviation of  list of numbers
q = statistics.variance(example_list)   #standard deviation of  list of numbers


print(x)
print(y)
print(z)
print(q)
