# 🎬 RUNWAY API - Capacidades Completas

## 📊 Resumen de la API de Runway

La API de Runway permite integrar modelos generativos de última generación directamente en aplicaciones, productos y sitios web.

**Pricing:** 1 crédito = $0.01 USD

---

## 🎥 GENERACIÓN DE VIDEO

### Modelos Disponibles:

| Modelo | Input | Output | Precio | Descripción |
|--------|-------|--------|--------|-------------|
| **gen4_turbo** | Image | Video | 5 créditos/seg | Generación rápida de video desde imagen |
| **gen4_aleph** | Video + Text/Image | Video | 15 créditos/seg | Modelo avanzado con múltiples inputs |
| **upscale_v1** | Video | Video | 2 créditos/seg | Mejora de resolución de video |
| **act_two** | Image o Video | Video | 5 créditos/seg | Animación y transformación |
| **veo3** | Text o Image | Video | 40 créditos/seg | Modelo Veo 3 (Google) |
| **veo3.1** | Text o Image | Video | 40 créditos/seg | Modelo Veo 3.1 mejorado |
| **veo3.1_fast** | Text o Image | Video | 20 créditos/seg | Versión rápida de Veo 3.1 |

---

## 🖼️ GENERACIÓN DE IMÁGENES

### Modelos Disponibles:

| Modelo | Input | Output | Precio | Descripción |
|--------|-------|--------|--------|-------------|
| **gen4_image** | Text/Image (References) | Image | 5 créditos/720p<br>8 créditos/1080p | Generación de imágenes de alta calidad con referencias |
| **gen4_image_turbo** | Text+Image (References) | Image | 2 créditos/imagen<br>(cualquier resolución) | Versión rápida y económica |
| **gemini_2.5_flash** | Text/Image (References) | Image | 5 créditos/imagen | Modelo Gemini de Google |

### ✨ Características Especiales:

**Gen-4 Image con Referencias:**
- Permite usar imágenes de referencia con tags
- Ejemplo: `@EiffelTower painted in the style of @StarryNight`
- Soporta múltiples referencias en un solo prompt
- Ratios personalizables (1920:1080, etc.)

---

## 🔊 GENERACIÓN DE AUDIO

### Modelos Disponibles:

| Modelo | Input | Output | Precio | Descripción |
|--------|-------|--------|--------|-------------|
| **eleven_multilingual_v2** | Text | Audio | 1 crédito/50 caracteres | Text-to-Speech multiidioma |
| **eleven_text_to_sound_v2** | Text | Audio | 1 crédito/6 seg | Generación de efectos de sonido |
| **eleven_voice_isolation** | Audio | Audio | 1 crédito/6 seg | Aislamiento de voz |
| **eleven_voice_dubbing** | Audio | Audio | 1 crédito/2 seg output | Doblaje de voz |
| **eleven_multilingual_sts_v2** | Audio | Audio | 1 crédito/2 seg output | Speech-to-Speech multiidioma |

---

## 💡 PARA LA LANDING DE C3 MARKETING

### ✅ LO QUE PODEMOS USAR:

#### 1. **Gen-4 Image** (RECOMENDADO)
**Perfecto para:**
- ✅ Hero image (contratista hispano con tablet)
- ✅ Imágenes de secciones (timeline, pasos del sistema)
- ✅ Escenas profesionales de servicios locales
- ✅ Mockups de Google Business Profile

**Ventajas:**
- Soporta referencias visuales (podemos usar fotos reales como base)
- Alta calidad (720p o 1080p)
- Control de estilo mediante referencias
- Precio razonable: 5-8 créditos por imagen

**Costo estimado para 14 imágenes:**
- 14 imágenes × 5 créditos = 70 créditos = **$0.70 USD** (720p)
- 14 imágenes × 8 créditos = 112 créditos = **$1.12 USD** (1080p)

#### 2. **Gen-4 Image Turbo** (ALTERNATIVA ECONÓMICA)
**Perfecto para:**
- ✅ Iconos y badges
- ✅ Imágenes secundarias
- ✅ Prototipos rápidos

**Ventajas:**
- Más económico: 2 créditos por imagen
- Cualquier resolución
- Generación rápida

**Costo estimado para 14 imágenes:**
- 14 imágenes × 2 créditos = 28 créditos = **$0.28 USD**

---

### ❌ LO QUE NO NECESITAMOS (Por Ahora):

#### Generación de Video
- ❌ **gen4_turbo, gen4_aleph, veo3, etc.**
- Razón: La landing necesita imágenes estáticas, no videos
- Costo: Mucho más caro (5-40 créditos por segundo)
- Posible uso futuro: Video testimonial, demo del sistema

#### Generación de Audio
- ❌ **eleven_multilingual_v2, etc.**
- Razón: No hay audio en la landing
- Posible uso futuro: Voiceover para video explicativo

---

## 🎯 RECOMENDACIÓN PARA TU PROYECTO

### Opción 1: Gen-4 Image (Calidad Premium)
**Usar para:**
- Hero principal (1080p)
- Imágenes de timeline (1080p)
- Imágenes de 4 pasos (720p)
- **Total:** ~$1.00 USD para 14 imágenes

### Opción 2: Gen-4 Image Turbo (Económico)
**Usar para:**
- Todas las imágenes
- **Total:** ~$0.30 USD para 14 imágenes

### Opción 3: Híbrido (Recomendado)
**Combinar:**
- Gen-4 Image para hero y secciones principales (5 imágenes × 8 créditos = 40 créditos)
- Gen-4 Image Turbo para iconos y secundarias (9 imágenes × 2 créditos = 18 créditos)
- **Total:** 58 créditos = **$0.58 USD**

---

## 📝 EJEMPLO DE CÓDIGO (Gen-4 Image con Referencias)

```javascript
import RunwayML from '@runwayml/sdk';

const client = new RunwayML({
  apiKey: process.env.RUNWAY_API_KEY
});

// Generar hero image con referencias
const task = await client.textToImage.create({
  model: 'gen4_image',
  ratio: '1920:1080',
  promptText: 'Professional Hispanic contractor in his 30s-40s holding a tablet showing a Google Business Profile, standing in front of a landscaping truck, professional photography, natural lighting, California style',
  referenceImages: [{
    uri: 'https://example.com/reference-contractor.jpg',
    tag: 'ContractorStyle'
  }]
}).waitForTaskOutput();

console.log('Image URL:', task.output[0]);
```

---

## ✅ CONCLUSIÓN

**SÍ, Runway API puede generar las imágenes para tu landing**, pero:

1. **Es principalmente para imágenes y video**, no es la herramienta más económica para imágenes estáticas simples
2. **Costo total estimado:** $0.30 - $1.00 USD para 14 imágenes
3. **Ventaja:** Calidad profesional con control mediante referencias
4. **Desventaja:** Requiere API key y configuración

### Alternativas a Considerar:

1. **Herramienta de generación de imágenes integrada aquí** (gratis, más rápido)
2. **Runway API** (tu opción, $0.30-$1.00, alta calidad)
3. **Midjourney/DALL-E** (si tienes acceso)
4. **Stock photos + edición** (Unsplash, Pexels)

---

## 🚀 PRÓXIMO PASO

**¿Quieres que use tu API de Runway para generar las imágenes?**

Si sí:
1. Necesito tu **API Key de Runway**
2. Generaré las 14 imágenes usando Gen-4 Image
3. Las optimizaré para web
4. Las integraré en la landing de Lovable

Si prefieres otra opción, puedo usar la herramienta integrada aquí (gratis y rápido).

**¿Qué prefieres?**
