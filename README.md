# Sistema RAG (Retrieval-Augmented Generation)

Este proyecto implementa un sistema RAG básico utilizando **LangChain**, un framework para construir aplicaciones con modelos de lenguaje.

## Características
- **Carga de Documentos**: Soporta archivos de texto y PDF en la carpeta `data/`.
- **Embeddings Locales**: Utiliza modelos de HuggingFace para transformar texto en vectores sin coste.
- **Base de Datos Vectorial**: Usa ChromaDB para almacenar y recuperar información eficientemente.
- **Generación**: Integrado con OpenAI para dar respuestas basadas en el contexto recuperado.

## Requisitos
- Python 3.14+
- Una clave de API de OpenAI (configurada en un archivo `.env`).

## Instalación
```bash
pip install -r requirements.txt
```

## Uso
1. Coloca tus archivos en la carpeta `data/`.
2. Ejecuta el script principal para crear la base de datos:
   ```bash
   python src/rag_system.py
   ```
3. Genera el informe de trabajo:
   ```bash
   python src/generate_docs.py
   ```

## Estructura del Proyecto
- `src/`: Código fuente del sistema y generador de documentación.
- `data/`: Folder para los documentos de conocimiento.
- `docs/`: Plan de ejecución y otros recursos.
- `chroma_db/`: Ubicación de la base de datos persistente (ignorada en git).

## Créditos
Desarrollado con la asistencia de **Antigravity AI** para Luis Morato Canet.
