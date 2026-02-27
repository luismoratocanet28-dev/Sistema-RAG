# Plan de Implementación: Sistema RAG (Retrieval-Augmented Generation)

Este documento detalla los pasos para crear el sistema RAG solicitado y la documentación asociada.

## 1. Diseño del Sistema
*   **Lenguaje:** Python
*   **Framework de RAG:** LangChain (estándar de la industria).
*   **Base de Datos Vectorial:** ChromaDB (ligera y local).
*   **Embeddings:** HuggingFace (Local) para evitar costes de API iniciales.
*   **LLM:** Configurable para usar OpenAI o modelos locales.
*   **Documentación:** Generación de un archivo Word (.docx) detallando el proceso.

## 2. Fases de Trabajo

### Fase 1: Configuración del Entorno
- [ ] Crear estructura de directorios (`data/`, `src/`, `docs/`).
- [ ] Crear archivo `requirements.txt`.
- [ ] Instalar dependencias necesarias.

### Fase 2: Desarrollo del Sistema RAG
- [ ] Implementar cargador de documentos (PDF, TXT).
- [ ] Implementar sistema de fragmentación (Text Splitting).
- [ ] Configurar el almacenamiento vectorial con ChromaDB.
- [ ] Crear la lógica de recuperación (Retrieval) y respuesta (Generation).

### Fase 3: Documentación en Word
- [ ] Crear script para generar el archivo `Proceso_Sistema_RAG.docx`.
- [ ] Incluir: Introducción, Herramientas (Antigravity), Opciones consideradas y Decisión final.

### Fase 4: Despliegue en GitHub
- [ ] Inicializar repositorio Git local.
- [ ] Crear `.gitignore` y `README.md`.
- [ ] Guiar al usuario para conectar con su cuenta de GitHub.

## 3. Posibilidades y Solución Escogida (Breve resumen)
*   **Posibilidad A:** RAG 100% Cloud (OpenAI + Pinecone). *Coste asociado y dependencia de internet.*
*   **Posibilidad B:** RAG Híbrido (LangChain + ChromaDB + Embeddings Locales). *Privacidad, bajo coste y alta flexibilidad.*
*   **Solución:** Se ha escogido la **Opción B** por ser ideal para desarrollo educativo e investigación personal sin costes fijos.
