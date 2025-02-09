
student_scores = [9,7.3,6.5, 4, 8, 5.4, 4.2, 7.8, 3.4, 9.2]

max = student_scores[1] 

for score in student_scores:
    if max < score:
        max = score

print(max)
