## Load Libraries
import streamlit as st 
from PIL import Image

# Display the c title
st.title("Hewan Lucu")

## set team iamge
image = Image.open('Team logo/logo.jpg')

# set the desired size
new_size = (400, 300)

#Resize the image
resized_image = image.resize(new_size)

##set the image
st.image(resized_image)

##info about the team
st.write("Kucing merupakan salah satu spesies hewan,")
st.write("Kucing merupakan hewan yang sangat lucu")

st.subheader("Dibawah adalah hewan lainnya")

##For members
st.header("SKucing Lucu")
st.info('Kucing')
lead=Image.open('Team photos/foto.jpg')
size=(400,400)
lead_image=lead.resize(size)
st.image(lead_image)
# Button to send an email
if st.button("Contact Me via Email"):
    st.markdown('<a href="anandadwi64@gmail.com">Send Email</a>', unsafe_allow_html=True)

# Button to visit LinkedIn profile
if st.button("Visit My LinkedIn Profile"):
    st.markdown('<a href="https://www.linkedin.com/in/anandadwisafitri/">LinkedIn</a>', unsafe_allow_html=True)  # Add the correct URL inside href

# Button to visit Medium
if st.button("Read My Blogs"):
    st.markdown('<a href="#">Medium</a>', unsafe_allow_html=True)  # Add the correct URL inside href

# Button to GitHub
if st.button("Check Out My GitHub Repositories"):
    st.markdown('<a href="https://github.com/anndhds">GitHub</a>', unsafe_allow_html=True)  # Add the correct URL inside href
