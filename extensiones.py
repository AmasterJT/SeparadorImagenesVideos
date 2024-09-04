class EXTENSIONES:
    """
    Esta clase `EXTENSIONES` contiene dos listas estáticas de extensiones de archivos para imágenes y videos.
    Estas listas están diseñadas para ser utilizadas en aplicaciones que requieren la identificación
    y clasificación de archivos de imagen y video basados en sus extensiones.

    Atributos:
    ----------
    IMAGENES : list
        Lista de extensiones de archivos que corresponden a formatos de imágenes.
        Incluye formatos rasterizados, vectoriales, formatos RAW de cámaras,
        formatos especializados, gráficos 3D, videojuegos, y otros formatos
        menos comunes, así como algunos formatos de archivo comprimido.

    VIDEOS : list
        Lista de extensiones de archivos que corresponden a formatos de video.
        Incluye formatos comunes y profesionales, formatos específicos de cámaras,
        videojuegos, transmisión en línea, multimedia y otros formatos antiguos o menos comunes.
    """

    IMAGENES = [
        # Formatos comunes rasterizados
        '.jpg', '.jpeg', '.png', '.bmp', '.heic', '.tiff', '.tif', '.webp',
        '.ico', '.svg', '.psd', '.xcf', '.hdr', '.exr', '.jxr', '.jp2', '.j2k',
        '.jpf', '.jpx', '.jpm', '.pgm', '.ppm', '.pbm', '.pcx', '.dds', '.pict',
        '.pct', '.tga', '.icns', '.cur', '.svgz', '.pgf',

        # Formatos RAW de cámaras
        '.raw', '.cr2', '.nef', '.orf', '.sr2', '.arw', '.dng', '.raf', '.3fr',
        '.erf', '.mef', '.mos', '.pef', '.rw2', '.rwl', '.srw', '.x3f',

        # Formatos vectoriales
        '.ai', '.eps', '.emf', '.wmf', '.cdr', '.odg', '.vml', '.emz', '.zvr',
        '.pov', '.vrml', '.dwg', '.dxf', '.cgm', '.svf', '.plt', '.stl', '.skp',

        # Formatos especializados y científicos
        '.dicom', '.dcm',  # Imágenes médicas (DICOM)
        '.fits', '.fts',   # Formatos para imágenes científicas y astronómicas
        '.img', '.ima',    # Generalmente usadas en imágenes médicas y científicas
        '.sid',            # Archivo MrSID, usado en imágenes geoespaciales
        '.ras',            # Sun Rasterfile
        '.img',            # Imagen de disco, pero también puede usarse para gráficos
        '.psb',            # Photoshop Big, similar a PSD pero para archivos grandes
        # Formato de imagen TIFF para el almacenamiento de gráficos de alta calidad
        '.btf', '.btif',

        # Formatos de videojuegos y gráficos 3D
        '.dds',            # DirectDraw Surface, usado en texturas de videojuegos
        '.mdl',            # Modelos 3D
        '.mtl',            # Material files for 3D objects
        '.obj',            # Formato de objeto 3D
        '.ply',            # Polygon File Format (modelos 3D)
        '.fbx',            # Autodesk FBX, usado para animación y gráficos 3D
        '.3ds',            # Formato 3D Studio
        '.max',            # Autodesk 3ds Max
        '.blend',          # Blender 3D
        '.c4d',            # Cinema 4D

        # Otros formatos de imagen menos comunes
        '.afphoto',        # Affinity Photo
        '.apng',           # Animated PNG
        '.ani',            # Animated cursor
        '.art',            # AOL ART
        '.blp',            # Blizzard Texture file
        '.cd5',            # Chasys Draw Image
        '.djvu',           # DjVu, usado para escaneos de alta compresión
        '.flif',           # Free Lossless Image Format
        '.icon',           # Íconos generales
        '.jp2',            # JPEG 2000, variante de JPEG con mejor compresión
        '.mng',            # Multiple-image Network Graphics (animación)
        '.pcd',            # Kodak Photo CD
        '.pic',            # PICT file
        '.psp',            # PaintShop Pro image
        '.qoi',            # Quite OK Image format
        '.ras',            # Sun Rasterfile
        '.sgi',            # Silicon Graphics Image
        '.xpm',            # X PixMap
        '.yuv',            # Imágenes YUV para procesamiento de video
        '.viff',           # Visualization Image File Format
        '.wbmp',           # Wireless Bitmap
        '.jbig',           # Joint Bi-level Image Group
        '.jbig2',          # JBIG2 para imágenes monocromáticas comprimidas
        '.rgbe',           # Radiance RGBE
        '.ff',             # Farbfeld, un formato simple sin pérdidas
        '.bpg',            # Better Portable Graphics, un formato de alta compresión

        # Formatos de archivo comprimido
        # Aunque son formatos de archivo comprimido, a veces contienen imágenes en su interior.
        '.gz', '.bz2', '.tar', '.zip',
    ]

    # ==================================================================================================
    # ==================================================================================================
    # ==================================================================================================
    # ==================================================================================================

    VIDEOS = [
        # Formatos comunes y populares
        '.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.f4v', '.webm',
        '.mpg', '.mpeg', '.m4v', '.3gp', '.3g2', '.mts', '.m2ts', '.ts',
        '.vob', '.mxf', '.ogv', '.rm', '.rmvb', '.asf', '.swf', '.divx',
        '.xvid', '.dv', '.mpe', '.mpv', '.m2v', '.qt', '.skm', '.yuv',
        '.h264', '.h265', '.hevc', '.amv', '.drc', '.f4p', '.f4a', '.f4b',
        '.vro', '.ism', '.ismv', '.m1v', '.m4p', '.bik', '.smk', '.mk3d',
        '.mjp', '.nsv', '.roq', '.rv',

        # Formatos profesionales y de cámaras
        '.avs',         # AVS Video
        '.cam',         # Video de cámara cruda
        '.m2p',         # MPEG-2 Program Stream
        '.m2t',         # MPEG-2 Transport Stream
        '.m2ts',        # MPEG-2 Blu-ray Transport Stream
        '.mod',         # Formato de video de cámaras de JVC, Canon y Panasonic
        '.tod',         # Video de alta definición de cámaras JVC
        '.fli',         # Autodesk Animator video
        '.flc',         # Autodesk FLC Animation file
        '.mpsub',       # MicroDVD video file
        '.dif',         # Digital Interface Format (video)
        '.ivr',         # RealPlayer Video Recording
        '.wve',         # Wondershare Video Editor project file

        # Formatos específicos de cámaras y transmisión
        '.ssif',        # Stereoscopic Interleaved Video (Blu-ray 3D)
        '.str',         # PlayStation video stream
        '.mpl',         # AVCHD playlist file
        '.braw',        # Blackmagic RAW (cámaras profesionales)
        '.dce',         # Formato de cámaras Kodak
        '.ims',         # Image Stream Segments (IMS)

        # Formatos de videojuegos y animación
        '.bik',         # Video de videojuegos de Bink
        '.smk',         # Smacker video (videojuegos)
        '.mve',         # Formato de archivo de Interplay
        '.ivf',         # Indeo Video Format
        '.dirac',       # Video Dirac (BBC)
        '.paf',         # Portable Animated Format
        '.vp6',         # Formato de video VP6, usado en Flash y On2
        '.seq',         # Cinemática o secuencia de video en varios formatos
        '.m2s',         # Motion Videos
        '.anim',        # Animaciones de varios programas

        # Formatos antiguos y menos comunes
        '.avchd',       # Advanced Video Codec High Definition
        '.evo',         # Enhanced Video Object, utilizado en HD DVD
        '.trp',         # HD video transport stream
        '.fbr',         # FlashBack Express export file
        '.rm',          # RealMedia
        '.ivs',         # IVI Video Streaming

        # Formatos de transmisión en línea
        # Lista de reproducción de video HLS (HTTP Live Streaming)
        '.m3u8',
        '.ts',          # Transport Stream usado para transmisión
        '.sdp',         # Protocolo de descripción de sesión, usado en transmisión
        '.dvr-ms',      # Microsoft Digital Video Recording
        '.wm',          # Formato Windows Media Video
        '.ismt',        # Smooth Streaming Media de Microsoft

        # Extensiones relacionadas con video y multimedia
        '.vr',          # Video Reality file
        '.av1',         # AOMedia Video 1, nuevo estándar de video (abierto)
        '.ivf',         # Indeo Video Format (antiguo)
        '.mpsub',       # MicroDVD Subtitle file (relacionado con video)
        '.ogm',         # Formato de Ogg Media (video)
        '.rms',         # Video RealMedia
        '.aaf',         # Advanced Authoring Format (intercambio multimedia)
        '.mve',         # Archivo de video Interplay (antiguo)

        # Otros formatos y menos comunes
        '.wtv',         # Windows Recorded TV Show
        '.drc',         # Dirac video (BBC)
        '.mvb',         # Multimedia Viewer Book (Microsoft)
        '.svi',         # Samsung Video Format
        '.flh',         # FLIC animation
        '.f4m',         # Video MPEG-4 (utilizado por Adobe Media Server)
        '.mj2',         # Motion JPEG 2000
        '.tsv',         # Tab-separated video file
        '.hdmov',       # High-definition QuickTime video
        '.m15',         # MPEG-1.5 video file
        '.m75',         # MPEG-7 video file
        '.dmb',         # Digital Multimedia Broadcasting
        '.dav',         # CCTV (DVR) video file
        '.vp8',         # Video VP8 (WebM)
        '.vp9',         # Video VP9 (WebM)
    ]
