import os 
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'SageAI'

list_of_files = [
    f'{project_name}/__init__.py',
    f'{project_name}/src/__init__.py',
    f'{project_name}/src/main.py',
    f'{project_name}/src/agents/__init__.py',
    f'{project_name}/src/agents/research_agent.py',
    f'{project_name}/src/agents/use_case_agent.py',
    f'{project_name}/src/agents/resource_agent.py',
    f'{project_name}/src/agents/proposal_agent.py',
    f'{project_name}/utils/__init__.py',
    f'{project_name}/utils/data_fetcher.py',
    f'{project_name}/utils/web_scrapper.py',
    f'{project_name}/utils/logger.py',
    f'{project_name}/src/data/raw',
    f'{project_name}/src/data/processed',
    f'{project_name}/src/reports/retail_ai_purposal.md',
    f'{project_name}/src/demo/app.py',
    f'{project_name}/src/demo/assets',
    f'{project_name}/src/test/test_research_agent.py',
    f'{project_name}/src/test/test_use_case_agent.py',
    f'{project_name}/src/test/test_resource_agent.py',
    f'{project_name}/src/test/test_proposal_agent.py',
    f'{project_name}/src/docs',
    f'{project_name}/src/config/configuration.py',
    'requirements.txt',
    'Dockerfile',
    'setup.py',
    '.dockerignore'
]


for filepath in list_of_files:
    filepath = Path(filepath)

    filedir , filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f'Creating Directory: {filedir} for file: {filename}')
    

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f'Creating empty file: {filepath}')
        
    else:
        logging.info(f"{filename} is already exists")

