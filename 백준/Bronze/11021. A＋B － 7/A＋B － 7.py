for i in range(1, int(input())+1):
    print(f"Case #{i}: {(lambda x, y: x + y)(*map(int, input().split()))}")