for i in range(int(input())):
    print((lambda x, y: x + y)(*map(int, input().split())))