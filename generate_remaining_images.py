#!/usr/bin/env python3
"""
Script para generar las 10 imágenes restantes con Runway API usando Gemini 2.5 Flash Image
Proyecto: Sistema Imán Local - C3 Marketing
Fase 3, 4 y 5
"""

import os
import requests
import time
import json
from pathlib import Path

# Configuración
RUNWAY_API_KEY = os.environ.get('RUNWAY_API_KEY')
RUNWAY_API_URL = "https://api.dev.runwayml.com/v1/text_to_image"
OUTPUT_DIR = Path("/home/ubuntu/c3-marketing-sistema-iman-local/assets/generated")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Verificar API Key
if not RUNWAY_API_KEY:
    raise ValueError("RUNWAY_API_KEY no está configurada en las variables de entorno")

print(f"✅ API Key configurada")
print(f"✅ Directorio de salida: {OUTPUT_DIR}")
print(f"✅ Modelo: gemini_2.5_flash")
print()

def generate_image_with_gemini(prompt, output_filename, ratio="1920:1080"):
    """
    Generar imagen con Gemini 2.5 Flash Image via Runway API
    """
    print(f"\n🎨 Generando: {output_filename}")
    print(f"   Ratio: {ratio}")
    
    # Preparar payload
    payload = {
        "model": "gemini_2.5_flash",
        "promptText": prompt,
        "ratio": ratio
    }
    
    # Headers
    headers = {
        "Authorization": f"Bearer {RUNWAY_API_KEY}",
        "Content-Type": "application/json",
        "X-Runway-Version": "2024-11-06"
    }
    
    try:
        # Hacer request
        print(f"  🚀 Enviando request a Runway API...")
        response = requests.post(RUNWAY_API_URL, json=payload, headers=headers)
        
        if response.status_code != 200:
            print(f"  ❌ Error {response.status_code}: {response.text}")
            return None
        
        result = response.json()
        task_id = result.get('id')
        
        if not task_id:
            print(f"  ❌ No se recibió task_id: {result}")
            return None
        
        print(f"  ⏳ Task ID: {task_id}")
        print(f"  ⏳ Esperando generación...")
        
        # Polling para obtener resultado
        status_url = f"https://api.dev.runwayml.com/v1/tasks/{task_id}"
        max_attempts = 60  # 5 minutos máximo
        attempt = 0
        
        while attempt < max_attempts:
            time.sleep(5)  # Esperar 5 segundos entre intentos
            attempt += 1
            
            status_response = requests.get(status_url, headers=headers)
            
            if status_response.status_code != 200:
                print(f"  ❌ Error obteniendo status: {status_response.text}")
                return None
            
            status_data = status_response.json()
            status = status_data.get('status')
            
            if status == 'SUCCEEDED':
                # Obtener URL de la imagen generada
                output_url = status_data.get('output', [None])[0]
                
                if not output_url:
                    print(f"  ❌ No se recibió URL de imagen: {status_data}")
                    return None
                
                print(f"  ✅ Imagen generada!")
                print(f"  📥 Descargando...")
                
                # Descargar imagen
                image_response = requests.get(output_url)
                
                if image_response.status_code != 200:
                    print(f"  ❌ Error descargando imagen")
                    return None
                
                # Guardar imagen
                output_path = OUTPUT_DIR / f"{output_filename}.png"
                with open(output_path, 'wb') as f:
                    f.write(image_response.content)
                
                print(f"  💾 Guardada: {output_path}")
                print(f"  ✅ Completado!")
                
                return str(output_path)
            
            elif status == 'FAILED':
                error = status_data.get('failure')
                print(f"  ❌ Generación falló: {error}")
                return None
            
            else:
                # PENDING o RUNNING
                progress = status_data.get('progress', 0)
                print(f"  ⏳ Progreso: {progress}% (intento {attempt}/{max_attempts})")
        
        print(f"  ❌ Timeout: La generación tomó más de 5 minutos")
        return None
        
    except Exception as e:
        print(f"  ❌ Error: {str(e)}")
        return None

# ============================================================================
# FASE 3: TIMELINE 90 DÍAS (3 imágenes)
# ============================================================================

