import pandas as pd
from zipfile import ZipFile
from pathlib import Path
import datetime as dt
from gpl import download_base_files

def ecmwf_ens_extraction(filePath):
    zips = [file for file in filePath.glob("**/*") if not ("EXT" in file.stem)]
    with ZipFile(file) as zp:
        zp.extractall("ENA Files")

def remove_enaprevs():
    enaprevs = [item for item in Path("ENA Files").glob("**/*") if "ENAPREVS" in item.name]
    for item in enaprevs:
        item.unlink()

def remove_ensemble():
    ensembles = [item for item in Path('Downloads').glob("**/*") if "ENSEMBLE" in item.name]
    for item in ensembles:
        item.unlink()

def import_ena(filePath):
    pass

def get_zips():
    dateStr = input("Digite o dia dos arquivos (dd/mm/yyyy)\n")
    targetDate = dt.datetime.strptime(dateStr, "%d/%m/%Y")
    download_base_files(targetDate)

get_zips()