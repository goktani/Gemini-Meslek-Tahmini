import google.generativeai as genai
import os

# Google Gemini API Anahtarını Buraya Ekleyin
GEMINI_API_KEY = "senin_api_anahtarin"

# API'yi yapılandır
genai.configure(api_key=GEMINI_API_KEY)

def meslek_oner(cumle):
    model = genai.GenerativeModel("gemini-pro")

    prompt = f"""
    Kullanıcı kendini şöyle tanıtıyor: "{cumle}".
    Bu kişiye uygun birkaç meslek öner ancak açıklamaları kısa ve öz olsun.
    """

    response = model.generate_content(prompt)
    return response.text

# Kullanıcıdan giriş al
if __name__ == "__main__":
    kullanici_cumlesi = input("Kendini birkaç kelimeyle tanıt: ")
    print("\nÖnerilen Meslekler:")
    print(meslek_oner(kullanici_cumlesi))
