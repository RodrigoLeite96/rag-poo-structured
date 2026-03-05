import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from utils.variables import (
    OPENAI_TOKEN
)
from Embeddings import Embeddings

if __name__ == "__main__":

    emb = Embeddings()
    db = emb.instantiate_chromadb()
    
    query = "INSERT YOUR QUESTION HERE"

    docs_chroma = db.similarity_search_with_score(query, k=5)

    context_text = "\n\n".join([doc.page_content for doc, _score in docs_chroma])

    PROMPT_TEMPLATE = """
    Answer the question based only on the following context:
    {context}
    Answer the question based on the above context: {question}.
    Provide a detailed answer.
    """

    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query)

    model = ChatOpenAI(openai_api_key=OPENAI_TOKEN)
    response = model.invoke(prompt)
    response_text = response.content

    print(response_text)
