''' 
count(value, /) 
- Method of builtins.tuple instance
- Return number of occurrences of value.

Arguments:
value - Mandatory - Positional-only and cannot be passed by keyword.
'''


# Case 1: count(value)
countries = ['India', 'France', 'India', 'Russia']
print(countries.count('India'))         # 2
print(countries.count('France'))        # 1
print(countries.count('China'))         # 0


# Case 2: count()
countries = ['India', 'France', 'India', 'Russia']
print(countries.count())                # TypeError: count() takes exactly one argument (0 given)


# Case 3: count(value)
countries = ['India', 'France', 'India', 'Russia']
print(countries.count(value='India'))   # TypeError: count() takes no keyword arguments
