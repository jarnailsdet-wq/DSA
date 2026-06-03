
# Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
# Output: [1, 2, 4, 3, 5, 0, 0, 0]
# Explanation: There are three 0s that are moved to the end.

# list =  [1, 2, 0, 4, 3, 0, 5, 0]
# zero = []

# for i in range(0,len(list)):
#     if list[i]!=0:
#         zero.append(list[i])
        
# for i in range(0,len(list)):
#     if list[i]==0:
#         zero.append(list[i])      
        
        
# print(zero)        
# print(list)

#approach 2

list =  [1, 2, 0, 4, 3, 0, 5, 0]
 

i = 0
for j in range(0,len(list)):
    print(f"i={i} , j={j} , list i = {list[i]} , list j = {list[j]} , clist = ")
    if list[j] !=0:
        temp = list[j]
        list[j]= list[i]
        list[i]=temp
        i+=1
print(list)        
        
