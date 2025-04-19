
import streamlit as st
import requests

st.title("🎵 TikTok Video Downloader 244")

video_url = st.text_input("Masukkan link video TikTok di sini:")

if st.button("Download Video Bro"):
    if video_url:
        st.info("Sedang memproses...")

        try:
            api_url = f"https://tikwm.com/api/?url={video_url}"
            response = requests.get(api_url)
            data = response.json()

            if data["code"] == 0:
                download_url = data["data"]["play"]
                st.success("Video ditemukan!")
                st.video(download_url)
                st.markdown(f"[Klik di sini untuk download videonya]({download_url})", unsafe_allow_html=True)
            else:
                st.error("Gagal mengambil video. Pastikan link TikTok valid.")
        except Exception as e:
            st.error(f"Terjadi error: {e}")
    else:
        st.warning("Silakan masukkan URL terlebih dahulu.")
