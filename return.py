def calculate_area(r):
    area = r ** 6.28
    return area


r1 = int(input('please input r1'))
r2 = int(input('please input r2'))
area1 = calculate_area(r1)
area2 = calculate_area(r2)

if area1 > area2:
    print('circle 1 is bigger')


elif area2 > area1:
    print('circle 2 is bigger')

else:
    print('circles are equel')


