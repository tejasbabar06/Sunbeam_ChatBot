from langchain_community.document_loaders import DirectoryLoader, TextLoader

def load_documents(path):
    loader = DirectoryLoader(
        path,
        glob="**/*.txt",
        loader_cls=TextLoader,
        show_progress=True
    )
    return loader.load()
