from datetime import datetime
from helper import clean_expenses_data
from helper import add_expenses_data
import argparse  
import pandas as pd

def data_summary(input_file):
    df = clean_expenses_data(input_file)
    if df is None or df.empty:
        print('No data found or invalid file.')
        return
    # converting date column to datetime format
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    # Drop rows with invalid or missing dates
    df = df.dropna(subset=['Date'])
    # Summarize by category
    summary = (df.groupby('Category')['Amount'].sum())
    # Total monthly expenses
    monthly_expenses = df[df['Date'].dt.month == datetime.now().month]['Amount'].sum().round(2)
    print(f'Summary by category:\n{summary}')
    print(f'\nTotal monthly expenses {monthly_expenses:.2f}')
# adding arguments for cleaner function and separation of functions
def get_arguments():
    parser = argparse.ArgumentParser(description='Expense Tracker CLI')
    parser.add_argument('--add', action='store_true', help='Add a new expense')
    parser.add_argument('--summary', action='store_true', help='Show expense summary')
    return parser.parse_args()
    
if __name__ == '__main__':
    arg = get_arguments()
    output_file = 'expenses_edited.csv'
    input_file = 'expenses.csv'
    if arg.add:
        add_expenses_data(input_file, output_file)
    elif arg.summary:
        data_summary(input_file)
    else:
        print('To run script use python script.py --add to add expenses or python script.py --summary for summary of expenses')
        