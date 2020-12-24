# Python program to find largest  
# creating empty list 
list1 = [] 
  
for i in range(5): 
    num = int(input("Enter 5 numbers: ")) 
    list1.append(num)

list1.sort()
print("Largest element is:", list1[-1])

# list1.sort(reverse = True)
# print("Largest element is:", list1[0])