
import csv
from decimal import Decimal
from tabulate import tabulate
# sudo apt-get install python-tabulate
def similarity(ary1, ary2):
    sum1=0
    mag1=0
    mag2=0
    for i in range(0, len(ary1)):
        sum1=sum1+ary1[i]*ary2[i]
    for i in range(0, len(ary1)):
        mag1=mag1+(ary1[i]**2)
        mag2=mag2+(ary2[i]**2)
    mag1=((mag1)**0.5)
    mag2=((mag2)**0.5)
    return float((sum1)/(mag1*mag2))

fname="itemInfo.txt"
itemVec=[]
temp=[]
itemVec.append(temp)

with open (fname) as f:
    for line in f:
        # print line
        id=""
        for x in range (0, len(line)):
            if line[x]=='|':
                break
            else:
                id=id+line[x]
        # print "id is \t", id
        line=line[-39:]
        # print line
        line=line.translate(None, "|")
        # print line
        temp=[]
        for i in range (0, len(line)):
            temp.append(line[i])
        temp.pop()
        temp=map(int, temp)
        # print temp
        itemVec.append(temp)

movieNameArray=[]
movieNameArray.append("NULL")


with open (fname) as f:
    for line in f:
        # print line
        first=-1;
        id=""
        for x in range (0, len(line)):
            if line[x]=='|':
                first=x
                break
            else:
                id=id+line[x]

        name=""
        for x in range (first+1, len(line)):
            if line[x]=='|':
                break
            else:
                name=name+line[x]
        # print "id is \t", id, "name is \t", name
        movieNameArray.append(name)
# for x in range (0, len(itemVec)):
#     print x, " -> ", itemVec[x]

userx=input("\nEnter which user to suggest movies for : ")
countx=input("\nHow Many Movies to suggest : ")


fname="utility.txt"
dataset=[]
userProfile=[]
avgRating=0
ratingCountForEachGenre=[]
for i in range(0, 19):
    ratingCountForEachGenre.append(0)
    userProfile.append(0)

with open(fname) as tsv:
    for line in csv.reader(tsv, dialect="excel-tab"):
        line = map(int, line)
        line = list(line)
        # print line
        if(line[0]==userx):
            dataset.append(line)
            movieId=line[1]
            # print itemVec[line[1]]
            for j in range(0, len(itemVec[movieId])):
                # print itemVec[movieId]
                if(itemVec[movieId][j]==1):
                    ratingCountForEachGenre[j]=ratingCountForEachGenre[j]+1
            avgRating=Decimal(avgRating+line[2])

# print ratingCountForEachGenre

# print dataset

avgRating=Decimal(avgRating/len(dataset))
print "\nAverage Rating of user ", userx, " -> ", Decimal(avgRating)

for x in range(0, len(dataset)):
    dataset[x][2]=((dataset[x][2])-(avgRating))
# print dataset, "\n______________________________________\n"


for x in range(0, len(dataset)):
    # print itemVec[dataset[x][1]]
    for i in range(0, len(itemVec[dataset[x][1]])):
        # print itemVec[dataset[x][1]][i],
        itemVec[dataset[x][1]][i]=float(itemVec[dataset[x][1]][i]*dataset[x][2])
        userProfile[i]=userProfile[i]+itemVec[dataset[x][1]][i]
        # print itemVec[dataset[x][1]][i],
    # print dataset[x][1], " -> ", itemVec[dataset[x][1]]

# print "user profile\n", userProfile

for i in range(0, len(userProfile)):
    # print i
    if userProfile[i]!=0:
        userProfile[i]=userProfile[i]/ratingCountForEachGenre[i]

print "\nnormalized user profile\n", userProfile

item_index = []
for i in range(1, len(itemVec)):
	item_index.append(i)

# print item_index
similarityMeasure=[]
for i in range(1, len(itemVec)):
    sim=similarity(itemVec[i], userProfile)
    # print userProfile
    similarityMeasure.append(sim)

#
# top_50 = [x for (y,x) in sorted(zip(similarityMeasure, item_index), key=lambda pair: pair[0], reverse=True)]
# print top_50

top=[b[0] for b in sorted(enumerate(similarityMeasure),key=lambda i:i[1])]
# print top
top=top[::-1]
top = top[:countx]
# print top

print "\n\nrecommended top movies for you\n"
# print top_50
myTable=[]
for i in range(0, len(top)):
    temp=[]
    temp.append(movieNameArray[top[i]])
    temp.append(similarityMeasure[top[i]])
    myTable.append(temp)

print tabulate(myTable, headers=['Name', 'Similarity'], tablefmt='orgtbl')
