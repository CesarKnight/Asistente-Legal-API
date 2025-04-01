from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain 
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()


def inicializar_llm() -> ChatOpenAI:
    openai_api_key = os.getenv("DEEPSEEK_API_KEY")
    openai_base_url = os.getenv("DEEPSEEK_API_URL")
    openai_model = os.getenv("LLM_MODEL")
    
    # Crear una instancia del modelo ChatOpenAI
    llm = ChatOpenAI(
        model_name= openai_model,
        temperature=0.5, 
        api_key=openai_api_key,
        base_url=openai_base_url,
    )
    
    return llm

def crear_vector_db() -> FAISS:
    
    loader = TextLoader("E:/Code/Python/Asistente-Legal-API/App/leyes/reglamento_codigo_de_transito.txt" , encoding='utf-8')
    leyes = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(leyes)
    
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    db = FAISS.from_documents(docs, embeddings)
    return db

def obtener_respuesta_query(db : FAISS, query, kdocs = 4):
    #segun openrouter puede hacer 16k tokens pero pongamos que tengo 2k tokens
    
    docs = db.similarity_search(query=query, k=kdocs)
    docs_page_content = " ".join([doc.page_content for doc in docs] )
    
    llm = inicializar_llm()
    
    prompt = PromptTemplate(
        input_variables=["question", "context"],
        template="""
        Responde exclusivamente en español. 
        Eres un asistente legal que puede responder preguntas sobre el 
        reglamento de tránsito boliviano.
        
        Responde a la siguiente pregunta: {question}
        Usa la siguiente información como referencia: {context}
        
        Usa solamente información de la referencia para responder.
        en caso de que no encuentres la respuesta en la referencia,
        responde con "No tengo información sobre eso".

        En tu respuesta referencia el articulo que corresponda a tu respuesta.
        """
    )
    
    chain = LLMChain(llm=llm, prompt=prompt)
    respuesta = chain.run(question=query, context=docs_page_content) 
    respuesta = respuesta.replace("\n", " ")
    return docs_page_content, respuesta

base = crear_vector_db()
query = "¿Que dice el artículo 115?"
respuesta = obtener_respuesta_query(base, query)
print(respuesta)
