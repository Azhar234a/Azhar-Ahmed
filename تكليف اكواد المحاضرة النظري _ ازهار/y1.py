import requests, sys

API_KEY = "378ee5ddcd5ef8de464c30c0e6ad2f35"
city = "Sanaa,ye"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ar"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()          # يطلق استثناء لو HTTP code ليس 200
    data = response.json()

    # هل الخادم أرجع كود خطأ داخل JSON نفسه؟
    if str(data.get("cod")) != "200":    # بعض الأحيان يكون 'cod' نصًا
        msg = data.get("message", "No details")
        raise ValueError(f"OpenWeatherMap error: {msg}")

    temp = data["main"]["temp"]
    print(f"درجة الحرارة في {city}: {temp}°C")

except requests.exceptions.HTTPError as e:
    print("طلب HTTP فشل:", e)
except requests.exceptions.ConnectionError:
    print("تعذّر الاتصال بالإنترنت أو بالخادم")
except ValueError as e:
    print(e)   # رسائل الخطأ التي أرسلها الخادم
except Exception as e:
    print("حدث خطأ غير متوقّع:", e)
