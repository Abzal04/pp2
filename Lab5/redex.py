####### ex1
import re
def match_pattern(string):
    pattern = r'ab*'
    if re.fullmatch(pattern, string):
        return True
    else:
        return False
tests = ["a", "ab", "abb", "abbb", "ac", "b", "bb"]
for testt in tests:
    if match_pattern(tests):
        print(f"'{testt}' matches")
    else:
        print(f"'{testt}' doesnt match ")

#33333 ex2
import re

def match_pattern(string):
    pattern = r'ab{2,3}'
    if re.fullmatch(pattern, string):
        return True
    else:
        return False
tests = ["a", "ab", "abb", "abbb", "ac", "b", "bb"]
for testt in tests:
    if match_pattern(tests):
        print(f"'{testt}' matches")
    else:
        print(f"'{testt}' doesnt match ")

###### ex3
import re

def find_sequences(text):
    pattern = r'[a-z]+_[a-z]+'
    sequences = re.findall(pattern, text)

text = "HERE_IS_EXAMPLE"
result = find_sequences(text)
print("Sequences found:")
for sequence in result:
    print(sequence)

###### ex4
import re

def find_sequences(text):
    pattern = r'[A-Z][a-z]+'
    sequences = re.findall(pattern, text)
    return sequences
text = "London Is The Capital"
result = find_sequences(text)
for sequence in result:
    print(sequence)

###### ex5
import re
def match_pattern(string):
    pattern = r'a.*b$'
    if re.match(pattern, string):
        return True
    else:
        return False
tests = ["acb", "azb", "abb", "ab", "a123b", "abc"]
for test in tests:
    if match_pattern(test):
        print(f"'{test}' matches ")
    else:
        print(f"'{test}' does not match ")

####### ex6
import re
def replace_with_colon(text):
    pattern = r'[ ,.]'
    replaced_text = re.sub(pattern, ':', text)
    return replaced_text
text = "I. hate, frogs"
result = replace_with_colon(text)
print(result)

######## ex7
import re
def snake_to_camel(snake_case_string):
    words = snake_case_string.split('_')
    camel_case_words = [words[0].lower()] + [word.capitalize() for word in words[1:]]
    camel_case_string = ''.join(camel_case_words)
    return camel_case_string
snake_case_string = "snake_case_example"
camel_case_string = snake_to_camel(snake_case_string)
print("Camel case string:", camel_case_string)


####### ex8
import re

def split_at_uppercase(string):
    split_strings = re.findall('[A-Z][^A-Z]*', string)
    return split_strings
a = "LondonLondonLondon"
result = split_at_uppercase(a)
print(result)

####### ex9
import re

def insert_spaces(string):
    between = re.sub(r'([a-zA-Z])', r'\1 \2', string)
    return between
a = "LnLnLn"
result = insert_spaces(a)
print(result)

######## ex10
import re
def camel_to_snake(camel_case):
    snake_case = ''
    for i, char in enumerate(camel_case):
        if i != 0 and char.isupper():
            snake_case += '_'
        snake_case+= char.lower()
    return snake_case
camel = "LnLnLn"
snake = camel_to_snake(camel)
print(snake)





