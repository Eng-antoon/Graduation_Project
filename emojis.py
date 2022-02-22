# Import required libraries
import demoji
# Text from where you want to convert emojis
text = "Convert 😄 the 😭 given emojis 😒 to 😠 text"
emojis = demoji.findall(text)
# Print converted emojis
print(emojis)