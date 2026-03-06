from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from utils.variables import OPENAI_TOKEN, CHROMA_PATH
from IndexData import IndexData


class Embeddings(IndexData):

    def __init__(self):
        """Initialize embeddings configuration and prepare document chunks."""
        super().__init__()
        self._openai_token = OPENAI_TOKEN
        self._chunks = self.get_chucnks()

    def instantiate_chromadb(self):
        """Build and persist a Chroma vector store from the prepared chunks."""

        embeddings = OpenAIEmbeddings(openai_api_key=self._openai_token)
        db_chroma = Chroma.from_documents(
            self._chunks, embeddings, persist_directory = CHROMA_PATH
        )

        return db_chroma
