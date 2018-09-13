european = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36,
            11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9,
            22, 18, 29, 7, 28, 12, 35, 3, 26]
american = [0, 28, 9, 26, 30, 11, 7, 20, 32, 17, 5, 22, 34, 15,
            3, 24, 36, 13, 1, 00, 27, 10, 25, 29, 12, 8, 19, 31,
            18, 6, 21, 33, 16, 4, 23, 35, 14, 2]

def max(sample_count, list):
    max = 0
    for cnt in range(0, len(list)):
        val = 0
        analyze_list = []
        if len(list) < cnt+sample_count:
            buffer_list = list + list
            analyze_list = buffer_list[cnt:cnt+sample_count]
        else:
            analyze_list = list[cnt:cnt+sample_count]

        for v in analyze_list:
            val += v

        if max < val:
            max = val

    return max

cnt = 0
for v in range(2,36+1):
    max_europ = max(v,european)
    max_amearica = max(v,american)
    print(str(max_amearica) + ":" + str(max_europ))
    if max_europ < max_amearica:
        cnt+=1

print(cnt)
