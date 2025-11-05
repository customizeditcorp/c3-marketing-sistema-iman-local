# 🎯 ESTRATEGIA DE MODELOS RUNWAY - Por Tipo de Imagen

## 📊 Análisis de Fotos del Equipo

### Fotos Recibidas:

1. **María Emilia** - `maria-emilia.png`
   - ✅ Fondo perfecto (oficina con iMac, limpio)
   - ✅ Iluminación profesional
   - ✅ Camisa coral C3 con logo
   - ✅ **NO necesita edición**

2. **Luis Arroyo** - `luis-arroyo.png`
   - ✅ Fondo perfecto (persianas, oficina)
   - ✅ Iluminación profesional
   - ✅ Camisa coral C3 con logo
   - ✅ **Necesita agregar tablet con GBP** (para hero)

3. **Carlos Cordero** - `carlos-cordero.jpg`
   - ⚠️ Fondo azul con "like" neón de Facebook
   - ⚠️ Camisa gris (no coral C3)
   - ⚠️ Lanyard Facebook visible
   - ⚠️ **Necesita transformación de fondo**

---

## 🎬 MODELOS DE RUNWAY DISPONIBLES

### Para Imágenes (3 modelos):

| Modelo | Input | Output | Precio | Mejor Para |
|--------|-------|--------|--------|------------|
| **gen4_image** | Text/Image References | Image | 5-8 créditos | Generación con referencias, alta calidad |
| **gen4_image_turbo** | Text+Image References | Image | 2 créditos | Generación rápida, cualquier resolución |
| **gemini_2.5_flash** | Text/Image References | Image | 5 créditos | Generación con modelo Gemini |

---

## ✅ RECOMENDACIÓN POR TIPO DE IMAGEN

### 🖼️ CATEGORÍA 1: Edición de Fotos Reales (Con Personas)

**Imágenes:**
1. Carlos - Transformar fondo azul → oficina
2. Luis - Agregar tablet con GBP en manos

**Modelo Recomendado:** `gen4_image` (NO Gemini)

**Razón:**
- ✅ Mejor para **edición de fotos reales**
- ✅ Mantiene **consistencia del personaje**
- ✅ Preserva **detalles faciales** y **expresión**
- ✅ Control fino con **reference images**
- ✅ Mejor para **background replacement**

**Configuración:**
```javascript
{
  model: 'gen4_image',
  ratio: '1920:1080',
  promptText: '[PROMPT DETALLADO]',
  referenceImages: [{
    uri: 'path/to/original-photo.jpg',
    tag: 'OriginalPhoto'
  }]
}
```

**Costo:** 8 créditos × 2 imágenes = 16 créditos = **$0.16 USD**

---

### 🎨 CATEGORÍA 2: Ilustraciones y Mockups (Sin Personas Reales)

**Imágenes:**
3. Mockup Google Mobile (búsqueda)
4. Mockup GBP Desktop
5. Timeline Mes 1, 2, 3 (ilustraciones)
6. Set de 6 iconos
7. Pasos 1-4 (ilustraciones)
8. Badges (3)
9. Background pattern

**Modelo Recomendado:** `gen4_image_turbo` (Económico)

**Razón:**
- ✅ **Más económico** (2 créditos vs 5-8)
- ✅ Perfecto para **ilustraciones flat**
- ✅ Perfecto para **iconos y badges**
- ✅ Perfecto para **mockups UI**
- ✅ **Cualquier resolución** (mismo precio)
- ✅ **Generación rápida**

**Configuración:**
```javascript
{
  model: 'gen4_image_turbo',
  ratio: '1920:1080', // o '1080:1080' para badges
  promptText: '[PROMPT DETALLADO]'
}
```

**Costo:** 2 créditos × 12 imágenes = 24 créditos = **$0.24 USD**

---

### 🤔 ¿Por Qué NO Usar Gemini 2.5 Flash?

**Gemini es bueno para:**
- ✅ Generación de imágenes desde cero con texto
- ✅ Imágenes conceptuales
- ✅ Ilustraciones artísticas

**Gemini NO es ideal para:**
- ❌ Edición de fotos reales de personas
- ❌ Mantener consistencia facial
- ❌ Background replacement preciso
- ❌ Mockups UI realistas
- ❌ **Costo:** Mismo que gen4_image (5 créditos) pero menos control

**Conclusión:** Gen4 Image es superior para nuestro caso de uso.

---

## 📋 PLAN DE EJECUCIÓN OPTIMIZADO

### FASE 1: Fotos del Equipo (Gen4 Image)

| # | Imagen | Modelo | Ratio | Créditos |
|---|--------|--------|-------|----------|
| 1 | Carlos - Fondo transformado | gen4_image | 1920:1080 | 8 |
| 2 | Luis - Con tablet GBP | gen4_image | 1920:1080 | 8 |

**Subtotal Fase 1:** 16 créditos = **$0.16 USD**

---

### FASE 2: Mockups y UI (Gen4 Image Turbo)

| # | Imagen | Modelo | Ratio | Créditos |
|---|--------|--------|-------|----------|
| 3 | Google Mobile Search | gen4_image_turbo | 1080:1920 | 2 |
| 4 | GBP Desktop Dashboard | gen4_image_turbo | 1920:1080 | 2 |

