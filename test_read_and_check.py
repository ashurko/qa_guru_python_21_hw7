import csv
import io
import zipfile
from io import TextIOWrapper
from pathlib import Path
from openpyxl import load_workbook
from pypdf import PdfReader

BASE_DIR = Path(__file__).parent
ARCHIVE_PATH = BASE_DIR / "archive.zip"

with zipfile.ZipFile(ARCHIVE_PATH) as zip_file:
    print(zip_file.namelist())


def test_csv():
    with zipfile.ZipFile(ARCHIVE_PATH) as zip_file:
        with zip_file.open('sample_csv.csv') as csv_file:
            csvreader = list(csv.reader(TextIOWrapper(csv_file, 'utf-8-sig')))
            first_row = csvreader[0]
            print("Первая строка:", first_row)
            assert first_row == ['Здесь тестовый текст csv']
            print("CSV проверен")
test_csv()

def test_xlsx():
    with zipfile.ZipFile(ARCHIVE_PATH) as zip_file:
        with zip_file.open('sample_xlsx.xlsx') as xlsx_file:
            in_memory_xlsx = io.BytesIO(xlsx_file.read())
            workbook = load_workbook(in_memory_xlsx)
            sheet = workbook.active
            cell_value = sheet['A1'].value
            print("Значение в ячейке A1:", cell_value)
            assert cell_value == "Здесь тестовый текст xlsx"
            print("XLSX проверен")
test_xlsx()

def test_pdf():
    with zipfile.ZipFile(ARCHIVE_PATH) as zip_file:
        with zip_file.open('sample_pdf.pdf') as pdf_file:
            reader = PdfReader(pdf_file)
            text = reader.pages[0].extract_text()
            print(text)
            assert "Здесь  тестовый  текст  pdf  " in text
            print("PDF проверен")
test_pdf()