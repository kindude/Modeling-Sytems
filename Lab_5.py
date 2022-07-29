import math
import random

class Request:
    __timeService = 0
    __timeCome = 0
    def __init__(self, timeCome, timeService):
        self.__timeCome = timeCome
        self.__timeService = timeService

    def __set_timeCome(self, timeCome):
        self.__timeCome = timeCome
    
    def __get_timeCome(self):
        return self.__timeCome

    timeCome = property(__get_timeCome,__set_timeCome)

    def __set_timeService(self, timeService):
        self.__timeService = timeService
    
    def __get_timeService(self):
        return self.__timeService

    timeService = property(__get_timeService,__set_timeService)

def timeService(my, sko, n): #Определение времени обсулживания по нормально закону распределения
    y = 0
    a = my/n - (math.sqrt(3)*sko/n)
    b = my/n + (math.sqrt(3)*sko/n)
    for i in range(n):
        eps =  random.random()
        x = a + (b-a)*eps
        y = y + x
    return y

def timeRequest(a, b):  #Опредедение времени поступления заявки по равномерному закону 
    y = (b - a) * random.random() + a
    return y

def main():
    tNow = 0 #текущее время
    n = 100 
    FreeChannels = []# Массив свободных каналов 
    Queue = []
    timeFreeChannel = [0, 0, 0, 0, 0, 0] #массив для времени освобождения канала
    timeWaitForAverage = 0
    timeProst = [0, 0, 0, 0, 0, 0]
    print("Заявка № \tВремя прихода \tНомер канала\t Время освобождения канала\t В очереди \tКоличество элементов очереди")
    for i in range(n):
        timeReq = timeRequest(5, 1.5) 
        tNow = tNow + timeReq #Время прихода заявок
        print(i+1,round(tNow,3), sep ="\t\t",end ="\t\t")
        timeSer = timeService(30, 8, n) # Время обслуживания
        req = Request(tNow,timeSer)
       # print(str(round(timeFreeChannel[0],3))+ '\t' + str(round(timeFreeChannel[1],3)) + '\t'   + str(round(timeFreeChannel[2],3)) + '\t'+ str(round(timeFreeChannel[3],3)) + '\t'+ str(round(timeFreeChannel[4],3)) + '\t' + str(round(timeFreeChannel[5],3)) + '\t' +str(round(tNow,3)),end = '\n')
        FreeChannels.clear()
        mint = timeFreeChannel[0]
       
        for j in range(6):
            if tNow > timeFreeChannel[j]:# Проверка есть ли свободные каналы 
                FreeChannels.append(j)
            if timeFreeChannel[j] <= mint:# Выбираем канал с минимальным временем освобождения
                mint = timeFreeChannel[j]
                noChannel = j
        if len(FreeChannels) == 0: # Если свободных каналов нет 
            Queue.append(req)# Добавляем заявку в очередь
            print("nan","nan",  "В очереди",len(Queue),sep="\t\t\t",end ="\n")
        elif len(FreeChannels) > 0: # Если есть свободные каналы, то анализируем очередь
            if(len(Queue)==0): #Если  в очереди ничего нет, то назначаем обслуживание заявки каналу  с минимальным временем освбождения 
                timeFreeChannel[noChannel] = mint +  req.timeService #Время освобождения  + время обслуживания заявки
                timeWaitForAverage = timeWaitForAverage + (tNow - req.timeCome)
                print(noChannel+1, round(timeFreeChannel[noChannel],3), "Не в очереди", len(Queue),sep ="\t\t\t",end="\n")
            elif(len(Queue) > 0):#Если количество заявок в очереди больше 0 
                print(noChannel+1, round(timeFreeChannel[noChannel],3),"В очереди", len(Queue), sep ="\t\t\t",end="\n")
                number = random.randrange(0, len(Queue)) #в случайном порядке выбирается заявка из очереди
                timeFreeChannel[noChannel] = mint + Queue[number].timeService
                timeWaitForAverage = timeWaitForAverage + (tNow - Queue[number].timeCome)  #Время ожидания
                Queue.pop(number)
            for k in range(6):
                timeProst[k] = round(timeProst[k] + (timeFreeChannel[k] - tNow)/100,3) #Среднее время простоя каналов
    print("Среднее время простоя для каждого канала:",*timeProst)
    print("Среднее время ожидания:",timeWaitForAverage/100)


if __name__ =="__main__":
    main()