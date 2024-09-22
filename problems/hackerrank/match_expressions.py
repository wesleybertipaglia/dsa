# platform: HackerRank
# title: Match Expressions

# Description:
# Given a list of strings, write a function that returns a list of strings that match the following regular expression:
# 'a', 'aa' and 'bababbb' match
# 'ab' and 'baba' do not match

import re

regular_expression = '(a$|aa|bababbb)'

def is_match(string):
    return re.match(regular_expression, string) is not None

strings_to_test = ['a', 'aa', 'bababbb', 'ab', 'baba']

for string in strings_to_test:
    print(f'{string} matches' if is_match(string) else f'{string} does not match')