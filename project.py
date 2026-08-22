import os 
from pathlib import Path   

categoria = {
        ".jpg": "Imagenes",
        ".png": "Imagenes",
        ".jpeg": "Imagenes",
        ".webp": "Imagenes",
        ".psd": "Imagenes",
        ".mp3": "Audio",
        ".mp4": "Audio",
        ".wav": "Audio",
        ".zip": "Compreso",
        ".exe": "Ejecutable",
        ".pdf": "Documento",
        ".docx": "Documento",
        ".csv": "Documento",
        ".rar": "Compreso",
        ".iso": "Iso's",
        ".txt": "Documento",
        ".odt": "Documento",
        ".pptx": "Documento",
        ".url": "Documento",
        ".msi": "Basura",
        ".msix": "Basura",
        ".py": "Codigo",
        ".js": "Codigo",
        ".html": "Codigo",
        ".css": "Codigo",
        ".cs": "Codigo",
        ".ts": "Codigo",
        ".php": "Codigo",
        ".c": "Codigo",
        ".cpp": "Codigo",
        ".java": "Codigo",
        ".kt": "Codigo",
        ".go": "Codigo"
}

numero = 0
carpet = Path.home() / "Downloads"
print (Path.exists(carpet))

Name = carpet.iterdir()

for numero, Name in enumerate(carpet.iterdir(), start=1,):
    print(numero, Name.name, Name.suffix)

    if Name.is_file() == False or not Name.suffix in categoria:
        print("Esto no es un archivo o el archivo no se encontro")
        continue
    else:
        print(categoria[Name.suffix])
        #destino = categoria[Name.suffix]
        #final = carpet / destino 
        #destino = final.mkdir(exist_ok=True)
       # Name.rename(final / Name.name)

#print("Archivos organizados correctamente")
  
    





