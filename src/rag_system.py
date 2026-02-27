import os
import shutil
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

class RAGSystem:
    def __init__(self, data_dir="data", db_dir="faiss_index", model_name="all-MiniLM-L6-v2"):
        self.data_dir = data_dir
        self.db_dir = db_dir
        self.embeddings = HuggingFaceEmbeddings(model_name=model_name)
        self.vector_store = None
        self.llm = None

    def create_database(self):
        """Carga documentos, los divide y crea la base de datos vectorial."""
        print(f"Cargando documentos desde {self.data_dir}...")
        
        loader = DirectoryLoader(self.data_dir, glob="./*.*", loader_cls=TextLoader)
        documents = loader.load()
        
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = text_splitter.split_documents(documents)
        
        print(f"Creados {len(chunks)} fragmentos. Indexando con FAISS...")
        
        self.vector_store = FAISS.from_documents(
            documents=chunks, 
            embedding=self.embeddings
        )
        self.vector_store.save_local(self.db_dir)
        print("Base de datos vectorial (FAISS) creada con éxito.")

    def initialize_llm(self, api_key=None):
        """Inicializa el modelo de lenguaje."""
        if not self.vector_store:
            if os.path.exists(self.db_dir):
                self.vector_store = FAISS.load_local(
                    self.db_dir, 
                    self.embeddings, 
                    allow_dangerous_deserialization=True
                )
            else:
                raise Exception("La base de datos no existe. Ejecuta create_database() primero.")
        
        os.environ["OPENAI_API_KEY"] = api_key or os.getenv("OPENAI_API_KEY", "tu_api_key_aqui")
        self.llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    def ask(self, query):
        """Realiza una consulta al sistema RAG manual."""
        if not self.llm:
            return "El LLM no está inicializado. Configura tu API Key de OpenAI."
        
        # 1. Recuperar documentos relevantes
        docs = self.vector_store.similarity_search(query, k=3)
        context = "\n\n".join([doc.page_content for doc in docs])
        
        # 2. Construir el prompt
        template = """Eres un asistente servicial. Responde a la pregunta basándote únicamente en el contexto proporcionado.
        
        Contexto:
        {context}
        
        Pregunta: {query}
        
        Respuesta:"""
        
        prompt = ChatPromptTemplate.from_template(template)
        chain = prompt | self.llm
        
        try:
            response = chain.invoke({"context": context, "query": query})
            return response.content
        except Exception as e:
            return f"Error al procesar la consulta: {str(e)}"

if __name__ == "__main__":
    rag = RAGSystem()
    rag.create_database()
    
    print("\n--- Sistema RAG Listo ---")
    print("Nota: Necesitas una OPENAI_API_KEY para generar respuestas finales.")
