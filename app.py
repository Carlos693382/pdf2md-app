"""App local/web en Streamlit: sube un PDF y descarga el Markdown resultante."""

import streamlit as st
from converter import pdf_bytes_to_markdown

st.set_page_config(
    page_title="PDF a Markdown",
    page_icon="📄",
    layout="centered",
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #ffffff;
    }

    h1, h2, h3 {
        color: #ff9900;
    }

    .stButton > button {
        background-color: #ff9900;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 0.6rem 1.2rem;
        font-weight: bold;
    }

    .stButton > button:hover {
        background-color: #e68a00;
        color: white;
    }

    .stDownloadButton > button {
        background-color: #ff9900;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 0.6rem 1.2rem;
        font-weight: bold;
    }

    .stDownloadButton > button:hover {
        background-color: #e68a00;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.image("logo_telpark.png", width=280)

st.title("PDF a Markdown")

st.write(
    "Sube un PDF y genera automáticamente un archivo Markdown descargable."
)

uploaded_file = st.file_uploader("Selecciona un PDF", type=["pdf"])

if uploaded_file is not None:
    if st.button("Convertir a Markdown"):
        with st.spinner("Convirtiendo el PDF..."):
            pdf_bytes = uploaded_file.getvalue()
            markdown_text = pdf_bytes_to_markdown(pdf_bytes)

        st.success("Conversión completada.")

        st.text_area("Vista previa del Markdown", markdown_text, height=400)

        st.download_button(
            label="Descargar Markdown",
            data=markdown_text,
            file_name=uploaded_file.name.replace(".pdf", ".md"),
            mime="text/markdown",
        )
