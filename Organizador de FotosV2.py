"""
Este script tiene como objetivo organizar automáticamente archivos de fotos y videos
almacenados en diferentes carpetas y subcarpetas dentro de un directorio raíz especificado 
(por defecto, "C:\\Users\\Alejandro\\Documents\\Fotos_Videos").

Funcionalidad principal:
------------------------
El programa escanea de manera recursiva todos los archivos dentro de las carpetas hijas del 
directorio raíz. Para cada archivo, intenta obtener la fecha de creación del contenido. 
En el caso de imágenes JPEG, se intenta extraer la fecha desde los metadatos EXIF. 
Si no es posible, o si se trata de otro tipo de archivo (como videos o imágenes sin EXIF), 
se utiliza la fecha de modificación del sistema de archivos como respaldo.

Una vez obtenida la fecha, el script crea automáticamente una estructura de carpetas basada 
en el año y el mes correspondiente. Por ejemplo, un archivo con fecha de 15 de marzo de 2024 
será movido a la carpeta "2024/marzo". Esta estructura se genera dentro del mismo directorio raíz 
y se crean nuevas carpetas según sea necesario.

El script también evita sobrescribir archivos con nombres duplicados en las carpetas destino. 
Si un archivo con el mismo nombre ya existe, se añade un número incremental al nombre del archivo 
(archivo_1.jpg, archivo_2.jpg, etc.).

Tipos de archivos soportados:
-----------------------------
Se consideran válidas las extensiones comunes de imágenes y videos: .jpg, .jpeg, .png, .mp4, 
.mov, .avi, .mkv, .heic. Este listado puede ser fácilmente ampliado según las necesidades.

Requisitos:
-----------
- Python 3.x
- Biblioteca externa `Pillow` para leer metadatos EXIF de las imágenes JPEG.
  Puede instalarse con el comando: pip install pillow

Este programa es útil para fotógrafos, creadores de contenido o cualquier usuario que quiera 
organizar grandes cantidades de fotos y videos dispersos en diferentes carpetas, estructurándolos 
de forma cronológica para facilitar su almacenamiento, respaldo o visualización.
"""

import os
import shutil
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime
from pathlib import Path

# Ruta raíz
ROOT_DIR = Path(r"E:\Fotos")

# Meses en español
MESES = {
    1: "enero", 2: "febrero", 3: "marzo", 4: "abril",
    5: "mayo", 6: "junio", 7: "julio", 8: "agosto",
    9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"
}

# Extensiones válidas (puedes agregar más si deseas)
VALID_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.mp4', '.mov', '.avi', '.mkv', '.heic', '.webp', '.AAE'}

def get_exif_date(path):
    try:
        image = Image.open(path)
        exif_data = image._getexif()
        if exif_data is None:
            return None
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id)
            if tag == 'DateTimeOriginal':
                return datetime.strptime(value, '%Y:%m:%d %H:%M:%S')
    except Exception:
        return None
    return None

def get_file_date(path):
    ext = path.suffix.lower()
    if ext in {'.jpg', '.jpeg'}:
        date = get_exif_date(path)
        if date:
            return date
    # Si no hay metadata, usar fecha de modificación del archivo
    timestamp = path.stat().st_mtime
    return datetime.fromtimestamp(timestamp)

def organize_files():
    for root, _, files in os.walk(ROOT_DIR):
        for file in files:
            path = Path(root) / file
            if path.suffix.lower() not in VALID_EXTENSIONS:
                continue
            try:
                date = get_file_date(path)
                if not date:
                    print(f"No se pudo determinar fecha para: {path}")
                    continue

                year = str(date.year)
                month = MESES[date.month]
                dest_dir = ROOT_DIR / year / month
                dest_dir.mkdir(parents=True, exist_ok=True)

                new_path = dest_dir / path.name

                # Evitar sobreescritura de archivos con mismo nombre
                counter = 1
                while new_path.exists():
                    new_name = f"{path.stem}_{counter}{path.suffix}"
                    new_path = dest_dir / new_name
                    counter += 1

                shutil.move(str(path), str(new_path))
                print(f"Movido: {path} → {new_path}")
            except Exception as e:
                print(f"Error procesando {path}: {e}")

if __name__ == "__main__":
    organize_files()
