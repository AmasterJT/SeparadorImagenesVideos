import os
import shutil
import argparse

from rich import print as rprint

from extensiones import EXTENSIONES


def separar_archivos(carpeta_original, verbose: False):

    carpeta_fotos = carpeta_original + "/FOTOS"
    carpeta_videos = carpeta_original + "/VIDEOS"
    # Crear las carpetas "FOTOS" y "VIDEOS" si no existen
    for carpeta in [carpeta_fotos, carpeta_videos]:
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

    # Obtener la lista de archivos en la carpeta original
    archivos = os.listdir(carpeta_original)

    # Extensiones comunes de imágenes
    extensiones_imagenes = EXTENSIONES.IMAGENES.copy()
    # Extensiones comunes de videos
    extensiones_videos = EXTENSIONES.VIDEOS.copy()

    # Recorrer cada archivo en la carpeta original
    for archivo in archivos:
        # Obtener la extensión del archivo
        _, extension = os.path.splitext(archivo.lower())

        # Construir la ruta completa del archivo
        ruta_archivo = os.path.join(carpeta_original, archivo)

        # Determinar si es una imagen o un video y moverlo a la carpeta correspondiente
        if extension in extensiones_imagenes:
            shutil.move(ruta_archivo, os.path.join(carpeta_fotos, archivo))
            if verbose:
                print(f"Se movió '{archivo}' a la carpeta 'FOTOS'")
        elif extension in extensiones_videos:
            shutil.move(ruta_archivo, os.path.join(carpeta_videos, archivo))
            if verbose:
                print(f"Se movió '{archivo}' a la carpeta 'VIDEOS'")
        elif os.path.isdir(carpeta_original + f"\{archivo}"):
            rprint("[yellow]" + f"'{archivo}' es un diretorio" + "[/yellow]")
        else:
            rprint("[red]" +
                   f"El archivo '{archivo}' no es una imagen ni un video y no se movió."+"[/red]")


def main():

    # Crear el objeto ArgumentParser
    parser = argparse.ArgumentParser(
        description='Descripción de lo que hace el script.')

    # Agregar parametros
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='Imprimir mensajes detallados.')
    # Agregar argumentos
    parser.add_argument('input', type=str,
                        help='Ruta del archivo de la carpeta.')

    # Parsear los argumentos
    args = parser.parse_args()

    separar_archivos(
        args.input, args.verbose)


if __name__ == "__main__":
    # Especifica la ruta de la carpeta original y las carpetas de destino
    # ruta_carpeta_original = "D:\Imágenes\imágenes-iphone8-2024"
    # ruta_carpeta_fotos = "ruta/a/tu/carpeta/FOTOS"
    # ruta_carpeta_videos = "ruta/a/tu/carpeta/VIDEOS"

    # Llama a la función para separar los archivos
    # separar_archivos(ruta_carpeta_original)

    main()
