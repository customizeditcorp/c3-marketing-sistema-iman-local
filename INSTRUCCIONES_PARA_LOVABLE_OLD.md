# 🎯 INSTRUCCIONES COMPLETAS PARA LOVABLE
## Landing Page: Sistema Imán Local™ - C3 Marketing

**Cliente:** C3 Marketing  
**Producto:** Sistema Imán Local™  
**Objetivo:** Landing page de conversión para negocios de servicios hispanos en California  
**Fecha:** Noviembre 2025

---

## 📦 ASSETS DISPONIBLES EN ESTE REPOSITORIO

### Imágenes Generadas (18 total)
Todas las imágenes están en `/assets/generated/`:

**Fotos del Equipo:**
- `02_luis_tablet_gbp_CORRECTED.png` - Luis con iPad mostrando GBP (HERO principal)
- `01_carlos_white_shirt_c3_orange_FINAL.png` - Carlos con logo C3 naranja (opcional para sección equipo)

**Mockups:**
- `03_google_mobile_search.png` - Búsqueda móvil "landscaping near me"
- `04_gbp_desktop_dashboard.png` - Dashboard GBP desktop "Martinez Landscaping"

**Timeline 90 Días (3 imágenes):**
- `05_timeline_mes1_fundacion.png` - Mes 1: Fundación Digital (rojo)
- `06_timeline_mes2_optimizacion.png` - Mes 2: Optimización (amarillo)
- `07_timeline_mes3_activacion.png` - Mes 3: Activación (gris)

**4 Pasos del Sistema (4 imágenes):**
- `08_paso1_fundacion_digital.png` - Laptop con GBP
- `09_paso2_magnetizacion_local.png` - Imán atrayendo clientes
- `10_paso3_confianza_visual.png` - Escudo con 5 estrellas
- `11_paso4_activacion_247.png` - Smartphone con notificaciones

**Badges (3 imágenes):**
- `12_badge_100_tuyo.png` - Badge "100% TUYO" (rojo)
- `13_badge_90_dias.png` - Badge "90 DÍAS" (amarillo)
- `14_badge_sin_ataduras.png` - Badge "SIN ATADURAS" (gris)

### Logos C3
En `/assets/logos/`:
- `c3white200x200.svg` - Logo horizontal blanco (USAR EN NAVBAR)
- `c3Verticalwhite200x200.svg` - Logo vertical blanco
- `c3orange200x200.png` - Logo horizontal naranja
- `c3Verticalorange200x200.png` - Logo vertical naranja

### Paleta de Colores
- `/assets/images/paleta.png` - Imagen de referencia de la paleta

---

## 🎨 DISEÑO Y ESTILO

### Paleta de Colores C3 (OBLIGATORIA)

```css
/* Colores principales */
--primary: #EF4125;        /* Rojo C3 - CTAs, branding */
--secondary: #F9B718;      /* Amarillo C3 - acentos, highlights */
--gray-dark: #58595B;      /* Gris oscuro - texto principal */
--gray-light: #E5E5E5;     /* Gris claro - backgrounds alternos */
--white: #FFFFFF;          /* Blanco - background principal */
--black: #000000;          /* Negro - títulos */
```

