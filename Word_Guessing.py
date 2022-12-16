word = input("Enter Ur Word : ")
word_un = list(len(word) * "_")

for i in range(len(word)+5):
    lett = input("Enter Ur Alphabet : ")
    if len(lett) != 1:
        print("Please Enter Only 1 Character!!")
        continue
    if lett in word:
        ind = word.find(lett)
        word_un[ind] = lett
        print("".join(word_un))
    else:
        print("Wrong!")

