from datetime import datetime, timedelta

data_atual = datetime.now()
data_futura = data_atual + timedelta(2)
print(data_futura)