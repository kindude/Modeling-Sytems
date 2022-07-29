import random
import math


def timeRequest(my, sko, n): #Определение времени поступления заявки по нормальному закону распределения
    y = 0
    a = my/n - (math.sqrt(3)*sko/n)
    b = my/n + (math.sqrt(3)*sko/n)
    for i in range(n):
        eps =  random.random()
        x = a + (b-a)*eps
        y = y + x
    return y

def timeService(my): #Определение времени обслуживания заявки по экспоненциальному закону распределения закону распределения
    x = round(abs(float(random.random())), 3)
    exp = round(abs((-my * math.log(x))), 3)
    return exp

def timeWait(my): #Определение времени ожидания заявки по экспоненциальному закону распределения закону распределения
    x = round(abs(float(random.random())), 3)
    exp = round(abs((-my * math.log(x))), 3)
    return exp

def main():
    tNow = 0 #текущее время
    my = 10 # мат ожидание
    sko = 1 # средне квадратичное отклонение 
    n = 100 #Количество испытаний для приближений к нормальному закону
    #noChannel = 0 # номер канал
    timeFreeChannel = [0, 0] #массив для времени освобождения канала
    refuse = 0 # Отказ 
    FreeChannels = []# Массив свободных каналов 
    timeWaitForAverage = 0
    timeProstForAverage1 = 0
    timeProstForAverage2 = 0
    print("tосв1\ttосв2\ttпост\tканал\ttобсл\ttожд")
    for i in range(n):
        timeReq = timeRequest(5, sko, n) 
        tNow = tNow + timeReq #Время прихода заявок
        timeSer = timeService(my) # Время обслуживания
        timeW = timeWait(my) # Время Ожидания
        FreeChannels.clear()
        mint = timeFreeChannel[0]
        print(str(round(timeFreeChannel[0],3)) + '\t' + str(round(timeFreeChannel[1],3)) + '\t' + str(round(tNow,3)),end = '\t')
        for j in range(2): 
            if timeFreeChannel[j] <= mint:# Выбираем канал с минимальным временем освобождения
                mint = timeFreeChannel[j]
                noChannel = j
            if tNow > timeFreeChannel[j]:# Проверка есть ли свободные каналы 
                FreeChannels.append(j)        
        if  len(FreeChannels) !=0: #Если есть свободные каналы
            timeFreeChannel[noChannel] = tNow + timeSer 
            
        elif len(FreeChannels) == 0: 
            timeWaitForAverage = timeWaitForAverage + timeW
            if(mint > timeW + tNow): #Если время освобождения канала больше чем время ожидания то происходит отказ
                refuse = refuse + 1 #Увеличиваем количество отказов 
            else:
                timeFreeChannel[noChannel] =  mint+timeSer #если каналы заняты то выбираем канал с минимальным временем и назначаем заявку              
        print(noChannel+1, end='\t')
        print(timeSer, timeW, sep='\t')
        timeProstForAverage1 = timeProstForAverage1 + (tNow - timeFreeChannel[0])
        timeProstForAverage2 = timeProstForAverage2 + (tNow - timeFreeChannel[1])
    print("Вероятность отказа =", refuse / n * 100,"%")
    print("Среднее значение времени ожидания =", round(timeWaitForAverage / n, 3))
    print("Среднее значение времени простоя канала № 1 =", round(timeProstForAverage1 / n, 3))
    print("Среднее значение времени простоя канала № 2 =", round(timeProstForAverage2 / n, 3))
   
if __name__ == '__main__':
    main()
