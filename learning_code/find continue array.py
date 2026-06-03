# Given a binary array arr[] consisting of only 0s and 1s, find the length of the longest contiguous sequence of either 1s or 0s in the array.

# Examples : 

#     Input: arr[] = [0, 1, 0, 1, 1, 1, 1]
#     Output: 4
#     Explanation: The maximum number of consecutive 1’s in the array is 4 from index 3-6.


list =  [1,1,4,4,4,4,8,8,8,9,9,9,9,6,9,9,9,9,9]
count=1
max_count=0
state=0
state2=0

for i in range(0,len(list)-1):
    
    
    print(f"i={i} ,  list i = {list[i]},listi+1 = {list[i+1]}, count = {count} , max_count = {max_count} , state = {state} , state2 = {state2}")
    if list[i]==list[i+1]:
        count+=1
         
        
    if list[i]!=list[i+1] or i+1==len(list)-1:
        
        if count>max_count:
            max_count=count
           
            state=list[i]
        count=1
          
print(max_count)        
print(count)  
print(state)     
       
 