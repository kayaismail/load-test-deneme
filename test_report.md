# N11 Load Test Raporu

## Test Bilgileri
- **Test Tarihi:** 13 Ağustos 2025
- **Test Süresi:** 60 saniye
- **Kullanıcı Sayısı:** 10
- **Spawn Rate:** 2 kullanıcı/saniye
- **Test URL:** https://www.n11.com/arama?q=iphone

## Test Senaryosu
- **GET /arama?q=iphone** - iPhone araması
- **Bekleme Süresi:** 1-3 saniye arası

## Test Sonuçları

### Başarı Oranı
- **Toplam İstek:** 31
- **Başarısız İstek:** 31 (%100)
- **Başarılı İstek:** 0 (%0)

### Yanıt Süreleri
- **Ortalama:** 114ms
- **Minimum:** 60ms
- **Maksimum:** 1250ms
- **Medyan:** 69ms

### İstek Dağılımı
- **Anasayfa (GET /):** 19 istek (100% başarısız)
- **iPhone Arama (GET /arama?q=iphone):** 12 istek (100% başarısız)

### Hata Analizi
- **Hata Kodu:** 403 Forbidden
- **Sebep:** N11 sitesi bot koruması kullanıyor
- **Tüm istekler engellendi**

## Sonuç
N11 sitesi güçlü bot koruması kullanıyor ve tüm otomatik istekleri engelliyor. Load test başarısız oldu çünkü site bot trafiğini tamamen blokluyor.

## Öneriler
1. Farklı bir test sitesi kullanın (httpbin.org, jsonplaceholder.typicode.com)
2. N11'in API endpoint'lerini deneyin (eğer varsa)
3. Daha gelişmiş bot koruması aşma teknikleri kullanın
