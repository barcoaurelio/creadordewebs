---
name: crear-web
description: "Creá un skill que, dado un pedido en lenguaje natural sobre un negocio, construya un sitio web usando el catálogo de plantillas locales."
---

# Skill: crear-web

Este skill permite crear un sitio web para un negocio a partir de una descripción en lenguaje natural, utilizando un catálogo de plantillas web verificadas.

## Flujo de trabajo

### 1. Extracción de datos
A partir del pedido en lenguaje natural, extraé los siguientes datos del negocio:
- **nombre**: nombre comercial
- **rubro**: tipo de negocio (restaurante, café, dentista, abogado, etc.)
- **ciudad**: ciudad donde opera
- **colores**: colores corporativos (si se especifican)
- **logo**: archivo de logo (si se proporciona)
- **fotos**: fotos del establecimiento, productos, equipo (si se proporcionan)
- **servicios**: lista de servicios ofrecidos
- **teléfono/WhatsApp**: número de contacto
- **horarios**: horario de atención
- **redes sociales**: enlaces a perfiles sociales

Si algún dato falta en el pedido, **no lo inventes**. Usá un marcador visible `[COMPLETAR]` y al final listá todos los datos que quedaron pendientes.

### 2. Selección de plantilla
Basado en el rubro y el estilo mencionado (o implícito) en el pedido, elegí una plantilla del catálogo localizado en `plantillas/`.

**Debes indicar claramente cuál plantilla elegiste y por qué, en una sola línea.** Por ejemplo:
> "Elegí la plantilla 'Bootstrap Restaurant' porque es ideal para restaurantes y tiene un estilo moderno y limpio."

### 3. Copia y edición de la plantilla
Copiá la plantilla seleccionada a una nueva carpeta bajo `projects/<nombre-negocio>/` (reemplazando espacios y caracteres especiales por guiones bajos o eliminándolos).

Edité la plantilla **leyendo sus archivos directamente** (no usando búsquedas y reemplazos a ciegas), actualizando:
- **Nombre del negocio**: en todas las apariciones (título, meta tags, encabezados, pies de página)
- **Colores**: modificá los archivos CSS o las variables de Tailwind según corresponda
- **Tipografías**: si se especifican, cambiá las fuentes en CSS o en el HTML
- **Logo**: reemplazá el archivo de logo existente por el provisto (o mantení el placeholder si no se proporciona)
- **Fotos**: reemplazá las imágenes de ejemplo por las provistas; si no hay fotos, usá imágenes libres de Unspash/Pexels según el rubro y anotá la fuente
- **Textos**: reemplazá todo el texto de ejemplo por textos en **español rioplatense**, describiendo los servicios, historia, valores, etc. del negocio. **Nunca fabriqués datos del negocio**; si falta información, usá `[COMPLETAR]`.

### 4. Limpieza de contenido de ejemplo
Eliminá cualquier contenido de ejemplo que venga en la plantilla:
- Números de teléfono de ejemplo
- Direcciones de ejemplo
- Reseñas o testimonios de ejemplo
- Textos "Lorem ipsum" o similares
- Links rotos o a sitios de ejemplo

### 5. Agregado de contacto real
Agregá un botón visible de WhatsApp que enlace al número de contacto real (si se proporcionó). También incluí los datos de contacto reales (teléfono, dirección, horarios) en la sección correspondiente.

### 6. Construcción y verificación
Ejecutá el comando de construcción indicado en el catálogo para la plantilla (si aplica). Luego, abrí el preview (ya sea abriendo el `index.html` o iniciando un servidor de desarrollo según el stack).

Tomá un screenshot de la página verificando que:
- No quede ningún texto de ejemplo
- No haya links rotos (todos los enlaces internos funcionan y los externos apuntan a lugares reales)
- Las imágenes se cargan correctamente
- El diseño se ve bien en móvil y escritorio (si la plantilla es responsive)

### 7. Actualización sobre negocio existente
Si el skill se ejecuta nuevamente sobre el mismo negocio (misma carpeta en `projects/`), **actualizá la carpeta existente** sin sobrescribir lo que ya fue personalizado. Es decir, solo actualizá los archivos que correspondan a datos nuevos o cambiados, respetando las ediciones manuales previas.

### 8. Cierre del skill
Al finalizar, indicá claramente:
- **Ruta del proyecto**: la ruta absoluta o relativa a la carpeta `projects/<nombre-negocio>/`
- **URL del preview**: cómo ver el sitio (ej. `file:///ruta/al/index.html` o `http://localhost:3000` si se usó un servidor)
- **Lista de lo que quedó pendiente de completar**: todos los datos que marcaste como `[COMPLETAR]` durante el proceso

## Notas importantes
- **Nunca fabriqués datos del negocio**: si el usuario no proporciona un dato, debe marcarse como `[COMPLETAR]`.
- **Textos siempre en español riopletense**: usá el voseo y el vocabulario característico del Río de la Plata.
- **Verificá las licencias**: respetá las licencias de las plantillas y de las imágenes libres que uses.
- **El skill es iterativo**: podés ejecutarlo tantas veces como necesites para ir completando la información.

---