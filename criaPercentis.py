import pandas as pd
from zipfile import ZipFile
from pathlib import Path
import datetime as dt
from gpl import download_base_files


def ecmwf_ens_extraction(): # extrai zips do modelo em questão
    zips = [item for item in Path(
        "Downloads/").glob("**/*") if not ("EXT" in item.stem) and item.suffix == ".zip"] # lista zips da pasta
    for item in zips:
        with ZipFile(item) as zp:
            zp.extractall("ENA Files") # extrai todos os zips para a pasta ENA Files


def remove_enaprevs(): # enaprevs não fazem parte do estudo feito nesse script
    enaprevs = [item for item in Path("ENA Files").glob(
        "**/*") if "ENAPREVS" in item.name] # listagem de todos enaprevs da pasta ENA Files
    for item in enaprevs:
        item.unlink() # remoção de cada arquivo


def remove_ensembles(): # ensembles não fazem parte do estudo desse script
    ensembles = [item for item in Path('Downloads').glob(
        "**/*") if "ENSEMBLE" in item.name] # lista ensembles da pasta Downloads
    for item in ensembles:
        item.unlink() # remove arquivo


def import_ena(filePath): # função para otimizar a reutilização de código
    # os dados em formato próprio para BD começa na lina 59
    # decimal define o separador de decimal para evitar dor de cabeça
    # sep define o separador do csv
    df = pd.read_csv(filePath, sep=";", decimal=",", skiprows=59) 
    return df


def get_zips(): # faz o download dos arquivos no pluvia
    dateStr = input("Digite o dia dos arquivos (dd/mm/yyyy)\n") # recebe a data do usuário
    targetDate = dt.datetime.strptime(dateStr, "%d/%m/%Y") # cria objeto de data
    download_base_files(targetDate) # chama a função de download do pluvia


def filter_subs(df): # filtra os dados de interesse
    df2 = df.query('Tipo == "Submercado" & Nome != "SIN" & Data != "MEDIA"') # queremos os dados que não sejam média nem do sistema todo
    columns = ["Data", "Nome", "ENA_MWmes"] # colunas de interesse na ordem apropriada
    df = df2[columns] # filtragem da coluna
    return df


# df = import_ena("ENA Files/ECMWF_ENS-37-2021-Diária-IA+SMAP-ENA.csv")
# filter_subs(df)
# teste de debug
