import datetime as dt
from getpass import getpass
from pathlib import Path

from src.functionsPluviaAPI import *

user = input("Usuário: ")
psswd = getpass("Senha: ")

id_maps = []
id_models = []

token = authenticatePluvia(user, psswd)

precipitationDataSources = ["ECMWF_ENS", "ECMWF_ENS_EXT"]
forecastModels = ['IA+SMAP', 'IA+SMAP']

for precipitationDataSource in precipitationDataSources:
    id_maps.append(getIdOfPrecipitationDataSource(precipitationDataSource))

for forecastModel in forecastModels:
    id_models.append(getIdOfForecastModel(forecastModel))

current_day = dt.datetime.today()

forecastdate = current_day.strftime("%d/%m/%Y")
format_directory = current_day.strftime("%Y-%m-%d")

directoryOfDownload = Path('Arquivos/%s' % format_directory)
if not (directoryOfDownload.exists()):
    Path.mkdir(directoryOfDownload)

forecasts = getForecasts(forecastdate, id_maps,
                         id_models, '', '', [current_day.year], [])

for forecast in forecasts:
    # downloadForecast(forecast['prevsId'], dir_download,
    #                  forecast['nome'] + ' - ' + forecast['membro'] + ' - Prevs.zip')
    downloadForecast(forecast['enaId'], directoryOfDownload,
                     forecast['nome'] + ' - ' + forecast['membro'] + '- ENA.zip')
    # downloadForecast(forecast['vnaId'], dir_download, forecast['nome'] + ' - ' + forecast['membro'] + '- VNA.csv')
    # downloadForecast(forecast['strId'], dir_download, forecast['nome'] + ' - ' + forecast['membro'] + '- STR.zip')
