import streamlit as st
import google.generativeai as genai

# --- 1. KONFIGURASI API ---
# Pastikan API Key Anda benar di dalam tanda petik
API_KEY = "AIzaSyBdor4GvP-NF7u2-EBUgy5BsrJATsdfrK0" 

try:
    genai.configure(api_key=API_KEY)
    # Menggunakan model paling stabil untuk aplikasi web
    model_ai = genai.GenerativeModel('gemini-1.5-flash-latest')
except Exception as e:
    st.error(f"Gagal konfigurasi API: {e}")

# --- 2. SETTING HALAMAN ---
st.set_page_config(page_title="Prompt Architect Pro", layout="centered")
st.header("🎬 AI Script Generator")
st.write("Profesional Tool untuk Alur Konten Otomatis")

# --- 3. INPUT USER ---
ide_user = st.text_area("Masukan Ide Adegan:", placeholder="Contoh: Iklan sepatu lari yang energik...")
tombol_proses = st.button("Generate Alur Lengkap", use_container_width=True)

# --- 4. LOGIKA GENERATOR ---
if tombol_proses:
    if not ide_user:
        st.warning("Mohon masukkan ide terlebih dahulu.")
    else:
        with st.spinner("Engineering sedang bekerja merancang naskah..."):
            perintah = f"""
            Bertindaklah sebagai Senior Creative Director & Copywriter.
            Kembangkan ide ini: '{ide_user}' menjadi naskah produksi lengkap.
            
            Wajib sertakan:
            - ADEGAN 1-3 (Detail Visual & Audio)
            - PROMPT GAMBAR/VIDEO (Expanded untuk AI Generator)
            - CTA (Call to Action yang persuasif)
            """
            try:
                # Menggunakan model_ai yang sudah didefinisikan di atas
                respon = model_ai.generate_content(perintah)
                st.session_state['hasil_akhir'] = respon.text
            except Exception as e:
                st.error(f"Terjadi kesalahan teknis: {e}")

# --- 5. OUTPUT & EDITING ---
if 'hasil_akhir' in st.session_state:
    st.markdown("---")
    st.subheader("Draft Naskah (Silakan Edit Jika Perlu):")
    # Fitur editing sesuai permintaan Anda
    teks_edit = st.text_area("Editor:", value=st.session_state['hasil_akhir'], height=450)
    
    col1, col2 = st.columns(2)
    with col1:
        st.download_button("Download Script (.txt)", teks_edit, file_name="naskah_produksi.txt")
    with col2:
        if st.button("Clear Canvas"):
            del st.session_state['hasil_akhir']
            st.rerun()
