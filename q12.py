import math

def main():

    for num in range(140,145):
        y = math.sqrt(num)
        list = []
        print(y)
        for v in str(y):
            if v not in list:
                list.append(v)
                
        if len(list) == 11:
            print(num)
            break
        

if __name__ == "__main__":
    main()