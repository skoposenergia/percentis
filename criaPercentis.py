import pandas as pd
from zipfile import ZipFile
from pathlib import Path


def zip_extraction(filePath):
    zips = [file for file in filePath.glob("**/*") if file.suffix == ".zip"]
    with ZipFile(file) as zp:
        zp.extractall("ENA Files")

def remove_enaprevs():
    enaprevs = [item for item in Path("ENA Files").glob("**/*") if "ENAPREVS" in file.name]
    for item in enaprevs:
        item.unlink()