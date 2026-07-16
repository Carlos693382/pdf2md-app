"""Lógica de conversión de PDF a Markdown."""

from pathlib import Path

import pymupdf4llm


def pdf_bytes_to_markdown(pdf_bytes: bytes) -> str:
    """Convierte el contenido binario de un PDF a texto Markdown.

    pymupdf4llm necesita una ruta de archivo, así que el PDF se
    escribe primero en un archivo temporal.
    """
    import tempfile

    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
        tmp.write(pdf_bytes)
        tmp_path = Path(tmp.name)

    try:
        markdown_text = pymupdf4llm.to_markdown(str(tmp_path))
    finally:
        tmp_path.unlink(missing_ok=True)

    return markdown_text


def pdf_file_to_markdown(pdf_path: str | Path) -> str:
    """Convierte un PDF ya guardado en disco a texto Markdown."""
    return pymupdf4llm.to_markdown(str(pdf_path))
