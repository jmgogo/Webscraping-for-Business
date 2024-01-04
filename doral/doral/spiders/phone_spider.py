import scrapy
import re
from typing import Dict, Iterator # Note: list, and set are built-in types in Python 3.9+

# Requirements
'''
1. Spider shall scrap website text.
2. Spider shall find matches with optional country code.
3. Spider shall remove duplicate phone numbers.
4. Spider shall keep at most two phone numbers.
5. Country code not included, Spider shall not match on a string of digits that is longer than 10 characters.
'''

# Trouble URLs
'''
https://www.lacremafoodandgrill.com
http://www.casalindatile.com
http://doral.cyclebar.com/robots.txt
https://www.tripadvisor.com/robots.txt
https://www.tripadvisor.com/Restaurant_Review-g34438-d784249-Reviews-Mondongo_s_Restaurante-Miami_Florida.html
'''

class PhoneNumbersSpider(scrapy.Spider):
    name: str = 'phone_numbers'
    start_urls: list[str] = ['https://www.onebehavior.com/']

    def parse(self, response: scrapy.http.Response) -> list[Dict[str, set[str]]]:
        # Extract content from the webpage
        content: str = ' '.join(response.css('html ::text').getall())  # join elements of text with space

        # Define a regular expression pattern for matching phone numbers
        phone_number_pattern = re.compile(
            r"""
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
        
        # Process Iterator for phone numbers
        phone_list: list[str] = [phone.group(0) for phone in phone_numbers]
        
        # clean phone list
        clean_list: set[str] = set(map(lambda x: re.sub('[-.() ]', '', x), phone_list))
                
        yield {'phone_numbers': clean_list}