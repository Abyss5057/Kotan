import random

numOpt = 4

numExam = 10
minQue = 1
maxQue = 10

examQueList = []
examOptList = [[]]

def randomListGenerate(min, max, length, jogai = []):
    if(max - min - len(jogai) + 1 < length):
        return -1

    output = []

    for i in range(length):
        kariNum = random.randint(min, max)

        while(kariNum in output  or  kariNum in jogai):
            kariNum = random.randint(min, max)
        
        output.append(kariNum)
    
    return output


def prepareExam(min : int, max : int, num : int):
    minQue = min
    maxQue = max
    numExam = num


def makeExam():
    examQueList = randomListGenerate(minQue, maxQue, numExam)
    
    for i in range(numExam):
        examOptList[i].append(randomListGenerate(minQue, maxQue, numOpt - 1, [examQueList[i]]))
        random.shuffle(examOptList[i])

makeExam()
print(examQueList)
print(examOptList)