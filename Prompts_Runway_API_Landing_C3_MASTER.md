# 🎬 PROMPTS RUNWAY API - LANDING C3 MARKETING
## Guía Completa para Generación de Assets Visuales

**Fecha:** Noviembre 2025  
**Para:** Manu (Implementador) - C3 Marketing  
**Cliente:** Luis A. Arroyo  
**Proyecto:** Landing Page Sistema Imán Local™

---

## 📋 ÍNDICE

1. [Información del Equipo](#equipo)
2. [Orden de Ejecución Recomendado](#orden)
3. [Prompts Nivel PRO (6)](#pro)
4. [Prompts Nivel Medio (9)](#medio)
5. [Especificaciones Técnicas](#specs)
6. [Checklist de Validación](#checklist)
7. [Tips Runway API](#tips)

---

## 👥 INFORMACIÓN DEL EQUIPO {#equipo}

### **Personas Identificadas:**

**Luis A. Arroyo** - Fundador C3 Marketing
- Foto: Coral/salmon shirt con logo "C3", fondo oficina persianas
- Uso: Hero principal, About, Team

**María Emilia** - Consultora Creativa
- Foto: Coral/salmon shirt, escritorio con iMac
- Uso: Team, About, Testimonials internos

**Carlos Cordero** - Equipo
- Foto: Camisa gris + lanyard Facebook, fondo azul con like neón
- Acción: Transformar fondo azul → oficina (match Luis/María)
- Uso: Team, About

---

## 🎯 ORDEN DE EJECUCIÓN RECOMENDADO {#orden}

### **FASE 1: FOTOS EQUIPO (Primera prioridad)**

**1.1 Transformar fondo Carlos** (Prompt #1)
- Input: Foto fondo azul
- Output: Fondo oficina blanco/persianas
- Tiempo: 5-10 min
- Validar: Cohesión con fotos Luis/María

### **FASE 2: HERO & MOCKUPS CRÍTICOS**

**2.1 Hero Luis con tablet** (Prompt #2)
- Input: Foto Luis coral shirt
- Output: Luis sosteniendo iPad con GBP
- Tiempo: 10-15 min
- Validar: Pantalla GBP legible

**2.2 Mockup Google Mobile** (Prompt #3)
- Input: N/A (generación pura)
- Output: iPhone con búsqueda "landscaping near me"
- Tiempo: 10-15 min
- Validar: UI Google auténtico

**2.3 Mockup GBP Desktop** (Prompt #4)
- Input: N/A (generación pura)
- Output: Mac con dashboard GBP
- Tiempo: 10-15 min
- Validar: Dashboard completo y profesional

### **FASE 3: ILUSTRACIONES TIMELINE (Críticas)**

**3.1 Timeline Mes 1** (Prompt #5)
- Output: Ilustración fundación digital
- Tiempo: 8-12 min
- Validar: Número "1" visible, colores C3

**3.2 Timeline Mes 2** (Prompt #7)
- Output: Ilustración magnetización local
- Tiempo: 8-12 min
- Validar: Consistencia con Mes 1

**3.3 Timeline Mes 3** (Prompt #8)
- Output: Ilustración activación 24/7
- Tiempo: 8-12 min
- Validar: Set completo cohesivo

### **FASE 4: ICONOS (Críticos)**

**4.1 Set de 6 iconos** (Prompt #6)
- Output: 6 iconos beneficios
- Tiempo: 10-15 min (todos juntos)
- Validar: Estilo consistente, mismo stroke

### **FASE 5: PASOS DEL SISTEMA**

**5.1-5.4 Pasos 1-4** (Prompts #9-12)
- Output: 4 ilustraciones pasos
- Tiempo: 6-8 min cada uno (24-32 min total)
- Validar: Números visibles, estilo cohesivo

### **FASE 6: ELEMENTOS ADICIONALES**

**6.1 Badges** (Prompt #13)
- Output: 3 badges en 1 imagen
- Tiempo: 5-8 min

**6.2 Background Pattern** (Prompt #14)
- Output: Pattern sutil
- Tiempo: 5-8 min

---

## **TIEMPO TOTAL ESTIMADO: 2-3 horas**

**Breakdown:**
- Fase 1: 10 min
- Fase 2: 45 min
- Fase 3: 30 min
- Fase 4: 15 min
- Fase 5: 30 min
- Fase 6: 15 min

---

## 🔥 PROMPTS NIVEL PRO {#pro}

### **Los 6 prompts con máximo detalle técnico**

---

### **PROMPT #1: TRANSFORMAR FONDO CARLOS** ⭐⭐⭐⭐⭐

#### Nivel: PRO | Prioridad: CRÍTICA | Tiempo: 5-10 min

```
[TASK: Background replacement - preserve subject 100%]
[REFERENCE STYLE: Match Luis's office photo aesthetic]

PRESERVE COMPLETELY:
- Subject: Carlos Cordero in gray shirt with Facebook lanyard
- Body position: Arms crossed, confident pose
- Facial features and expression: Professional, approachable
- Clothing details: Gray button-up shirt, Facebook lanyard, watch
- Natural lighting on subject

TRANSFORM BACKGROUND:
FROM: Blue wall with neon "like" sign
TO: Clean office environment matching reference photo

NEW BACKGROUND SPECIFICATIONS:
- Wall: Off-white/light beige (#F5F5F0)
- Window blinds: Horizontal aluminum blinds (visible behind subject)
- Lighting: Soft natural office lighting (diffused, no harsh shadows)
- Depth: Slight background blur (f/2.8 equivalent)
- Style: Professional office, minimalist, clean

LIGHTING ADJUSTMENTS:
- Maintain natural skin tones
- Soft key light from camera left (window light)
- Even illumination, no dramatic shadows
- Color temperature: 5200K (warm daylight)

QUALITY REQUIREMENTS:
- Seamless edge transition (subject to background)
- No halo effects or selection artifacts
- Match grain/noise levels of reference photo
- Professional photography quality
- Resolution: Maintain original high resolution

TECHNICAL NOTES:
- Strength: 0.75 (strong background change, preserve subject)
- Preserve original subject sharpness
- Match color grading of Luis's photo
- Natural integration, photorealistic result

NEGATIVE PROMPT: No artificial green screen look, no obvious compositing, no edge halos, no color spill, no unnatural lighting transitions, no quality degradation on subject
```

**VALIDACIÓN:**
- [ ] Fondo coincide con estilo Luis/María
- [ ] Carlos preservado 100% (sin distorsión)
- [ ] Iluminación natural y consistente
- [ ] No artifacts de compositing
- [ ] Cohesión visual con equipo

---

### **PROMPT #2: HERO LUIS CON TABLET** ⭐⭐⭐⭐⭐

#### Nivel: PRO | Prioridad: CRÍTICA | Tiempo: 10-15 min

```
[STYLE: Corporate photography, environmental portrait, shallow DOF]
[COMPOSITION: Rule of thirds, 3/4 angle, confident professional pose]
[REFERENCE: Use Luis's existing coral shirt photo as base]

MAIN SUBJECT:
- Person: Luis A. Arroyo (Hispanic male, 35-45, bald/short hair)
- Expression: Confident smile, approachable, trustworthy demeanor
- Eye contact: Looking at camera (connection with viewer)
- Posture: Relaxed confidence, slight lean forward

WARDROBE & PROPS:
- Shirt: Coral/salmon C3 branded shirt (#EF4125 family) with "C3" logo visible
- Key prop: iPad Pro 12.9" (2024 model, space gray)
- Holding position: 45° angle toward camera, screen visible
- Hand position: Natural grip, professional not casual
- Watch visible: Subtle professional timepiece (black/dark)

TABLET SCREEN CONTENT (CRITICAL - HIGHLY DETAILED):
Display active Google Business Profile interface:
- Business name: "Garcia Landscaping" or similar Hispanic-owned business
- Location: San Luis Obispo, CA (visible in address)
- Star rating: 5 gold stars (★★★★★) prominently displayed
- Review count: "47 reviews" in gray text below stars
- Status indicator: Green "Open now" badge with clock icon
- Photo grid: 6 professional service photos visible (landscaping work)
- Category badge: "Landscaping Service" visible
- CTA buttons: "Call" and "Website" buttons visible
- Map section: Small map showing location (optional, can be partially visible)
- Screen brightness: Realistic (not blown out), readable text

ENVIRONMENT & BACKGROUND:
- Setting: Modern office (match Luis's existing photo style)
- Background: Horizontal aluminum window blinds (off-white/beige wall)
- Left side: Partial white shelving with subtle props (water bottle, notebooks)
- Right side: Clean negative space
- Depth of field: Subject sharp (f/2.8), background 50% soft blur

LIGHTING SETUP (NATURAL LOOKING):
- Key light: Soft window light from camera left (70% intensity)
- Fill light: Reflector bounce from right (30% intensity, subtle)
- Rim light: Natural backlight from window (separates subject from background)
- No visible harsh shadows on face
- Even skin tones, professional color grading
- Golden hour quality (warm, inviting, not midday harsh)

COLOR GRADING & POST-PROCESSING:
- Overall: Warm professional tone (5200-5500K)
- Skin tones: Natural, healthy, Latino complexion accurate
- Brand color: Coral shirt prominent but not oversaturated (#EF4125 ±5%)
- Background: Slightly cooler (color separation)
- Contrast: Medium (professional not dramatic)
- Saturation: Slightly elevated (modern corporate style, not flat)
- Highlights: Protected (no blown out whites)
- Shadows: Lifted slightly (detail in dark areas)

CAMERA TECHNICAL SPECS:
- Focal length: 50mm prime lens character
- Aperture: f/2.8 (shallow DOF, professional look)
- Camera angle: Eye level, slight 3/4 turn
- Framing: Medium shot (waist up), room for text overlay top/bottom
- Resolution: 1920x1080px minimum (web hero standard)
- Quality: Print-ready equivalent (300dpi compression quality)
- Format: Landscape 16:9 ratio
- Sensor: Full-frame DSLR aesthetic (Canon 5D IV / Sony A7 III equivalent)

COMPOSITION RULES:
- Rule of thirds: Subject on right third, tablet screen on left third
- Negative space: 40% on left (room for headline text overlay)
- Eye line: Upper third horizontal line
- Tablet screen: Lower left third intersection (power point)
- Balance: Visual weight distributed (subject + prop)

MOOD & EMOTION:
- Overall feeling: Success, confidence, expertise, approachability
- Cultural authenticity: Hispanic professional, bilingual business context
- Trust signals: Professional attire, quality tools (iPad), real results (GBP)
- Aspirational: "This could be you" feeling for target audience (Octavio)

USAGE CONTEXT:
- Hero section of landing page
- Must work with text overlay (headline + subheadline on left negative space)
- CTAs will be placed below (ensure clean bottom third)
- Mobile crop consideration: Subject still prominent at 9:16 ratio

NEGATIVE PROMPT: 
No generic stock photo look, no artificial studio backdrop, no harsh top-down lighting, no dated fashion or tech, no clipart or illustrated elements, no exaggerated expressions or poses, no visible watermarks or logos (except C3 shirt), no distracting background elements, no unnatural skin retouching, no color casts, no motion blur, no low resolution artifacts, no obvious compositing, no floating/disconnected props

CONSISTENCY REQUIREMENTS:
[SEED: Request same seed for matching set]
[STYLE REFERENCE: Match Luis's existing professional photos]
[QUALITY: Hero-grade, featured image quality]

POST-GENERATION VALIDATION:
✓ Tablet screen content clearly visible and readable
✓ GBP interface looks authentic (2025 current design)
✓ C3 logo on shirt visible but not distracting
✓ Face well-lit, professional expression
✓ Background appropriately blurred but recognizable
✓ No technical artifacts or errors
✓ Warm, inviting, professional overall tone
```

**VALIDACIÓN:**
- [ ] Luis reconocible y profesional
- [ ] iPad visible con GBP legible en pantalla
- [ ] Logo C3 visible en shirt
- [ ] Lighting natural y cálido
- [ ] Composición rule of thirds
- [ ] Espacio para text overlay (izquierda)
- [ ] Fondo match con fotos existentes

---

### **PROMPT #3: MOCKUP GOOGLE SEARCH MOBILE** ⭐⭐⭐⭐⭐

#### Nivel: PRO | Prioridad: CRÍTICA | Tiempo: 10-15 min

```
[DEVICE: iPhone 14 Pro mockup - ultra realistic]
[SCREEN CONTENT: Google Search results - "landscaping near me"]
[STYLE: Product photography, floating device, soft shadows]

DEVICE SPECIFICATIONS:
- Model: iPhone 14 Pro (2023) - Space Black
- Orientation: Portrait (vertical)
- Screen: Active, bright, no glare
- Bezels: Accurate to model (thin, Dynamic Island visible at top)
- Condition: Pristine (no scratches, fingerprints minimal)
- Shadow: Soft drop shadow beneath device (floating effect)

SCREEN CONTENT LAYOUT (TOP TO BOTTOM):

1. STATUS BAR (iOS 17 style):
   - Time: 2:47 PM (left)
   - Signal/WiFi/Battery: Full strength (right)
   - Dynamic Island: Subtle, not expanded

2. GOOGLE SEARCH BAR:
   - Google logo (colored) on left
   - Search query: "landscaping near me" (visible text in bar)
   - Voice/Camera icons on right
   - Below search bar: Tabs (All, Images, Maps, Videos, News)
   - "Maps" tab active/selected

3. GOOGLE MAPS SECTION (3 Business Listings):

   LISTING #1 (TOP - PROFESSIONAL):
   - Business name: "Garcia's Landscaping" (bold)
   - Star rating: ★★★★★ 5.0 (47 reviews) - GOLD STARS
   - Category badge: "Landscaping service"
   - Distance: "2.3 mi" with location pin icon
   - Status: Green "Open" indicator with "Closes 6 PM"
   - Thumbnail photos: 3 professional photos visible (lawn, hardscape, team)
   - Phone icon + "Call" button visible
   - Directions icon visible
   - Professional complete listing aesthetic

   LISTING #2 (MIDDLE - MEDIOCRE):
   - Business name: "Local Yards & More"
   - Star rating: ★★★☆☆ 3.2 (8 reviews) - Mixed stars
   - Category: "Landscape designer"
   - Distance: "3.1 mi"
   - Status: "Hours not available" (gray text)
   - Photos: 1 mediocre photo or no photo (placeholder)
   - Less prominent, incomplete profile feel

   LISTING #3 (BOTTOM - POOR):
   - Business name: "Landscaping Service" (generic)
   - Star rating: No rating (gray "No reviews")
   - Category: Basic or uncategorized
   - Distance: "4.5 mi"
   - Status: No hours listed
   - Photos: None (gray placeholder or single poor quality)
   - Minimal information, amateur appearance

4. MAP VIEW (SMALL):
   - Small map section below listings (optional, can be cropped)
   - Shows pins for businesses
   - California/SLO area recognizable if included

VISUAL HIERARCHY:
- Listing #1: Most prominent, professional, complete (occupies 40% of visible results)
- Clear contrast: Professional vs amateur listings obvious at glance
- Color coding: Green "Open" stands out, gold stars prominent

DEVICE PRESENTATION:
- Viewing angle: Straight-on or slight 15° tilt for depth
- Hand holding device: Optional but recommended
   - Hand: Hispanic male hand (natural skin tone)
   - Grip: Natural thumb-and-fingers hold (right hand)
   - Background: Blurred neutral (office or outdoor soft focus)
- OR floating device on clean surface with soft shadow

LIGHTING & RENDERING:
- Screen brightness: Optimal (readable but not blown out)
- Screen reflection: Minimal (anti-glare coating effect)
- Device edges: Crisp, accurate
- Shadow: Soft, realistic (not heavy Photoshop drop shadow)
- Overall lighting: Even, professional product shot quality

COLOR & VISUAL ACCURACY:
- Google branding: Accurate colors (red, yellow, blue, green in logo)
- iOS interface: Current iOS 17 design language
- Star colors: Gold (#F9B718 or similar)
- Green indicators: Google Maps green (#34A853)
- Text: Black on white, high contrast, readable
- Professional listing: Subtle color highlights

TECHNICAL SPECIFICATIONS:
- Resolution: 800x1200px (portrait, standard mobile mockup)
- Format: PNG with transparency OR on subtle neutral background
- Quality: Product photography grade
- Screen: Realistic pixel density (Retina display quality)
- No visible pixels or artifacts

COMPOSITION:
- Device centered or slightly off-center for visual interest
- Screen content occupies 85% of device (accurate bezels)
- Negative space: Clean, not cluttered
- Focus: Screen content sharp, device edges sharp
- Background: Minimal distraction (if present)

MOOD & MESSAGE:
- Clear visual story: "This is how customers search"
- Obvious contrast: Professional vs amateur listings
- Educational: Shows importance of complete GBP
- Target audience: Business owners seeing search reality

USAGE CONTEXT:
- Landing page "Problem" section
- Demonstrates search behavior
- Shows competitive landscape
- Mobile-first search emphasis (60% of searches)

NEGATIVE PROMPT:
No unrealistic screen glow, no pixelated UI elements, no incorrect iOS version, no Android device, no outdated Google interface, no fake/placeholder text (use realistic business names), no oversaturated colors, no heavy filters, no visible template watermarks, no low-res screenshots, no distorted aspect ratios, no floating disconnected elements, no cartoonish renders

CONSISTENCY:
[DEVICE STYLE: Match professional product mockup standards]
[UI ACCURACY: Use current 2025 Google Maps / iOS design]
[BRAND COLORS: Maintain Google's official color palette]

VALIDATION CHECKLIST:
✓ iOS interface current and accurate
✓ Google Maps layout authentic (2025)
✓ Business listings realistic and readable
✓ Clear visual hierarchy (pro vs amateur obvious)
✓ Device rendering photorealistic
✓ Screen brightness optimal for readability
✓ No technical artifacts or errors
```

**VALIDACIÓN:**
- [ ] iPhone 14 Pro reconocible
- [ ] iOS 17 interface auténtico
- [ ] Google Maps UI correcto (2025)
- [ ] 3 listings visibles y legibles
- [ ] Contraste claro: profesional vs amateur
- [ ] Screen brightness óptimo
- [ ] No pixelación

---

### **PROMPT #4: MOCKUP GBP DESKTOP** ⭐⭐⭐⭐⭐

#### Nivel: PRO | Prioridad: CRÍTICA | Tiempo: 10-15 min

*(Contenido completo del prompt #4 de la sección anterior)*

[Incluir aquí el prompt extenso del GBP Desktop que generé anteriormente]

---

### **PROMPT #5: TIMELINE MES 1 - FUNDACIÓN DIGITAL** ⭐⭐⭐⭐⭐

#### Nivel: PRO | Prioridad: ALTA | Tiempo: 8-12 min

*(Contenido completo del prompt #5 de Timeline Mes 1)*

[Incluir aquí el prompt extenso del Timeline Mes 1]

---

### **PROMPT #6: SET DE 6 ICONOS** ⭐⭐⭐⭐⭐

#### Nivel: PRO | Prioridad: CRÍTICA | Tiempo: 10-15 min

*(Contenido completo del prompt master de iconos)*

[Incluir aquí el prompt extenso de los 6 iconos]

---

## 📊 PROMPTS NIVEL MEDIO {#medio}

### **Los 9 prompts eficientes pero completos**

---

### **PROMPT #7: TIMELINE MES 2 - MAGNETIZACIÓN LOCAL**

#### Nivel: MEDIO | Prioridad: ALTA | Tiempo: 8-12 min

```
Modern flat illustration, 800x600px landscape. Local SEO magnetization concept.

MAIN ELEMENTS:
- Stylized California map (center, 50% of canvas, outline style)
- 3-4 location pins on map (red #EF4125, drop pin style)
- Magnifying glass (top-right, overlapping map, 30% size)
- Keyword tags: "#1", "#2", "#3" (floating, yellow #F9B718 badge style)
- Upward trending graph (bottom-right, subtle, 20% size)
- Google "G" icon (small, top-left corner, optional)

COLORS:
- Primary: #EF4125 (red) - pins, main elements
- Secondary: #F9B718 (yellow) - keyword badges, highlights
- Structural: #5C5C5C (gray) - map lines, graph
- Background: White (#FFFFFF)

STYLE:
- Clean geometric shapes
- Minimalist business illustration
- Flat 2D (no 3D effects)
- Icon-based, professional

NUMBER INDICATOR:
- Large "2" in red circle (top-left corner)
- White text on #EF4125 background
- Size: 72px

COMPOSITION:
- Centered, balanced
- 30% negative space
- Grid-aligned elements

MESSAGE: "Optimizing for local search visibility"

TECHNICAL:
- Format: PNG or SVG
- Resolution: 800x600px
- Transparent OR white background
- File size: Under 500KB
```

**VALIDACIÓN:**
- [ ] Número "2" visible
- [ ] Colores C3 correctos
- [ ] Estilo consistente con Mes 1
- [ ] California map reconocible
- [ ] Keywords prominentes

---

### **PROMPT #8: TIMELINE MES 3 - ACTIVACIÓN 24/7**

#### Nivel: MEDIO | Prioridad: ALTA | Tiempo: 8-12 min

```
Modern flat illustration, 800x600px landscape. Automated 24/7 system concept.

MAIN ELEMENTS:
- Central 24/7 clock (50% of canvas, circular, showing "24" or full circle)
- Notification badges (3-4 floating, various colors, pop-up style)
- Smartphone with ring/notification icon (right, 30% size, vertical)
- Calendar with appointment dots (left, 30% size)
- Growth chart arrow (bottom, trending up, 20% size)
- Toggle switch "ON" position (top, small, green indicator)

COLORS:
- Primary: #EF4125 (red) - clock, main elements
- Secondary: #F9B718 (yellow) - notifications
- Active: #009933 (green) - "ON" toggle, growth
- Structural: #5C5C5C (gray) - outlines
- Background: White

STYLE:
- Energetic but professional
- Clean geometric shapes
- Icon-based, modern
- Dynamic feel (movement suggested)

NUMBER INDICATOR:
- Large "3" in red circle (top-left)
- White text on #EF4125
- Size: 72px

MESSAGE: "System working automatically 24/7"

TECHNICAL:
- Format: PNG or SVG
- Resolution: 800x600px
- Optimized for web
```

**VALIDACIÓN:**
- [ ] Número "3" visible
- [ ] 24/7 concept clear
- [ ] Green "ON" prominent
- [ ] Dynamic feel
- [ ] Cohesivo con Mes 1 y 2

---

### **PROMPTS #9-12: PASOS 1-4 DEL SISTEMA**

#### Nivel: MEDIO | Prioridad: ALTA | Tiempo: 6-8 min cada uno

---

**PROMPT #9: PASO 1 - FUNDACIÓN DIGITAL**

```
Modern flat illustration, 600x600px square. Digital foundation concept.

MAIN ELEMENTS:
- 3 devices stacked: Desktop (back), tablet (middle), phone (front)
- .com domain symbol (top-right, floating)
- Gmail envelope (top-left, floating)
- Upward arrow (bottom, growth)

COLORS: C3 palette (#EF4125, #F9B718, #5C5C5C) on white
NUMBER: XXL "1" (80px, prominent, top-left OR overlay)
STYLE: Icon-based, clean, organized, flat 2D

Technical: 600x600px, PNG/SVG, under 400KB
```

---

**PROMPT #10: PASO 2 - MAGNETIZACIÓN LOCAL**

```
Modern flat illustration, 600x600px square. Local SEO concept.

MAIN ELEMENTS:
- Google Maps pin (center, large, red)
- "#1" ranking badge (prominent, yellow)
- Magnifying glass (overlapping pin)
- Target/bullseye icon (small)
- Map lines/geography (subtle background)

COLORS: C3 palette
NUMBER: XXL "2" (80px, prominent)
STYLE: Clean, professional, icon-focused

Technical: 600x600px, PNG/SVG
```

---

**PROMPT #11: PASO 3 - CONFIANZA VISUAL**

```
Modern flat illustration, 600x600px square. Responsive design concept.

MAIN ELEMENTS:
- 3 devices showing same website (desktop, tablet, mobile)
- 5 gold stars (review rating, prominent)
- Camera icon (professional photos)
- Checkmark (quality indicator)

COLORS: C3 palette, gold stars #F9B718
NUMBER: XXL "3" (80px, prominent)
STYLE: Device-focused, professional

Technical: 600x600px, PNG/SVG
```

---

**PROMPT #12: PASO 4 - ACTIVACIÓN 24/7**

```
Modern flat illustration, 600x600px square. Automation activation concept.

MAIN ELEMENTS:
- Toggle switch "ON" (large, center, green)
- Notification bubbles (3-4, popping effect)
- Calendar with appointments (marked dates)
- Upward trending chart
- Checkmarks (completion indicators)

COLORS: C3 palette + green #009933 for "ON"
NUMBER: XXL "4" (80px, prominent)
STYLE: Dynamic, energetic, professional

Technical: 600x600px, PNG/SVG
```

**VALIDACIÓN (Pasos 1-4):**
- [ ] Números 1-4 claramente visibles
- [ ] Estilo visual consistente (set cohesivo)
- [ ] Colores C3 correctos
- [ ] Concept claro en cada uno
- [ ] Mismo stroke weight/style

---

### **PROMPT #13: BADGES (3 en 1)**

#### Nivel: MEDIO | Prioridad: MEDIA | Tiempo: 5-8 min

```
3 circular badges, horizontal layout, 600x200px total (200x200px each).

BADGE 1: "100% TUYO"
- Icon: Key (center)
- Text: "100% TUYO" (curved or below)
- Colors: White text on #EF4125 OR #EF4125 border on white

BADGE 2: "90 DÍAS"
- Icon: Calendar (center)
- Text: "90 DÍAS"
- Same color treatment as Badge 1

BADGE 3: "SIN ATADURAS"
- Icon: Broken chain (center)
- Text: "SIN ATADURAS"
- Same color treatment

STYLE:
- Circular OR shield shape (choose one, consistent)
- Professional, trustworthy
- Badge/seal aesthetic
- Modern, clean

PURPOSE: Trust indicators for landing page

Technical: 600x200px total, PNG with transparency, optimized
```

**VALIDACIÓN:**
- [ ] 3 badges mismo estilo
- [ ] Icons claros y reconocibles
- [ ] Text legible
- [ ] Colores C3
- [ ] Trust/credibility feeling

---

### **PROMPT #14: BACKGROUND PATTERN**

#### Nivel: MEDIO | Prioridad: BAJA | Tiempo: 5-8 min

```
Subtle geometric background pattern, 1920x1080px, tileable/seamless.

PATTERN OPTIONS (choose one):
- Abstract dots (random or grid)
- Subtle lines (diagonal or wave)
- Geometric shapes (very subtle)

COLORS:
- Base: #DCDCDC (light gray)
- Accents: #EF4125 and #F9B718 at 10-15% opacity (barely visible)

PURPOSE:
- Background texture for landing page sections
- Should NOT compete with content
- Barely visible, adds subtle depth

STYLE:
- Minimal, professional
- Modern, clean
- Not distracting

TECHNICAL:
- 1920x1080px
- Tileable (seamless repeat)
- PNG or SVG
- Optimized file size (under 200KB)
```

**VALIDACIÓN:**
- [ ] Pattern muy sutil (no invasivo)
- [ ] Tileable (se repite sin costuras)
- [ ] Colores C3 al 10-15% opacity
- [ ] No distrae del contenido principal

---

## 📐 ESPECIFICACIONES TÉCNICAS {#specs}

### **FORMATOS DE EXPORTACIÓN**

**Fotos/Mockups:**
- Formato: PNG o JPG
- Resolución: As specified per prompt (1920x1080, 800x1200, etc.)
- Calidad: High (85-95% quality)
- Color space: RGB
- Compression: Optimized for web (TinyPNG después si necesario)

**Ilustraciones:**
- Formato: SVG preferido (escalable) OR PNG 2x
- Transparencia: Sí (alpha channel)
- Resolución: As specified (600x600, 800x600)
- Optimización: Clean paths (SVG) o compressed (PNG)

**Iconos:**
- Formato: SVG REQUIRED (vectorial)
- Tamaño canvas: 200x200px per icon
- Padding: 20px (active area 160x160px)
- Stroke: 4px consistent
- Exportar: Individual files + set completo

---

### **COLORES C3 OFICIALES (HEX)**

```css
/* Primarios */
--c3-red: #EF4125;
--c3-yellow: #F9B718;

/* Secundarios */
--c3-dark-gray: #5C5C5C;
--c3-light-gray: #DCDCDC;
--c3-border-gray: #9C9C9B;

/* Adicionales */
--c3-white: #FFFFFF;
--c3-green: #009933; /* Solo para indicadores "ON/Active" */
```

---

### **DIMENSIONES ESTÁNDAR**

| Asset Type | Dimensions | Ratio | Format |
|------------|------------|-------|---------|
| Hero | 1920x1080px | 16:9 | PNG/JPG |
| Mobile Mockup | 800x1200px | 2:3 | PNG |
| Desktop Mockup | 1200x800px | 3:2 | PNG |
| Timeline | 800x600px | 4:3 | PNG/SVG |
| Pasos | 600x600px | 1:1 | PNG/SVG |
| Iconos | 200x200px | 1:1 | SVG |
| Badges | 600x200px | 3:1 | PNG |
| Pattern | 1920x1080px | 16:9 | PNG/SVG |

---

## ✅ CHECKLIST DE VALIDACIÓN {#checklist}

### **POR CADA ASSET GENERADO:**

**CALIDAD TÉCNICA:**
- [ ] Resolución correcta (según specs)
- [ ] Sin pixelación o artifacts
- [ ] Colores C3 precisos (no desviados)
- [ ] Formato correcto (PNG/SVG según requerido)
- [ ] File size optimizado (web-ready)

**BRAND CONSISTENCY:**
- [ ] Paleta C3 respetada
- [ ] Estilo profesional pero accesible
- [ ] Tono hispano-friendly (si aplica)
- [ ] Logo C3 visible (donde aplique)

**FUNCIONALIDAD:**
- [ ] Legible/reconocible al tamaño de uso
- [ ] Funciona con text overlay (si aplica)
- [ ] Mobile-friendly (responsive consideration)
- [ ] Message claro

**COHESIÓN:**
- [ ] Consistente con otros assets del set
- [ ] Matching style (si es parte de serie)
- [ ] Same visual language

---

### **CHECKLIST COMPLETO FINAL:**

**FOTOS EQUIPO:**
- [ ] Carlos fondo transformado (match Luis/María)
- [ ] Cohesión visual equipo completa

**HERO & MOCKUPS:**
- [ ] Luis con tablet (GBP visible)
- [ ] Google mobile search (3 listings claros)
- [ ] GBP desktop dashboard (completo)

**TIMELINE:**
- [ ] Mes 1, 2, 3 (set cohesivo)
- [ ] Números 1, 2, 3 visibles
- [ ] Estilo consistente

**ICONOS:**
- [ ] 6 iconos mismo style
- [ ] Stroke 4px consistent
- [ ] Todos SVG format

**PASOS:**
- [ ] Pasos 1, 2, 3, 4 (set cohesivo)
- [ ] Números prominentes
- [ ] Concepts claros

**EXTRAS:**
- [ ] 3 Badges profesionales
- [ ] Background pattern sutil

**TOTAL: 18 assets visuales ✅**

---

## 💡 TIPS RUNWAY API {#tips}

### **MEJORES PRÁCTICAS:**

**1. ITERACIÓN:**
- Primera generación rara vez es perfecta
- Iterar 2-3 veces por asset crítico
- Ajustar "strength" si necesario (0.6-0.9 range)

**2. CONSISTENCIA:**
- Generar assets relacionados en misma sesión
- Usar mismo "seed" para set cohesivo (si Runway lo soporta)
- Mantener mismo style reference

**3. PROMPTS:**
- Copiar prompts EXACTOS (no parafrasear)
- Negative prompts son críticos (no omitir)
- Si algo falla, añadir más detalles al negative prompt

**4. CALIDAD:**
- Siempre usar "High Quality" setting
- Verificar preview antes de download final
- Re-generar si artifacts visibles

**5. ORGANIZACIÓN:**
- Nombrar archivos lógicamente:
  - `hero-luis-tablet.png`
  - `mockup-google-mobile.png`
  - `timeline-mes-1.svg`
  - `icon-visibilidad.svg`
- Crear carpeta `assets/landing/` con subcarpetas:
  - `/fotos`
  - `/mockups`
  - `/ilustraciones`
  - `/iconos`

**6. BACKUP:**
- Guardar versiones intermedias
- No borrar hasta tener final aprobado
- Mantener prompts usados (para futuras iteraciones)

---

### **TROUBLESHOOTING COMÚN:**

**Problema: Colores incorrectos**
- Solución: Especificar HEX codes en prompt
- Añadir "color accuracy: critical" en technical specs

**Problema: UI elements no auténticos**
- Solución: Especificar "current 2025 design" + "authentic interface"
- Añadir negative: "no outdated UI, no generic mockup"

**Problema: Inconsistencia en sets**
- Solución: Generar todos del set en misma sesión
- Usar reference image del primero para los siguientes

**Problema: Text ilegible en mockups**
- Solución: Especificar "readable text at [size]"
- Aumentar tamaño de texto en prompt
- Re-generar con "high contrast" requirement

**Problema: Subject distorsionado (Carlos transformation)**
- Solución: Bajar strength a 0.65-0.7
- Añadir "preserve subject 100%" multiple veces
- Especificar qué NO cambiar

---

### **OPTIMIZACIÓN POST-GENERACIÓN:**

**Compression:**
1. Usar TinyPNG o similar para comprimir PNGs
2. Target: 60-80% size reduction sin pérdida visual
3. SVGs: usar SVGOMG para limpiar código

**Responsive:**
- Generar @2x versions para Retina displays
- Test en mobile (assets se ven bien small)
- Crop alternativo para mobile si necesario

**Naming convention:**
```
hero-luis-tablet.png
hero-luis-tablet@2x.png
mockup-google-search-mobile.png
mockup-gbp-desktop.png
timeline-mes-1.svg
timeline-mes-2.svg
timeline-mes-3.svg
icon-visibilidad.svg
icon-confianza.svg
... etc
```

---

## 🚀 ENTREGA FINAL A LUIS

### **ESTRUCTURA DE CARPETAS:**

```
/assets-landing-c3/
  /fotos/
    - carlos-fondo-oficina.png
    - hero-luis-tablet.png
    - hero-luis-tablet@2x.png
  /mockups/
    - google-search-mobile.png
    - gbp-desktop.png
  /ilustraciones/
    /timeline/
      - mes-1-fundacion.svg
      - mes-2-magnetizacion.svg
      - mes-3-activacion.svg
    /pasos/
      - paso-1-fundacion.svg
      - paso-2-magnetizacion.svg
      - paso-3-confianza.svg
      - paso-4-activacion.svg
  /iconos/
    - icon-visibilidad.svg
    - icon-confianza.svg
    - icon-control.svg
    - icon-escalabilidad.svg
    - icon-247.svg
    - icon-sin-barreras.svg
  /extras/
    - badges-set.png
    - background-pattern.svg
```

---

### **DOCUMENTACIÓN:**

Crear archivo `ASSETS_README.md` con:
- [ ] Lista de todos los assets generados
- [ ] Dimensiones y formatos
- [ ] Dónde usar cada asset en landing
- [ ] Colores HEX usados
- [ ] Notas especiales (si alguno requiere ajuste)

---

## 📞 CONTACTO Y SOPORTE

**Si algo no funciona o necesitas ajustes:**

**Luis A. Arroyo**
- Email: luis@c3marketinghub.com

**Para preguntas técnicas Runway:**
- Documentación Runway API
- Support Runway si bugs

---

## ✅ CHECKLIST FINAL ANTES DE ENVIAR A LUIS

- [ ] 18 assets generados
- [ ] Todos validados según checklist
- [ ] Organizados en carpetas lógicas
- [ ] Archivos nombrados correctamente
- [ ] Comprimidos/optimizados para web
- [ ] README.md creado
- [ ] Preview thumbnails generados (opcional)
- [ ] ZIP file creado para entrega

---

**TIEMPO TOTAL ESTIMADO: 2-3 horas**

**¡ÉXITO MANU! 🚀**

---

**FIN DEL DOCUMENTO MAESTRO**

*Este documento contiene todos los prompts necesarios para generar los assets visuales de la Landing Page Sistema Imán Local™ de C3 Marketing usando Runway API.*

*Versión 1.0 - Noviembre 2025*
