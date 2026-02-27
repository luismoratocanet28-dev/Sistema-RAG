# 🤖 Sistema RAG Premium: Retrieval-Augmented Generation

[![Python Version](https://img.shields.io/badge/python-3.14%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0%2B-green.svg)](https://fastapi.tiangolo.com/)
[![LangChain](https://img.shields.io/badge/LangChain-Enabled-orange.svg)](https://www.langchain.com/)

Un sistema avanzado de **Generación Aumentada por Recuperación (RAG)** diseñado para interactuar de forma inteligente con tus documentos locales. Este sistema combina la potencia de modelos de lenguaje de gran tamaño (LLMs) con una base de datos vectorial eficiente para proporcionar respuestas precisas y contextualmente relevantes.

---

## 🌟 Características Principales

- **📂 Gestión Inteligente de Documentos**: Sube y procesa archivos PDF y de texto de forma dinámica.
- **🔍 Recuperación de Alta Precisión**: Utiliza **FAISS** y **Embeddings de HuggingFace** para una búsqueda semántica ultrarrápida.
- **⚡ Interfaz Moderna**: Aplicación web construida con FastAPI y una interfaz intuitiva con efectos de "glassmorphism".
- **🤖 LLM Integrado**: Configurado para usar OpenAI (GPT-4/GPT-3.5) para una generación de lenguaje natural fluida.
- **📄 Generación de Informes**: Script especializado para generar memorias de proyecto automáticas en formato Word.

---

## 🛠️ Tecnologías Utilizadas

| Componente | Tecnología |
| :--- | :--- |
| **Backend** | Python, FastAPI, Uvicorn |
| **IA Framework** | LangChain |
| **Vector DB** | FAISS / ChromaDB |
| **Embeddings** | HuggingFace (Sentence Transformers) |
| **Frontend** | HTML5, CSS3 (Glassmorphism), Vanilla JS |
| **Documentación** | python-docx |

---

## 🚀 Instalación y Configuración

### 1. Clonar el repositorio
```bash
git clone https://github.com/luismoratocanet28-dev/Sistema-RAG.git
cd Sistema-RAG
```

### 2. Instalar dependencias
Se recomienda usar un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configurar variables de entorno
Crea un archivo `.env` en la raíz del proyecto basándote en `.env.example`:
```env
OPENAI_API_KEY=tu_clave_aqui
```

---

## 📖 Modo de Uso

### Iniciar el Servidor Web
Ejecuta la aplicación principal para lanzar la interfaz web:
```bash
python src/app.py
```
Accede a `http://localhost:8000` en tu navegador.

### Generar Documentación del Proyecto
Si deseas generar la memoria técnica del proyecto:
```bash
python src/generate_docs.py
```

---

## 📁 Estructura del Proyecto

```text
Sistema-RAG/
├── data/               # Documentos fuente (PDF, TXT)
├── docs/               # Documentación y planos de implementación
├── faiss_index/        # Base de datos vectorial persistente
├── src/                # Código fuente correlacionado
│   ├── app.py          # Aplicación FastAPI y servidor
│   ├── rag_system.py   # Lógica central del sistema RAG
│   └── generate_docs.py # Utilidad de generación de informes
├── requirements.txt    # Dependencias del proyecto
└── .env.example        # Plantilla para configuración
```

---

## 🤝 Créditos

Este sistema ha sido desarrollado como un proyecto industrial premium para **Luis Morato Canet**, con la asistencia técnica de **Antigravity AI**.

---

© 2026 Sistema RAG - Eficiencia Industrial S.L.
