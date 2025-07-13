import numpy as np
data = np.array([[1,2,np.nan], [4,np.nan,6]])
print("the data pre-cleaning:\n",data)
col_mean =np.nanmean(data,axis=0)
data[np.isnan(data)]=col_mean[np.isnan(data).nonzero()[1]]
print("the data post-cleaning:\n")