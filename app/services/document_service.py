from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_document(file_path):

    # Remove surrounding quotes and whitespace
    file_path = file_path.strip().strip('"').strip("'")

    path = Path(file_path)

    print("Checking:", path)
    print("Exists:", path.exists())

    if not path.exists():
        raise FileNotFoundError(f"Document not found: {path}")

    extension = path.suffix.lower()

    if extension == ".pdf":
        loader = PyPDFLoader(str(path))

    elif extension == ".docx":
        loader = Docx2txtLoader(str(path))

    else:
        raise ValueError("Only PDF and DOCX files are supported")

    return loader.load()

def split_documents(documents):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = text_splitter.split_documents(documents)

    return chunks    