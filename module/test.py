import requests

# Sizning Advent of Code sessiya cookie'nizni kiriting
session_cookie = "53616c7465645f5fc31851eb9211c820ba3b79d92f352f43fe88171d1cdf01472f7a70046a60cff9c02ae2583b8fa66ff0b0d86694931de8f3bbd40ea07d301b"

# 1-kun kiritmasi uchun URL
input_url = "https://adventofcode.com/2024/day/1/input"

# So'rov yuborish
response = requests.get(input_url, cookies={"session": session_cookie})

# Natijani tekshirish
if response.status_code == 200:
    input_data = response.text
    print("Kiritmalar muvaffaqiyatli yuklandi!")
    print(input_data)
else:
    print(f"Kiritmalarni yuklashda xato: {response.status_code}")
