prices = list(map(int,input().split(';')))
prices.sort(reverse=True)
for i in prices:
    print('{:>9,}'.format(i))


