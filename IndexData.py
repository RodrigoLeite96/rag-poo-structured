from langchain_text_splitters import RecursiveCharacterTextSplitter
from LoadPDF import LoadPDF

class IndexData(LoadPDF):


    def __init__(self):
        """Configure text splitting parameters and load PDF pages."""
        super().__init__()
        self._chunck_size = 500
        self._chunck_overlap = 50
        self._pages = self.get_pages()


    def get_chucnks(self):
        """Split loaded pages into chunks for embedding and retrieval."""

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = text_splitter.split_documents(self._pages)

        return chunks
