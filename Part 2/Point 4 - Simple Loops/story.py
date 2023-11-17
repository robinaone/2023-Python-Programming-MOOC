story = ""
last = ""
while True:
    word = input("Please type in a word: ")
    if word == "end" or word == last:
        break
    story += word + " "
    last = word
print(f"{story}")