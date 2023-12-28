input_string = input("Please type in a word: ")
input_character = input("Please type in a character: ")
i = 0

while i < len(input_string)-2:
    if input_string[i] == input_character:
        print(input_string[i:i+3])
        break
    i += 1

#Model solution wanted me to use index.find, whoops
#word = input("Please type in a word: ")
#character = input("Please type in a character: ")
#index = word.find(character)
#if index!=-1 and len(word)>=index+3:
#    print(word[index:index+3])