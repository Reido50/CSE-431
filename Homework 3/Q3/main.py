# Get first line of input
num_genes = int(input())

# Determine if ids are in correct order
genes = [int(x) for x in input().split()]   # List comprehension implementation taken from https://stackoverflow.com/questions/1574678/efficient-way-to-convert-strings-from-split-function-to-ints-in-python
sorted_genes = sorted(genes)


# Return "no" if it gets to this point
print("no")
