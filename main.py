from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()


def generar_nombre_mascota():
    # Cargar la clave de API de OpenAI desde las variables de entorno
    openai_api_key = os.getenv("DEEPSEEK_API_KEY")
    openai_base_url = os.getenv("DEEPSEEK_API_URL")

    # Crear una instancia del modelo ChatOpenAI
    llm = ChatOpenAI(
        model_name="deepseek/deepseek-r1-distill-qwen-32b:free", 
        temperature=0.5, 
        api_key=openai_api_key,
        base_url=openai_base_url,
    )

    # Definir el prompt para generar un nombre de mascota
    prompt = "Genera un nombre original y divertido para una gata."

    # Generar el nombre de la mascota
    nombre_mascota = llm(prompt)

    return nombre_mascota.content


if __name__ == "__main__":
    print("Generando un nombre para tu mascota...")
    print(generar_nombre_mascota())
