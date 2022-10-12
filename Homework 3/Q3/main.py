import bisect

def is_gene_fixable():
    # Get first line of input
    num_genes = int(input())

    # Determine if ids are in correct order
    genes = [int(x) for x in input().split()]   # List comprehension implementation taken from https://stackoverflow.com/questions/1574678/efficient-way-to-convert-strings-from-split-function-to-ints-in-python
    sorted_genes = sorted(genes)

    # Is it already sorted?
    if genes == sorted_genes:
        return "yes"

    # Look for a jank spot
    prev = -1
    nums = None
    for i in range(len(genes)):
        # Start the prev tracker
        if prev < 0:
            prev = i
            continue
            
        # Is this the jank spot?
        if genes[i] < genes[prev]:
            # Find where gene[prev] is in sorted_genes
            sorted_pos = bisect.bisect_left(sorted_genes, genes[prev])   
            nums = (prev, sorted_pos)
            break

        prev = i

    # Backup genes
    backup = genes.copy()

    # Does swapping work?
    temp = genes[nums[0]]
    genes[nums[0]] = genes[nums[1]]
    genes[nums[1]] = temp
    if genes == sorted_genes:
        return "yes\nswap " + str(nums[0] + 1) + " " + str(nums[1] + 1)

    # Restore backup
    genes = backup.copy()

    # Does reversing work?
    iter = 0
    for i in range(nums[0], nums[1] + 1, 1):
        genes[i] = backup[nums[1] - iter]
        iter += 1
    if genes == sorted_genes:
        return "yes\nreverse " + str(nums[0] + 1) + " " + str(nums[1] + 1)

    return "no"

print(is_gene_fixable())
