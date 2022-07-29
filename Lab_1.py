
from os import sep


a = []
v1 = 3.14159
v2 = 0.542101
step = 0
p = open("D:\АСУ-19\Modeling Systems\output.txt", "w+")

dt = list([0] * 10 )
intervals = []

step_intervals = 1/10
for i in range(10):
    intervals.append(step_intervals)
    step_intervals += 1/10

for n in range(100):

    t = v1 + v2
    if t >= 4:
        t = t - 4

    v1 = v2
    v2 = t
    eps = t / 4
    a.append(eps)
    p.write(str(eps) + "\n")

    for i in range(len(dt)):
        if intervals[i] > eps:
            dt[i] += 1
            break

for i in range(len(dt)):
    p.write(str(dt[i]) + "\n")

print(*a, sep='\n')
print(*dt)
p.close()
