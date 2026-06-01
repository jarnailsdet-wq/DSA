#largest
# Find the Largest/Smallest Element: Iterate once to find the maximum or minimum value.
# Find the Second Largest Element: A common twist that requires keeping track of two values during a single pass.
# Check if Array is Sorted: Loop through the array to see if every element is less than or equal to the next one.

list = [4,8,11,77,9]
max=0
min=100
smax=0
for i in range(0,len(list)):
    if list[i]>max:
        max=list[i]
    if list[i]<min:
        min=list[i]      
print(max)
print(min)   

for i in range (0,len(list)):
    if list[i]>smax and list[i]<max:
        smax=list[i]
print(smax)        

for i in range (0,len(list)-1):  
    if not list[i]<=list[i+1]:
        print("Not sorted")
        break
        
  

     
             
    