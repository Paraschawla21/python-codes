test_height = int(input("\nEnter the height of the wall in meters: "))
test_width = int(input("\nEnter the width of the wall in meters: "))
test_coverage = int(input("\nEnter the rate per squares of meters: "))
import math
def paint(height, width, coverage):
    cans_required = ((height * width) / coverage)
    print(f"\nNo of paint cans required: {math.ceil(cans_required)}\n")
paint(height = test_height, width = test_width, coverage = test_coverage)