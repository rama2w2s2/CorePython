'''
count(value, /) method of builtins.tuple instance
    Return number of occurrences of value.
'''


# Example 1: count with value as the argument
countries = ['India', 'France', 'India', 'Russia', 'Australia']
print(countries.count('India'))         # 2
print(countries.count('Australia'))     # 1
print(countries.count('China'))         # 0


# Example 2: count with no argument
countries = ['India', 'France', 'India', 'Russia', 'Australia']
print(countries.count())
'''TypeError: count() takes exactly one argument (0 given)'''
