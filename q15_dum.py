
<<<<<<< HEAD
steps = 4


def step(a, b):
    if a > b:
        return 0
    if a == b:
        return 1

    cnt = 0
    for a_step in range(1, steps + 1):
        for b_step in range(1, steps + 1):
            cnt += step(a + a_step, b - b_step)

    return cnt


print(step(0, 10))
=======
stairs = 10
max_step = 4

def move(a_pos, b_pos):
    if a_pos > b_pos:
        return 0
    if a_pos == b_pos:
        return 1
    cnt = 0
    for step_a in range(1, max_step + 1):
        for step_b in range(1, max_step+1):
            cnt += move(a_pos + step_a, b_pos - step_b)

    return cnt
    
def main():
    print(move(0, stairs))
            
if __name__ == "__main__":
    main()
>>>>>>> 3fafef41a7bb97fcf741b9aaa5665b610a9a90b4
