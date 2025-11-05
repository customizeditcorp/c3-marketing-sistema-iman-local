# Runway API - Endpoint Correcto

## ✅ Endpoint para Text/Image to Image

**URL:** `POST https://api.dev.runwayml.com/v1/text_to_image`

**NO:** `POST https://api.dev.runwayml.com/v1/images/generate` ❌

---

## Modelos Disponibles

### Para generación de imágenes:

1. **gen4_image_turbo** - Rápido y económico (2 créditos)
2. **gen4_image** - Alta calidad (5-8 créditos)
3. **gemini_2.5_flash** - Google Gemini (5 créditos)

---

## Request Body

```json
{
  "promptText": "string (required, max 1000 chars)",
  "ratio": "string (required)",
  "model": "string (required)",
  "seed": integer (optional),
  "referenceImages": [
    {
      "uri": "string (URL de imagen)",
      "tag": "string"
    }
  ],
  "contentModeration": {
    "publicFigureThreshold": "auto"
  }
}
```

---

## Ratios Soportados

### gen4_image_turbo y gen4_image:
- 1920:1080
- 1080:1920
- 1024:1024
- 1360:768
- 1080:1080
- 1168:880
- 1440:1080
- 1080:1440
- 1808:768
- 2112:912
- 1280:720
- 720:1280
- 720:720
- 960:720
- 720:960
- 1680:720
- 1344:768
- 768:1344
- 1024:1024
- 1184:864
- 864:1184
- 1536:672
- 832x1248
- 1248x832
- 896x1152
- 1152x896

### gemini_2.5_flash:
- 1344:768
- 768:1344
- 1024:1024
- 1184:864
- 864:1184
- 1536:672
- 832x1248
- 1248x832
- 896x1152
- 1152x896

---

## Headers Requeridos

```
Authorization: Bearer {YOUR_API_KEY}
Content-Type: application/json
X-Runway-Version: 2024-11-06
```

---

## Response

```json
{
  "id": "task_id_string",
  "status": "PENDING",
  ...
}
```

Luego hacer polling a: `GET https://api.dev.runwayml.com/v1/tasks/{task_id}`

---

## Ejemplo cURL

```bash
curl -X POST https://api.dev.runwayml.com/v1/text_to_image \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "X-Runway-Version: 2024-11-06" \
  -d '{
    "promptText": "A professional photo",
    "ratio": "1920:1080",
    "model": "gemini_2.5_flash",
    "referenceImages": [{
      "uri": "https://example.com/image.jpg",
      "tag": "Reference"
    }]
  }'
```
