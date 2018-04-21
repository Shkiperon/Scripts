#!/usr/bin/python3
import sys
import os
abc = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
summator = 0
count = 0
iteration = 0
needsum = 20
for a in abc:
	for b in abc:
		for c in abc:
			for d in abc:
				for e in abc:
					summator = a+b+c+d+e
					iteration = iteration+1
					if(summator == needsum):
						print(iteration)
						count = count+1
count = count*count
print("Number of lucky tickets where the number of digits is 5 and sum " + str(needsum) + " is " + str(count))
