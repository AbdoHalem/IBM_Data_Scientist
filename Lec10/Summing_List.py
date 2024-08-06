x = [1,10,"5","hi",8,"7"]
sum = 0

for i in x:
    if(type(i) == int):
       sum += i
    elif(i.isdigit()):
       sum += int(i)
    else:
       continue
print("Sum of integers =", sum)
