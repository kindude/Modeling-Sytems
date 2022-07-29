import random
import math

def InputNumbers():
    n = int(input("Put number of details:"))
    return n

def Count(n):

    dt = list([0] * 11 )
    intervals = []

    step_intervals = 1/10
    for i in range(11):
        intervals.append(step_intervals)
        step_intervals += 1/10
    
    defectiveGoods = 0
    Me = 0.5
    
    Part_dimensions = []
    Random_deviation = [] 

    for i in range(n):
        x = round(float(random.random()), 3)
        Part_dimensions.append(x)

        t = round(abs((-Me * math.log(x))), 3)

        Random_deviation.append(t)

        if(t >= Me):
            defectiveGoods += 1
        for j in range(len(dt)):
            if intervals[j] > t:
                dt[j] += 1
                break
        
        
    print(*Part_dimensions)
    print(*Random_deviation)
    print(dt, sep="\n")
    Percent = (defectiveGoods / n) * 100
    print("Percent of defective goods:" + str(Percent) + " %")
 
def main():
    n = InputNumbers()
    Count(n)

if __name__== "__main__":

    main()
