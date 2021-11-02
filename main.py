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
    return data


def task3(dataFrameObj):
    indexesName = [[*['Test 1' for _ in range(len(dataFrameObj.index) // 2)], *['Test 2' for _ in range(len(dataFrameObj.index) // 2)]],
                   [*[i + 1 for i in range(len(dataFrameObj.index) // 2)], *[roman.toRoman(i + 1) for i in range(len(dataFrameObj.index) // 2)]]]
    indexes = list(zip(*indexesName))
    multiInd = pd.MultiIndex.from_tuples(indexes)
    multiIndexObject = pd.DataFrame(dataFrameObj.values, index=multiInd)
    print(multiIndexObject)


def task4():
    data1 = pd.DataFrame({'motherCity': ['A', 'B', 'C', 'D'], 'childcount': [100000, 24653, 355223, 453234]})
    data2 = pd.DataFrame({'motherCity': ['A', 'C', 'B', 'D'], 'medyears': [10, 12, 17, 12]})
    merged_data = pd.merge(data1, data2)
    data3 = pd.DataFrame({'motherCity': ['D', 'F', 'G', 'H'], 'medyears': [10, 12, 17, 12]})
    data4 = pd.DataFrame({'medyears': [10, 17, 12], 'mapweight': ['30', '15', '44']})
    data5 = pd.DataFrame({'medyears': [10, 17, 17, 10, 12], 'agedifference': [5, 2, 6, 18, 3]})
    data6 = pd.DataFrame({'motherTown': ['A', 'C', 'D', 'B'], 'fweight': [67, 89, 78, 120]})
    data7 = pd.DataFrame({'motherCity': ['A', 'B', 'C', 'D'], 'childcount': [980700, 38863, 246778, 678904]})

    print('\nЗ\'єднання «один-до-одного»\n', pd.merge(data1, data2))
    print('\nЗ\'єднання «багато-до-одного»\n', pd.merge(merged_data, data4))
    print('\nЗ\'єднання «багато-до-багатьох»\n', pd.merge(merged_data, data5))
    print('\nЗ\'єднання при різній назвій стовпців\n',
          pd.merge(data1, data6, left_on='motherCity', right_on='motherTown'))
    print('\nВидалення спільного стовпця\n',
          pd.merge(data1, data6, left_on='motherCity', right_on='motherTown').drop('motherTown', axis=1))
    print('\nInner\n', pd.merge(data1, data3))
    print('\nOuter\n', pd.merge(data1, data3, how='outer'))
    print('\nLeft\n', pd.merge(data1, data3, how='left'))
    print('\nRight\n', pd.merge(data1, data3, how='right'))
    print('\nОднакові стовпці за якими не відбувається злиття, додаються суфікси\n',
          pd.merge(data1, data7, on='motherCity'))
    print('\nДодамо суфікси самостійно\n', pd.merge(data1, data7, on='motherCity', suffixes=['_2001', '_2021']))


task1()
dataFrame = task2()
task3(dataFrame)
task4()
