def GetArea_01(width, height):
    area = width * height  # area 為區域變數
    global aarea           # aarea 為全域變數
    aarea = 1
    return area
getarea_01 = GetArea_01(7,16)  # getarea_01 為全域變數
print(getarea_01,",", aarea)  #112