sentence = input("Enter a sentence: ")
sentence_length = len(sentence)

file_name = input("Enter a file name: ")
file_name = f"{file_name}.txt"

with open(file_name, "w") as file:
    file.write(sentence)
    file.close()

print(f"You've written {sentence_length} characters to {file_name}")
