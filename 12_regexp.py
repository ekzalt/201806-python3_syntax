import re

text = 'lorem 1 ipsum 2 dolor 3 sit 4 amet'

regExp = r'\d'

result = re.findall(regExp, text)

print(result)
