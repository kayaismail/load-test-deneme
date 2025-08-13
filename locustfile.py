from locust import HttpUser, task, between

class N11LoadTest(HttpUser):
    """N11 Load Test - Sadece iPhone araması"""
    
    wait_time = between(1, 3)  # Her istek arasında 1-3 saniye bekle
    
    def on_start(self):
        """Test başladığında çalışır"""
        # Basit headers
        self.client.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'tr-TR,tr;q=0.9,en;q=0.8'
        })
        print("🔧 Kullanıcı başlatıldı")
    
    @task
    def search_iphone(self):
        """Sadece iPhone araması yapar"""
        try:
            # Sadece iPhone arama URL'sine GET isteği
            with self.client.get("/arama?q=iphone", catch_response=True) as response:
                if response.status_code == 200:
                    response.success()
                    print(f"✅ iPhone araması başarılı - Status: {response.status_code}")
                else:
                    response.failure(f"Search failed: {response.status_code}")
                    print(f"❌ iPhone araması başarısız - Status: {response.status_code}")
                    
        except Exception as e:
            print(f"❌ Test hatası: {e}")
