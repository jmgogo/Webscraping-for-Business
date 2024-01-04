import re

# Initalize list of strings
list_of_strings = ['dog0000000000dog', 'cat000.000.0000cat', 'dog2+01.000.000.0000', 'cat2cat +01-000-000-0000', 'dog3000000000', 'cat3',]

# Join list of strings with a space between each
one_big_string = ' '.join(list_of_strings)

# Print for confirmation
print(one_big_string)

# compile phone number pattern
phone_number_pattern = re.compile(r"""
            (?<![\d.])         # negative lookbehind to ensure no digits or decimals before
            (\+0?1[\s.-]?)?    # optional country code
            \(?\d{3}\)?[\s.-]? # area code
            \d{3}[\s.-]?       # 3 digit telephone prefix
            \d{4}              # 4 digit line number
            (?![\d.])          # negative lookahead to ensure no digits or decimals after
            """
        , re.X)
        
# Find all matches of the pattern in the text content
phone_numbers = phone_number_pattern.finditer(one_big_string)
phone_list = [phone.group(0) for phone in phone_numbers]
print(phone_list)