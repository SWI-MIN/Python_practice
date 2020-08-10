wh1 = 1
while(wh1 < 10):
    wh2 = 1
    while(wh2 < 10):
        whans = wh1 * wh2
        print('%2dx%2d = %-2d   '%(wh1, wh2, whans), end='')
        wh2+=1
    print()  
    wh1+=1