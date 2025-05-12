# Search the maximum and minimum element in the given array using NumPy
import numpy as np
A=np.array([13,45,2,43,77,23,42])
MX=np.max(A)
print("Maximum element in the given array is : ",MX)
MI=np.min(A)
print("Minimum element in the given array is : ",MI)

# Sort the elements in the given array using Numpy
import numpy as np
A=np.array([13,45,2,43,77,23,42])
S=np.sort(A)
print("The sorted array is : ",S)

# Find the mean of every NumPy array in the given list
import numpy as np
A=np.array([[13,45,2,43,77,23,42],[1,2,3,4,5,6,7]])
print(A)
M=np.mean(A[0])
K=np.mean(A[1])
J=np.mean(A)
print("Mean of the first array         : ",M)
print("Mean of the second array        : ",K)
print("Mean of the both array combined : ",J)

# Add rows and columns in Numpy array
import numpy as np
A=np.array([[13,45,2,43,77,23,42],[1,2,3,4,5,6,7]])
print("The initial array ")
print(A)
B=np.array([23,45,41,87,99,65,86])
C=np.array([[9],[8],[4]])
D=np.append(A,[B],axis=0)
D=np.append(D,C,axis=1)
print()
print("The array after adding new columns and rows")
print(D)

# Reverse a Numpy array
import numpy as np
A=np.array([13,45,2,43,77,23,42])
print("The array")
print(A)
rev=A[::-1]
print()
print("The reversed array")
print(rev)

# Multiply two matrices in a single line using NumPy
import numpy as np
A=np.array([[1,2,3],[4,5,6],[7,8,9]])
B=np.array([[5,8,3],[7,4,2],[9,3,7]])
print("The two matrices to be multiplied is ")
print(A)
print()
print(B)
print()
C=np.dot(A,B)
print("The multiplied matrix is ")
print(C)



