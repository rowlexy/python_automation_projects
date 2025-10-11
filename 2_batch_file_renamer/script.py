import pypdf as pdf
from pathlib import Path
import os

self_bill_dir = Path('self_bill')
def replicate_invoice():
    for inv in self_bill_dir.glob('*.pdf'):
        reader = pdf.PdfReader(inv)
        for i in range(20):
            # replicating the existing invoice * 20 
            writer = pdf.PdfWriter()
            for page in reader.pages:
                writer.add_page(page)
                file_name = self_bill_dir/f'{inv.stem}_{i+1}.pdf'
                with open(file_name, 'wb') as file:
                    writer.write(file)
                print(f'{file_name.name} successfully added to {self_bill_dir}')


def rename_invoices(log_file):
    for file in self_bill_dir.iterdir():
        if file.is_file() and file.suffix == '.pdf':
            file_name = file.stem.split('_')
            file_name.pop(0)
            new_name = 'Invoice_' + '_'.join(file_name) + file.suffix
            new_path =  self_bill_dir/new_name
            file.rename(new_path)
            with open(log_file, 'a') as log:
                log.write(f'Old: {file.name} -> New: {new_path.name}\n')
            print(f'Details saved in {log_file} ')
        else:
            print('File does not exist')

def delete_invoices():
    for file in self_bill_dir.glob('*.pdf'):
        os.remove(file)
        
if __name__ == '__main__':
    log_file = 'log_details.txt'
    replicate_invoice()
    rename_invoices(log_file)