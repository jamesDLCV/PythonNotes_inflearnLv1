# exercise
# if elements of array <= 0, print 0,
# else print the elements.

import numpy as np

a = np.array([-5, 4, -3, 2, -1])
print(a)

# if a <= 0, then True otherwise False
mask = (a <= 0)
print(mask)

# a[mask], print only True
print(a[mask])

# if True, print 0, then print the elements
a[mask] = 0
print(a)