import streamlit as st
import google.generativeai as genai

# --- KONFIGURASI ---
# Ganti dengan API Key asli Anda dari Google AI Studio
API_KEY = "AIzaSyBdor4GvP-NF7u2-EBUgy5BsrJATsdfrK0" 

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="Prompt Architect", layout="centered")

# --- UI APLIKASI ---
st.header("🎬 AI Script Generator")
st.write("Ubah ide satu kalimat menjadi naskah produksi lengkap.")

# Input
ide = st.text_area("Ide Adegan:", placeholder="Contoh: Iklan sepatu lari yang energik di tengah kota Jakarta")
tombol = st.button("Generate Script")

# Logic
if tombol and ide:
    with st.spinner("Sedang menulis naskah..."):
        prompt_rahasia = f"""
        Bertindaklah sebagai Sutradara Profesional. 
        Tugas: Kembangkan ide '{ide}' menjadi script video pendek.
        Output wajib ada:
        1. Judul Konsep
        2. Prompt Visual (untuk AI Video Generator)
        3. Naskah (Visual & Audio) per scene
        4. CTA (Kalimat Penutup)
        """
        try:
            hasil = model.generate_content(prompt_rahasia)
            st.session_state['hasil'] = hasil.text
        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")

# Output
if 'hasil' in st.session_state:
    st.markdown("---")
    st.subheader("Hasil Draft:")
    # Text area agar bisa diedit user
    final_text = st.text_area("Silakan edit di sini:", value=st.session_state['hasil'], height=500)
    st.download_button("Simpan Script (.txt)", data=final_text, file_name="script_final.txt")
