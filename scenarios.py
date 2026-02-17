
# --- 1. GÜNLÜK SENARYOLAR (SAHNELER) ---
# water: Harcanan su miktarı (Litre)
# money: Seçim sonucunda kazanılan/kaybedilen para (TL)
# stage: Sahnenin geçtiği mekan

daily_scenes = [
    # --- EV (Banyo/Mutfak) ---
    {"stage": "Banyo", "text": "1. Diş fırçalarken musluğu açık bırakıyor musun?", "image": "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&q=80&w=1200", "options": {"Evet": {"water": 12, "money": 0}, "Hayır": {"water": 2, "money": 10}}},
    {"stage": "Banyo", "text": "2. Duş süren ortalama ne kadar?", "image": "https://images.unsplash.com/photo-1559839734-2b71f15024d5?auto=format&fit=crop&q=80&w=1200", "options": {"15 Dakika": {"water": 150, "money": 0}, "5 Dakika": {"water": 50, "money": 20}}},
    {"stage": "Mutfak", "text": "3. Bulaşıkları elde mi yoksa makinede mi yıkarsın?", "image": "https://images.unsplash.com/photo-1584622781564-1d9876a13d00?auto=format&fit=crop&q=80&w=1200", "options": {"Elde": {"water": 100, "money": 0}, "Makinede": {"water": 15, "money": 15}}},
    {"stage": "Banyo", "text": "4. Sifonun sızdırdığını fark ettin, ne zaman tamir edersin?", "image": "https://images.unsplash.com/photo-1504148455328-c376907d081c?auto=format&fit=crop&q=80&w=1200", "options": {"Hemen": {"water": 5, "money": -10}, "Haftaya": {"water": 200, "money": 0}}},
    {"stage": "Mutfak", "text": "5. Sebzeleri akan su altında mı yoksa kapta mı yıkarsın?", "image": "https://images.unsplash.com/photo-1590779033100-9f60705a013d?auto=format&fit=crop&q=80&w=1200", "options": {"Akan Su": {"water": 15, "money": 0}, "Kapta": {"water": 3, "money": 10}}},
    {"stage": "Banyo", "text": "6. Yüzünü yıkarken musluğu sabunlanırken kapatıyor musun?", "image": "https://images.unsplash.com/photo-1616391182219-e080b4d1043a?auto=format&fit=crop&q=80&w=1200", "options": {"Hayır": {"water": 10, "money": 0}, "Evet": {"water": 1, "money": 10}}},

    # --- OKUL (7-11) ---
    {"stage": "Okul", "text": "7. Şişende kalan suyu ne yaparsın?", "image": "https://images.unsplash.com/photo-1523240715639-99f84d3d740c?auto=format&fit=crop&q=80&w=1200", "options": {"Dökerim": {"water": 0.5, "money": 0}, "Çiçeklere dökerim": {"water": 0, "money": 10}}},
    {"stage": "Okul", "text": "8. Okul tuvaletinde açık kalmış bir musluk gördün?", "image": "https://images.unsplash.com/photo-1585744944323-9336d3969562?auto=format&fit=crop&q=80&w=1200", "options": {"Kapatırım": {"water": 0, "money": 15}, "Görmezden gelirim": {"water": 20, "money": 0}}},
    {"stage": "Spor", "text": "9. Okul spor salonunda duş alırken?", "image": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&q=80&w=1200", "options": {"Uzun kalırım": {"water": 80, "money": 0}, "Hızlıca çıkarım": {"water": 20, "money": 10}}},
    {"stage": "Okul", "text": "10. Bahçedeki fıskiyeler boş alanı suluyor?", "image": "https://images.unsplash.com/photo-1558905619-17254261b646?auto=format&fit=crop&q=80&w=1200", "options": {"Haber veririm": {"water": 0, "money": 20}, "Bana ne": {"water": 100, "money": 0}}},
    {"stage": "Kantin", "text": "11. İçecek tercihin?", "image": "https://images.unsplash.com/photo-1525193612562-0ec53b0e5d7c?auto=format&fit=crop&q=80&w=1200", "options": {"Cam Şişe": {"water": 1, "money": 5}, "Plastik Şişe": {"water": 5, "money": 0}}},

    # --- GİZLİ SU / ENDÜSTRİ (12-16) ---
    {"stage": "Restoran", "text": "12. Bugün ne yemeli? (Sanal Su Tüketimi)", "image": "https://images.unsplash.com/photo-1550547660-d9450f859349?auto=format&fit=crop&q=80&w=1200", "options": {"Hamburger": {"water": 2400, "money": 0}, "Salata": {"water": 150, "money": 10}}},
    {"stage": "Mağaza", "text": "13. Yeni bir kot pantolon üretimi için kaç litre su harcanır?", "image": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?auto=format&fit=crop&q=80&w=1200", "options": {"Bilmiyorum (Satın Al)": {"water": 8000, "money": -50}, "Tasarruf et (Alma)": {"water": 0, "money": 50}}},
    {"stage": "Giyim", "text": "14. Sadece bir tişört üretmek için 2700 litre su harcandığını biliyor musun?", "image": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?auto=format&fit=crop&q=80&w=1200", "options": {"Artık biliyorum": {"water": 0, "money": 20}, "Şaşırtıcı": {"water": 10, "money": 5}}},
    {"stage": "Teknoloji", "text": "15. Eski telefonun sağlam ama yenisi çıktı?", "image": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&q=80&w=1200", "options": {"Hemen alırım": {"water": 12000, "money": -500}, "Sabrederim": {"water": 0, "money": 100}}},
    {"stage": "Cafe", "text": "16. Kahve mi çay mı? (Su ayak izi)", "image": "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&q=80&w=1200", "options": {"Kahve": {"water": 140, "money": 0}, "Çay": {"water": 30, "money": 10}}},

    # --- ÇEVRE / TARIM (17-20) ---
    {"stage": "Bahçe", "text": "17. Bahçeyi ne zaman sulamalıyız?", "image": "https://images.unsplash.com/photo-1585315532009-436329e469d8?auto=format&fit=crop&q=80&w=1200", "options": {"Öğlen": {"water": 100, "money": 0}, "Akşamüstü": {"water": 30, "money": 20}}},
    {"stage": "Garaj", "text": "18. Arabayı nasıl yıkamalı?", "image": "https://images.unsplash.com/photo-1520340356584-f9917d1eea6f?auto=format&fit=crop&q=80&w=1200", "options": {"Hortum": {"water": 150, "money": 0}, "Kova": {"water": 20, "money": 20}}},
    {"stage": "Park", "text": "19. Çim yerine az su isteyen bitkiler (Xeriscape) dikilmeli mi?", "image": "https://images.unsplash.com/photo-1584479898061-15742e14f50d?auto=format&fit=crop&q=80&w=1200", "options": {"Evet": {"water": -50, "money": 50}, "Hayır": {"water": 50, "money": 0}}},
    {"stage": "Final", "text": "20. Su tasarrufu bir tercih değil, zorunluluktur. Katılıyor musun?", "image": "https://images.unsplash.com/photo-1468421870903-4df1664ac249?auto=format&fit=crop&q=80&w=1200", "options": {"Kesinlikle": {"water": 0, "money": 100}, "Belki": {"water": 0, "money": 0}}}
]

market_items = {
    "Tasarruflu Musluk Başlığı": {"cost": 50, "save_rate": 0.20},
    "Damlama Sulama Sistemi": {"cost": 120, "save_rate": 0.60},
    "Akıllı Sifon": {"cost": 80, "save_rate": 0.30}
}
# --- 3. BİLGİ KARTLARI (ARALARDA ÇIKACAK NOTLAR) ---
info_cards = [
    "Damlama sulama sistemi, vahşi sulamaya göre %60 daha verimlidir.",
    "Bir kot pantolon üretimi için yaklaşık 7.600 litre su harcanır.",
    "Dünya suyunun sadece %1'i erişilebilir tatlı sudur.",
    "Damlatan bir musluk günde 30 litreden fazla su israf edebilir."
]
