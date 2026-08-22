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
        ".msi": "Basura",
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

carpet = Path.home() / "Downloads"
print (Path.exists(carpet))

Name = carpet.iterdir()

for Name in carpet.iterdir():
    print(Name.name, Name.is_file(), Name.suffix)
     

    if Name.is_file() == False:
        print("Esto no es un archivo")
        continue
        print(categoria[Name.suffix])

destino = categoria[Name.suffix]
final = carpet / destino 
destino = final.mkdir(exist_ok=True)
carpet.rename(final / Name.name)

print("Archivos organizados correctamente")
  
    





