# N11 Load Test Projesi

Bu proje, N11 e-ticaret sitesi üzerinde Locust kullanarak load test gerçekleştirmek için oluşturulmuştur.

## 📋 Proje Açıklaması

N11 sitesi üzerinde iPhone araması senaryosu ile load test yapılması amaçlanmıştır. Ancak site güçlü bot koruması kullandığı için HTTP istekleri 403 Forbidden hatası ile engellenmektedir.

## 🚀 Kurulum

### Gereksinimler
- Python 3.9+
- pip3

### Adımlar

1. **Projeyi klonlayın:**
```bash
git clone <repo-url>
cd n11Load
```

2. **Bağımlılıkları yükleyin:**
```bash
pip3 install -r requirements.txt
```

## 🧪 Test Çalıştırma

### Web Arayüzü ile
```bash
python3 -m locust -f locustfile.py --host=https://www.n11.com
```
Tarayıcınızda `http://localhost:8089` adresine gidin.

### Headless Mod
```bash
python3 -m locust -f locustfile.py --host=https://www.n11.com --users=10 --spawn-rate=2 --run-time=60s --headless
```

## 📊 Test Sonuçları

### Son Test Sonuçları (13 Ağustos 2025)
- **Toplam İstek:** 31
- **Başarısız İstek:** 31 (%100)
- **Başarılı İstek:** 0 (%0)
- **Hata Kodu:** 403 Forbidden

### Detaylı Rapor
`test_report.md` dosyasında detaylı test raporu bulunmaktadır.

## 📁 Proje Yapısı

```
n11Load/
├── locustfile.py          # Ana test dosyası
├── requirements.txt       # Python bağımlılıkları
├── test_report.md        # Test raporu
├── README.md             # Bu dosya
└── .gitignore           # Git ignore dosyası
```

## 🔧 Test Senaryosu

### Mevcut Senaryo
- **URL:** `https://www.n11.com/arama?q=iphone`
- **Metod:** GET
- **Bekleme Süresi:** 1-3 saniye
- **Kullanıcı Sayısı:** 10 (ayarlanabilir)

### Test Akışı
1. Kullanıcı başlatılır
2. iPhone araması yapılır
3. Sonuçlar loglanır
4. Bekleme süresi
5. Tekrar

## ❌ Bilinen Sorunlar

### Bot Koruması
N11 sitesi güçlü bot koruması kullanmaktadır:
- Tüm HTTP istekleri 403 Forbidden ile engellenir
- User-Agent spoofing yeterli değil
- Cookie ve header manipülasyonu başarısız

### Çözüm Önerileri
1. **Farklı Test Sitesi:** httpbin.org, jsonplaceholder.typicode.com
2. **API Endpoint'leri:** N11'in resmi API'lerini kullanın
3. **Selenium:** Gerçek browser otomasyonu (bot korumasını aşar)

## 📈 Performans Metrikleri

### Yanıt Süreleri
- **Ortalama:** 114ms
- **Minimum:** 60ms
- **Maksimum:** 1250ms
- **Medyan:** 69ms

### İstek Dağılımı
- **Anasayfa (GET /):** 19 istek
- **iPhone Arama (GET /arama?q=iphone):** 12 istek

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Commit yapın (`git commit -m 'Add amazing feature'`)
4. Push yapın (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## 📞 İletişim

Proje ile ilgili sorularınız için issue açabilirsiniz.

---

**Not:** Bu proje eğitim amaçlıdır. Gerçek sistemlerde load test yapmadan önce gerekli izinleri alın.
