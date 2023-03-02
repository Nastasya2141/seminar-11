import matplotlib.pyplot as plt
import random
import numpy as np 

def zadacha1():
    x_list = []
    y_list = []

    for x in range (-10, 11):
        y = 5 * x * x + 10 * x - 30
        x_list.append(x)
        y_list.append(y)


    plt.axhline(y = 0, color = "r", linestyle = "--")
    plt.plot(y_list)
    plt.show()

def zadacha2():
    price_house=np.random.randint(3000000,20000000,15)
    square_house=np.random.randint(100,300,15)
    meter_price=[round(price_house[i]/square_house[i]) for i in range(len(price_house))]
    optimal_price=50000
    recommend_houses= []

    for i in range(len(meter_price)):
        if meter_price[i]<=optimal_price:
            recommend_houses.append(meter_price[i])   
    print(recommend_houses)

    numbers=[]
    for i in range (len(recommend_houses)):
        numbers.append(i+1)
    print(numbers,recommend_houses)

    numbers=[
    'House1',
    'House2',
    'House3',
    'House4',
    'House5',
    'House6',
    'House7',
    'House8',
    'House9',
    'House10',
    'House11',
    'House12',
    'House13',
    'House14',
    'House15']

    plt.axhline(y=50000,color='r',linestyle='--')
    plt.bar(numbers,meter_price)
    plt.show()

# zadacha1()
# zadacha2()