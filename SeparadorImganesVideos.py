import os
import shutil  # Para mover archivos y directorios
import argparse  # Para manejar argumentos de línea de comandos
from rich import print as rprint  # Para imprimir mensajes con formato y colores

# Importa las extensiones de archivos desde un módulo externo
from extensiones import EXTENSIONES


def separar_archivos(carpeta_original, verbose=False):
    """
    Separa archivos en la carpeta original en dos subcarpetas: "FOTOS" y "VIDEOS".
    Los archivos se mueven a la carpeta correspondiente según su extensión. 

    Parámetros:
    carpeta_original (str): Ruta a la carpeta que contiene los archivos a separar.
    verbose (bool): Si es True, imprime mensajes detallados sobre los archivos movidos.
    """
    # Definir rutas para las carpetas de destino
    carpeta_fotos = os.path.join(carpeta_original, "FOTOS")
    carpeta_videos = os.path.join(carpeta_original, "VIDEOS")

    # Crear las carpetas "FOTOS" y "VIDEOS" si no existen
    for carpeta in [carpeta_fotos, carpeta_videos]:
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

    # Obtener la lista de archivos en la carpeta original
    archivos = os.listdir(carpeta_original)

    # Copiar las extensiones de imágenes y videos desde el módulo EXTENSIONES
    extensiones_imagenes = EXTENSIONES.IMAGENES.copy()
    extensiones_videos = EXTENSIONES.VIDEOS.copy()

    # Recorrer cada archivo en la carpeta original
    for archivo in archivos:
        # Obtener la extensión del archivo (en minúsculas para comparación)
        _, extension = os.path.splitext(archivo.lower())

        # Construir la ruta completa del archivo
        ruta_archivo = os.path.join(carpeta_original, archivo)

        # Determinar si el archivo es una imagen o un video y moverlo a la carpeta correspondiente
        if extension in extensiones_imagenes:
            shutil.move(ruta_archivo, os.path.join(carpeta_fotos, archivo))
            if verbose:
                print(f"Se movió '{archivo}' a la carpeta 'FOTOS'")
        elif extension in extensiones_videos:
            shutil.move(ruta_archivo, os.path.join(carpeta_videos, archivo))
            if verbose:
                print(f"Se movió '{archivo}' a la carpeta 'VIDEOS'")
        elif os.path.isdir(ruta_archivo):
            rprint("[yellow]" + f"'{archivo}' es un directorio" + "[/yellow]")
        else:
            rprint(
                "[red]" + f"El archivo '{archivo}' no es una imagen ni un video y no se movió." + "[/red]")


def main():
    """
    Función principal que configura el análisis de argumentos de línea de comandos
    y llama a la función separar_archivos con los argumentos proporcionados.
    """
    # Crear el objeto ArgumentParser para manejar los argumentos de línea de comandos
    parser = argparse.ArgumentParser(
        description='Organiza archivos en carpetas "FOTOS" y "VIDEOS" basándose en su extensión.')

    # Agregar parámetro para la opción verbose
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='Imprimir mensajes detallados sobre el proceso.')

    # Agregar argumento posicional para la ruta de la carpeta de entrada
    parser.add_argument('input', type=str,
                        help='Ruta a la carpeta que contiene los archivos a organizar.')

    # Parsear los argumentos de la línea de comandos
    args = parser.parse_args()

    # Llamar a la función separar_archivos con los argumentos proporcionados
    separar_archivos(args.input, args.verbose)


if __name__ == "__main__":
    main()
