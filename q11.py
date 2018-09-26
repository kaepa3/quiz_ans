
def fib(count):
    if count == 0 or count == 1:
        return 1
    else:     
        return fib(count -1) + fib(count -2)

count = 0
for v in range(0,10):
    val = fib(v)
    div = 0
    for char in str(val):
        div += int(char)
    if val % div == 0:
        print(val)
        count += 1
        if count > 12:
            break

print("-----------")

a = 1
b = 1    
count = 0
while (count < 12):
    c = a + b
    div = 0
    for char in str(c):
        div += int(char)

    if c % div == 0:
        print(c)
        count += 1
    a = b
    b = c
