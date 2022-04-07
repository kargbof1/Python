//swapping value of two variables 
a = 10
b = 20 

c = a // c ten
a = b //a twenty
b = c  // b ten

a, b = b, a  //short cut version 

//extract the largest and smallest value from a set

numbers = [6, 12, 14, 4, 29,39, 31,22, 11,20,19,18,1,2,3,4,5,8]
largest = max(numbers)
smallest = min(numbers)

//List comprehesion 
evens = [x for x in range(20) if x % 2 == 0]

//subset of data within a List that you wish to perform an action on 
//Map Pass a seperate function to apply to each Function In OUr List instead of for loops
//Filter removing values In a List that do Not meet specified condition 
//Reduce 

def square(n):
   return n**2

def even(n):
  return n % 2 ==0
  
def multiply(x,y):
  return x * y
  
squares = list(map(square,numbers))
evens = list(filter (even, numbers))
products= reduct(multiply, numbers)

//Lambda Functions replaces DEF
square1 = list(map(lambda x : x**2 == 0, numbers))