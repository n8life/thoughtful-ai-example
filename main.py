import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader, JSONLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain import hub

load_dotenv()

def main():
    print("Welcome to the Thoughtful AI CLI Assistant.  Type 'exit' to quit.")
    json_path = "./data.json"

    # Use jq_schema to extract each question-answer pair from the questions array
    loader = JSONLoader(
        file_path=json_path,
        jq_schema='.questions[]',
        text_content=False,  # Load as metadata, not just text
        json_lines=False  # Since it's a regular JSON file, not JSONL
    )
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=30)
    docs = text_splitter.split_documents(documents=documents)

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local("faiss_index_react")

    new_vectorstore = FAISS.load_local(
        "faiss_index_react",
        embeddings,
        allow_dangerous_deserialization=True
    )

    retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")

    combine_docs_chain = create_stuff_documents_chain(
        OpenAI(temperature=0), retrieval_qa_chat_prompt
    )

    retrieval_chain = create_retrieval_chain(
        new_vectorstore.as_retriever(), combine_docs_chain,
    )

    while True:
        question = input("Ask a question: ")

        if question == "exit":
            break
        res = retrieval_chain.invoke({"input": question})

        print(res["answer"])


if __name__ == "__main__":
    main()
