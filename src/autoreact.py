import streamlit as st
import tempfile
import os
from generate import startGen
from PIL import Image
import zipfile
from io import BytesIO
global PROCESSED
PROCESSED = False
global ZIPDIR
global OLD
OLD = None
st.set_page_config(
    page_title="Auto-React by Austen Furutani",
    page_icon="🚀",
)
image = Image.open('img/howto.png')
st.title('Auto-React 🔧')
st.caption("🤓 Created By: Austen Furutani")
st.link_button('LinkedIn', "https://www.linkedin.com/in/austen-furutani/")
st.divider()
st.header("Welcome to the future of UI development")
st.write("Auto-React utalizes OpenAI's GPT 4.0 to create React.js templates to help developers get their project off the ground.")
st.write("This project is NOT meant to replace developers but to help them get a jump start.")
st.image(image, use_column_width=True)
st.divider()




def zip_directory(directory):
    print(directory)
    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for foldername, subfolders, filenames in os.walk(directory):
            for filename in filenames:
                print(filename)
                file_path = os.path.join(foldername, filename)
                zip_file.write(file_path, os.path.relpath(file_path, directory))
    zip_buffer.seek(0)
    return zip_buffer
st.header("Generate REACT.JS files here")
files = st.file_uploader("Upload .png layout mock up files here to generate REACT.js files", accept_multiple_files=True)
if OLD is None:
    OLD = 1
    for file in files:
        temp_dir = tempfile.mkdtemp()
        path = os.path.join(temp_dir, file.name)
        print(path)
        with open(path, "wb") as f:
            f.write(file.getvalue())

        with tempfile.TemporaryDirectory() as temp_dir: 
            startGen.start(path, temp_dir)
            PROCESSED = True

            zip_buffer = zip_directory(temp_dir)
            st.download_button(
                    label="Download ZIP",
                    data=zip_buffer,
                    file_name="generated_react_files.zip",
                    mime="application/zip"
                )