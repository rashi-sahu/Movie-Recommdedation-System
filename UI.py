"""
Simple User Interface
"""
from movielens import *
from sklearn.cluster import KMeans

import numpy as np
import pickle
import random
import sys
import time
# from __future__ import print_function

user = []
item = []

d = Dataset()
d.load_users("data/u.user", user)
d.load_items("data/u.item", item)

n_users = len(user)
n_items = len(item)

# https://www.journaldev.com/15638/python-pickle-example
# Python Pickle is used to serialize and deserialize a python object structure.
# Any object on python can be pickled so that it can be saved on disk.
# To retrieve pickled data, pickle.load() 
utility_matrix = pickle.load( open("utility_matrix.pkl", "rb") )
print len(utility_matrix)
print len(utility_matrix[0])
# Find the average rating for each user and stores it in the user's object
for i in range(0, n_users):
    x = utility_matrix[i]
    user[i].avg_r = sum(a for a in x if a > 0) / sum(a > 0 for a in x)

# Find the Pearson Correlation Similarity Measure between two users
def pcs(x, y, ut):
    num = 0
    den1 = 0
    den2 = 0
    A = ut[x - 1]		#New user's utility row(19 values) 
    B = ut[y - 1]		#The user being compared
    num = sum((a - user[x - 1].avg_r) * (b - user[y - 1].avg_r) for a, b in zip(A, B) if a > 0 and b > 0)
    den1 = sum((a - user[x - 1].avg_r) ** 2 for a in A if a > 0)
    den2 = sum((b - user[y - 1].avg_r) ** 2 for b in B if b > 0)
    den = (den1 ** 0.5) * (den2 ** 0.5)
    if den == 0:
        return 0
    else:
        return num / den

# Perform clustering on items
#Appending the movie genre array for all movies in dataset into an array
movie_genre = []
for movie in item:
    movie_genre.append([movie.unknown, movie.action, movie.adventure, movie.animation, movie.childrens, movie.comedy,
                        movie.crime, movie.documentary, movie.drama, movie.fantasy, movie.film_noir, movie.horror,
                        movie.musical, movie.mystery, movie.romance, movie.sci_fi, movie.thriller, movie.war, movie.western])
# print movie_genre
print len(item)
movie_genre = np.array(movie_genre)
cluster = KMeans(n_clusters=19)	#The number of clusters to form as well as the number of centroids to generate. is 19
cluster.fit_predict(movie_genre) # Compute cluster centers and predict cluster index for each sample.

ask = random.sample(item, 10)	# To ask user to rate 10 random movies
new_user = np.zeros(19)     #creating a new user

print "Please rate the following movies (1-5)---------------------------------"




for movie in ask:
	# print (movie.title, end = "")
	sys.stdout.write(movie.title)
	sys.stdout.write(":----- ")
	# print movie
	# print movie.unknown, movie.action, movie.adventure, movie.animation, movie.childrens, movie.comedy, movie.crime, movie.documentary, movie.drama, movie.fantasy, movie.film_noir, movie.horror,movie.musical, movie.mystery, movie.romance, movie.sci_fi, movie.thriller, movie.war, movie.western
	array1=[]
	# array1.append(movie.unknown, movie.action, movie.adventure, movie.animation, movie.childrens, movie.comedy, movie.crime, movie.documentary, movie.drama, movie.fantasy, movie.film_noir, movie.horror,movie.musical, movie.mystery, movie.romance, movie.sci_fi, movie.thriller, movie.war, movie.western)
	# print array1
	array1.append(movie.unknown)
	array1.append(movie.action)
	array1.append(movie.adventure)
	array1.append(movie.animation)
	array1.append(movie.childrens)
	array1.append(movie.comedy)
	array1.append(movie.crime)
	array1.append(movie.documentary)
	array1.append(movie.drama)
	array1.append(movie.fantasy)
	array1.append(movie.film_noir)
	array1.append(movie.horror)
	array1.append(movie.musical)
	array1.append(movie.mystery)
	array1.append(movie.romance)
	array1.append(movie.sci_fi)
	array1.append(movie.thriller)
	array1.append(movie.war)
	array1.append(movie.western)

	# print array1
	if array1[0]==1:
		sys.stdout.write("unknown")
		sys.stdout.write(" ")
		# print ("unknown", end=' ')
	if array1[1]==1:
		sys.stdout.write("action")
		sys.stdout.write(" ")
		# print ("action", end=' ')
	if array1[2]==1:
		sys.stdout.write("adventure")
		sys.stdout.write(" ")
		# print ("adventure", end=' ')
	if array1[3]==1:
		sys.stdout.write("animation")
		sys.stdout.write(" ")
		# print ("animation", end=' ')
	if array1[4]==1:
		sys.stdout.write("childrens")
		sys.stdout.write(" ")
		# print ("childrens", end=' ')
	if array1[5]==1:
		sys.stdout.write("comedy")
		sys.stdout.write(" ")
		# print ("comedy", end=' ')
	if array1[6]==1:
		sys.stdout.write("crime")
		sys.stdout.write(" ")
		# print ("crime", end=' ')
	if array1[7]==1:
		sys.stdout.write("documentary")
		sys.stdout.write(" ")
		# print ("documentary", end=' ')
	if array1[8]==1:
		sys.stdout.write("drama")
		sys.stdout.write(" ")
		# print ("drama", end=' ')
	if array1[9]==1:
		sys.stdout.write("fantasy")
		sys.stdout.write(" ")
		# print ("fantasy", end=' ')
	if array1[10]==1:
		sys.stdout.write("film_noir")
		sys.stdout.write(" ")
		# print ("film_noir", end=' ')
	if array1[11]==1:
		sys.stdout.write("horror")
		sys.stdout.write(" ")
		# print ("horror", end=' ')
	if array1[12]==1:
		sys.stdout.write("musical")
		sys.stdout.write(" ")
		# print ("musical", end=' ')
	if array1[13]==1:
		sys.stdout.write("mystery")
		sys.stdout.write(" ")
		# print ("mystery", end=' ')
	if array1[14]==1:
		sys.stdout.write("romance")
		sys.stdout.write(" ")
		# print ("romance", end=' ')
	if array1[15]==1:
		sys.stdout.write("sci_fi")
		sys.stdout.write(" ")
		# print ("sci_fi", end=' ')
	if array1[16]==1:
		sys.stdout.write("thriller")
		sys.stdout.write(" ")
		# print ("thriller", end=' ')
	if array1[17]==1:
		sys.stdout.write("war")
		sys.stdout.write(" ")
		# print ("war", end=' ')
	if array1[18]==1:
		sys.stdout.write("western")
		sys.stdout.write(" ")
		# print ("western", end=' ')	

	


	a = int(input())

	if new_user[cluster.labels_[movie.id - 1]] != 0:
		new_user[cluster.labels_[movie.id - 1]] = (new_user[cluster.labels_[movie.id - 1]] + a) / 2
	else:
		new_user[cluster.labels_[movie.id - 1]] = a
	# print new_user

