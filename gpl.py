import datetime as dt
from getpass import getpass
from pathlib import Path

from src.functionsPluviaAPI import *


def download_base_files(downloadDate):
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

    # downloadDate = dt.datetime.today() - dt.timedelta(days=1)

    forecastdate = downloadDate.strftime("%d/%m/%Y")
    format_directory = downloadDate.strftime("%Y-%m-%d")

    directoryOfDownload = Path('Downloads/%s' % format_directory)
    if not (directoryOfDownload.exists()):
        Path.mkdir(directoryOfDownload)

    forecasts = getForecasts(forecastdate, id_maps,
                             id_models, '', 'false', [downloadDate.year], [])

    for forecast in forecasts:
        # downloadForecast(forecast['prevsId'], dir_download,
        #                  forecast['nome'] + ' - ' + forecast['membro'] + ' - Prevs.zip')
        downloadForecast(forecast['enaId'], directoryOfDownload,
                         forecast['nome'] + ' - ' + forecast['membro'] + '- ENA.zip')
        # downloadForecast(forecast['vnaId'], dir_download, forecast['nome'] + ' - ' + forecast['membro'] + '- VNA.csv')
        # downloadForecast(forecast['strId'], dir_download, forecast['nome'] + ' - ' + forecast['membro'] + '- STR.zip')
