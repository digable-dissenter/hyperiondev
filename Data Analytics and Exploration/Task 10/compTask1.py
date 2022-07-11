import numpy as np

# Question 1
# array() function takes from 1 to 2 positional arguments but 3 were given
# Tuple must have size 2
# Correct way:
numpy_values = np.array([(1, 0, 0), (0, 1, 0)])
print('Question 1:\n')
print(numpy_values)

# Question 2
# Output [0 0 0] vs [[0 0 0]]
# [0 0 0] is a one-dimensional array
# [[0 0 0]] is a two-dimensional array
a = np.array([0, 0, 0])
a2 = np.array([[0, 0, 0]])
print('\nQuestion 2:\n')
print(a) 
print(a2)

# Question 3
print('\nQuestion 3:\n')
arr = np.linspace(1,48,48).reshape(3,4,4)
'''
    reshape method outputs the array into a 3 by 4
    dimensional array, with 4 rows and columns in 
    each dimension.
'''
print(arr)

# 20.0
'''
    20.0 is in 2nd block, first row, and last number in first row of arr
    declared above
    1 prints out the 2nd block
    0 prints out the 1st row (of 2nd block)
    3 prints out the 4th number (from the 1st row of the 2nd block)
    Reference: (StackOverflow,2021)
'''
print("Array range printed for 20.0")
print(arr[1, 0, 3]) 

# [9. 10. 11. 12.]
'''
    [9. 10. 11. 12.] is in first block in arr, and since range is all in the same row (3rd) 
    in 1st block, we print that. 0:1 range specifies that we only want one row in this sequence
    otherwise would also print [25. 26. 27. 28.], i.e. 3rd row in 2nd block with [0:2]
    arr[0:1] prints 
'''
print("\nArray range printed for [9. 10. 11. 12.]")
print(arr[0:1, 2]) 

# [[33. 34. 35. 36.] [37. 38. 39. 40.] [41. 42. 43. 44.] [45. 46. 47. 48.]]
'''
    This sequence is all in the 3rd block in arr, so just print that
    arr[2] accomplishes this
'''
print("\nArray range printed for [[33. 34. 35. 36.] [37. 38. 39. 40.] [41. 42. 43. 44.] [45. 46. 47. 48.]]")
print(arr[2])

# [[5. 6.], [21. 22.] [37. 38.]]
'''
    This sequence prints the first two numbers from the
    2nd row of each block.
    : prints all blocks
    1 prints 2nd row (from all blocks)
    :2 prints first two numbers (in 2nd row from all blocks)
'''
print("\nArray range printed for [[5. 6.], [21. 22.] [37. 38.]]")
print(arr[:, 1, :2])

# [[36. 35.] [40. 39.] [44. 43.] [48. 47.]]
'''
    This sequence prints the first the last two numbers from the 
    3rd dimension in reverse order.

    Used the numpy's flip method to achieve the desired result after
    specifying the exact range we wish to filter for
'''
print("\nArray range printed for [[36. 35.] [40. 39.] [44. 43.] [48. 47.]]\n")
print(np.flip(arr[2,:,2:],axis=1))

# [13. 9. 5. 1.] [29. 25. 21. 17.] [45. 41. 37. 33.]]
'''
    Similar to above, except this sequence prints the first column from each 
    dimension in descending order.

    Used the numpy's flip method to achieve the desired result after
    specifying the exact range we wish to filter for
'''
print("\nArray range printed for [13. 9. 5. 1.] [29. 25. 21. 17.] [45. 41. 37. 33.]]\n")
print(np.flip(arr[:,:,0],axis=1))

## [[1. 4.] [45. 48.]]
'''
    This example represents the corner elements of arr.
    Thus advanced indexing needs to be applied

    First retrieve corner element positions
    corner1 = arr[0][0][0]
    corner2 = arr[0][0][3]
    corner3 = arr[2][3][0]
    corner4 = arr[2][3][3]

    Then break each up, using np.array function for rows,
    columns, and dimensions, and then combine for final result

    Reference: (Tutorialspoint, 2021)
    Reference: (GeeksForGeeks,2021)
'''
print("\nArray range printed for [[1. 4.] [45. 48.]]\n")

rows = np.array([[0,0],[3,3]])
cols = np.array([[0,3],[0,3]])
dim = np.array([[0],[2]])

print(arr[dim,rows,cols])

# [[25. 26. 27. 28.], [29. 30. 31. 32.], [33. 34. 35. 36.], [37. 38. 39. 40.]]
'''
    This sequence prints out the last 2 rows from the 2nd dimension
    & the first two rows from the 3rd dimension.

    To achieve this, referred to flatten and reshape methods.
    Initially, the entire sequence of numbers from the 2nd & 3rd dimensions
    were flattened. We could specify the exact range to be reshaped.

    Reference: (Numpy.org,2021)
'''
print("\nArray range printed for [[25. 26. 27. 28.], [29. 30. 31. 32.], [33. 34. 35. 36.], [37. 38. 39. 40.]]\n")
flatten_arr = arr[1:,].flatten()
print(flatten_arr[8:24].reshape(4,1,4))


