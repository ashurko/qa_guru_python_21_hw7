import os
import zipfile
from pathlib import Path

BASE_DIR = Path(__file__).parent
TMP_DIR = BASE_DIR / "tmp"
ARCHIVE_PATH = BASE_DIR / "archive.zip"

def create_archive():
    with zipfile.ZipFile(ARCHIVE_PATH, 'w') as zf:
        for file in ('sample_csv.csv', 'sample_xlsx.xlsx', 'sample_pdf.pdf'):
            add_file = TMP_DIR / file
            zf.write(add_file, os.path.basename(add_file))
        print("Архив создан!")

create_archive()