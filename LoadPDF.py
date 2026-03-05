import os
from langchain_community.document_loaders import PyPDFLoader
from utils.variables import (
    DOC_PATH
)

class LoadPDF():

    def __init__(self):
        self._doc_path = DOC_PATH 


    def get_pages(self):
        """ """

        loader = PyPDFLoader(self._doc_path)
        pages = loader.load()

        return pages