# Organizador Inteligente de Fotos y Videos

Este es un Jupyter Notebook diseñado para automatizar la organización de grandes bibliotecas de fotos y videos
Funciona de manera modular, permitiendo detectar duplicados, limpiar copias accidentales y estructurar archivos por fecha

Pensado para: **Fujifilm X-T30 II**, **DJI Mini 3 Pro** e **iPhone 13**, en **macOS** con una SSD externa en formato exFAT.

## Características

El notebook está dividido en 4 módulos independientes:

1.  **Escanear Archivos:** Inventario rápido de archivos multimedia (.jpg, .heic, .raf, .dng, .mp4, .mov, etc.). Ignora los archivos ocultos que crea macOS (`._foto.jpg`, `.DS_Store`).
2.  **Detector de Duplicados (Hash):** Compara el contenido real de los archivos (MD5) para encontrar duplicados exactos, incluso si tienen nombres diferentes.
3.  **Limpiador de Copias Accidentales:** Elimina archivos como `foto_2.jpg`, `foto 2.jpg` o `foto copia.jpg`, **solo si son idénticos al original**.
4.  **Organización Cronológica:** Mueve los archivos a `Año/Mes_Nombre` (ej. `2025/11_Noviembre`) usando la **fecha real de captura** (EXIF en fotos, metadatos en videos). Las Live Photos, RAW+JPG y archivos acompañantes (.AAE, .SRT, .LRF) se mueven juntos.

Todos los módulos empiezan en modo simulación (`DRY_RUN = True`): muestran lo que harían sin tocar nada.

## Instalación (macOS)

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

Después, en VS Code, abre `Gestor de Fotos.ipynb` y selecciona el kernel `.venv`.

## Configuración

Antes de ejecutar, abre la celda de **Configuración Global** y modifica las rutas:

```python
# Nombre de tu SSD externa tal como aparece en Finder
NOMBRE_SSD = "MiSSD"

# Carpeta donde están tus fotos desordenadas
CARPETA_ORIGEN = Path.home() / "Documents" / "Fotos_Videos"

# Carpeta donde quieres que se organicen
CARPETA_DESTINO = Path("/Volumes") / NOMBRE_SSD / "Fotos"
```

## Versiones anteriores

La carpeta `legacy/` guarda los scripts originales de Windows. Ya no se usan.

## Extra

Este pequeño proyecto nació de mi pasión por la fotografía y los videos con drones. 
Gestionar tal volumen de archivos solía ser una tarea tediosa y lenta, pero gracias a este programa, ahora organizar mis datos es un proceso rápido, automático y eficiente
