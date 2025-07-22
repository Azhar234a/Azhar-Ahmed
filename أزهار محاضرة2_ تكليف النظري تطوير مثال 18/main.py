# weather_forecast_collector.py
import requests
from datetime import datetime, timedelta
import pandas as pd
from typing import List, Dict

# 1. إعدادات
API_KEY = "378ee5ddcd5ef8de464c30c0e6ad2f35"
CITIES = ["Sanaa", "London", "Tokyo", "Paris", "New York",
          "Dubai", "Berlin", "Cairo", "Moscow", "Sydney"]

BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"

# 2. جلب بيانات الطقس
def fetch_weather_forecast(city: str) -> List[Dict]:
    try:
        params = {"q": city, "appid": API_KEY, "units": "metric"}
        res = requests.get(BASE_URL, params=params, timeout=10)
        res.raise_for_status()
        data = res.json()

        forecasts = []
        for entry in data["list"]:
            forecasts.append({
                "city": city,
                "datetime": entry["dt_txt"],
                "temp_min": entry["main"]["temp_min"],
                "temp_max": entry["main"]["temp_max"],
                "weather": entry["weather"][0]["main"]
            })
        return forecasts
    except Exception as e:
        print(f"⚠️  فشل جلب بيانات {city}: {e}")
        return []

# 3. جمع البيانات لجميع المدن
all_rows = []
for city in CITIES:
    all_rows.extend(fetch_weather_forecast(city))

# 4. تحويل إلى DataFrame
df = pd.DataFrame(all_rows)

# 5. تنظيف البيانات
df = df.drop_duplicates()
df = df.dropna()

# 6. تنسيق الأعمدة
df["datetime"] = pd.to_datetime(df["datetime"])
df["date"] = df["datetime"].dt.date
df["hour"] = df["datetime"].dt.hour

# 7. تحليل (تطبيق أوامر المحاضرة)
print("✅ عدد الصفوف:", df.shape[0])
print("📄 معلومات DataFrame:")
print(df.info())
print("\n🧪 إحصائيات:")
print(df.describe(include="all"))

# 8. GroupBy: متوسط الحرارة لكل مدينة
city_avg = df.groupby("city")[["temp_min", "temp_max"]].mean().reset_index()
print("\n🌡️ متوسط الحرارة لكل مدينة:\n", city_avg)

# 9. Pivot Table: عدد التوقعات لكل ساعة
pivot_hour = df.pivot_table(index="hour", columns="city", values="weather", aggfunc="count")
print("\n🕒 توزيع التوقعات حسب الساعات:\n", pivot_hour.fillna(0).astype(int))

# 10. حفظ البيانات
df.to_csv("weather_data.csv", index=False)
print("\n📁 تم حفظ البيانات في weather_data.csv")
