from datetime import datetime
import pandas as pd
from pathlib import Path

def clean_expenses_data(input_file):
    try:
        if Path(input_file).suffix == '.csv':
            df = pd.read_csv(input_file)
            df = df.drop(columns=['Mode', 'Subcategory', 'Income/Expense', 'Currency'], errors='ignore')
            df = df.rename(columns={'Note':'Description'})
            return df
        else:
            print('Only .csv format is allowed')
            return None
    except Exception as e:
        print(f'Error: {e}')
        return None
    
def add_expenses_data(input_file, output_file):
    try:
        df = clean_expenses_data(input_file)
        if df is None:
            return False
        print('Add a new expense\n-----------------\n')
        date_time = input('Enter date and time (DD-MM-YYYY HH:MM): ')
        if not date_time:
            parsed_date = datetime.now()
        elif ' ' not in date_time:
            parsed_date = datetime.strptime(date_time, '%d-%m-%Y').replace(hour=datetime.now().hour, minute=datetime.now().minute) 
        else:
            parsed_date = datetime.strptime(date_time, '%d-%m-%Y %H:%M')
        category = input('Enter category: ')
        description = input('Enter a short description: ')
        amount = input('Enter amount spent: ')
        # Collecting the users input in a dictionary
        new_expenses = {
            'Date': parsed_date,
            'Category': category,
            'Description': description,
            'Amount': float(amount)
        }
        # Adding the users input to the dataframe
        df = pd.concat([df, pd.DataFrame([new_expenses])], ignore_index=True)
        print(f'Expenses added: [{parsed_date}, {category}, {description}, {amount}]')
        df.to_csv(output_file, index=False)
        print(f'Data appended to {output_file}')
        print(f'Total records now: {len(df)}')
        return df
    except ValueError:
        print('Unable to add data to the dataframe')
        return None
    except KeyboardInterrupt:
        print('Process interrupted by user')
        return False
if __name__ == '__main__':
    output_file = 'expenses_edited.csv'
    input_file = 'expenses.csv'
    add_expenses_data(input_file, output_file)