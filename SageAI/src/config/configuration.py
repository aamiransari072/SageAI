from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()

class getConfig:
    
    def __init__(self):
        self.google_search_engine = os.getenv('GOOGLE_SEARCH_ENGINE')
        self.search_engine_id = os.getenv('SEARCH_ENGINE_ID')
    
    def get_config(self):
        return {
            'key':self.google_search_engine,
            'cx': self.search_engine_id,
            'num':3
            }
    def getReportdir(self):
        return r"D:\Projects\SageAI\SageAI\src\reports"
    
    def get_prompt(self):
        self.few_shot_prompt = """Extract the following details from the given company description: company_name, industry_type, and strategic_focus_area.

                                EXAMPLE 1:
                                Description: Apple Inc. is a leading technology company based in Cupertino, California. It designs, manufactures, and sells consumer electronics, software, and services. Apple focuses on innovation in mobile technology, computers, wearables, and online services.
                                JSON Response:
                                ```
                                {
                                "CompanyName": "Apple Inc.",
                                "IndustryType": "Technology",
                                "Strategic_Focus_Areas": ["Innovation", "Consumer Electronics", "Software", "Online Services"]
                                }
                                ```

                                EXAMPLE 2:
                                Description: Tesla, Inc. is an American electric vehicle and clean energy company. It designs electric cars, solar panels, and energy storage products. Tesla’s mission is to accelerate the world’s transition to sustainable energy.
                                JSON Response:
                                ```
                                {
                                "CompanyName": "Tesal Inc.",
                                "IndustryType": "Automotive, Clean Energy",
                                "Strategic_Focus_Areas": ["Electric Vehicles", "Sustainable Energy", "Solar Products", "Energy Storage"]
                                }
                                ```

                                EXAMPLE 3:
                                Description: Amazon is a global e-commerce and cloud computing giant, headquartered in Seattle, Washington. Amazon offers a wide range of services including online retail, Amazon Web Services (AWS), and artificial intelligence products.
                                JSON Response:
                                ```
                                {
                                "CompanyName": "Amazon",
                                "IndustryType": "E-commerce, Cloud Computing",
                                "Strategic_Focus_Areas": ["Online Retail", "Cloud Computing", "Artificial Intelligence"]
                                }
                                ```

                                EXAMPLE 4:
                                Description: Microsoft Corporation is a multinational technology company that produces computer software, consumer electronics, and personal computers. Microsoft’s most famous products include the Windows operating system, Office productivity suite, and Azure cloud services.
                                JSON Response:

                                ```
                                {
                                "CompanyName": "Microsoft Corporation",
                                "IndustryType": "Technology",
                                "Strategic_Focus_Areas": ["Software", "Cloud Services", "Artificial Intelligence", "Productivity Tools"]
                                }
                                ```



                                EXAMPLE 5:
                                Description: Google LLC is a multinational technology company specializing in internet services, including search, cloud computing, advertising, and AI technologies. Google is also a major player in hardware products such as smartphones and smart home devices.
                                JSON Response:


                                ```
                                {
                                "CompanyName": "Google LLC",
                                "IndustryType": "Technology",
                                "Strategic_Focus_Areas": ["Search", "Cloud Computing", "Advertising", "Artificial Intelligence", "Smartphones", "Smart Home Devices"]
                                }
                                ```

                                """
        return self.few_shot_prompt
