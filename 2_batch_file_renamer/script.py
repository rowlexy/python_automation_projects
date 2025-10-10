import pypdf as pdf
from pathlib import Path

self_bill_dir = Path('self_bill')
def replicate_invoice():
    for inv in self_bill_dir.glob('*.pdf'):
        reader = pdf.PdfReader(inv)
        for i in range(100):
            writer = pdf.PdfWriter()
            for page in reader.pages:
                writer.add_page(page)
                file_name = self_bill_dir/f'{inv.stem}_{i+1}.pdf'
                with open(file_name, 'wb') as file:
                    writer.write(file)
                print(f'{file_name.name} successfully added to {self_bill_dir}')


def rename_invoices():
    for file in self_bill_dir.iterdir():
        if file.is_file() and file.suffix == '.pdf':
            file_name = file.stem.split('_')
            file_name.pop(0)
            new_name = 'Invoice_' + '_'.join(file_name) + file.suffix
            new_path =  self_bill_dir/new_name
            file.rename(new_path)
        else:
            print('File does not exist')
rename_invoices()