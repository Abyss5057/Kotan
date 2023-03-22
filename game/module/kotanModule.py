import random

numExam = 10
minQue = 0
maxQue = 10

examQueList = []

def shuffleListPlus(moto : list, jogai : list):
    kansei = []

def prepareExam():
    pass


def makeExam():
    for i in range(numExam):
        temp = random.randint(minQue,maxQue)
        if(temp in examQueList):
            pass
        else:
            examQueList.append(temp)
    
    print(examQueList)

makeExam()