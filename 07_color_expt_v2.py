import colored

# Reference of sorts is here
# https://pypi.org/project/colored/

# text = colored('Hello, World!', 'green')
# print(text)

color = colored.fg('#00FFFF')
# res = colored.attr('bold')
print (color + "Hello World !!!")

print ('%s Hello Something !!! %s' % (colored.fg(216), colored.attr(1)))
