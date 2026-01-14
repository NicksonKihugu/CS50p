# Prompt user for text
text = input()
words = text.split()

# Format sep in print
print(*words, sep="...")