

cal = ["*",""]

for idx in range(1000,5932):
    v = str(idx)
    for cal1 in range(len(cal)):
        for cal2 in range(len(cal)):
            for cal3 in range(len(cal)):
                data = v[0] + cal[cal1] + v[1] + cal[cal2] + v[2] + cal[cal3] + v[3]
                if len(data) >4:
                    while True:
                        bef  = len(data)
                        data = data.replace('*0', '*')
                        if '**' in data or data[-1:]=='*':
                            data = "0"
                            break
                        elif bef == len(data):
                            break
                    result = eval(data)
                    if str(result) == v[::-1]:
                        print(v)
                        exit(1)
                    