**Uso de colores:**
- **Rojo (#EF4125):** CTAs principales, logo, elementos de urgencia
- **Amarillo (#F9B718):** Badges, highlights, timeline Mes 2
- **Gris oscuro (#58595B):** Texto body, timeline Mes 3
- **Gris claro (#E5E5E5):** Backgrounds alternos de secciones
- **Blanco (#FFFFFF):** Background principal

### Tipografía

**Fuentes Google:**
```html
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Open+Sans:wght@400;500;600&display=swap" rel="stylesheet">
```

**Uso:**
- **Headings (H1-H6):** Poppins Bold (700)
- **Body text:** Open Sans Regular (400)
- **Tamaños:**
  - H1: 48-60px (desktop), 32-40px (mobile)
  - H2: 36-48px (desktop), 28-32px (mobile)
  - H3: 24-30px
  - Body: 16-18px
  - Small: 14px

### Estilo Visual

**Características:**
- ✅ Profesional pero cálido (no frío corporativo)
- ✅ Directo y claro (no pretencioso)
- ✅ Hispano-friendly (accesible, empático)
- ✅ Orientado a resultados (no genérico)

**Elementos de diseño:**
- Border radius: 8-12px
- Sombras sutiles: `box-shadow: 0 4px 6px rgba(0,0,0,0.1)`
- Espaciado generoso: 60-80px entre secciones
- Padding interno: 40-60px en cards

---

## 🏗️ WIREFRAME Y ESTRUCTURA

### Inspiración del Template Figma

**Referencia:** Digital Agency Landing Page (Figma Community)

**Características clave a implementar:**
1. **Layout asimétrico** (no centrado genérico)
2. **Hero potente** con imagen grande + texto a la izquierda
3. **Secciones alternas** (blanco/gris claro)
4. **Cards en grid** para beneficios (3 columnas desktop, 1 mobile)
5. **Timeline visual** (horizontal o vertical según espacio)
6. **CTAs múltiples** estratégicamente ubicados
7. **Navbar sticky** con logo + CTA
8. **Footer completo** con información de contacto

---

## 📄 ESTRUCTURA DE LA LANDING (12 SECCIONES)

### SECCIÓN 1: HERO

**Layout:**
- Grid 2 columnas (desktop): Contenido izquierda, imagen derecha
- Stack vertical (mobile)

**Contenido:**

**Badges (arriba, horizontal):**
- Mostrar las 3 imágenes de badges en fila
- `12_badge_100_tuyo.png`
- `13_badge_90_dias.png`
- `14_badge_sin_ataduras.png`

**H1:**
```
De Invisible a Visible en 90 Días
```

**H2 (subtítulo):**
```
Presencia digital completa que atrae clientes locales 24/7, ads-ready desde día 1, 100% tuyo
```

**Copy de apoyo:**
```
¿Pierdes contratos cada mes porque no apareces en Google o no te ves profesional? El Sistema Imán Local™ convierte tu negocio de servicios en un imán de clientes locales en solo 90 días.
```

**CTAs:**
1. **Primario (rojo):** "Agendar Llamada de Diagnóstico Gratuita"
2. **Secundario (outline rojo):** "Ver Cómo Funciona ↓" (scroll a #como-funciona)

**Imagen:**
- `02_luis_tablet_gbp_CORRECTED.png`
- Mostrar grande, con sombra
- Alt text: "Profesional mostrando Google Business Profile"

---

### SECCIÓN 2: PROBLEMA

**Background:** Gris claro (#E5E5E5)

**H2:**
```
¿Por Qué Pierdes Clientes Cada Mes?
```

**Copy intro:**
```
La realidad dolorosa: estás perdiendo trabajos y contratos porque los clientes ya no contratan al primer número que encuentran.
```

**Subsección: El Nuevo Proceso de Decisión del Cliente**

**5 Pasos (cards en grid):**

1. **Buscan en Google**
   - Icon: 🔍 (Search icon)
   - Copy: "landscaping near me" → Si no apareces, ya perdiste

2. **Comparan Perfiles**
   - Icon: 👁️ (Eye icon)
   - Copy: Ven tu competencia con fotos, reseñas, horarios → Si no te ves profesional, te descartan

3. **Visitan Websites**
   - Icon: 🌐 (Globe icon)
   - Copy: Verifican que eres legítimo → Si no tienes website o se ve mal, siguiente

4. **Leen Reseñas**
   - Icon: ⭐ (Star icon)
   - Copy: Confirman confiabilidad → Sin reseñas = sin confianza

5. **Eligen al Más Confiable**
   - Icon: 📉 (Trending down icon)
   - Copy: El que pasó todos los filtros gana el contrato

**Callout Box (destacado con borde rojo):**
```
💔 Si tu negocio no aparece o se ve desactualizado digitalmente, simplemente quedas fuera de la competencia.
```

**Los Costos Ocultos (3 cards):**

1. **Pierdes dinero:**
   - 2-10 clientes potenciales cada mes
   - Contratos que se van a la competencia

2. **Pierdes tiempo:**
   - Dependes 100% de referencias (no escalable)
   - Frustración de hacer buen trabajo pero no conseguir clientes nuevos

3. **Pierdes oportunidades:**
   - Barrera de idioma con herramientas digitales
   - Pagar mensualidades eternas sin ser dueño de nada

---

### SECCIÓN 3: SOLUCIÓN

**Background:** Blanco
**ID:** `#como-funciona` (para scroll del CTA hero)

**H2:**
```
La Solución: Sistema Imán Local™
```

**Tagline (italic, amarillo):**
```
El sistema que convierte tu negocio en un imán de clientes locales
```

**Copy intro:**
```
No vendemos "servicios de marketing digital" genéricos. Implementamos un sistema específico probado con más de 10 negocios de servicios hispanos en California.
```

**¿Por Qué Funciona? (4 cards con checkmarks):**

1. ✓ **Diseñado para negocios de servicios**
   - No es teoría. Es un proceso paso a paso probado con contratistas reales.

2. ✓ **En tu idioma**
   - Sin barreras de comunicación. Todo en español, claro y directo.

3. ✓ **Tú eres el dueño**
   - No pagas rentas eternas. Todo es tuyo al terminar los 90 días.

4. ✓ **Listo para escalar**
   - Empieza orgánico o acelera con publicidad cuando quieras.

**Callout Box (destacado con gradiente rojo-amarillo):**
```
🏆 A diferencia de otras agencias que te cobran mensualidades eternas y nunca eres dueño de nada, con el Sistema Imán Local™ TODO es tuyo desde el día 1.
```

**Mockups (2 imágenes lado a lado):**
- Izquierda: `03_google_mobile_search.png`
- Derecha: `04_gbp_desktop_dashboard.png`

---

### SECCIÓN 4: TIMELINE 90 DÍAS

**Background:** Gris claro (#E5E5E5)

**H2:**
```
Tu Transformación en 90 Días
```

**Layout:** 3 cards grandes (alternando imagen izquierda/derecha)

**MES 1: FUNDACIÓN DIGITAL**

**Badge:** "MES 1" (fondo rojo)
**Días:** 1-30
**Imagen:** `05_timeline_mes1_fundacion.png`

**Lo que construimos:**
- ✓ Google Business Profile creado y en verificación
- ✓ Website profesional publicado
- ✓ Análisis de competencia y keywords
- ✓ Brief completo de tu negocio

**Resultado (box rojo claro):**
```
🎯 Ya eres visible digitalmente. Los clientes pueden encontrarte.
```

---

**MES 2: OPTIMIZACIÓN**

**Badge:** "MES 2" (fondo amarillo)
**Días:** 31-60
**Imagen:** `06_timeline_mes2_optimizacion.png`

**Lo que optimizamos:**
- ✓ SEO local implementado
- ✓ 10 keywords estratégicas activas
- ✓ Contenido refinado
- ✓ Perfil completamente optimizado

**Resultado (box amarillo claro):**
```
🎯 Tu presencia digital trabaja a tu favor. Empiezas a destacar.
```

---

**MES 3: ACTIVACIÓN COMPLETA**

**Badge:** "MES 3" (fondo gris)
**Días:** 61-90
**Imagen:** `07_timeline_mes3_activacion.png`

**Lo que entregas:**
- ✓ Todas las credenciales (eres dueño 100%)
- ✓ Capacitación completa
- ✓ Guía de gestión de reviews
- ✓ Sistema listo para Google Ads

**Resultado (box gris claro):**
```
🎯 Sistema imán completo trabajando 24/7. Listo para escalar.
```

---

### SECCIÓN 5: BENEFICIOS

**Background:** Blanco

**H2:**
```
Qué Logras con el Sistema Imán Local™
```

**Grid 3x2 (6 cards con iconos):**

1. **🔍 VISIBILIDAD**
   - **Subtítulo:** Ya no serás invisible
   - **Copy:** Apareces cuando clientes buscan tu servicio en tu zona. Google Business Profile verificado + Website profesional.

2. **💪 CONFIANZA**
   - **Subtítulo:** Te verás tan profesional como la competencia
   - **Copy:** Presencia digital completa que genera credibilidad instantánea. No más perder contratos por verte "pequeño".

3. **🔑 CONTROL**
   - **Subtítulo:** Eres dueño 100% de todo
   - **Copy:** Todas las credenciales en tus manos. Si dejas de trabajar con nosotros, te quedas con todo. Sin ataduras.

4. **📈 ESCALABILIDAD**
   - **Subtítulo:** Listo para crecer cuando quieras
   - **Copy:** Sistema ads-ready desde día 1. Elige: orgánico (gratis pero más lento) o acelerado (con publicidad).

5. **⏰ 24/7**
   - **Subtítulo:** Tu negocio trabaja mientras duermes
   - **Copy:** Website + GBP optimizado atrayendo clientes automáticamente. Ya no dependes solo de referencias.

6. **🇲🇽 SIN BARRERAS**
   - **Subtítulo:** Todo en español, sin complicaciones
   - **Copy:** Entendemos tu negocio, tu idioma, tus desafíos. Implementación sin estrés técnico.

---

### SECCIÓN 6: 4 PASOS DEL SISTEMA

**Background:** Gris claro (#E5E5E5)

**H2:**
```
Los 4 Pasos del Sistema Imán Local™
```

**Layout:** 4 cards grandes (alternando imagen izquierda/derecha)

**PASO 1: FUNDACIÓN DIGITAL**

**Número grande:** 01 (gris claro, background)
**Imagen:** `08_paso1_fundacion_digital.png`

**Descripción:**
```
Establecemos tu presencia profesional
```

**Qué hacemos:**
- Creación de correo Gmail corporativo
- Compra y configuración de dominio + hosting
- Brief completo de tu negocio
- Diseño de website profesional (5-7 páginas)
- Creación de Google Business Profile
- Setup de LinkTree

**Resultado:**
```
Base digital sólida lista para trabajar
```

---

**PASO 2: MAGNETIZACIÓN LOCAL**

**Número grande:** 02
**Imagen:** `09_paso2_magnetizacion_local.png`

**Descripción:**
```
Te optimizamos para ser encontrado en tu zona
```

**Qué hacemos:**
- Investigación de 10 keywords estratégicas
- Optimización de categorías y servicios
- Configuración de áreas de cobertura
- Benchmarking de competencia
- Estructura técnica SEO correcta
- Schema markup básico

**Resultado:**
```
Visible para clientes en tu zona específica
```

---

**PASO 3: CONFIANZA VISUAL**

**Número grande:** 03
**Imagen:** `10_paso3_confianza_visual.png`

**Descripción:**
```
Creamos la imagen profesional que convierte
```

**Qué hacemos:**
- Diseño responsive (mobile + desktop)
- Optimización de fotos de servicios
- Fotos de verificación profesionales
- Avatar y portada para GBP
- Meta descriptions optimizadas
- Contenido que convierte visitas en clientes

**Resultado:**
```
Presencia digital que genera confianza instantánea
```

---

**PASO 4: ACTIVACIÓN 24/7**

**Número grande:** 04
**Imagen:** `11_paso4_activacion_247.png`

**Descripción:**
```
Tu sistema imán empieza a trabajar
```

**Qué hacemos:**
- Verificación de Google Business Profile
- Publicación completa del website
- Entrega de todas las credenciales
- Video tutorial de gestión
- Guía de gestión de reseñas
- Checklist de mantenimiento

**Resultado:**
```
Sistema completo 100% tuyo trabajando automáticamente
```

---

### SECCIÓN 7: ENTREGABLES

**Background:** Blanco

**H2:**
```
Qué Incluye Exactamente el Sistema Imán Local™
```

**Layout:** 3 columnas con checklists

**COLUMNA 1: 🌐 PRESENCIA DIGITAL COMPLETA**

**Website Profesional:**
- 5-7 páginas (Home + Services + Locations + About + Contact)
- Diseño responsive optimizado para mobile y desktop
- Hosting configurado en Squarespace (~$16-23/mes pago directo)
- Dominio configurado y activo

**Google Business Profile:**
- Perfil verificado y optimizado
- Configurado con tus servicios y áreas
- Fotos profesionales cargadas
- Listo para recibir reseñas

**Infraestructura Digital:**
- Correo Gmail corporativo configurado
- LinkTree con todos tus enlaces
- Todas las credenciales documentadas

---

**COLUMNA 2: 📍 OPTIMIZACIÓN LOCAL**

**SEO Implementado:**
- 10 keywords estratégicas investigadas
- Meta descriptions optimizadas
- Estructura técnica SEO correcta
- Schema markup básico

**Posicionamiento Local:**
- Configuración de área de cobertura
- Categorías correctas en GBP
- Benchmarking vs competencia
- Optimización para búsquedas "near me"

---

**COLUMNA 3: 📚 CAPACITACIÓN & SOPORTE**

**Documentación Completa:**
- Video tutorial de gestión (20 minutos)
- Guía de gestión de reseñas
- Checklist de mantenimiento mensual
- Manual de credenciales

**Soporte Incluido:**
- 90 días de soporte durante implementación
- Revisiones ilimitadas hasta aprobación
- Ajustes sin costo adicional

---

**BONO INCLUIDO (destacado con fondo amarillo claro):**

**🎁 Guía de Reviews Automáticas** (Valor: $200)
- Plantillas de mensajes para WhatsApp/SMS
- Script probado paso a paso
- Video tutorial
- Checklist mensual

---

### SECCIÓN 8: BONOS ADICIONALES

**Background:** Gris claro (#E5E5E5)

**H2:**
```
Bonos Exclusivos Según Tu Necesidad
```

**Copy intro:**
```
Además del bono incluido, evaluamos tu situación y te asignamos el bono adicional que más te ayude:
```

**3 Cards (grid 3 columnas):**

**OPCIÓN 1: Kit de Lanzamiento Digital**
**Valor:** $350

**Perfecto si:** Estás empezando y necesitas imagen profesional completa

**Incluye:**
- 50 tarjetas de presentación con QR
- 2 playeras con logo
- 2 gorras con logo
- LinkTree completamente configurado

---

**OPCIÓN 2: Acelerador de Visibilidad**
**Valor:** $300

**Perfecto si:** Quieres resultados inmediatos mientras el SEO trabaja

**Incluye:**
- 30 días de asesoría en Google Ads
- Guía de keywords para publicidad
- Estrategia de presupuesto recomendada
- Setup inicial de campaña

---

**OPCIÓN 3: Refresh de Identidad Visual**
**Valor:** $350

**Perfecto si:** Tu logo/marca actual no refleja profesionalismo

**Incluye:**
- Actualización o rediseño de logo
- Manual básico de marca
- Reforzamiento de identidad visual
- Vía Customize It (empresa aliada)

---

### SECCIÓN 9: GARANTÍA

**Background:** Blanco

**H2:**
```
Garantía Total de Propiedad
```

**Copy intro:**
```
Entendemos que invertir $3,300 en tu presencia digital es una decisión importante. Por eso garantizamos tu inversión de forma única:
```

**Callout Box grande (fondo gradiente rojo-amarillo claro):**

```
🛡️ AL FINAL DE LOS 90 DÍAS RECIBES:

✓ Todas las credenciales (Gmail, Squarespace, GBP)
✓ Acceso completo a todos tus activos digitales
✓ Documentación completa de tu sistema
✓ Propiedad 100% de website, dominio y perfiles
```

**Garantía en texto:**
```
Si no puedes acceder a algún activo digital al final de los 90 días, lo resolvemos inmediatamente o te reembolsamos la parte proporcional.
```

**Diferenciador (bold):**
```
A diferencia de otras agencias que te cobran $500-1,200 mensuales eternamente y nunca eres dueño de nada, con nosotros TODO es tuyo. Si decides dejar de trabajar con C3 Marketing después de los 90 días, te quedas con todo tu sistema funcionando.
```

---

### SECCIÓN 10: PRECIO E INVERSIÓN

**Background:** Gris claro (#E5E5E5)

**H2:**
```
Inversión en Tu Presencia Digital
```

**Tabla de Valor:**

| Componente | Valor |
|------------|-------|
| Website profesional (5-7 páginas) | $1,500 |
| Google Business Profile verificado | $1,200 |
| Optimización SEO + Keywords | $800 |
| Capacitación + Documentación | $300 |
| Bono: Guía de Reviews | $200 |
| **VALOR TOTAL** | **$4,000** |

---

**Precio Destacado (muy grande, centrado):**

```
💰 TU INVERSIÓN HOY: $3,300
```

**Ahorro:**
```
Ahorras $700 al iniciar ahora
```

---

**Opciones de Pago (3 cards):**

**Opción A: Pago Completo**
```
$3,135
(5% descuento por pago anticipado)
```

**Opción B: 3 Pagos Mensuales**
```
$1,100 por mes
durante implementación
```

**Opción C: Plan Personalizado**
```
Según tu situación específica
```

---

**Nota de Hosting (pequeña, gris):**
```
+ Hosting Squarespace: ~$16-23/mes (pago directo al proveedor - eres dueño desde día 1)
```

---

**Urgencia Ética (callout box con borde amarillo):**

```
⏰ CONDICIÓN ESPECIAL:

Solo disponible para los primeros 10 negocios de servicios que inicien este mes.

¿Por qué esta limitación?
Solo podemos manejar la implementación de 10 negocios simultáneamente para garantizar calidad y atención personalizada. Después de estos 10 espacios, el precio base aumenta a $3,800.
```

---

### SECCIÓN 11: TESTIMONIOS

**Background:** Blanco

**H2:**
```
Resultados Reales de Negocios Como el Tuyo
```

**Layout:** 3 cards testimonios (grid 3 columnas, stack mobile)

**Formato de cada testimonio:**

```
[Foto del cliente - placeholder si no hay foto real]

"[Quote del cliente sobre su transformación]"

- [Nombre], [Tipo de negocio]
📍 [Ciudad, CA]

Resultado:
• [Métrica específica 1]
• [Métrica específica 2]
• [Beneficio emocional]
```

**Nota:** Usar testimonios reales si están disponibles. Si no, usar casos de estudio sin foto enfocados en métricas objetivas (GBP verificado, website activo, tiempo de implementación).

**Ejemplo de placeholder:**

```
"Antes perdía contratos porque no aparecía en Google. Ahora mi perfil está verificado y mi website se ve tan profesional como la competencia grande."

- Juan Martínez, Martinez Landscaping
📍 San Jose, CA

Resultado:
• GBP verificado en 4 semanas
• Website profesional activo
• Ya no depende solo de referencias
```

---

### SECCIÓN 12: FAQ + CTA FINAL

**Background:** Gris claro (#E5E5E5)

**H2:**
```
Preguntas Frecuentes
```

**Layout:** Accordion (9 preguntas)

**1. ¿Para qué tipo de negocios funciona esto?**

```
El Sistema Imán Local™ está diseñado específicamente para negocios de servicios locales (home services) como landscaping, plomería, HVAC, electricidad, construcción, pintura, etc. Si tienes 4+ empleados y quieres dejar de depender solo de referencias, esto es para ti.
```

---

**2. ¿Realmente seré dueño de todo?**

```
Sí, 100%. Al final de los 90 días recibes todas las credenciales: Gmail, Squarespace, Google Business Profile. Todo está a tu nombre desde el principio. Si dejas de trabajar con nosotros, te quedas con todo funcionando.
```

---

**3. ¿Por qué 90 días y no más rápido?**

```
La verificación de Google Business Profile toma 3-5 semanas (especialmente para negocios sin sede física). La optimización SEO necesita tiempo para implementarse correctamente. 90 días es el tiempo real para hacer las cosas bien, no para cobrar más meses de mensualidades.
```

---

**4. ¿Qué pasa después de los 90 días?**

```
Tu sistema sigue trabajando 100% solo. No hay mensualidades obligatorias. Solo pagas el hosting de Squarespace (~$16-23/mes directo al proveedor). Si quieres mantenimiento opcional (actualizar contenido, gestionar reseñas, etc.), podemos ofrecer planes desde $300/mes, pero NO es obligatorio.
```

---

**5. ¿Necesito saber de tecnología?**

```
No. Todo el proceso técnico lo manejamos nosotros. Tú solo necesitas aprobar diseños y proveer fotos de tus servicios. Al final te capacitamos para las tareas básicas (responder reseñas, actualizar horarios), pero son cosas simples.
```

---

**6. ¿Funciona si no tengo oficina física?**

```
Sí. Tenemos experiencia específica verificando negocios de área de servicio (sin dirección física visible). El proceso toma ~5 semanas vs ~3 semanas con oficina, pero funciona perfecto.
```

---

**7. ¿Incluye publicidad en Google?**

```
El sistema te deja ads-ready desde día 1, pero la inversión en publicidad es adicional y opcional. Puedes empezar orgánico (gratis) o acelerar con ads cuando quieras (presupuesto sugerido: $500-1,000/mes).
```

---

**8. ¿Qué pasa si no estoy satisfecho?**

```
Durante los 90 días hacemos revisiones ilimitadas hasta tu aprobación. Al final, si no tienes acceso a todos tus activos digitales como prometimos, te reembolsamos la parte proporcional.
```

---

**9. ¿Por qué solo 10 espacios al mes?**

```
Cada implementación requiere atención personalizada: brief detallado, diseño custom, verificación manual, capacitación 1-on-1. Para mantener calidad, limitamos a 10 implementaciones simultáneas.
```

---

### CTA FINAL (grande, centrado, fondo blanco)

**H2:**
```
Estás a Una Llamada de Convertirte en Visible
```

**Copy:**
```
Si has llegado hasta aquí, probablemente el Sistema Imán Local™ tiene sentido para tu negocio.

El siguiente paso es simple:
```

**CTA Principal (botón muy grande, rojo):**
```
📞 Agendar Llamada de Diagnóstico Gratuita
```

**Qué Pasa en la Llamada:**

```
30 minutos donde:

✓ Analizamos tu situación específica
✓ Identificamos tus obstáculos actuales
✓ Verificamos si eres candidato ideal
✓ Respondemos todas tus preguntas
✓ Si encajamos, diseñamos tu plan de 90 días

No es una llamada de venta agresiva. Es una conversación profesional para determinar si podemos ayudarte.
```

---

## 🧭 NAVBAR (Sticky)

**Background:** Blanco con sombra sutil
**Position:** Fixed top

**Contenido:**
- **Izquierda:** Logo C3 (`c3white200x200.svg` con fondo de color o versión naranja si fondo blanco)
- **Derecha:** CTA "Agenda tu Auditoría Gratuita" (botón rojo)

**Responsive:**
- Desktop: Logo + CTA
- Mobile: Logo más pequeño + CTA compacto

---

## 🦶 FOOTER

**Background:** Gris oscuro (#58595B)
**Color texto:** Blanco

**Contenido:**

**Columna 1: Logo + Tagline**
- Logo C3 blanco
- "De invisible a visible. En 90 días."
- "Sistema Imán Local™ - C3 Marketing"

**Columna 2: Contacto**
- **Email:** luis@c3marketinghub.com
- **Web:** c3localmarketing.com
- **Teléfono:** [Agregar número]

**Columna 3: Enlaces Rápidos**
- Cómo Funciona
- Beneficios
- Precio
- FAQ
- Agendar Llamada

**Copyright (centrado, abajo):**
```
© 2025 C3 Marketing. Todos los derechos reservados.
```

---

## 🎯 CTAS ESTRATÉGICOS

**Ubicaciones de CTAs:**
1. Navbar (siempre visible)
2. Hero (2 CTAs: primario + secundario)
3. Después de Problema
4. Después de Timeline
5. Después de Precio
6. CTA Final (grande)

**Texto consistente:**
- "Agendar Llamada de Diagnóstico Gratuita"
- "Agenda tu Auditoría Gratuita"

**Estilo:**
- Botón rojo (#EF4125)
- Texto blanco
- Hover: Rojo más oscuro (#D63820)
- Border radius: 8px
- Padding: 16px 32px
- Font: Poppins SemiBold 16px

---

## 📱 RESPONSIVE DESIGN

**Breakpoints:**
- Mobile: < 640px
- Tablet: 640px - 1024px
- Desktop: > 1024px

**Mobile-first:**
- Stack todas las secciones verticalmente
- Grid 3 columnas → 1 columna
- Imágenes full-width
- Texto centrado
- CTAs full-width
- Navbar compacto

**Desktop:**
- Grid 2-3 columnas según sección
- Imágenes lado a lado con texto
- Texto alineado izquierda
- CTAs inline
- Navbar completo

---

## ✅ CHECKLIST DE IMPLEMENTACIÓN

**Antes de empezar:**
- [ ] Descargar assets del repositorio usando `lov-download-to-repo`
- [ ] Verificar que todas las 18 imágenes están disponibles
- [ ] Confirmar logos C3 en formato SVG

**Durante desarrollo:**
- [ ] Configurar paleta de colores C3 en CSS
- [ ] Importar fuentes Google (Poppins + Open Sans)
- [ ] Crear navbar sticky con logo + CTA
- [ ] Implementar las 12 secciones en orden
- [ ] Agregar accordion para FAQ
- [ ] Crear footer completo
- [ ] Configurar responsive mobile-first
- [ ] Agregar smooth scroll para CTAs

**Antes de entregar:**
- [ ] Verificar que todas las imágenes cargan correctamente
- [ ] Probar todos los CTAs
- [ ] Revisar responsive en mobile/tablet/desktop
- [ ] Verificar contraste de colores (accesibilidad)
- [ ] Optimizar imágenes para web
- [ ] Agregar alt text a todas las imágenes

---

## 📚 ARCHIVOS DE REFERENCIA

**En este repositorio:**
- `/docs/Landing_Content_Sistema_Iman_Local.md` - Contenido completo detallado
- `/docs/Brief_Manu_Landing_Framer.md` - Brief original con especificaciones
- `/FIGMA_TEMPLATE_ANALYSIS.md` - Análisis del template Figma
- `/COLORES_Y_DISENO_LANDING.md` - Guía de colores y diseño
- `/RUNWAY_PROMPTS.md` - Prompts usados para generar imágenes

---

## 🚀 NOTAS FINALES

**Objetivo de conversión:**
- La landing debe convertir visitantes en llamadas agendadas
- Cada sección debe construir sobre la anterior (problema → solución → prueba → precio → acción)
- Los CTAs deben ser claros y consistentes
- El diseño debe verse profesional pero accesible (hispano-friendly)

**Tono de voz:**
- Directo y honesto (no pretencioso)
- Profesional pero cálido (no frío corporativo)
- Empático con los desafíos de negocios hispanos
- Orientado a resultados concretos (no promesas vagas)

**Diferenciadores clave a destacar:**
1. **Propiedad total** (no rentas eternas)
2. **90 días** (tiempo real, no mensualidades infinitas)
3. **En español** (sin barreras de idioma)
4. **Probado con hispanos** (no teoría genérica)

---

**¡Éxito con la implementación!** 🎉
