# Zara Stok Takip Botu

Bu Python betiği, Selenium kullanarak Zara web sitesindeki belirli bir ürünün stok durumunu kontrol eder ve hedef beden stokta olduğunda Telegram üzerinden bildirim gönderir.

---

## Özellikler

- Belirli ürünün belirli bedeninin stokta olup olmadığını kontrol eder.
- Telegram bot aracılığıyla anlık bildirim gönderir.
- Otomatik olarak belirli aralıklarla (10 dakika) stok kontrolü yapar.
- Çerez onayı popup’ını otomatik kapatır.

---

## Gereksinimler

- Python 3.x
- Selenium
- Microsoft Edge WebDriver
- requests kütüphanesi

---

## Kurulum

1. Python ortamınızı hazırlayın (tercihen virtualenv kullanın):

```bash
python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate
Gerekli paketleri yükleyin:

pip install selenium requests
Microsoft Edge WebDriver'ı bilgisayarınıza indirin ve PATH’e ekleyin:

Microsoft Edge WebDriver İndir

Kullanım
Proje klasöründe .env dosyası oluşturun ve içine aşağıdaki bilgileri yazın:

BOT_TOKEN=TelegramBotTokenBuraya
CHAT_ID=TelegramChatIDBuraya
main.py dosyasındaki url ve hedef_beden değişkenlerini kontrol etmek istediğiniz ürün ve bedenle güncelleyin.

Botu çalıştırın:

python main.py
