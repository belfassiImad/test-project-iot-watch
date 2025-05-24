import requests
import pandas as pd
from sklearn.linear_model import LinearRegression
import datetime

#localisation d'agadir
latitude =30.4202
longitude =-9.5982
#choix des jours
end_date = datetime.date.today()
start_date = end_date - datetime.timedelta(days=7)

url = (
    f"https://api.open-meteo.com/v1/forecast"
    f"?latitude={latitude}&longitude={longitude}"
    f"&start_date={start_date}&end_date={end_date}"
    f"&daily=temperature_2m_max&timezone=auto"
)
response = requests.get(url)
data = response.json()

if "daily" not in data:
    raise ValueError("Erreur dans la récupération des données")



temps = data["daily"]["temperature_2m_max"]
jours = list(range(1, len(temps) + 1))

df = pd.DataFrame({
    'day': jours,
    'temperature': temps
})

model = LinearRegression()
model.fit(df[['day']], df['temperature'])

future_days = pd.DataFrame({'day': list(range(8, 15))})
predicted_temps = model.predict(future_days)

for day, temp in zip(range(8, 15), predicted_temps):
    print(f"🌡️ Température prévue pour le jour {day} à Agadir est : {temp:.2f}°C")
