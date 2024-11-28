



data = {
    "CompanyName": "Apple", 
    "IndustryType": "Technology", 
    "Strategic_Focus_Areas": "Consumer Electronics, Software, Services, Wearables, Online Services, Cloud Computing, Artificial Intelligence"
    }


import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
gemini_api_key = os.getenv('GOOGLE_API_KEY')
print(gemini_api_key)
genai.configure(api_key = gemini_api_key)
model = genai.GenerativeModel(
    'gemini-1.5-flash-latest',
    generation_config=genai.GenerationConfig(
        temperature=0.1,
    ))

prompt = """
You are an advanced AI strategist tasked with generating innovative use cases for AI and GenAI in the given industry.
The goal is to improve performance, enhance customer satisfaction, and align with the specified strategic focus areas.
Industry Type: {IndustryType}
Strategic Focus Areas: {Strategic_Focus_Areas}
""".format(**data)

response = model.generate_content(prompt)
print(response.text)


# from SageAI.src.agents.research_agent import ResearchAgent

# agent = ResearchAgent()
# print(agent.get_research("Apple"))

