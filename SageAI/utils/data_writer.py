import os 
from pathlib import Path


def write_report(report_dir,company_name,data):
    report_dir = Path(report_dir)
    company_name = company_name.replace(" ", "_").replace(":", "_").replace("/", "_").replace(".","_")
    company_name = Path(company_name)
    report_dir.mkdir(parents=True, exist_ok=True)
    final_path = report_dir/f"{company_name}.txt"
    
    with open(final_path,'a') as file:
        file.write(data)
        

