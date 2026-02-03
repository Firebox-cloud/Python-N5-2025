scores = [75,82,93,65,78]
highestScores = scores[0]
for index in range(1,len(scores)):
    if scores[index] > highestScores:
        highestScores = scores[index]

print("The highest score is",highestScores) you