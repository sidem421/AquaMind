# --- 1. GÜNLÜK SENARYOLAR (SAHNELER) ---
# water: Harcanan su miktarı (Litre)
# money: Seçim sonucunda kazanılan/kaybedilen para (TL)
# stage: Sahnenin geçtiği mekan

daily_scenes = daily_scenes = [
    # --- EV VE KİŞİSEL BAKIM (1-6) ---
    {"stage": "Banyo", "text": "1. Diş fırçalarken musluğu açık bırakıyor musun?", "options": {"Evet": {"water": 12, "money": 0}, "Hayır": {"water": 2, "money": 10}}},
    {"stage": "Banyo", "text": "2. Duş süren ortalama ne kadar?", "options": {"15 Dakika": {"water": 150, "money": 0}, "5 Dakika": {"water": 50, "money": 20}}},
    {"stage": "Mutfak", "text": "3. Bulaşıkları elde mi yoksa makinede mi yıkarsın?", "options": {"Elde": {"water": 100, "money": 0}, "Makinede": {"water": 15, "money": 15}}},
    {"stage": "Banyo", "text": "4. Sifonun sızdırdığını fark ettin, ne zaman tamir edersin?", "options": {"Hemen": {"water": 5, "money": -10}, "Haftaya": {"water": 200, "money": 0}}},
    {"stage": "Mutfak", "text": "5. Sebzeleri akan su altında mı yoksa kapta mı yıkarsın?", "options": {"Akan Su": {"water": 15, "money": 0}, "Kapta": {"water": 3, "money": 10}}},
    {"stage": "Banyo", "text": "6. Traş olurken/Yüz yıkarken musluk açık mı?", "options": {"Evet": {"water": 10, "money": 0}, "Hayır": {"water": 1, "money": 10}}},

    # --- OKUL VE SOSYAL YAŞAM (7-11) ---
    {"stage": "Okul", "text": "7. Okulda yarısı dolu su şişeni ne yaparsın?", "options": {"Dökerim": {"water": 0.5, "money": 0}, "Çiçeklere dökerim": {"water": 0, "money": 10}}},
    {"stage": "Okul", "text": "8. Okul tuvaletinde açık kalmış musluk gördün?", "options": {"Kapatırım": {"water": 0, "money": 15}, "Geçer giderim": {"water": 20, "money": 0}}},
    {"stage": "Spor", "text": "9. Spor sonrası çok terledin, nasıl temizlenirsin?", "options": {"Uzun banyo": {"water": 100, "money": 0}, "Hızlı duş": {"water": 30, "money": 10}}},
    {"stage": "Okul", "text": "10. Arkadaşın su savaşı yapmayı teklif etti?", "options": {"Kabul ederim": {"water": 30, "money": -10}, "Reddederim": {"water": 0, "money": 20}}},
    {"stage": "Kantin", "text": "11. İçecek alırken hangisini seçersin?", "options": {"Cam şişe (Geri dönüşümlü)": {"water": 1, "money": 5}, "Plastik şişe": {"water": 5, "money": 0}}},

    # --- GİZLİ SU AYAK İZİ (12-16) ---
    {"stage": "Yemek", "text": "12. Öğle yemeğinde ne yersin? (Üretimdeki su tüketimi)", "options": {"Hamburger": {"water": 2400, "money": 0}, "Sebze Yemeği": {"water": 200, "money": 10}}},
    {"stage": "Giyim", "text": "13. İhtiyacın olmadığı halde yeni bir kot pantolon alır mısın?", "options": {"Evet": {"water": 8000, "money": -50}, "Hayır": {"water": 0, "money": 50}}},
    {"stage": "Giyim", "text": "14. Bir tişört üretimi için kaç litre su harcanır biliyor musun?", "options": {"2700 Litre (Evet)": {"water": 0, "money": 20}, "Bilmiyorum (Hayır)": {"water": 10, "money": 0}}},
    {"stage": "Teknoloji", "text": "15. Eski telefonun çalışıyor ama yenisini istiyorsun?", "options": {"Alırım": {"water": 12000, "money": -500}, "Eskisini kullanırım": {"water": 0, "money": 100}}},
    {"stage": "Yemek", "text": "16. Kahve mi çay mı? (Su ayak izi farkı)", "options": {"Kahve": {"water": 140, "money": 0}, "Çay": {"water": 30, "money": 10}}},

    # --- ÇEVRE VE BAHÇE (17-20) ---
    {"stage": "Bahçe", "text": "17. Bahçeyi ne zaman sulamalıyız?", "options": {"Öğlen sıcağında": {"water": 100, "money": 0}, "Güneş battıktan sonra": {"water": 40, "money": 20}}},
    {"stage": "Sokak", "text": "18. Arabayı hortumla mı yoksa kovayla mı yıkamalı?", "options": {"Hortum": {"water": 150, "money": 0}, "Kova": {"water": 20, "money": 20}}},
    {"stage": "Çevre", "text": "19. Yağmur suyu toplama sistemi kurmak ister misin?", "options": {"Evet": {"water": -50, "money": -100}, "Hayır": {"water": 0, "money": 0}}},
    {"stage": "Çevre", "text": "20. Yerel belediyeden su tasarrufu eğitimi talep eder misin?", "options": {"Evet": {"water": 0, "money": 50}, "Hayır": {"water": 0, "money": 0}}}
]

# --- 2. MARKET SİSTEMİ (TEKNOLOJİK GELİŞTİRMELER) ---
# cost: Satın alma bedeli (TL)
# save_rate: Su tüketimini düşürme katsayısı (Örn: 0.20 demek %20 tasarruf demek)

market_items = {
    "Tasarruflu Musluk Başlığı": {
        "cost": 50, 
        "save_rate": 0.20, 
        "desc": "Mutfak ve banyo sularını %20 daha verimli kullanmanı sağlar."
    },
    "Damlama Sulama Sistemi": {
        "cost": 120, 
        "save_rate": 0.60, 
        "desc": "Bahçe sulama işlemlerinde %60 devasa tasarruf sağlar."
    },
    "Akıllı Sifon Aparatı": {
        "cost": 80, 
        "save_rate": 0.30, 
        "desc": "Tuvaletlerde her basışta %30 daha az su harcar."
    },
    "Yağmur Hasadı Deposu": {
        "cost": 200, 
        "save_rate": 0.40, 
        "desc": "Bahçe ve genel temizlik için bedava su biriktirir."
    }
}

# --- 3. BİLGİ KARTLARI (ARALARDA ÇIKACAK NOTLAR) ---
info_cards = [
    "Damlama sulama sistemi, vahşi sulamaya göre %60 daha verimlidir.",
    "Bir kot pantolon üretimi için yaklaşık 7.600 litre su harcanır.",
    "Dünya suyunun sadece %1'i erişilebilir tatlı sudur.",
    "Damlatan bir musluk günde 30 litreden fazla su israf edebilir."
]

