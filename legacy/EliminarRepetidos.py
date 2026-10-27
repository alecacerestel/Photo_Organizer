import os
from pathlib import Path

# Cambia esta ruta por la carpeta donde quieres eliminar los archivos
CARPETA_OBJETIVO = Path(r"E:\Fotos\2025")  # <-- ajusta esta ruta

def eliminar_archivos_duplicados(carpeta):
    count = 0
    for path in carpeta.rglob("*"):
        if path.is_file():
            nombre = path.stem
            if nombre.endswith("_2"):
                print(f"Eliminando: {path}")
                try:
                    path.unlink()
                    count += 1
                except Exception as e:
                    print(f"Error eliminando {path}: {e}")
    print(f"\nTotal de archivos eliminados: {count}")

if __name__ == "__main__":
    eliminar_archivos_duplicados(CARPETA_OBJETIVO)
