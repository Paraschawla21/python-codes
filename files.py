# file = open("my_file.txt")
with open("my_file.txt", mode = "a") as file:
    # print(file.read())
# contents = file.read()
# print(file.read())
    file.write("\nNew Text.")
file.close()