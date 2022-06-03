from operator import matmul
import numpy as np
text = input("\nEnter your PLAIN TEXT:\n").upper()  # ACT
key = input("\nEnter your KEY:\n").upper()  # GYBNQKURP
def hill_cypher(text, key):
    text_matrix = []
    key_matrix = []
    for ele in text:
        x = ord(ele) - 65
        text_matrix.append(x)   # [] because it will be a matrix
    temp = []
    for ele in key:
        y = ord(ele) - 65
        temp.append(y)
        if len(temp) == len(text):
            key_matrix.append(temp)
            temp = []
    ans = ""
    ans_list = np.matmul(key_matrix, text_matrix)
    for i in ans_list:
        ans += chr((i % 26) + 65)
    return ans
print(f"\nYour CYPHER TEXT is:\n{hill_cypher(text, key)}\n")  # POH