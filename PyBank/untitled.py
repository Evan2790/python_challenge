from pathlib import Path
import csv

budget_data_path = Path('budget_data.csv')
with open(budget_data_path, 'r') as budget_data: 
    text = budget_data.read()
    budget_data = text
    print(budget_data)
    
