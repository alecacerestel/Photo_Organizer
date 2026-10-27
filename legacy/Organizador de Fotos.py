import os
import shutil
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime
from pathlib import Path

# Ruta raíz
ROOT_DIR = Path(r"C:\Users\Alejandro\Documents\Fotos_Videos")

# Meses en español
MESES = {
    1: "enero", 2: "febrero", 3: "marzo", 4: "abril",
    5: "mayo", 6: "junio", 7: "julio", 8: "agosto",
    9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"
}

# Extensiones válidas (puedes agregar más si deseas)
VALID_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.mp4', '.mov', '.avi', '.mkv', '.heic'}

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
