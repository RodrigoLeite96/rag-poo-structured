import os
from langchain_community.document_loaders import PyPDFLoader
from utils.variables import (
    DOC_PATH
)

class LoadPDF():

    def __init__(self):
        """Store the PDF path configured for document loading."""
        self._doc_path = DOC_PATH 


    def get_pages(self):
        """Load and return all pages from the configured PDF file."""

        loader = PyPDFLoader(self._doc_path)
        pages = loader.load()

        return pages