**Subtotal Fase 2:** 4 créditos = **$0.04 USD**

---

### FASE 3: Ilustraciones Timeline (Gen4 Image Turbo)

| # | Imagen | Modelo | Ratio | Créditos |
|---|--------|--------|-------|----------|
| 5 | Timeline Mes 1 | gen4_image_turbo | 1080:1080 | 2 |
| 6 | Timeline Mes 2 | gen4_image_turbo | 1080:1080 | 2 |
| 7 | Timeline Mes 3 | gen4_image_turbo | 1080:1080 | 2 |

**Subtotal Fase 3:** 6 créditos = **$0.06 USD**

---

### FASE 4: Iconos (Gen4 Image Turbo)

| # | Imagen | Modelo | Ratio | Créditos |
|---|--------|--------|-------|----------|
| 8 | Set 6 iconos (1 imagen) | gen4_image_turbo | 1920:1080 | 2 |

**Subtotal Fase 4:** 2 créditos = **$0.02 USD**

---

### FASE 5: Pasos del Sistema (Gen4 Image Turbo)

| # | Imagen | Modelo | Ratio | Créditos |
|---|--------|--------|-------|----------|
| 9 | Paso 1 - Fundación | gen4_image_turbo | 1080:1080 | 2 |
| 10 | Paso 2 - Magnetización | gen4_image_turbo | 1080:1080 | 2 |
| 11 | Paso 3 - Confianza | gen4_image_turbo | 1080:1080 | 2 |
| 12 | Paso 4 - Activación | gen4_image_turbo | 1080:1080 | 2 |

**Subtotal Fase 5:** 8 créditos = **$0.08 USD**

---

### FASE 6: Elementos Adicionales (Gen4 Image Turbo)

| # | Imagen | Modelo | Ratio | Créditos |
|---|--------|--------|-------|----------|
| 13 | Badges (3 en 1) | gen4_image_turbo | 1920:600 | 2 |
| 14 | Background Pattern | gen4_image_turbo | 1920:1080 | 2 |

**Subtotal Fase 6:** 4 créditos = **$0.04 USD**

---

## 💰 COSTO TOTAL OPTIMIZADO

| Fase | Modelo | Imágenes | Créditos | Costo USD |
|------|--------|----------|----------|-----------|
| 1 | gen4_image | 2 | 16 | $0.16 |
| 2-6 | gen4_image_turbo | 12 | 24 | $0.24 |
| **TOTAL** | - | **14** | **40** | **$0.40 USD** |

---

## 🎯 COMPARACIÓN CON ESTRATEGIA ORIGINAL

| Estrategia | Modelo Principal | Costo Total |
|------------|------------------|-------------|
| **Original** | gen4_image para todo | $1.03 USD |
| **Optimizada** | gen4_image + turbo | **$0.40 USD** |
| **Ahorro** | - | **$0.63 USD (61%)** |

---

## ✅ VENTAJAS DE ESTA ESTRATEGIA

### Para Fotos del Equipo:
- ✅ **Gen4 Image** mantiene consistencia facial perfecta
- ✅ Background replacement de alta calidad
- ✅ Preserva detalles y expresiones
- ✅ Vale la pena el costo extra (8 créditos vs 2)

### Para Ilustraciones y Mockups:
- ✅ **Gen4 Image Turbo** es perfecto y económico
- ✅ Calidad suficiente para UI/ilustraciones
- ✅ 75% más barato (2 vs 8 créditos)
- ✅ Misma calidad para elementos no-fotográficos

---

## 🚀 RESPUESTA A TU PREGUNTA

### "¿Usar Gemini para Carlos y Gen4 para consistencia?"

**Respuesta:** NO, usar **Gen4 Image para AMBOS** (Carlos y Luis)

**Razón:**
1. **Gen4 Image es mejor que Gemini** para edición de fotos reales
2. **Gemini** cuesta lo mismo (5 créditos) pero con menos control
3. **Gen4 Image** tiene mejor track record para background replacement
4. **Consistencia:** Usar mismo modelo para ambas fotos del equipo

### Estrategia Correcta:

✅ **Gen4 Image** → Fotos del equipo (Carlos, Luis)  
✅ **Gen4 Image Turbo** → Todo lo demás (ilustraciones, mockups, iconos)  
❌ **Gemini** → NO usar para este proyecto

---

## 📝 ORDEN DE EJECUCIÓN FINAL

1. **Carlos - Fondo** (gen4_image, 8 créditos)
2. **Luis - Tablet** (gen4_image, 8 créditos)
3. **Mockup Google** (gen4_image_turbo, 2 créditos)
4. **Mockup GBP** (gen4_image_turbo, 2 créditos)
5-7. **Timeline 1-3** (gen4_image_turbo, 2 créditos × 3)
8. **Iconos** (gen4_image_turbo, 2 créditos)
9-12. **Pasos 1-4** (gen4_image_turbo, 2 créditos × 4)
13-14. **Badges + Pattern** (gen4_image_turbo, 2 créditos × 2)

**Total:** 40 créditos = **$0.40 USD**

---

**Fecha:** Noviembre 2025  
**Proyecto:** Sistema Imán Local - C3 Marketing  
**Estrategia:** Optimizada Gen4 Image + Turbo
