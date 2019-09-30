# by Max Huber
# init variables
word = input("Enter word: ")
vowels = ['a','e','i','o','u','y']
isVowelCase = False
i = 0

# check if starts with vowel
for x in vowels:
	if word[:1] == vowels[i]:
		isVowelCase = True
	i = i + 1

#print
if isVowelCase == True:
	print(word+"ay")
else:
	print(word[1:] + word[0:1] + "ay")
