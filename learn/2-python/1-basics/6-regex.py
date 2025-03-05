import re

phrase = "Hello, my name is Wesley. I am 25 years old, and I am a software engineer."

# ordinary characters: match themselves
re.search(r'Wesley', phrase)  # <re.Match object; span=(18, 24), match='Wesley'>
re.search(r'Jhon', phrase)    # None

# period (.) : match any character except newline
re.search(r'.esley', phrase)  # <re.Match object; span=(17, 23), match='Wesley'>
re.search(r'.ears', phrase)   # <re.Match object; span=(25, 30), match=' years'>

# caret (^) : match the start of the string
re.search(r'^Hello', phrase)  # <re.Match object; span=(0, 5), match='Hello'>
re.search(r'^Wesley', phrase) # None

# dollar ($) : match the end of the string
re.search(r'engineer\.$', phrase)  # <re.Match object; span=(58, 67), match='engineer.'>
re.search(r'Hello$', phrase)       # None

# asterisk (*) : match 0 or more repetitions of the preceding character
re.search(r'a*', phrase)  # <re.Match object; span=(0, 0), match=''> (matches zero 'a's)
re.search(r'e*', phrase)  # <re.Match object; span=(0, 0), match=''> (matches zero 'e's)

# plus (+) : match 1 or more repetitions of the preceding character
re.search(r'a+', phrase)  # <re.Match object; span=(15, 16), match='a'>
re.search(r'e+', phrase)  # <re.Match object; span=(1, 2), match='e'>

# question mark (?) : match 0 or 1 repetition of the preceding character
re.search(r'a?', phrase)  # <re.Match object; span=(0, 0), match=''>
re.search(r'e?', phrase)  # <re.Match object; span=(0, 1), match='H'>

# curly braces ({m,n}) : match between m and n repetitions of the preceding character
re.search(r'\d{1,2}', phrase)  # <re.Match object; span=(27, 29), match='25'> (matches one or two digits)
re.search(r'\w{4,}', phrase)   # <re.Match object; span=(0, 5), match='Hello'> (matches four or more word characters)

# square brackets ([]) : match any one of the enclosed characters
re.search(r'[aeiou]', phrase)  # <re.Match object; span=(1, 2), match='e'> (matches any one vowel)
re.search(r'[0-9]', phrase)    # <re.Match object; span=(27, 28), match='2'> (matches any one digit)

# pipe (|) : match either the pattern before or the pattern after the pipe
re.search(r'Wesley|engineer', phrase)  # <re.Match object; span=(18, 24), match='Wesley'>
re.search(r'John|engineer', phrase)    # <re.Match object; span=(58, 67), match='engineer.'>

# backslash (\) : escape special characters or denote special sequences
re.search(r'\.', phrase)  # <re.Match object; span=(24, 25), match='.'> (matches the period character)
re.search(r'\d', phrase)  # <re.Match object; span=(27, 28), match='2'> (matches any digit)
re.search(r'\w', phrase)  # <re.Match object; span=(0, 1), match='H'> (matches any word character)
re.search(r'\s', phrase)  # <re.Match object; span=(5, 6), match=' '> (matches any whitespace character)

# grouping with parentheses (()) : group parts of a pattern
match = re.search(r'(\d+)', phrase)  # <re.Match object; span=(27, 29), match='25'>
if match:
    print(match.group(1))  # 25 (extracts the matched number)
