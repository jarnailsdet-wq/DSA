count =0
# for i in range(1,5):
#     for j in range(1,i+1):
        
#         count+=1
      
#         print(count,end=" ")    
#     print("")       


for i in range(1,5):
    for j in range(2,i+1):
        
        print("-",end=" ")  
    for k in range(1,6-i): 
        count+=1  
        print(count,end=" ")     
    print("")       
