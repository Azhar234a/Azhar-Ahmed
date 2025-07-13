import numpy as np
blood_pressure=np.random.randint(80,200,(100,2))
mean_bp=np.mean(blood_pressure,axis=0)
high_bp=blood_pressure[blood_pressure[:,0]>140]
print("high_bp:\n",high_bp)
correlation=np.corrcoef(blood_pressure[:,0],blood_pressure[:,1])
print("correlation:\n",correlation)