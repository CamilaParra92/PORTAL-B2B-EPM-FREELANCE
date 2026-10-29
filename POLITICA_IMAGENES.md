# Política de imágenes de productos (PRODUCTS_DATA)

**Regla vigente desde 2026-08-12: las imágenes de los productos (campo `img` en `PRODUCTS_DATA`) están congeladas.**

## Qué significa esto

- Subir un nuevo `products_export` (CSV de Shopify) **no** debe disparar una actualización automática de imágenes.
- Subir un Excel/planilla con links directos de imágenes tampoco debe disparar una actualización automática de imágenes.
- El campo `img` de cada producto solo se modifica cuando Cami lo pide **explícitamente, indicando el o los SKU** a cambiar.
- Todo lo demás (precios, stock, disponibilidad, nombres, categorías) sí se sigue actualizando normalmente a partir de los archivos que Cami suba — la regla aplica **solo** al campo `img`.

## Por qué existe esta regla

Un proceso anterior (comparar CSV vs. `PRODUCTS_DATA` y aplicar el diff de imágenes automáticamente) generó actualizaciones masivas no solicitadas y quedó desalineado con cambios manuales hechos directamente en archivos/CDN fuera del flujo de export. Para evitar perder trabajo ya validado y evitar sorpresas, el catálogo de imágenes actual se toma como línea base estable y solo se edita a pedido puntual.

## Qué debe hacer quien (o el agente que) procese un archivo nuevo

1. Si Cami sube un `products_export` o un Excel de imágenes: actualizar precios/stock/disponibilidad como corresponda, **pero ignorar cualquier diferencia en `img`**.
2. Si Cami pide cambiar la foto de un SKU puntual: actualizar solo ese `img`, dejando el resto del catálogo intacto.
3. Nunca correr un diff masivo de imágenes contra un export sin que Cami lo pida explícitamente para ese propósito.

Este archivo vive en los repos `PORTAL-B2B-EPM`, `PORTAL-B2B-EPM-LUIS` y `PORTAL-B2B-EPM-FREELANCE` y debe mantenerse igual en todos.
