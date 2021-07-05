# 1. Biggie Size - Given a list, write a function that changes 
# all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, 
# but whose values are now [-1, "big", "big", -5]

# def biggieSize(numberList):
#     for x in range(len(numberList)):
#         if(numberList[x]>0):
#             numberList[x]="big"
#     return numberList
# print(biggieSize([-1,3,5,-5]))

# 2. Count Positives - Given a list of numbers, create a function
# to replace the last value with the number of positive values. 
# (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

# def countPositives(numberList):
#     positiveCount = 0
#     for x in range(len(numberList)):
#         if(numberList[x]>0):
#             positiveCount+=1
#     numberList[len(numberList)-1]=positiveCount
#     return numberList;
# print(countPositives([-1,1,1,1]))
# print(countPositives([1,6,-4,-2,-7,-2]))

# 3. Sum Total - Create a function that takes a list and returns the sum of all 
# the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

# def sumTotal(numberList):
#     sum=0
#     for i in range(len(numberList)):
#         sum+=numberList[i]
#     return sum
# print(sumTotal([1,2,3,4]))
# print(sumTotal([6,3,-2]))

# 4. Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5

# def average(numberList):
#     sum = 0
#     for x in range(len(numberList)):
#         sum+=numberList[x]
#     return sum/len(numberList)

# print(average([1,2,3,4]))
# print(average([9,6,3,0]))

# 5. Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

# def length(numberList):
#     return len(numberList)

# print(length([37,2,1,-9]))
# print(length([]))

# 6. Minimum - Create a function that takes a list of numbers and returns the minimum 
# value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

# def minimum(numberList):
#     if(len(numberList)!=0):
#         minNumber = numberList[0]
#         for i in range(len(numberList)):
#             if(minNumber>numberList[i]):
#                 minNumber=numberList[i]
#         return minNumber
#     else:
#         return False
# print(minimum([37,2,1,-9]))
# print(minimum([]))
# print(minimum([-10,-8,-25,-1]))

# 7. Maximum - Create a function that takes a list and returns the maximum value
# in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

# def maximumValue(numberList):
#     if(len(numberList)!=0):
#         max = numberList[0]
#         for i in range(len(numberList)):
#             if(max<numberList[i]):
#                 max=numberList[i]
#         return max
#     else:
#         return False

# print(maximumValue([37,2,1,-9]))
# print(maximumValue([]))
# print(maximumValue([-10,-8,-25,-1]))

# 8. Ultimate Analysis - Create a function that takes a list and returns a 
# dictionary that has the sumTotal, average, minimum, maximum and length of the list.
#Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 
# 'minimum': -9, 'maximum': 37, 'length': 4 }

# def ultimateAnalysis(numberList):
#     if(len(numberList)!=0):
#         sum = 0
#         avg = 0
#         min = numberList[0]
#         max = numberList[0]
#         for i in range(len(numberList)):
#             sum+=numberList[i]
#             if(min>numberList[i]):
#                 min=numberList[i]
#             if(max<numberList[i]):
#                 max=numberList[i]
#         avg=sum/len(numberList)
#         ultimateDict = {
#             "sumTotal": sum,
#             "average": avg,
#             "minimum": min,
#             "maximum": max,
#             "length of list": len(numberList)
#         }
#     else:
#         return False
#     return ultimateDict
    
# print(ultimateAnalysis([37,2,1,-9]))
# print(ultimateAnalysis([7,-29,90,1,5,8,9,100]))
# print(ultimateAnalysis([]))


# 9. Reverse List - Create a function that takes a list and return that list 
# with values reversed. Do this without creating a second list. 
# (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37] 

# This one made me super happy.  Pulled it from my head only 
# help I needed was converting the float to an int!

# def reverseList(numberList):
#     if(len(numberList)!=0):
#         numHold = numberList[0]
#         for i in range(int(len(numberList)/2)):
#             numHold = numberList[i]
#             numberList[i] = numberList[len(numberList)-1-i]
#             numberList[len(numberList)-1-i] = numHold
#         return numberList
#     else:
#         return False
# print(reverseList([37,2,1,-9]))
# print(reverseList([]))
# print(reverseList([1,2,3,4,5,6,7,8,9,23,45,64,1]))
            