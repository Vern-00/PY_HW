from log import timestamp

@timestamp
def hi():
    print('hi')
def main():
    hi()

main()
'''
Output:
$ python3 test.py
Wed Oct 19 17:27:12 2022
hi
'''

"""
from print_caps import allcaps

@allcaps
def greet():
    return "hello World!"
def main():
    print(greet())

main()

'''
Output:
$ python3 test.py
HELLO WORLD!
'''
"""