import scrapy
import pandas as pd


class DoralSpider(scrapy.Spider):
    name = "doral_spider"

    def start_requests(self):
        urls = [
            "https://www.cityofdoral.com/businesses/local-discounts/"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # retreive business info...        
        business_name = ...
        industry = ...
        phone = ...
        contact_name = ...
        
        
        row_data = zip(business_name, industry, phone, contact_name)
        
        for item in row_data:
            scraped_info = {
                #key:value
                'Business Name': business_name,
                'Industry': industry,
                'Phone': phone,
                'Contact Name': contact_name
            }
       
                
        # Creating a pandas DataFrame from the list
        # business_df = pd.DataFrame(business_list, columns=['Business'])
        
        # Writing the DataFrame to a CSV file
        # csv_file_path = 'doral_businesses.csv'
        
        # business_df.to_csv(f'doral/data/{csv_file_path}', index=False)
                