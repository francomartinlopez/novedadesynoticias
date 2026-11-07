# Novedades y noticias

Web de novedades diarias por secciones. Una tarea programada de Claude escribe cada mañana (6:00, hora de Argentina) un archivo `datos/ediciones/AAAA-MM-DD.json`, corre `python3 armar_indice.py` y hace push. Netlify publica solo.

Formato de cada edición:
```json
{"fecha":"2026-11-07","secciones":{"argentina":[{"titulo":"…","resumen":"…","fuente":"…","url":"https://…","fecha":"2026-11-06","tema":"…"}]}}
```
Las secciones están en `secciones.json`. La lista de cuentas de X prioritarias está en `cuentas-x.json` y la de canales de YouTube para la sección Videos, en `canales-youtube.json`.
Los medios y sitios a revisar están en `fuentes.json`.

Cantidad: ninguna sección puede quedar vacía; cada sección lleva exactamente 3 o 6 notas (la grilla es de 3 columnas, así no quedan huecos). La sección Locales lleva siempre 6: 2 de Rosario, 2 de Córdoba, 1 de la Ciudad de Buenos Aires y 1 del Gran Buenos Aires (conurbano), en ese orden. La sección Clima local lleva siempre 6: 1 de Rosario, 1 de Córdoba, 1 del AMBA (CABA y Gran Buenos Aires) y 3 de Argentina en general.

Reglas de contenido: nada de farándula ni chismes sobre famosos; solo se incluyen personas famosas cuando hay una cuestión judicial importante, una muerte u otro hecho de relevancia pública real.

Todas las ediciones quedan guardadas en `datos/ediciones/`. `armar_indice.py` genera `datos/indice.json` (lista de ediciones) y `datos/busqueda.json` (todas las notas, para el buscador de la web, que filtra por palabra, fecha y temática).

Si no hay suficiente material nuevo para una sección, se completa hasta 3 con notas o videos de los días anteriores (lo más reciente posible), siempre del tema de la sección y distintos a los de la edición anterior.
