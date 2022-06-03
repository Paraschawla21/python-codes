def vernam_cypher(text, key, choose):
    j = 0
    answer = ""
    for i in range(len(text)):
        j = j % len(key)
        if text[i] != " ":
            if choose == "encrypt":
                sum = (((ord(text[i]) - 65) + (ord(key[j]) - 65)) % 26) + 65
                answer += chr(sum)
            elif choose == "decrypt":
                sum = (ord(text[i]) - 65) - (ord(key[j]) - 65)
                if sum >= 0:
                    sum += 65
                    answer += chr(sum)
                elif sum < 0:
                    sum += 65
                    sum += 26
                    answer += chr(sum)
            j += 1
        else:
            answer += " "
    return answer
should_continue = True
while should_continue:
    choose = input("\nType 'encrypt' for encrpytion, 'decrypt' for decryption:\n").lower()
    text = input("\nEnter your message:\n").upper()
    key = input("\nEnter your key:\n").upper()
    print(f"\nYour {choose}ed text is:", vernam_cypher(text, key, choose))
    result = input("\nType 'yes' if you wish to continue, otherwise type 'no'\n").lower()
    if result == "no":
        should_continue = False
        print("Goodbye...!!\n")