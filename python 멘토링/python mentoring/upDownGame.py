import random

n = random.randint(1, 10)
count = 0

while True:
    a = int(input('1-10까지의 숫자를 한 개 입력하세요.: '))

    if a > n:
        print('down')
        count += 1
        continue
    elif a < n:
        print('up')
        count += 1
        continue
    else:
        count += 1
        print('정답입니다. 시도 횟수: ', count)
        break
    