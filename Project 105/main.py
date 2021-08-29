import csv 
import math

with open("data.csv", newline = "") as f:
    reader = csv.reader(f)
    data = list(reader)

d = data[0]

def mean(data):
    n = len(data)
    total = 0 
    for x in data:
        total += int(x)                     
    mean = total/n
    return mean

squaredList = []

for n in d:
    a = int(n)-mean(d)
    a = a**2
    squaredList.append(a)

sum = 0

for i in squaredList:
    sum = sum + i

result = sum/(len(d)-1)

SD = math.sqrt(result)
print(SD)