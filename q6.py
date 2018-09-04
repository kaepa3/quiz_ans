
def analyze(first, val):
    if val == 1:
        return False
    elif val == first:
        return True
    
    if val%2 != 0:
        return analyze(first, val*3+1)
    else:
        return analyze(first, val/2)
         



result = 0
for  i in range(2,10001,2):
    start = i *3 +1
    if analyze(i,start) is True:
        result = result +1

print(result)
