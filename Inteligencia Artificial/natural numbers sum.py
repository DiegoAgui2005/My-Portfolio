def natnumb(n):
    if n == 0:
        return 0
    else:
        return n + natnumb(n-1)

n = 20
for i in range(10):
    print(natnumb(i))