utility_new = np.vstack((utility_matrix, new_user))

user.append(User(944, 21, 'M', 'student', 110018))  #Appending the new user

pcs_matrix = np.zeros(n_users)  #init the pearson correaltion matrix

# print "Finding users which have similar preferences."
for i in range(0, n_users + 1):
    if i != 943:
        pcs_matrix[i] = pcs(944, i + 1, utility_new)	  #findind pcs value with eac user and new user	

# print len(pcs_matrix)

user_index = []
for i in user:
	user_index.append(i.id - 1)
# print user_index
user_index = user_index[:943]
user_index = np.array(user_index)


top_5 = [x for (y,x) in sorted(zip(pcs_matrix, user_index), key=lambda pair: pair[0], reverse=True)]
# print top_5    #a sorted array of pcs matrix printing its index

top_5 = top_5[:5]
# print top_5

top_5_genre = []

for i in range(0, 5):
	maxi = 0
	maxe = 0
	for j in range(0, 19):
		if maxe < utility_matrix[top_5[i]][j]:
			maxe = utility_matrix[top_5[i]][j]
			maxi = j
	top_5_genre.append(maxi)	# which genre was rated heighest by the user top_5[i]

print "\nMovie genres you'd like : "

resultant=[]
for i in top_5_genre:
	if i == 0:
		print "unknown"
		if "unknown" not in resultant:
			resultant.append("unknown")
	elif i == 1:
		print "action"
		if "action" not in resultant:
			resultant.append("action")
	elif i == 2:
		print "adventure"
		if "adventure" not in resultant:
			resultant.append("adventure")
	elif i == 3:
		print "animation"
		if "animation" not in resultant:
			resultant.append("animation")
	elif i == 4:
		print "childrens"
		if "childrens" not in resultant:
			resultant.append("childrens")
	elif i == 5:
		print "comedy"
		if "comedy" not in resultant:
			resultant.append("comedy")
	elif i == 6:
		print "crime"
		if "crime" not in resultant:
			resultant.append("crime")
	elif i == 7:
		print "documentary"
		if "documentary" not in resultant:
			resultant.append("documentary")
	elif i == 8:
		print "drama"
		if "drama" not in resultant:
			resultant.append("drama")
	elif i == 9:
		print "fantasy"
		if "fantasy" not in resultant:
			resultant.append("fantasy")
	elif i == 10:
		print "film_noir"
		if "film_noir" not in resultant:
			resultant.append("film_noir")
	elif i == 11:
		print "horror"
		if "horror" not in resultant:
			resultant.append("horror")
	elif i == 12:
		print "musical"
		if "musical" not in resultant:
			resultant.append("musical")
	elif i == 13:
		print "mystery"
		if "mystery" not in resultant:
			resultant.append("mystery")
	elif i == 14:
		print "romance"
		if "romance" not in resultant:
			resultant.append("romance")
	elif i == 15:
		print "science fiction"
		if "science fiction" not in resultant:
			resultant.append("science fiction")
	elif i == 16:
		print "thriller"
		if "thriller" not in resultant:
			resultant.append("thriller")
	elif i == 17:
		print "war"
		if "war" not in resultant:
			resultant.append("war")
	else:
		print "western"
		if "western" not in resultant:
			resultant.append("western")

print resultant