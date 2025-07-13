from numpy.lib import NumpyVersion
if NumpyVersion(np.__version__) < '1.7.0':
 print('skip')
 # skip