# Seeing as we only go up to 9, range is 1 to 10
# On each line, the product of x for each y in the nested loop is output
# The bit of code for printing this in a pyramid form, using the end= parameter is referenced from:
# https://pynative.com/print-pattern-python-examples/

for x in range(1, 10):
    for y in range(1, x+1):
# The x+1 makes sure every number in x range is counted
        print('%d' % (x*y), end=' ')
# Print for next number
    print('')

# More comments:
# The end= parameter ends the print output with a space in this example
# It combines all the products from same number on one line
# Reference: https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/
