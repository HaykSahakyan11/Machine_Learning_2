#  Finding the Users Active Minutes


def findingUsersActiveMinutes(logs, k):
    mp = {}
    for i, t in logs:
        mp.setdefault(i, set()).add(t)

    print(mp)
    ans = [0] * k
    for v in mp.values():
        if len(v) <= k:
            ans[len(v) - 1] += 1
    return ans


logs = [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]]
logs_2 = [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3], [0, 6]]
k = 5
print(findingUsersActiveMinutes(logs=logs, k=k))
