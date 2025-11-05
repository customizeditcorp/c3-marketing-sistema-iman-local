#!/usr/bin/env python3
"""
Script para generar imágenes con Runway API usando Gemini 2.5 Flash Image
Proyecto: Sistema Imán Local - C3 Marketing
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

def upload_image_to_runway(image_path):
    """Subir imagen de referencia a Runway y obtener URI"""
    print(f"  📤 Subiendo imagen de referencia: {image_path}")
    
    # Usar el comando manus-upload-file para subir a S3
    result = os.popen(f'manus-upload-file "{image_path}"').read().strip()
    
    if result and result.startswith('http'):
        print(f"  ✅ Imagen subida: {result}")
        return result
    else:
        print(f"  ❌ Error subiendo imagen: {result}")
        return None

def generate_image_with_gemini(prompt, output_filename, ratio="1920:1080", reference_image_path=None):
    """
    Generar imagen con Gemini 2.5 Flash Image via Runway API
    
    Args:
        prompt: Texto descriptivo para generar la imagen
        output_filename: Nombre del archivo de salida (sin extensión)
        ratio: Aspect ratio (default: 1920:1080)
        reference_image_path: Path a imagen de referencia (opcional)
    """
    print(f"\n🎨 Generando: {output_filename}")
    print(f"   Ratio: {ratio}")
    
    # Preparar payload
    payload = {
        "model": "gemini_2.5_flash",
        "promptText": prompt,
        "ratio": ratio
    }
    
    # Agregar imagen de referencia si existe
    if reference_image_path and os.path.exists(reference_image_path):
        reference_uri = upload_image_to_runway(reference_image_path)
        if reference_uri:
            payload["referenceImages"] = [
                {
                    "uri": reference_uri,
                    "tag": "ReferencePhoto"
                }
            ]
    
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
# FASE 1: FOTOS DEL EQUIPO
# ============================================================================

def generate_phase_1():
    """Generar fotos del equipo (Carlos y Luis)"""
    print("\n" + "="*80)
    print("FASE 1: FOTOS DEL EQUIPO (2 imágenes)")
    print("="*80)
    
    # Imagen 1: Carlos - Fondo transformado
    carlos_prompt = """Professional corporate headshot photo. Hispanic male professional in coral/salmon colored polo shirt with small 'C3' logo on chest. Modern office background with white desk, iMac computer, and clean professional setting. Natural lighting, soft shadows. High quality corporate photography. The person should maintain their exact facial features, expression, and pose. Only the background should be changed to a modern office environment. Professional business atmosphere. 1920x1080 landscape format."""
    
    generate_image_with_gemini(
        prompt=carlos_prompt,
        output_filename="01_carlos_office_background",
        ratio="1920:1080",
        reference_image_path="/home/ubuntu/c3-marketing-sistema-iman-local/assets/team-photos/carlos-cordero.jpg"
    )
    
    # Imagen 2: Luis - Con tablet mostrando GBP
    luis_prompt = """Professional corporate photo. Hispanic male professional in coral/salmon colored long-sleeve polo shirt with 'C3' logo. He is holding a modern tablet (iPad style) in his hands, displaying a Google Business Profile dashboard on the screen. The tablet screen shows a professional landscaping business profile with 5 gold stars, business photos, and the Google Maps interface. Modern office background with white blinds. Natural professional lighting. High quality corporate photography. The person maintains a confident, professional expression. 1920x1080 landscape format."""
    
    generate_image_with_gemini(
        prompt=luis_prompt,
        output_filename="02_luis_tablet_gbp",
        ratio="1920:1080",
        reference_image_path="/home/ubuntu/c3-marketing-sistema-iman-local/assets/team-photos/luis-arroyo.png"
    )
    
    print("\n✅ FASE 1 COMPLETADA")

# ============================================================================
# FASE 2: MOCKUPS UI
# ============================================================================

def generate_phase_2():
    """Generar mockups de interfaces Google"""
    print("\n" + "="*80)
    print("FASE 2: MOCKUPS UI (2 imágenes)")
    print("="*80)
    
    # Imagen 3: Google Mobile Search
    mobile_prompt = """Modern smartphone mockup showing Google search results. Mobile screen displays search query 'landscaping near me' with local business results. Show 3 business listings with star ratings, business names, and 'Google Business Profile' badges. Clean Google interface with map at top showing location pins. Professional UI design. Vertical mobile format 1080x1920. Realistic Google search interface with local pack results."""
    
    generate_image_with_gemini(
        prompt=mobile_prompt,
        output_filename="03_google_mobile_search",
        ratio="1080:1920"
    )
    
    # Imagen 4: GBP Desktop Dashboard
    desktop_prompt = """Desktop computer mockup showing complete Google Business Profile dashboard. Large monitor display with full GBP interface. Show business name 'Martinez Landscaping', 5 gold stars rating (4.9), professional landscaping photos, business hours, location on Google Maps, customer reviews section, and performance metrics. Clean professional interface. Landscape format 1920x1080. Realistic Google Business Profile admin view."""
    
    generate_image_with_gemini(
        prompt=desktop_prompt,
        output_filename="04_gbp_desktop_dashboard",
        ratio="1920:1080"
    )
    
    print("\n✅ FASE 2 COMPLETADA")

# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*80)
    print("🎬 GENERACIÓN DE IMÁGENES - RUNWAY API + GEMINI 2.5 FLASH")
    print("Proyecto: Sistema Imán Local - C3 Marketing")
    print("="*80)
    
    # Generar Fase 1 (Fotos del equipo)
    generate_phase_1()
    
    # Generar Fase 2 (Mockups UI)
    generate_phase_2()
    
    print("\n" + "="*80)
    print("🎉 GENERACIÓN COMPLETADA")
    print(f"📁 Imágenes guardadas en: {OUTPUT_DIR}")
    print("="*80)
