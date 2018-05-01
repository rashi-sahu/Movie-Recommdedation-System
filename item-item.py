import csv
from decimal import Decimal
import math
import time
def maxm(a, b):
    if a>=b:
        return a
    return b

#similarity value between two item vectors
def sim(item1, item2):
    userCount=len(item1)
    # print item1, item2
    sum1=0
    sum2=0
    for i in range(userCount):
        sum1=sum1+item1[i]
        sum2=sum2+item2[i]
    avg1=Decimal(Decimal(sum1)/Decimal(userCount))
    avg2=Decimal(Decimal(sum2)/Decimal(userCount))
    # print sum1, sum2, avg1, avg2
    for i in range(userCount):
        if(item1[i]!=0):
            item1[i]=Decimal(item1[i]-avg1)
        if(item2[i]!=0):
            item2[i]=Decimal(item2[i]-avg2)
    psum=0
    prod1=0
    prod2=0
    for i in range(userCount):
        psum=psum+Decimal(item1[i]*item2[i])
        prod1=(prod1+(item1[i]**2))
        prod2=(prod2+(item2[i]**2))
    prod1=math.sqrt(prod1)
    prod2=math.sqrt(prod2)

    fprod=Decimal(prod1*prod2)
    if fprod==0:
        fprod=1
    return (psum/fprod)

fname="utility.txt"
dataset=[]
itemCount=0
userCount=0
start_time = time.time()

with open(fname) as tsv:
    for line in csv.reader(tsv, dialect="excel-tab"):
        line = map(int, line)
        line = list(line)
        # print line
        dataset.append(line)


# print dataset

for i in range(len(dataset)-1):
    itemCount=maxm(itemCount, dataset[i][1])
    userCount=maxm(userCount, dataset[i][0])

utilityMatrix=[]

print "No of users, ", userCount
print "No of items, ", itemCount

for i in range(itemCount+1):
    array=[]
    for j in range(userCount+1):
        array.append(0)
    utilityMatrix.append(array)
print len(dataset)
for i in range(len(dataset)-1):
    utilityMatrix[dataset[i][1]][dataset[i][0]]=dataset[i][2]
#
# for i in range(1, 11):
#     for j in range(1, 11):
#         print utilityMatrix[i][j],
#     print "\n"

userx=input("Which user to give suggestion for ? ")
itemx=input("Which items expected rating ? ")


item_index = []
for i in range(1, itemCount+1):
	item_index.append(i)
# print item_index

thefile = open('simArray.txt', 'w')

simArray=[]
for i in range(1, itemCount+1):
    simArray.append(sim(utilityMatrix[itemx], utilityMatrix[i]))
print len(simArray)
# weightedSimArray=[]

# for i in range(0, len(simArray)):
#     if i!=itemx:
#         weightedSimArray.append(simArray[i]*utilityMatrix[i][userx])
#     else:
#         weightedSimArray.append(simArray[i])

for x in simArray:
  thefile.write("%s\n" % x)

print("--- %s seconds ---" % (time.time() - start_time))

# print len(weightedSimArray)

# print weightedSimArray[0]


top_50 = [x for (y,x) in sorted(zip(simArray, item_index), key=lambda pair: pair[0], reverse=True)]
top_50 = top_50[:50]

# print top_50

weightedSum=0
denom=0
for i in range(0, len(top_50)):
    weightedSum=weightedSum+(utilityMatrix[top_50[i]][userx]*simArray[top_50[i]])
    multp=1
    if utilityMatrix[top_50[i]][userx]==0:
        multp=0
    denom=denom+(simArray[top_50[i]]*multp)

print "predicted rating : ", Decimal(weightedSum/denom)
