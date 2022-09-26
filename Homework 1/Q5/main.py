num_tests = int(input())

for i in range(num_tests):
    # Get current line of input
    line = input().split()
    gallons = int(line[0])
    gals_per_cell = int(line[1])
    empties_per_cell = int(line[2])

    # Init local variables
    cells = 0
    empties = 0

    # Use all gallons
    cells += gallons // gals_per_cell
    empties = cells

    # Use all empties
    while empties >= empties_per_cell:
        new_cells = empties // empties_per_cell
        empties = empties % empties_per_cell + new_cells
        cells += new_cells

    print(cells)