def generate_phase_3():
    """Generar ilustraciones de timeline de 90 días"""
    print("\n" + "="*80)
    print("FASE 3: TIMELINE 90 DÍAS (3 imágenes)")
    print("="*80)
    
    # Imagen 5: Mes 1 - Fundación Digital
    mes1_prompt = """Modern infographic illustration for digital foundation phase. Large bold number "30" in coral red (#EF4125) at the top. Title "FUNDACIÓN DIGITAL" in bold sans-serif font. Clean white background with subtle geometric patterns. Icon showing a computer screen with Google Business Profile logo. Checklist items: "Perfil GBP optimizado", "Categorías estratégicas", "NAP consistente", "Fotos profesionales". Professional business illustration style. Minimalist and clean design. 1920x1080 landscape format."""
    
    generate_image_with_gemini(
        prompt=mes1_prompt,
        output_filename="05_timeline_mes1_fundacion",
        ratio="1920:1080"
    )
    
    # Imagen 6: Mes 2 - Optimización
    mes2_prompt = """Modern infographic illustration for optimization phase. Large bold number "60" in golden yellow (#F9B718) at the top. Title "OPTIMIZACIÓN LOCAL" in bold sans-serif font. Clean white background with subtle geometric patterns. Icon showing a magnifying glass over a map with location pins. Checklist items: "Keywords locales", "Posts semanales", "Reviews activas", "Q&A optimizado". Professional business illustration style. Minimalist and clean design. 1920x1080 landscape format."""
    
    generate_image_with_gemini(
        prompt=mes2_prompt,
        output_filename="06_timeline_mes2_optimizacion",
        ratio="1920:1080"
    )
    
    # Imagen 7: Mes 3 - Activación
    mes3_prompt = """Modern infographic illustration for activation phase. Large bold number "90" in dark gray (#58595B) at the top. Title "ACTIVACIÓN 24/7" in bold sans-serif font. Clean white background with subtle geometric patterns. Icon showing a smartphone with notification bell and stars. Checklist items: "Tráfico constante", "Leads calificados", "Reputación sólida", "ROI medible". Professional business illustration style. Minimalist and clean design. 1920x1080 landscape format."""
    
    generate_image_with_gemini(
        prompt=mes3_prompt,
        output_filename="07_timeline_mes3_activacion",
        ratio="1920:1080"
    )
    
    print("\n✅ FASE 3 COMPLETADA")

# ============================================================================
# FASE 4: 4 PASOS DEL SISTEMA (4 imágenes)
# ============================================================================

def generate_phase_4():
    """Generar ilustraciones de los 4 pasos del sistema"""
    print("\n" + "="*80)
    print("FASE 4: 4 PASOS DEL SISTEMA (4 imágenes)")
    print("="*80)
    
    # Imagen 8: Paso 1 - Fundación Digital
    paso1_prompt = """Modern illustration showing digital foundation concept. Large number "1" in coral red (#EF4125) circle badge. Central icon: laptop computer with Google Business Profile dashboard on screen. Surrounding elements: checkmarks, location pin, star ratings, professional photos icons. Title "FUNDACIÓN DIGITAL" at bottom. Clean professional style with coral red, golden yellow, and dark gray colors. White background. Isometric or flat design style. 1920x1080 landscape format."""
    
    generate_image_with_gemini(
        prompt=paso1_prompt,
        output_filename="08_paso1_fundacion_digital",
        ratio="1920:1080"
    )
    
    # Imagen 9: Paso 2 - Magnetización Local
    paso2_prompt = """Modern illustration showing local magnetization concept. Large number "2" in golden yellow (#F9B718) circle badge. Central icon: magnet attracting customer icons from a map. Surrounding elements: search keywords, location pins, mobile phones, Google Maps interface. Title "MAGNETIZACIÓN LOCAL" at bottom. Clean professional style with coral red, golden yellow, and dark gray colors. White background. Isometric or flat design style. 1920x1080 landscape format."""
    
    generate_image_with_gemini(
        prompt=paso2_prompt,
        output_filename="09_paso2_magnetizacion_local",
        ratio="1920:1080"
    )
    
    # Imagen 10: Paso 3 - Confianza Visual
    paso3_prompt = """Modern illustration showing visual trust concept. Large number "3" in dark gray (#58595B) circle badge. Central icon: shield with 5 gold stars and verified checkmark. Surrounding elements: customer review bubbles, professional photos, before/after images, testimonial quotes. Title "CONFIANZA VISUAL" at bottom. Clean professional style with coral red, golden yellow, and dark gray colors. White background. Isometric or flat design style. 1920x1080 landscape format."""
    
    generate_image_with_gemini(
        prompt=paso3_prompt,
        output_filename="10_paso3_confianza_visual",
        ratio="1920:1080"
    )
    
    # Imagen 11: Paso 4 - Activación 24/7
    paso4_prompt = """Modern illustration showing 24/7 activation concept. Large number "4" in coral red (#EF4125) circle badge. Central icon: smartphone with notification bell ringing, showing incoming leads and calls. Surrounding elements: clock showing 24/7, phone calls, email messages, lead forms, analytics dashboard. Title "ACTIVACIÓN 24/7" at bottom. Clean professional style with coral red, golden yellow, and dark gray colors. White background. Isometric or flat design style. 1920x1080 landscape format."""
    
    generate_image_with_gemini(
        prompt=paso4_prompt,
        output_filename="11_paso4_activacion_247",
        ratio="1920:1080"
    )
    
    print("\n✅ FASE 4 COMPLETADA")

