
# Reverse the Array: Flip the array so the first element becomes the last, the second becomes the second-to-last, etc.

# list = [1,2,3,4]
# rev=[0]
# temp = 0
# pt1 = 0
# pt2=len(list)-1
# for pt1 in range(0,len(list)):
#     if pt2>pt1:
#         print(f"i={pt1} , j={pt2} , list i = {list[pt1]} , list j = {list[pt2]} ")
#         temp=list[pt1]
#         list[pt1]=list[pt2]
#         list[pt2]=temp
        
        
        
#         print(list[pt1])
#         print(list[pt2])  
#         pt2=pt2-1  
#         print(list)
# print(f"final list:{list}")        
            
            
            

list = [1,2,3,4]
rev=[0]
temp = 0
pt1 = 0
pt2=len(list)-1
while(pt2>pt1):
     
        print(f"i={pt1} , j={pt2} , list i = {list[pt1]} , list j = {list[pt2]} ")
        temp=list[pt1]
        list[pt1]=list[pt2]
        list[pt2]=temp
        
        
        
        print(list[pt1])
        print(list[pt2])  
        pt2=pt2-1  
        print(list)
        pt1=pt1+1
print(f"final list:{list}")        
            
        
