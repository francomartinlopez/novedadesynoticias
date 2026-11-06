# Novedades y noticias

Web de novedades diarias por secciones. Una tarea programada de Claude escribe cada mañana (6:00, hora de Argentina) un archivo `datos/ediciones/AAAA-MM-DD.json`, corre `python3 armar_indice.py` y hace push. Netlify publica solo.

Formato de cada edición:
```json
{"fecha":"2026-11-07","secciones":{"argentina":[{"titulo":"…","resumen":"…","fuente":"…","url":"https://…","fecha":"2026-11-06","tema":"…"}]}}
```
Las secciones están en `secciones.json`. La lista de cuentas de X prioritarias está en `cuentas-x.json` y la de canales de YouTube para la sección Videos, en `canales-youtube.json`.
Los medios y sitios a revisar están en `fuentes.json`.

Cantidad: cada sección lleva exactamente 3 o 6 notas (la grilla es de 3 columnas, así no quedan huecos).

Reglas de contenido: nada de farándula ni chismes sobre famosos; solo se incluyen personas famosas cuando hay una cuestión judicial importante, una muerte u otro hecho de relevancia pública real.

Todas las ediciones quedan guardadas en `datos/ediciones/`. `armar_indice.py` genera `datos/indice.json` (lista de ediciones) y `datos/busqueda.json` (todas las notas, para el buscador de la web, que filtra por palabra, fecha y temática).
