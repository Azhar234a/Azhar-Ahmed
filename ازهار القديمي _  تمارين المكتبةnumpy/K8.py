np.mean(intake)
6753.636363636364
intake.std(ddof=1)
1142.1232221373727
t = (np.mean(intake)-7725)/(intake.std(ddof=1)/np.sqrt(len(intake)))
t
-2.8207540608310198