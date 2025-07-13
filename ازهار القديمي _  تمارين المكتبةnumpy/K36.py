import numpy as np
x = np.array([[0, 1], [2, 3]], dtype='<u2')
x.tobytes()
b'\x00\x00\x01\x00\x02\x00\x03\x00'
x.tobytes('C') == x.tobytes()
True
x.tobytes('F')
b'\x00\x00\x02\x00\x01\x00\x03\x00'