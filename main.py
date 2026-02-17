import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from database import init_db, update_or_add_student, get_leaderboard
from scenarios import daily_scenes, market_items

# Sayfa konfigürasyonu (Tarayıcı sekmesinde görünecek isim)
st.set_page_config(page_title="AquaMind | Su Verimliliği", page_icon="💧", layout="centered")

# Veritabanını başlat
init_db()

# --- CSS: DİNAMİK ARKA PLAN VE STİL ---
def set_bg(url):
    st.markdown(f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0,0.55)), url("{url}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            transition: background-image 1s ease-in-out;
        }}
        /* İçerik kutusunu güzelleştirme */
        .main-container {{
            background: rgba(255, 255, 255, 0.92);
            padding: 40px;
            border-radius: 25px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.3);
            color: #1e1e1e;
        }}
        /* Metrik kartlarını özelleştirme */
        [data-testid="stMetricValue"] {{
            color: #0077b6;
        }}
        </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE (HAFIZA) YÖNETİMİ ---
if 'page' not in st.session_state:
    st.session_state.page = "login"
if 'current_scene' not in st.session_state:
    st.session_state.update({
        'user': "",
        'money': 100,
        'water': 0,
        'owned_items': [],
        'current_scene': 0,
        'history': []
    })

# --- SAYFA 1: GİRİŞ EKRANI ---
if st.session_state.page == "login":
    set_bg("https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?q=80&w=1200")
    st.title("🌊 AquaMind: Su Yönetimi")
    st.markdown("### Geleceğin akışı senin kararlarında.")
    
    with st.container():
        u_name = st.text_input("Adın Soyadın / Okul No:", placeholder="Örn: Ahmet Yılmaz")
        if st.button("Simülasyona Başla"):
            if u_name:
                st.session_state.user = u_name
                st.session_state.page = "game"
                st.rerun()
            else:
                st.warning("Devam etmek için bir isim girin.")

# --- SAYFA 2: OYUN EKRANI (20 SORU) ---
elif st.session_state.page == "game":
    if st.session_state.current_scene < len(daily_scenes):
        scene = daily_scenes[st.session_state.current_scene]
        set_bg(scene['image']) # Her soruda değişen görsel
        
        # Sidebar: Durum ve Market
        with st.sidebar:
            st.header(f"👤 {st.session_state.user}")
            st.metric("💰 Bakiye", f"{st.session_state.money} TL")
            st.metric("💧 Toplam Su", f"{st.session_state.water:.1f} L")
            
            st.write("---")
            st.subheader("🛒 Market")
            for item, info in market_items.items():
                if item not in st.session_state.owned_items:
                    if st.button(f"{item} ({info['cost']} TL)"):
                        if st.session_state.money >= info['cost']:
                            st.session_state.money -= info['cost']
                            st.session_state.owned_items.append(item)
                            st.success(f"{item} Alındı!")
                            st.rerun()
                else:
                    st.info(f"✅ {item} (Aktif)")

        # Ana Oyun Alanı
        st.subheader(f"Soru {st.session_state.current_scene + 1} / 20")
        st.info(f"📍 Mekan: {scene['stage']}")
        st.write(f"### {scene['text']}")
        
        choice = st.radio("Seçimin nedir?", list(scene['options'].keys()))
        
        if st.button("Kararı Uygula →"):
            res = scene['options'][choice]
            
            # Tasarruf katsayısı hesaplama
            reduction = 1.0
            if "Tasarruflu Musluk Başlığı" in st.session_state.owned_items and scene['stage'] in ["Banyo", "Mutfak"]:
                reduction = 0.8
            if "Damlama Sulama Sistemi" in st.session_state.owned_items and scene['stage'] == "Bahçe":
                reduction = 0.4
            
            st.session_state.water += res['water'] * reduction
            st.session_state.money += res['money']
            st.session_state.current_scene += 1
            st.rerun()
            
    else:
        # FİNAL EKRANI
        set_bg("https://images.unsplash.com/photo-1468421870903-4df1664ac249?q=80&w=1200")
        st.balloons()
        st.title("📊 Simülasyon Tamamlandı!")
        st.write(f"Sayın **{st.session_state.user}**, tüm günlük kararlarını verdin.")
        
        col1, col2 = st.columns(2)
        col1.metric("Toplam Harcanan Su", f"{st.session_state.water:.1f} Litre")
        col2.metric("Kalan Bakiye", f"{st.session_state.money} TL")
        
        if st.button("Sonuçları Kaydet ve Sıralamayı Gör"):
            update_or_add_student(st.session_state.user, st.session_state.water, st.session_state.money, 100)
            st.session_state.page = "admin"
            st.rerun()

# --- SAYFA 3: LİDERLİK TABLOSU ---
elif st.session_state.page == "admin":
    set_bg("https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1200")
    st.title("🏆 Su Koruyucuları Sıralaması")
    
    df = get_leaderboard()
    if not df.empty:
        st.dataframe(df, use_container_width=True)
        
        # Basit Grafik
        st.write("### 📉 Su Tüketimi Dağılımı")
        st.bar_chart(df.set_index("Öğrenci Adı")["Toplam Su (L)"])
    
    if st.button("Ana Menüye Dön"):
        # Oyunu sıfırla
        st.session_state.clear()
        st.rerun()

