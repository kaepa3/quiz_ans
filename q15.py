
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