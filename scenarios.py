# --- 1. GÜNLÜK SENARYOLAR (SAHNELER) ---
# water: Harcanan su miktarı (Litre)
# money: Seçim sonucunda kazanılan/kaybedilen para (TL)
# stage: Sahnenin geçtiği mekan

daily_scenes = [
    {
        "stage": "Banyo (Sabah)",
        "text": "Sabah uyandın, ellerini yıkayacaksın. Musluğu nasıl kullanırsın?",
        "options": {
            "Musluğu tam açarım, işim bitene kadar akar.": {"water": 12, "money": 0},
            "Sadece ıslatırken açar, sabunlarken kapatırım.": {"water": 2, "money": 10},
            "Sensörlü musluk varmış gibi çok kısa sürede hallederim.": {"water": 1, "money": 15}
        }
    },
    {
        "stage": "Mutfak (Kahvaltı)",
        "text": "Kahvaltıdan sonra kirli tabağını nasıl temizlersin?",
        "options": {
            "Akan suyun altında uzunca durularım.": {"water": 20, "money": 0},
            "Bulaşık makinesinin dolmasını beklerim.": {"water": 2, "money": 20},
            "Az miktarda su dolu bir kapta çalkalarım.": {"water": 5, "money": 10}
        }
    },
    {
        "stage": "Okul (Tuvaletler)",
        "text": "Okul tuvaletinde bir musluğun bozuk olduğunu ve su damlattığını gördün.",
        "options": {
            "Bana ne, okulun sorunu diyerek geçerim.": {"water": 50, "money": 0},
            "Gidip hemen bir öğretmene veya görevliye haber veririm.": {"water": 0, "money": 40},
            "Kendi imkanlarımla musluğu iyice sıkıştırmaya çalışırım.": {"water": 5, "money": 15}
        }
    },
    {
        "stage": "Bahçe (Sulama)",
        "text": "Bahçedeki çiçeklerin sulanması gerekiyor. Hangi yöntemi seçersin?",
        "options": {
            "Hortumu açıp her yeri bolca sularım.": {"water": 100, "money": 0},
            "Kovayla sadece bitki diplerine su dökerim.": {"water": 30, "money": 10},
            "Yağmur suyu deposundaki birikmiş suyu kullanırım.": {"water": 0, "money": 30}
        }
    },
    {
        "stage": "Alışveriş (Tüketim)",
        "text": "Yeni bir tişört almak istiyorsun ama evde benzerleri var. Su ayak izini düşünürsen?",
        "options": {
            "Modayı takip ederim, hemen alırım.": {"water": 2700, "money": -50},
            "Almaktan vazgeçerim, olanları kullanırım.": {"water": 0, "money": 50},
            "İkinci el veya sürdürülebilir bir ürün bakarım.": {"water": 500, "money": 20}
        }
    }
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
