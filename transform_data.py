import datetime

def unix_dh(timestamp_unix):
    data_humana = datetime.datetime.fromtimestamp(timestamp_unix)

    return data_humana.strftime('%d/%m/%Y %H:%M:%S')
#estao 3 horas na frente

def dh_unix(data_humana, formato='%d/%m/%Y %H:%M:%S'):
    data = datetime.datetime.strptime((data_humana + " 21:00:00"), formato)
    timestamp_unix = int(data.timestamp())
    
    return timestamp_unix
