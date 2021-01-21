import pandas as pd
from zipfile import ZipFile


def zip_extraction(filePath):
    zips = [file for file in filePath.glob("**/*") if file.suffix == ".zip"]
    with ZipFile(file) as zp:
        zp.extractall()

