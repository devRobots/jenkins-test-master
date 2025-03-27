import os
import sys

ruta_modulos_b2b = os.path.join(os.path.dirname(__file__), "b2b-modules")

if os.path.exists(ruta_modulos_b2b):
    ruta_absoluta = os.path.abspath(ruta_modulos_b2b)
    if ruta_absoluta not in sys.path:
        sys.path.append(ruta_absoluta)

    from logfunctions import log_message
    log_message("100", "Funciona!!!")
else:
    print(f"Error: La ruta '{ruta_modulos_b2b}' no existe.")