# ============================================================================
# FASE 5: BADGES Y ASSETS (3 imágenes)
# ============================================================================

def generate_phase_5():
    """Generar badges y assets visuales"""
    print("\n" + "="*80)
    print("FASE 5: BADGES Y ASSETS (3 imágenes)")
    print("="*80)
    
    # Imagen 12: Badge "100% Tuyo"
    badge1_prompt = """Professional badge design. Circular badge with coral red (#EF4125) background. White text "100% TUYO" in bold sans-serif font. Small icon of a key or ownership symbol. Clean modern design. Slight shadow or 3D effect. Transparent or white background. High quality vector-style illustration. 1024x1024 square format."""
    
    generate_image_with_gemini(
        prompt=badge1_prompt,
        output_filename="12_badge_100_tuyo",
        ratio="1024:1024"
    )
    
    # Imagen 13: Badge "90 Días"
    badge2_prompt = """Professional badge design. Circular badge with golden yellow (#F9B718) background. White text "90 DÍAS" in bold sans-serif font. Small icon of a calendar or clock symbol. Clean modern design. Slight shadow or 3D effect. Transparent or white background. High quality vector-style illustration. 1024x1024 square format."""
    
    generate_image_with_gemini(
        prompt=badge2_prompt,
        output_filename="13_badge_90_dias",
        ratio="1024:1024"
    )
    
    # Imagen 14: Badge "Sin Ataduras"
    badge3_prompt = """Professional badge design. Circular badge with dark gray (#58595B) background. White text "SIN ATADURAS" in bold sans-serif font. Small icon of broken chains or freedom symbol. Clean modern design. Slight shadow or 3D effect. Transparent or white background. High quality vector-style illustration. 1024x1024 square format."""
    
    generate_image_with_gemini(
        prompt=badge3_prompt,
        output_filename="14_badge_sin_ataduras",
        ratio="1024:1024"
    )
    
    print("\n✅ FASE 5 COMPLETADA")

# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*80)
    print("🎬 GENERACIÓN DE IMÁGENES RESTANTES - RUNWAY API + GEMINI 2.5 FLASH")
    print("Proyecto: Sistema Imán Local - C3 Marketing")
    print("Imágenes 5-14 (10 imágenes)")
    print("="*80)
    
    # Generar Fase 3 (Timeline)
    generate_phase_3()
    
    # Generar Fase 4 (4 Pasos)
    generate_phase_4()
    
    # Generar Fase 5 (Badges)
    generate_phase_5()
    
    print("\n" + "="*80)
    print("🎉 GENERACIÓN COMPLETADA")
    print(f"📁 Imágenes guardadas en: {OUTPUT_DIR}")
    print("\n📊 RESUMEN TOTAL:")
    print("   - Fase 1-2: 4 imágenes (Carlos, Luis, Mockups)")
    print("   - Fase 3: 3 imágenes (Timeline 90 días)")
    print("   - Fase 4: 4 imágenes (4 Pasos del Sistema)")
    print("   - Fase 5: 3 imágenes (Badges)")
    print("   - TOTAL: 14 imágenes generadas")
    print("\n💰 COSTO TOTAL: ~$0.70 USD (70 créditos)")
    print("="*80)
