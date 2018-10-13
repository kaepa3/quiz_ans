
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
