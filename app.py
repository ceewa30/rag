from src.data_loader import load_all_documents

if __name__ == "__main__":
    data_directory = "./data"  # Adjust the path as needed
    docs = load_all_documents(data_directory)
    print(f"Total documents loaded: {len(docs)}")
    for i, doc in enumerate(docs):
        print(f"Document {i+1} : {doc.metadata}")
