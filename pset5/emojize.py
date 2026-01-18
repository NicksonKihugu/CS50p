import emoji

text = input("Input: ")
emoji_result = emoji.emojize(text, language='alias')
print(f"Output: {emoji_result}")
