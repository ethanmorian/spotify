N = input()
if len(N) < 2:
    N = '0'+N
n = N
cnt = 1

while True:
    if len(n) < 2:
        n = '0'+n
    a = str(eval(f'{n[0]}+{n[1]}'))
    n = f'{n[-1]}{a[-1]}'
    if n == N:
        print(cnt)
        break
    cnt += 1