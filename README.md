# Thermo Table Reader (RAG)

This application reads a thermodynamics PDF, creates embeddings, stores them in ChromaDB, and answers a question using OpenAI via LangChain.

## Project Flow

1. `LoadPDF.py` loads the PDF from `documents/tabelas-thermo.pdf`.
2. `IndexData.py` splits pages into chunks.
3. `Embeddings.py` creates embeddings and persists vectors in `vector-db/`.
4. `app.py` runs similarity search and sends the retrieved context to the LLM.

## Requirements

- Python 3.10+
- OpenAI API key

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies inside the virtual environment:

```bash
pip install -r requirements.txt
```

## Configuration

Edit `utils/variables.py`:

- `OPENAI_TOKEN`: your OpenAI API key
- `DOC_PATH`: PDF path (default: `./documents/tabelas-thermo.pdf`)
- `CHROMA_PATH`: vector DB directory (default: `vector-db`)

## Run

In `app.py`, set:

```python
query = "INSERT YOUR QUESTION HERE"
```

Then run:

```bash
python app.py
```

The script will:

- build/update Chroma vectors from the PDF chunks
- retrieve the top-5 relevant chunks
- print the final answer in the terminal

## Main Files

- `app.py`: entrypoint and LLM call
- `LoadPDF.py`: PDF loading
- `IndexData.py`: chunking logic
- `Embeddings.py`: embedding + Chroma persistence
- `utils/variables.py`: runtime variables

## Notes

- `vector-db/` is generated/persisted local data.
- If API/auth errors happen, verify `OPENAI_TOKEN`.
- If PDF path errors happen, verify `DOC_PATH`.
