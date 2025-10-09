from datetime import datetime
from pathlib import Path
import pandas as pd

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
    df = clean_expenses_data(input_file)
    if df is None:
        return False
    print('Add a new expense\n-----------------\n')
    try:
        attempts = 0
        parsed_date = None
        while attempts < 3:
            date_time = input('Enter date and time (DD-MM-YYYY HH:MM): ')
            try:
                if not date_time:
                    parsed_date = datetime.now()
                elif ' ' not in date_time:
                    parsed_date = datetime.strptime(date_time, '%d-%m-%Y').replace(hour=datetime.now().hour, minute=datetime.now().minute) 
                else:
                    parsed_date = datetime.strptime(date_time, '%d-%m-%Y %H:%M')
                break
            except ValueError:
                attempts += 1
                print(f"Invalid date format. Please use 'DD-MM-YYYY' or 'DD-MM-YYYY HH:MM'. {attempts} attempts remaining.\n")
        else:
            print("Too many invalid attempts. Exiting the loop.")
            return None        
        category = input('Enter category: ')
        description = input('Enter a short description: ')
        
        attempts = 0
        amount = None
        while attempts < 3:
            amount = input('Enter amount spent: ')
            try:     
                amount = float(amount)
                break
            except ValueError:
                attempts += 1
                print(f"Invalid amount. Please enter a numeric value (e.g. 125.50). {attempts} attempts remaining.\n")
        else:
            print("Too many invalid attempts. Exiting the loop.")
            return None

        # Collecting the users input in a dictionary
        new_expenses = {
            'Date': parsed_date,
            'Category': category,
            'Description': description,
            'Amount': float(amount)
        }
        # Parsing the df['Date] as datetime
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        
        # Adding the users input to the dataframe
        df = pd.concat([df, pd.DataFrame([new_expenses])], ignore_index=True)
        
        
        df.to_csv(output_file, index=False)
        print(f'Expenses added: [{parsed_date}, {category}, {description}, {amount}]')
        print(f'Data appended to {output_file}')
        print(f'Total records now: {len(df)}')
        print('\nSummary by category:')
        return df
    except ValueError:
        print('Unable to add data to the dataframe')
        return None
    except KeyboardInterrupt:
        print('Process interrupted by user')
        return False
      