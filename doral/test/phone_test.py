import re
from typing import TypedDict, Iterator # Note: list, and set are built-in types in Python 3.9+

content = '''
    b0305-2047034
    +11231231233000
    +11231231233
    fdsf 123.456.7890
    '''
    
# Create typed dictionary class for business info
class BusinessDict(TypedDict):
    business_name: str
    industry: str
    offer: str
    website: str
    phone: set[str]
    
# initialize business info
business: BusinessDict = dict()

print(business)

def get_business_info(business: BusinessDict, content: str) -> BusinessDict:
    
    business['business_name'] = 'mcdonalds'
    business['industry'] = 'food'
    business['offer'] = 'delivery'
    business['website'] = 'mcdonalds.com'
    business['phone'] = parse_phone(content)
    
    return business

def parse_phone(content):
    
    # Define a regular expression pattern for matching phone numbers
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
    phone_numbers: Iterator[re.Match[str]] = phone_number_pattern.finditer(content)
    
    # Process the extracted phone numbers
    phone_list: list[str] = [phone.group(0) for phone in phone_numbers]
    
    # clean phone list
    clean_list: set[str] = set(map(lambda x: re.sub('(\+0?1[\s.-]?)|[-.() ]', '', x), phone_list))
    return clean_list
        
business_info = get_business_info(business, content)

print(business_info)
