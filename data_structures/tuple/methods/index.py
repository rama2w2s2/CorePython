''' 
index(value, start=0, stop=9223372036854775807, /) 
- Method of builtins.tuple instance
- Return first index of value.    
- Raises ValueError if the value is not present.

Arguments:
value - Mandatory - Positional-only and cannot be passed by keyword.
start - Optional  - Positional-only and cannot be passed by keyword.
stop  - Optional  - Positional-only and cannot be passed by keyword.
'''


# Case 1: index(value)
countries = ['India', 'France', 'India', 'Russia', 'Australia']
print(countries.index('France'))            # 1
print(countries.index('India'))             # 0
print(countries.index('China'))             # ValueError: 'China' is not in list


# Case 2: index(value, start)
countries = ['India', 'France', 'India', 'Russia', 'Australia']
print(countries.index('India', 1))          # 2      
print(countries.index('India', 3))          # ValueError: 'India' is not in list


# Case 3: index(value, start, stop)
countries = ['India', 'France', 'India', 'Russia', 'Australia']
print(countries.index('Russia', 1, 4))      # 3     
print(countries.index('Australia', 3, 5))   # 4
print(countries.index('France', 2, 4))      # ValueError: 'France' is not in list


