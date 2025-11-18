# Organizador Inteligente de Fotos y Videos

Este es un Jupyter Notebook diseñado para automatizar la organización de grandes bibliotecas de fotos y videos
Funciona de manera modular, permitiendo detectar duplicados, limpiar copias accidentales y estructurar archivos por fecha

## Características

El script está dividido en 4 módulos independientes:

1.  **Escanear Archivos:** Inventario rápido de archivos multimedia (.jpg, .mp4, .raw, etc.)
2.  **Detector de Duplicados (Hash):** Compara el contenido real de los archivos (MD5) para encontrar duplicados exactos, incluso si tienen nombres diferentes.
3.  **Limpiador de Sufijos "_2":** Detecta y elimina archivos generados típicamente al copiar y pegar erróneamente (ej. `foto_2.jpg`).
4.  **Organización Cronológica:** Mueve los archivos a una estructura de carpetas ordenada automáticamente: `Año/Mes_Nombre` (ej. `2025/11_Noviembre`).

## Configuración

Antes de ejecutar, abre la **Celda 2** ("Configuración Global") y modifica las rutas:

```python
# Carpeta donde están tus fotos desordenadas
CARPETA_ORIGEN = Path(r"C:\Tu\Ruta\Origen")

# Carpeta donde quieres que se organicen
CARPETA_DESTINO = Path(r"D:\Tu\Ruta\Destino")
```
## Extra

Este pequeño proyecto nació de mi pasión por la fotografía y los videos con drones. 
Gestionar tal volumen de archivos solía ser una tarea tediosa y lenta, pero gracias a este programa, ahora organizar mis datos es un proceso rápido, automático y eficiente
