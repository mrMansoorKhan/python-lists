# list[startingIdx : endingIdx] ==> ending idx not included

marks = [95 , 93 , 91, 98 , 88]
print(marks[1:4])

marks[ : 4] #same as marks[0:4]

marks[1:] # same as marks[1:len(marks)]

marks[-3,-1]