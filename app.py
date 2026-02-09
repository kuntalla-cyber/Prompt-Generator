import streamlit as st
import google.generativeai as genai

# --- 1. SETTING API ---
# Masukkan API Key Anda di bawah ini
API_KEY = "AIzaSyBdor4GvP-NF7u2-EBUgy5BsrJATso..." 

try:
    genai.configure(api_key=API_KEY)
    # GANTI KE PRO 1.0: Ini model paling stabil untuk akun gratis
    model = genai.GenerativeModel('gemini-1.0-pro')
except Exception as e:
    st.error(f"Error Config: {e}")

# --- 2. TAMPILAN ---
st.set_page_config(page_title="Generator Naskah", layout="centered")
st.title("🎬 Script Generator Profesional")

ide_konten = st.text_input("Ide Adegan:", placeholder="Contoh: Iklan sepatu lari")

if st.button("Generate Sekarang"):
    if ide_konten:
        with st.spinner("Sedang merancang alur..."):
            try:
                # Perintah singkat & padat
                perintah = f"Buat naskah video lengkap berdurasi 30 detik untuk ide: {ide_konten}. Sertakan adegan visual dan teks narasi."
                response = model.generate_content(perintah)
                
                # Menampilkan hasil langsung di layar
                st.markdown("### Hasil Naskah:")
                st.write(response.text)
                st.session_state['hasil'] = response.text
            except Exception as e:
                # Jika error lagi, ini akan memberitahu kita ALASAN ASLINYA
                st.error(f"Sistem Google Menjawab: {e}")
    else:
        st.warning("Silakan isi ide terlebih dahulu.")

# Tombol simpan
if 'hasil' in st.session_state:
    st.download_button("Simpan Naskah (.txt)", st.session_state['hasil'], file_name="naskah.txt")
