import pandas as pd
from zipfile import ZipFile
from pathlib import Path
import datetime as dt
from gpl import download_base_files


def ecmwf_ens_extraction():
    zips = [item for item in Path(
        "Downloads/").glob("**/*") if not ("EXT" in item.stem) and item.suffix == ".zip"]
    for item in zips:
        with ZipFile(item) as zp:
            zp.extractall("ENA Files")


def remove_enaprevs():
    enaprevs = [item for item in Path("ENA Files").glob(
        "**/*") if "ENAPREVS" in item.name]
    for item in enaprevs:
        item.unlink()


def remove_ensembles():
    ensembles = [item for item in Path('Downloads').glob(
        "**/*") if "ENSEMBLE" in item.name]
    for item in ensembles:
        item.unlink()


def import_ena(filePath):
    df = pd.read_csv(filePath, sep=";", decimal=",", skiprows=59)
    return df


def get_zips():
    dateStr = input("Digite o dia dos arquivos (dd/mm/yyyy)\n")
    targetDate = dt.datetime.strptime(dateStr, "%d/%m/%Y")
    download_base_files(targetDate)


def filter_subs(df):
    pass
