import random

Pcargo = [0.1, 0.2, 0.4, 0.3] # Вероятность прихода самосвалов
Pdefect = 0.08 # Вероятность появления дефекта
Defect = 0.05 # Процент дефекта
totalWeight = 0 #общий вес
AppearenceEveryCargo = [0, 0, 0, 0] #появление каждого груза 
A = {"0.1": 10,  #Количество тонн в каждом самосвале
     "0.2": 15,
     "0.4": 20,
     "0.3": 25  
}
arrived = 0 
n = 100
for i in range(n):
    L = 0
    eps = random.random()
   
    for j in range(len(Pcargo)):
        L = L + Pcargo[j]
        if eps < L:
            arrived = Pcargo[j]
            eps2 = random.random() #генерация одиночного случайного события появления брака с вероятностью 0.08
            if eps2 < Pdefect:
                weight =  A[str(arrived)] * (1 - Defect)
            else:
                weight = A[str(arrived)]
               
            totalWeight += weight 
            
            AppearenceEveryCargo[j] += 1
            break
            
        
    print("Приехал самосвал с вероятностью ", arrived," с грузом ", A[str(arrived)])
print()

for i in range(len(AppearenceEveryCargo)):
    AppearenceEveryCargo[i] = round(AppearenceEveryCargo[i]/n * 100, 3)
print("Практическая вероятность прихода каждого самомсвала:")     
print(*AppearenceEveryCargo, sep = " %  ", end = " %\n\n")
print("Исходя из того, что самосвалы приезжают каждые 10 минут, а смена длится 8 часов, то получим что средий вес за смену будет равен: ",end="")
print(round(totalWeight/48, 3), "тонн")

