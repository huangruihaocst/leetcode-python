import os

name = input('Problem Name: ')

if not os.path.exists(name):
    os.mkdir(name)
with open(name + '/solution.py', 'w') as f:
    f.write('')

with open(name + '/README.md', 'w') as f:
    f.write('# ' + name + '\n\n' + '## Solution\n\n')
