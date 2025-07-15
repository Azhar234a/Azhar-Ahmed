import requests   # 1) استيراد المكتبة أولاً

url = "https://api.github.com/repos/psf/requests"
     # 2) تعريف المتغيّر قبل استعماله
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)   # 3) استخدام url بعد تعريفه
print(response.status_code)
print(response.text[:200])   # طباعة أول 200 حرف من المحتوى
