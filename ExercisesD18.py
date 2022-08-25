import re
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
#Qual é a palavra mais frequente no parágrafo a seguir?
regex_pattern = r'[Ll]ove'  # this square bracket mean either A or a
matches = re.findall(regex_pattern, paragraph)
print(matches)  # ['Apple', 'apple']
