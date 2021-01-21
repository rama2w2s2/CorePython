'''
index(value, start=0, stop=9223372036854775807, /) method of builtins.tuple instance
    Return first index of value.    
    Raises ValueError if the value is not present.
'''


# Example 1: Index with value as the argument
countries = ['India', 'France', 'India', 'Russia', 'Australia']
print(countries.index('France'))            # 1
print(countries.index('India'))             # 0
print(countries.index('China'))             # ValueError: 'China' is not in list


# Example 2: Index with value, start as arguments
print(countries.index('India', 1))          # 2      
print(countries.index('India', 3))          # ValueError: 'India' is not in list


# Example 3: Index with value, start, stop as arguments
print(countries.index('Russia', 1, 4))      # 3     
print(countries.index('France', 2, 4))      # ValueError: 'France' is not in list
print(countries.index('Australia', 3, 5))   # 4
print(countries.index('Australia', 3, 4))   # ValueError: 'Australia' is not in list

