# Uso Correcto de referenceImages en Runway API

## Endpoint Correcto

**POST** `/v1/text_to_image`

## Parámetro: referenceImages

**Tipo:** Array de objetos  
**Descripción:** Un array de hasta 3 imágenes para usar como referencias para la imagen generada

### Estructura de cada objeto:

```json
{
  "uri": "string (required)",
  "tag": "string"
}
```

### Campo `uri`:
- **Required:** Sí
- **Tipo:** String (URL)
- **Descripción:** Una URL HTTPS o data URI que contiene una imagen codificada para usar como referencia
- **Nota:** Ver documentación de "our docs" para más información sobre inputs de imagen

### Campo `tag`:
- **Required:** No
- **Tipo:** String (3-16 caracteres)
- **Descripción:** Un nombre para referirse a la imagen de referencia en el prompt
- **Formato:** Alfanumérico (con guiones bajos), debe empezar con letra
- **Uso:** Se puede referenciar en el prompt usando sintaxis @tag
- **Nota:** Los tags son case-sensitive

## Modelos que Soportan referenceImages

- `gen4_image_turbo` - **requiere al menos 1 imagen de referencia**
- `gen4_image` - **requiere al menos 1 imagen de referencia**
- `gemini_2.5_flash` - soporta imágenes de referencia

## Ejemplo de Uso

```json
{
  "model": "gemini_2_5_flash",
  "promptText": "Professional photo editing using @person as base",
  "ratio": "1920:1080",
  "referenceImages": [
    {
      "uri": "https://example.com/image.jpg",
      "tag": "person"
    }
  ]
}
```

## Para Nano Banana (Preservación de Identidad)

Cuando se usa Gemini 2.5 Flash con Nano Banana para preservar identidad:

1. **Subir la imagen original** como referenceImage
2. **Usar tag descriptivo** (ej: "luis", "carlos")
3. **Referenciar en el prompt** con @tag
4. **Especificar preservación** en el prompt (ej: "preserve @luis face exactly")

## Formato de URI

Opciones:
1. **HTTPS URL:** `https://example.com/image.jpg`
2. **Data URI:** `data:image/jpeg;base64,/9j/4AAQ...`

Para usar imágenes locales, se necesita:
- Convertir a base64 y usar data URI, O
- Subir a un servidor y obtener URL pública

## contentModeration

**Nota:** Este campo solo está permitido para:
- `gen4_image_turbo`
- `gen4_image`

NO está disponible para `gemini_2_5_flash`
