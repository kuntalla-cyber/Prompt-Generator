import streamlit as st
import google.generativeai as genai

# --- 1. KONFIGURASI API ---
# Gunakan API Key yang sudah Anda buat
API_KEY = "AIzaSyCq_O6SR9whuc8sFj0Wp_1jyfoh31VyBa4" 

if API_KEY.startswith(" "):
    API_KEY = API_KEY.strip()

try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Gagal konfigurasi: {e}")

# --- 2. TAMPILAN APLIKASI ---
st.set_page_config(page_title="Script Generator", layout="centered")
st.title("🎬 AI Script Generator")
st.write("Ubah ide Anda menjadi naskah profesional.")

# Input ide dari pengguna
ide = st.text_area("Ide Adegan:", placeholder="Contoh: Iklan sepatu bola yang keren")

# Tombol untuk menjalankan
if st.button("Generate Sekarang"):
    if ide:
        with st.spinner("Sedang memproses naskah..."):
            try:
                # Perintah ke AI
                response = model.generate_content(f"Buat naskah video lengkap untuk ide: {ide}")
                
                # Menampilkan hasil
                st.subheader("Hasil Naskah:")
                st.write(response.text)
                st.session_state['hasil'] = response.text
            except Exception as e:
                st.error(f"Sistem Google Menjawab: {e}")
    else:
        st.warning("Masukkan ide terlebih dahulu!")

# Tombol simpan hasil
if 'hasil' in st.session_state:
    st.download_button("Simpan Naskah (.txt)", st.session_state['hasil'], file_name="naskah.txt")
