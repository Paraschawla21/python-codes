for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))[:n]
    flag = 0
    flag2 = 0
# #     for i in range(0, n-1):
# #         for j  in range(i+1, n):
# #             if (arr[i] + arr[j] >= arr[i] * arr[j]):
# #                 flag += 1
# #     print(flag)
    for i in range(n):
        if arr[i] == 1:
            flag += 1
        for j in range(i+1, n):
            if arr[i] == 2:
                if arr[j] == 2:
                    flag2 += 1
        count = flag + flag2
    print(count)