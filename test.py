while(True):
    try:
        a = int(input('pls intput a number : '))
        b = int(input('pls intput a number : '))
        r = a % b
    except (ValueError,ZeroDivisionError) as err:
        print('find {} error' .format(err))
    else:
        print('r = ',r)
