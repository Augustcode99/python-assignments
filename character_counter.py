def splitter(sentence):
    return [char for char in sentence]

words = input("enter a sentence for evaluation: ")
master_count = {}
chars = splitter(words)


for i in words:
    char_count = chars.count(i)
    master_count[i] = char_count
    
print(master_count)