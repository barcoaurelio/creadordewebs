# Myron Mena · Instalador de Durlock

Web de una página para **Myron Mena**, instalador de durlock (construcción en seco) en **San Carlos de Bariloche, Río Negro, Argentina** y alrededores.

## Cómo verla

No requiere build. Abrí `index.html` en cualquier navegador, o serví la carpeta:

```bash
npx serve .
# o
python -m http.server
```

## Cómo editar

Todo el contenido vive en `index.html` (una sola página, HTML + Tailwind CDN):

- **Textos y secciones**: buscá el texto directo en el HTML.
- **Colores**: en el bloque `tailwind.config` del `<head>` (navy, safety/amarillo, wapp/verde WhatsApp, fbb/azul Facebook).
- **Fotos**: reemplazá `myr11.jpg` y `myr12va.jpg` por archivos con el mismo nombre.

## Datos de contacto

- WhatsApp / Teléfono: **+54 9 2944 39-2186** (enlaces `wa.me/5492944392186` con mensaje precargado de presupuesto)
- Facebook: **https://www.facebook.com/myron.mena/**
- Zona: Bariloche y alrededores (centro, Alto, Dina Huapi, Villa Los Coihues, Arelauquen, Colonia Suiza)

## Estructura

| Sección | id | Contenido |
|---|---|---|
| Hero | `#top` | Título, foto real de obra, botón WhatsApp |
| Servicios | `#servicios` | Tabiques, cielorrasos, revestimientos, aislación, terminaciones, ampliaciones |
| Por qué elegirme | `#porque` | 4 puntos de confianza |
| Trabajos | `#trabajos` | Galería con fotos reales + CTA a Facebook |
| Zona | `#zona` | Bariloche y alrededores + mapa OpenStreetMap |
| Contacto | `#contacto` | Tarjetas WhatsApp y Facebook |
| Botón flotante | — | WhatsApp fijo abajo a la derecha |

## Licencia

Plantilla base: **local_services** (free-small-business), licencia MIT — ver `LICENSE`.
