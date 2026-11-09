def money(n):
    money_all = 0
    money_100 = 0
    while n != 0:
        if n >= 100:
            n /= 100
            money_100 += 1
            money_all += 1
            print(n, money_all)
            continue


n = input()
money(int(n))
