import pandas as pd
import numpy as np
import roman


def task1():
    data = pd.read_csv('Birthweight.csv')
    subData = np.array(data['Gestation'])
    subMassive = pd.Series(subData, index=[roman.toRoman(i + 1) for i in range(len(subData))])
    print(subMassive)

    print('\nЗвернення за прямим індексом:\n{}'. format(subMassive.loc['XXXIV':'XL']))
    print('\nЗвернення за прямим індексом:\n{}'.format(subMassive[33:40]))

def task2():
    data = pd.read_csv('Birthweight.csv')
    data['ratio'] = round(data['Length']/data['Birthweight'], 2)
    print(data)
task1()
task2()
