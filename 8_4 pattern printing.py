#patern printing


for i in range(1,7):
    for i in range (i):
        print("*",end=" ")
    print()    
    
for p in range(1,7):
    for u in range (p):
        if u>0 and u<p-1 and p<6:
                print("-",end=" ")
        else:
            print("*",end=" ")        
                
    print("")   
    
    
# for i in range(1,5):
#      for j in range(1,5):
#          if j>1 and j<4 and i>1 and i<4:
#             print(" ",end=" ")     
#          else :   
            
#             print("*",end=" ")    
#      print("")       
         