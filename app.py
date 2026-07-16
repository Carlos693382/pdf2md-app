"""App local en Streamlit: sube un PDF y descarga el Markdown resultante."""

from pathlib import Path

import streamlit as st

from converter import pdf_bytes_to_markdown

st.set_page_config(page_title="PDF a Markdown", page_icon="📄")

st.title("📄 PDF a Markdown")
st.write(
    "Sube un PDF (puede tener varias páginas) y genera un archivo "
    "Markdown descargable."
)

uploaded_file = st.file_uploader("Selecciona un PDF", type=["pdf"])

if uploaded_file is not None:
    if st.button("Convertir a Markdown"):
        with st.spinner("Convirtiendo..."):
            pdf_bytes = uploaded_file.getvalue()
            markdown_text = pdf_bytes_to_markdown(pdf_bytes)

        st.success("Conversión completada.")

        st.text_area("Vista previa", markdown_text, height=400)

        output_name = Path(uploaded_file.name).stem + ".md"
        st.download_button(
            label="Descargar Markdown",
            data=markdown_text.encode("utf-8"),
            file_name=output_name,
            mime="text/markdown",
        )
