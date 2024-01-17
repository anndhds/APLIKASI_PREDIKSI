#Loaad libraries needed
import streamlit as st 


# Set page configuration
st.set_page_config(
    page_title= "Selamat Datang di Aplikasi Time Series",
    page_icon= "🥸",
    layout="wide"
)

# Add content to your Streamlit app
st.markdown("# 👋 Selamat Datang di Aplikasi Prediksi Penjualan Produk di seluruh toko")

# Display the wafing GIF
st.image("https://www.animatedimages.org/data/media/707/animated-welcome-image-0215.gif")

# Add CSS for  animation
st.write("""
    <style>
       @keyframes slide-in {
           0% {
               transform: translateX(-100%);
               }
               100% {
                   transform: translateX(0);
               }
          }
          .slide-in-animation {
              animation: slide-in 1.5s ease-in-out;
          }
    </style>
""", unsafe_allow_html=True)

# Text with animattion
st.write('<div class="slide-in-animation"> Aplikasi ini dengan batuan model regresi linear yang akan memungkinkan anda memprediksi penjualan di toko Favorita.</div>' , unsafe_allow_html= True)

#add a sidebar to select pages
st.sidebar.success("Pilih halaman atas.")


# Create a streamlit container for the subheader
subheader_container = st.container()

# Define the subheader content
subheader_content = """
<div class= "slide-in-animation">
<h3>Hal yang DapatAnda LAkukan Di Aplikasi Ini:</h3>
<ul>
    <li>Perkiraan Penjualan Pada Tanggal Tertentu untuk Toko Favorita</li>
    <li>Lihat Kumpulan data dan berinteraksi dengan visual yang menunjukkan penjualan harian dieluruh toko</li>
    <li>Kenali lebih banyak tentang tim</li>
</ul>
</div>
"""

# Aplly CSS animation using HTML/CSS
subheader_container.markdown(subheader_content, unsafe_allow_html=True)

# Add CSS for animation
st.write("""
    <style>
       @keyframes slide-in {
           0% {
               transform: translateX(-100%);
               }
               100% {
                   transform: translateX(0);
               }
          }
          .slide-in-animation {
              animation: slide-in 1.5s ease-in-out;
          }
    </style>
""", unsafe_allow_html=True)