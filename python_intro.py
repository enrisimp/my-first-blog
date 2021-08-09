print('Hello, Django girls!')
def hi():
    print('Hi there!')
    print('How are you?')
hi()

def hi(name):
    if name == 'Ola':
        print('Hi Ola!')
    elif name == 'Sonja':
        print('Hi Sonja!')
    else:
        print('Hi ' + name + '!')

hi("Rachel")
hi('Sonja')
hi('Ola')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    hi(name)
    print('Next girl')