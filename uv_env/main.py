import streamlit as st
from ImageCrop import CropImage

def main():
    st.title("CROP YOUR IMAGE")
    image = st.file_uploader("Upload your image", type=['jpg','png'])
    if image:
        st.image(image)
        if st.button('CROP') :
            CropImage(image)
            col = st.columns([15, 15,  15])
            col[0].image('original.png',caption="Original")
            col[1].image('process.png',caption="Processed" )
            col[2].image('crop.png',caption="Cropped")
            
if __name__ == "__main__":
    main()
