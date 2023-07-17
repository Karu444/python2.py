def myFunc(e):
    return e[2] * e[3]

cars = [[8,"Carlos", 100, 10000], 
        [1, "Diana", 25, 25000], 
        [6, "Oscar", 80, 50000]]

cars.sort(reverse=True, key=myFunc)
print(cars)