def fob(end_num):
    for n in range(1, end_num+1):
        if n % 15 == 0:
            print(n, 'FoozBuzz')
        elif n % 3 == 0:
            print(n, 'Fooz')
        elif n % 5 == 0:
            print(n, 'Buzz')
        else:
            print(n)


