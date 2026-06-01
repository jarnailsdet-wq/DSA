# task 1 - http://uitestingplayground.com/textinput
# input some value then click the button and check if the button got the exact text or not (major focus asserts)
# task 2 - http://uitestingplayground.com/disabledinput
# input some value then click the button and wait for the input to be enable (major focus waits)
# task 3 - http://uitestingplayground.com/verifytext
# check the text present in different type of tags (playwright can directly having visible text any where from the screen) - (major focus experiment with text & playwright)


# task 3 - DSA Logic questions ( Arrays)



# Count Occurrences: Count how many times a specific element X appears in the array.

list = [4,11,77,11,11]
nlist = []
clist =[0]
count=0
for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        print(f"i={i} , j={j} , list i = {list[i]} , list j = {list[j]} , clist = {clist} , count = {count}")
        if list[i] in nlist:
            # print("skipped")
            count+=1
            continue
        
        if list[i] == list[j]:
            count+=1
            
            nlist.append(list[i])
            
            
            
             
print(nlist)
print(count)
print(clist)        
        
    

