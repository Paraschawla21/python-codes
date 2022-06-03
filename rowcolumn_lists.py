row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
map = [row1, row2, row3]
print(f"\n{row1}\n{row2}\n{row3}\n")
position = print("Enter the position you wish to write x:")
row_position = input("Row: ")
column_position = input("Column: ")
position = row_position + column_position
horizontal = int(position[0])
vertical = int(position[1])
map[horizontal - 1][vertical - 1] = 'x'
print(f"\n{row1}\n{row2}\n{row3}\n")