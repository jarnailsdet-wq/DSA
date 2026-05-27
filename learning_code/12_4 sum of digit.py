#sum of digit of a number
# num=int(input("Enter the number : "))
# total=0
# for i in str(num):
#     total=int(i)+total
# print(total)

it=687
digi=0
total=0
while it>0:
    digi=it%10
    it=int(it/10)
    print(f"digi={digi},it = {it}")
    total=total+digi
print(int(total))    
    
    