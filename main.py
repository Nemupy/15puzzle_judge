def emp_dist(s):
    dist = [6, 5, 4, 3, 5, 4, 3, 2, 4, 3, 2, 1, 3, 2, 1, 0]
    emp = s.index(16)
    return (dist[emp])


def swap_count(s):
    swap_count = 0
    t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    while s != t:
        for i in range(len(s)):
            if s[i] != t[i]:
                idx = s.index(t[i])
                s[i], s[idx] = s[idx], s[i]
                swap_count += 1
                break
    return (swap_count)


s = [1, 7, 2, 12, 13, 14, 4, 3, 8, 9, 10, 16, 11, 5, 15, 6]


if (emp_dist(s) + swap_count(s)) % 2 == 0:
    print("可能")
else:
    print("不可能")
