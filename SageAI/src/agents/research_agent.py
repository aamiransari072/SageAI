from SageAI.utils.data_fetcher import get_data 
from SageAI.utils.data_fetcher import process_data
from SageAI.utils.data_writer import write_report
from SageAI.src.config.configuration import getConfig
import google.generativeai as genai
from dotenv import load_dotenv
import os
from pathlib import Path

import typing_extensions as typing
# load_dotenv()
# gemini_api_key = os.getenv('GOOGLE_API_KEY')
# config = getConfig()
# report_dir = Path(config.getReportdir())
# genai.configure(api_key=gemini_api_key)



class CompanyDetail(typing.TypedDict):
    CompanyName:str
    IndustryType:str
    Strategic_Focus_Areas:str


# model = genai.GenerativeModel(
#     'gemini-1.5-flash-latest',
#     generation_config=genai.GenerationConfig(
#         temperature=0.1,
#         top_p=1,
#         max_output_tokens=250,
#         response_mime_type="application/json",
#         response_schema=CompanyDetail,
#     ))

# few_shot_prompt = """Extract the following details from the given company description: company_name, industry_type, and strategic_focus_area.

# EXAMPLE 1:
# Description: Apple Inc. is a leading technology company based in Cupertino, California. It designs, manufactures, and sells consumer electronics, software, and services. Apple focuses on innovation in mobile technology, computers, wearables, and online services.
# JSON Response:
# ```
# {
# "CompanyName": "Apple Inc.",
# "IndustryType": "Technology",
# "Strategic_Focus_Areas": ["Innovation", "Consumer Electronics", "Software", "Online Services"]
# }
# ```

# EXAMPLE 2:
# Description: Tesla, Inc. is an American electric vehicle and clean energy company. It designs electric cars, solar panels, and energy storage products. Tesla’s mission is to accelerate the world’s transition to sustainable energy.
# JSON Response:
# ```
# {
# "CompanyName": "Tesal Inc.",
# "IndustryType": "Automotive, Clean Energy",
# "Strategic_Focus_Areas": ["Electric Vehicles", "Sustainable Energy", "Solar Products", "Energy Storage"]
# }
# ```

# EXAMPLE 3:
# Description: Amazon is a global e-commerce and cloud computing giant, headquartered in Seattle, Washington. Amazon offers a wide range of services including online retail, Amazon Web Services (AWS), and artificial intelligence products.
# JSON Response:
# ```
# {
# "CompanyName": "Amazon",
# "IndustryType": "E-commerce, Cloud Computing",
# "Strategic_Focus_Areas": ["Online Retail", "Cloud Computing", "Artificial Intelligence"]
# }
# ```

# EXAMPLE 4:
# Description: Microsoft Corporation is a multinational technology company that produces computer software, consumer electronics, and personal computers. Microsoft’s most famous products include the Windows operating system, Office productivity suite, and Azure cloud services.
# JSON Response:

# ```
# {
# "CompanyName": "Microsoft Corporation",
# "IndustryType": "Technology",
# "Strategic_Focus_Areas": ["Software", "Cloud Services", "Artificial Intelligence", "Productivity Tools"]
# }
# ```



# EXAMPLE 5:
# Description: Google LLC is a multinational technology company specializing in internet services, including search, cloud computing, advertising, and AI technologies. Google is also a major player in hardware products such as smartphones and smart home devices.
# JSON Response:


# ```
# {
# "CompanyName": "Google LLC",
# "IndustryType": "Technology",
# "Strategic_Focus_Areas": [Search", "Cloud Computing", "Advertising", "Artificial Intelligence", "Smartphones", "Smart Home Devices"]
# }
# ```

# """
# query = 'Apple'
# data = get_data(query)

# data = process_data(data)
# info = ""
# for d in data:
#     info += d

# # final_prompt  = few_shot_prompt.format(query=data)
# # print(final_prompt)
# response = model.generate_content([few_shot_prompt,info])
# research_data = response.text


# write_report(report_dir,query,research_data)


class ResearchAgent:
    def __init__(self):
        self.gemini_api_key_ = os.getenv('GOOGLE_API_KEY')
        self.company_detail = CompanyDetail
        self.config = getConfig()
        self.few_shot_prompt = self.config.get_prompt()
        self.model = genai.GenerativeModel(
            'gemini-1.5-flash-latest',
            generation_config=genai.GenerationConfig(
                temperature=0.1,
                top_p=1,
                max_output_tokens=250,
                response_mime_type="application/json",
                response_schema=self.company_detail,
            ))
    
    def get_research(self,query):
        self.data = get_data(query)
        self.preprocess_data = process_data(self.data)
        result = self.model.generate_content([self.few_shot_prompt,self.preprocess_data])
        return result.text
    



    














