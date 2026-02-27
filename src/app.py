from fastapi import FastAPI, Request, Form, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
import os
import shutil
from src.rag_system import RAGSystem
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Sistema RAG Premium")

# Configurar estáticos y plantillas
# Asumimos que los archivos estarán en src/static
static_path = os.path.join(os.path.dirname(__file__), "static")
if not os.path.exists(static_path):
    os.makedirs(static_path)

app.mount("/static", StaticFiles(directory=static_path), name="static")

# Inicializar sistema RAG
rag = RAGSystem()

@app.on_event("startup")
async def startup_event():
    # Asegurarse de que la BD existe al arrancar
    if not os.path.exists(rag.db_dir):
        print("Creando base de datos inicial...")
        rag.create_database()
    rag.initialize_llm()

@app.get("/")
async def read_root():
    from fastapi.responses import FileResponse
    return FileResponse(os.path.join(static_path, "index.html"))

@app.post("/ask")
async def ask_rag(query: str = Form(...)):
    try:
        answer = rag.ask(query)
        return JSONResponse(content={"answer": answer})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        file_path = os.path.join(rag.data_dir, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Re-crear la base de datos con el nuevo archivo
        rag.create_database()
        rag.initialize_llm()
        
        return JSONResponse(content={"message": f"Archivo {file.filename} subido e indexado con éxito."})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
