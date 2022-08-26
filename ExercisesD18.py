import re
#Qual é a palavra mais frequente no parágrafo a seguir?


txt = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

regex_pattern = r'[Ll]ove|[Tt]eaching|[Ii]f|[Yy]ou'
matches = re.findall(regex_pattern, txt)
print(f"{matches}")  # ['Apple', 'banana', 'apple', 'banana']



