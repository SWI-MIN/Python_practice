import math
def GetArea(width, height):
    area = width * height
    return area
square_area = GetArea(7,16)
print(square_area)  #112

# square_area_01 = GetArea(7,16)
# square_area_02 = GetArea(width = 7,height = 16)
# square_area_03 = GetArea(height = 16,width = 7)
# square_area_01 = square_area_02 = square_area_03  # 三者相等


def Circle(ardius):
    area = ardius * ardius * math.pi
    length = ardius * 2 * math.pi
    return area, length
circle_area, circumference = Circle(5) # circumference(圓周長)
print(circle_area, circumference) # 78.53981633974483 31.41592653589793
print(int(circle_area), int(circumference)) # 78, 31



# 全域變數 & 區域變數
def GetArea_01(width, height):
    area = width * height  # area 為區域變數
    global aarea           # aarea 為全域變數
    aarea = 1
    return area
getarea_01 = GetArea_01(7,16)  # getarea_01 為全域變數
print(getarea_01,",", aarea)  # 112 , 1

