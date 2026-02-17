import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from database import init_db, update_or_add_student, get_leaderboard
from scenarios import daily_scenes, market_items

# Veritabanını sistem başladığında hazırla
init_db()

# --- SESSION STATE AYARLARI ---
if 'page' not in st.session_state:
    st.session_state.page = "login"
if 'money' not in st.session_state:
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
    st.title("💧 AquaMind: Su Yönetimi Simülasyonu")
    st.markdown("### Liselerde Bilim Uygulamaları Projesi")
    
    tab1, tab2 = st.tabs(["Öğrenci Girişi", "Yönetici Paneli"])
    
    with tab1:
        u_name = st.text_input("Adın Soyadın / Okul No:", placeholder="Örn: Ahmet Yılmaz")
        if st.button("Oyuna Başla"):
            if u_name:
                st.session_state.user = u_name
                st.session_state.page = "game"
                st.rerun()
            else:
                st.warning("Lütfen giriş yapmak için isminizi yazın.")

    with tab2:
        admin_pass = st.text_input("Yönetici Şifresi:", type="password")
        if st.button("Yönetici Girişi"):
            if admin_pass == "004380":
                st.session_state.page = "admin"
                st.rerun()
            else:
                st.error("Hatalı şifre!")

# --- SAYFA 2: OYUN EKRANI ---
elif st.session_state.page == "game":
    # Yan Panel (Sidebar) - Durum Göstergeleri
    with st.sidebar:
        st.header(f"👤 {st.session_state.user}")
        st.metric("💰 Bakiye", f"{st.session_state.money} TL")
        
        # Su Barı Görselleştirme
        st.write("### 💧 Su Tüketimi")
        limit = 200
        progress = min(st.session_state.water / limit, 1.0)
        st.progress(progress)
        st.caption(f"{st.session_state.water} L / {limit} L")
        
        st.write("---")
        st.subheader("🛒 Market")
        for item, info in market_items.items():
            if item not in st.session_state.owned_items:
                if st.button(f"{item} ({info['cost']} TL)"):
                    if st.session_state.money >= info['cost']:
                        st.session_state.money -= info['cost']
                        st.session_state.owned_items.append(item)
                        st.success(f"{item} Aktif!")
                        st.rerun()
            else:
                st.info(f"✅ {item}")

    # Ana Oyun Alanı
    st.title("🌊 Günlük Kararlar")
    
    if st.session_state.current_scene < len(daily_scenes):
        scene = daily_scenes[st.session_state.current_scene]
        st.subheader(f"Mekan: {scene['stage']}")
        st.write(scene['text'])
        
        choice = st.radio("Ne yapmaya karar verdin?", list(scene['options'].keys()))
        
        if st.button("Kararı Uygula"):
            res = scene['options'][choice]
            
            # Tasarruf Sistemleri Kontrolü
            harcanan = res['water']
            if "Tasarruflu Musluk Başlığı" in st.session_state.owned_items and scene['stage'] == "Banyo":
                harcanan *= 0.8
            
            st.session_state.water += harcanan
            st.session_state.money += res['money']
            st.session_state.history.append(st.session_state.water)
            st.session_state.current_scene += 1
            st.rerun()
    else:
        st.success("🎉 Tebrikler! Tüm günlük kararları tamamladın.")
        st.write(f"Toplam Harcanan Su: **{st.session_state.water:.1f} Litre**")
        
        if st.button("Sonuçları Kaydet ve Bitir"):
            update_or_add_student(st.session_state.user, st.session_state.water, st.session_state.money, 100)
            st.session_state.page = "login"
            st.session_state.current_scene = 0 # Reset for next session
            st.rerun()

# --- SAYFA 3: ADMIN PANELİ ---
elif st.session_state.page == "admin":
    st.title("🔐 Yönetici Analiz Paneli")
    if st.button("⬅ Ana Menüye Dön"):
        st.session_state.page = "login"
        st.rerun()
    
    st.write("### 🏆 Öğrenci Sıralaması (En Az Su Tüketenler)")
    df = get_leaderboard()
    
    if not df.empty:
        st.dataframe(df, use_container_width=True)
        
        # Grafiksel Gösterim
        st.write("### 📊 Tüketim Grafiği")
        fig, ax = plt.subplots()
        ax.bar(df["Öğrenci Adı"], df["Toplam Su (L)"], color='skyblue')
        plt.xticks(rotation=45)
        st.pyplot(fig)
        
        # Veri İndirme
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Verileri CSV Olarak İndir", csv, "aquamind_sonuclar.csv", "text/csv")
    else:
        st.info("Henüz kaydedilmiş bir veri bulunmuyor.")
