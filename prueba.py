from datetime import datetime
fecha1 = datetime.strptime("16-01","%d-%m")
fecha2 = datetime.strptime("20-03","%d-%m")
dias = (fecha2-fecha1).days
print(f"el numero de los dias es: {dias} dias")