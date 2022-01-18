c_alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input().lower()

for i in c_alphabet :
    word = word.replace(i,"c")

print(len(word))