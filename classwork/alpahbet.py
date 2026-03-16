alphabet = ['a','b','c','d']

# for letter in alphabet:
#     print(letter)

let = input("Enter letter: ")

for fack_let in alphabet:
    if fack_let == let:
        print("Number exist")

    else:
        alphabet.append(let)
        print(alphabet)