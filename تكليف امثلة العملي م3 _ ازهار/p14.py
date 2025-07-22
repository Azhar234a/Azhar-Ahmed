import numpy as np

scores = np.array([65,72,80,55,90,45,85,70,75,60,95,50])
q1=np.percentile(scores,25)
median=np.percentile(scores,50)
q3=np.percentile(scores,75)
scores_rage=np.max(scores) - np.min(scores)
print(f"Q1 (25%): {q1}")
print(f"median (50%): {median}")
print(f"Q3 (75%): {q3}")
print(f"Rage : {scores_rage}")
