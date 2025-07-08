from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import time
import requests

# ———— 1) Ortam değişkenlerini yükle ————
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# ———— 2) Ayarlar ————
url = "https://www.zara.com/tr/tr/godeli-halter-yaka-kisa-elbise-p03067350.html"
hedef_beden = "XL"

# ———— 3) Telegram mesaj gönderme ————
def telegram_gonder(mesaj):
    api_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": mesaj}
    resp = requests.post(api_url, data=data)
    if resp.status_code == 200:
        print("→ Telegram’a mesaj gönderildi.")
    else:
        print("→ Telegram hatası:", resp.text)

# ———— 4) Stok kontrol fonksiyonu ————
def stok_kontrol_et():
    options = Options()
    # options.add_argument("--headless")  # İstersen gizli modda çalıştır

    driver = webdriver.Edge(options=options)

    try:
        print("→ Sayfa açılıyor...")
        driver.get(url)
        time.sleep(5)

        # — Sayfanın HTML'sini kaydet (debug için) —
        with open("sayfa.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)

        # — Çerez popup'ı kapat —
        try:
            cerez_kapat = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "ot-sdk-close"))
            )
            cerez_kapat.click()
            print("→ Çerez popup’ı kapatıldı.")
        except:
            print("→ Çerez popup’ı bulunamadı veya zaten kapalı.")

        # — EKLE butonuna tıkla —
        ekle_buton = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.product-detail-cart-buttons__button"))
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", ekle_buton)
        time.sleep(1)
        ekle_buton.click()
        print("→ 'EKLE' butonuna tıklandı, bedenler açılıyor...")

        # — Beden listesini bekle —
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "size-selector-sizes-size__label"))
        )

        bedenler = driver.find_elements(By.CLASS_NAME, "size-selector-sizes-size__label")
        print(f"Çekilen beden sayısı: {len(bedenler)}")

        for beden in bedenler:
            ad = beden.text.strip()
            classlar = beden.get_attribute("class")
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Beden: {ad}, Class’lar: {classlar}")

            if ad == hedef_beden:
                if "disabled" not in classlar:
                    mesaj = f"🎉 {hedef_beden} BEDEN stokta! Satın al:\n{url}"
                    telegram_gonder(mesaj)
                else:
                    print(f"× {hedef_beden} stokta değil.")
                break
        else:
            print(f"× {hedef_beden} beden listede bulunamadı.")

    finally:
        driver.quit()

# ———— 5) Döngü ————
if __name__ == "__main__":
    while True:
        stok_kontrol_et()
        print("10 dakika bekleniyor...\n")
        time.sleep(600)
