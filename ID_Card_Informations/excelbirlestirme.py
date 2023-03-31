import pandas as pd
import glob
import os

def excel_combine():
    # Tüm Excel dosyalarını al
    excel_files = glob.glob("*.xlsx")  # Dosya uzantısı .xlsx ise "*.xlsx" yazabilirsiniz.
    # Excel dosyalarını birleştir
    combined_data = pd.concat([pd.read_excel(f) for f in excel_files])
    # Excel dosyalarını sil	
    for f in excel_files:
        os.remove(f)
    # Birleştirilmiş verileri bir Excel dosyasına yaz
    combined_data.to_excel("combined_data.xlsx", index=False)

excel_combine()
