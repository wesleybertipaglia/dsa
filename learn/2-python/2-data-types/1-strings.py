# creating
single_quoted_string = 'Hello, World!'

double_quoted_string = "Hello, World!"

triple_quoted_string = '''
Hello, World!
'''

# concatenation
concatenated_string = 'Hello, ' + 'World!'
concatenated_string = 'Hello,' + ' World! ' + 2

# repetition
repeated_string = 'Hello, ' * 3

# length
length = len('Hello, World!')
unicode_from_char = ord("a")
char_from_unicode = chr(90)

# access
first_character = 'Hello, World!'[0] # H
last_character = 'Hello, World!'[-1] # !

# slicing
substring = 'Hello, World!'[0:5] # Hello
substring = 'Hello, World!'[:5] # Hello
substring = 'Hello, World!'[7:] # World!
substring = 'Hello, World!'[::-1] # !dlroW ,olleH

# formatting
formatted_string = f'Hello, World! {2 + 2}'

# methods: format
upper_case = 'Hello, World!'.upper() # HELLO, WORLD!
lower_case = 'Hello, World!'.lower() # hello, world!
title_case = 'Hello, World!'.title() # Hello, World!
capitalize = 'hello, world!'.capitalize() # Hello, world!
strip_string = ' Hello, World! '.strip() # Hello, World!

# methods: transform
replace_string = 'Hello, World!'.replace('Hello', 'Hi') # Hi, World!
split_string = 'Hello, World!'.split(',') # ['Hello', ' World!']
join_string = ','.join(['Hello', ' World!']) # Hello, World!

# methods: search
find_string = 'Hello, World!'.find('World') # 7
index = 'Hello, World!'.index('World') # 7

# methods: check
is_alpha = 'Hello, World!'.isalpha() # False -> space and ! is not alphabet
is_digit = 'Hello, World!'.isdigit() # False
is_space = 'Hello, World!'.isspace() # False
is_upper = 'Hello, World!'.isupper() # False
is_lower = 'Hello, World!'.islower() # False
is_title = 'Hello, World!'.istitle() # True

is_start = 'Hello, World!'.startswith('Hello') # True
is_end = 'Hello, World!'.endswith('!') # True

is_in = 'Hello' in 'Hello, World!' # True
is_not_in = 'Hi' not in 'Hello, World' # True

count = 'Hello, World!'.count('l') # 3

# special characters
escaped_character = 'Hello, World!\n' # new line
escaped_character = 'Hello, World!\t' # tab
escaped_character = 'Hello, World!\\' # backslash
escaped_character = 'Hello, World!\"' # double quote
escaped_character = 'Hello, World!\'' # single quote
escaped_character = 'Hello, World!\r' # carriage return
escaped_character = 'Hello, World!\b' # backspace
escaped_character = 'Hello, World!\f' # form feed
escaped_character = 'Hello, World!\v' # vertical tab
escaped_character = 'Hello, World!\a' # bell
escaped_character = 'Hello, World!\0' # null
