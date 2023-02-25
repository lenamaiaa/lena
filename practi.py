class car():
    def __init__(self):
        print('new car')
        name = ''
        color = ''
        model = 1900
        cylinder= 0.0
        price = 0



car_1 = car()
car_1.price = 5000
car_1.model = 2005
car_1.color = 'red'
car_1.cylinder = 4
car_1.name = 'accent'



car_2 = car()
car_2.price = 15000
car_2.model = 2015
car_2.color = 'blue'
car_2.cylinder = 6
car_2.name = 'prius'
print(car_2.cylinder)