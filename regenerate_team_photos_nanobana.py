#!/usr/bin/env python3
"""
Regenerar fotos del equipo con Gemini 2.5 Flash + Nano Banana
Usando prompts profesionales para preservar identidad
"""

import os
import sys
import time
import json
import requests
from pathlib import Path

# Configuración
API_KEY = os.environ.get('RUNWAY_API_KEY')
BASE_URL = "https://api.dev.runwayml.com"
OUTPUT_DIR = Path("/home/ubuntu/c3-marketing-sistema-iman-local/assets/generated")
TEAM_PHOTOS_DIR = Path("/home/ubuntu/c3-marketing-sistema-iman-local/assets/team-photos")

# Headers para la API
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def upload_image_to_runway(image_path):
    """Subir imagen de referencia a Runway"""
    print(f"  📤 Subiendo imagen de referencia: {image_path}")
    
    # Leer la imagen
    with open(image_path, 'rb') as f:
        image_data = f.read()
    
    # Subir a Runway
    upload_url = f"{BASE_URL}/v1/uploads"
    files = {
        'file': (os.path.basename(image_path), image_data)
    }
    
    response = requests.post(
        upload_url,
        headers={"Authorization": f"Bearer {API_KEY}"},
        files=files
    )
    
    if response.status_code == 200:
        result = response.json()
        cdn_url = result.get('url')
        print(f"  ✅ Imagen subida: {cdn_url}")
        return cdn_url
    else:
        print(f"  ❌ Error subiendo imagen: {response.status_code}")
        print(f"     {response.text}")
        return None

def generate_image_with_reference(prompt, reference_image_url, output_filename, strength=0.5):
    """Generar imagen con Gemini usando imagen de referencia"""
    print(f"\n🎨 Generando: {output_filename}")
    print(f"   Strength: {strength}")
    
    # Payload para la API
    payload = {
        "model": "gemini_2_5_flash",
        "prompt": prompt,
        "width": 1920,
        "height": 1080,
        "image": reference_image_url,
        "strength": strength
    }
    
    print(f"  🚀 Enviando request a Runway API...")
    
    # Hacer request
    response = requests.post(
        f"{BASE_URL}/v1/image_to_image",
        headers=headers,
        json=payload
    )
    
    if response.status_code != 200:
        print(f"  ❌ Error {response.status_code}: {response.text}")
        return False
    
    result = response.json()
    task_id = result.get('id')
    
    if not task_id:
        print(f"  ❌ No se recibió task_id")
        return False
    
    print(f"  ⏳ Task ID: {task_id}")
    print(f"  ⏳ Esperando generación...")
    
    # Polling para obtener resultado
    max_attempts = 60  # 5 minutos máximo
    attempt = 0
    
    while attempt < max_attempts:
        time.sleep(5)
        attempt += 1
        
        status_response = requests.get(
            f"{BASE_URL}/v1/tasks/{task_id}",
            headers=headers
        )
        
        if status_response.status_code != 200:
            print(f"  ❌ Error obteniendo status: {status_response.status_code}")
            continue
        
        status_data = status_response.json()
        status = status_data.get('status')
        
        print(f"  ⏳ Status: {status} (intento {attempt}/{max_attempts})")
        
        if status == 'SUCCEEDED':
            image_url = status_data.get('output', [None])[0]
            if image_url:
                # Descargar imagen
                print(f"  📥 Descargando imagen...")
                img_response = requests.get(image_url)
                
                if img_response.status_code == 200:
                    output_path = OUTPUT_DIR / output_filename
                    with open(output_path, 'wb') as f:
                        f.write(img_response.content)
                    
                    file_size = len(img_response.content) / 1024  # KB
                    print(f"  ✅ Guardada: {output_path} ({file_size:.0f} KB)")
                    return True
                else:
                    print(f"  ❌ Error descargando imagen")
                    return False
            else:
                print(f"  ❌ No se recibió URL de imagen")
                return False
        
        elif status == 'FAILED':
            error = status_data.get('error', 'Unknown error')
            print(f"  ❌ Generación falló: {error}")
            return False
    
    print(f"  ❌ Timeout esperando generación")
    return False

def main():
    print("=" * 80)
    print("🎬 REGENERACIÓN DE FOTOS DEL EQUIPO - NANO BANANA")
    print("Proyecto: Sistema Imán Local - C3 Marketing")
    print("=" * 80)
    
    if not API_KEY:
        print("❌ Error: RUNWAY_API_KEY no configurada")
        sys.exit(1)
    
    print(f"✅ API Key configurada")
    print(f"✅ Directorio de salida: {OUTPUT_DIR}")
    print(f"✅ Modelo: gemini_2_5_flash con Nano Banana")
    
    # Crear directorio de salida si no existe
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    print("\n" + "=" * 80)
    print("IMAGEN 1: LUIS CON IPAD MOSTRANDO GBP")
    print("=" * 80)
    
    # Subir foto de Luis
    luis_photo = TEAM_PHOTOS_DIR / "luis-arroyo.png"
    luis_url = upload_image_to_runway(luis_photo)
    
    if not luis_url:
        print("❌ Error subiendo foto de Luis")
        sys.exit(1)
    
    # Prompt para Luis (versión condensada del prompt profesional)
    luis_prompt = """Professional photo editing: Add iPad Pro to Luis's hands showing Google Business Profile.

CRITICAL PRESERVATION (100%):
- Luis's face: EXACT preservation, no changes to facial features, expression, or skin tone
- Body & pose: Maintain exact stance and position
- Clothing: C3 coral shirt (#EF4125) with logo - preserve completely
- Background: Office with horizontal blinds - preserve exactly
- Lighting: Natural office lighting - maintain

ADDITIVE ELEMENTS:
- iPad Pro 12.9" Space Gray in landscape orientation
- Held naturally at torso level, 45° angle toward camera
- Right hand primary grip, left hand support
- Screen shows Google Business Profile dashboard:
  * Business: "Garcia Landscaping"
  * Rating: 5.0 stars (★★★★★) prominently displayed
  * Location: San Luis Obispo, CA
  * Professional landscaping photos in grid
  * Stats: views, clicks, calls visible
  * Clean, professional UI

INTEGRATION:
- Natural shadows from iPad on shirt and hands
- iPad receives same office lighting
- Realistic perspective and proportions
- Seamless integration (not composited look)

OUTPUT: 1920x1080, professional photography quality, hero image for landing page"""
    
    success = generate_image_with_reference(
        prompt=luis_prompt,
        reference_image_url=luis_url,
        output_filename="02_luis_tablet_gbp_CORRECTED.png",
        strength=0.50  # Balance entre preservación y edición
    )
    
    if not success:
        print("❌ Error generando imagen de Luis")
    
    print("\n" + "=" * 80)
    print("IMAGEN 2: CARLOS - TRANSFORMACIÓN DE FONDO")
    print("=" * 80)
    
    # Subir foto de Carlos
    carlos_photo = TEAM_PHOTOS_DIR / "carlos-cordero.jpg"
    carlos_url = upload_image_to_runway(carlos_photo)
    
    if not carlos_url:
        print("❌ Error subiendo foto de Carlos")
        sys.exit(1)
    
    # Prompt para Carlos (versión condensada)
    carlos_prompt = """Professional photo editing: Replace background only, preserve subject completely.

ABSOLUTE PRESERVATION (100%):
- Carlos's face: PIXEL-PERFECT preservation, no reconstruction
- Expression: Confident, slight smile - exact preservation
- Pose: Arms crossed - maintain exactly
- Clothing: Gray shirt, Facebook lanyard, watch - preserve completely
- Body proportions: Exact as photographed

BACKGROUND REPLACEMENT:
Replace blue Facebook background with:
- Professional office environment
- Horizontal aluminum window blinds (like Luis's photo)
- Off-white/beige wall
- Natural office lighting from left
- Soft, slightly out of focus (f/2.8 depth of field)
- Matches Luis's office style for team photo cohesion

INTEGRATION:
- Precise edge masking around Carlos
- Natural shadow behind Carlos on wall
- No blue color spill on edges
- No halos or artifacts
- Carlos fits naturally in new environment
- Same lighting direction as new background

OUTPUT: High resolution, professional team photo, matches Luis's photo style"""
    
    success = generate_image_with_reference(
        prompt=carlos_prompt,
        reference_image_url=carlos_url,
        output_filename="01_carlos_office_background_CORRECTED.png",
        strength=0.65  # Más fuerza para cambiar fondo, pero Nano Banana protege a Carlos
    )
    
    if not success:
        print("❌ Error generando imagen de Carlos")
    
    print("\n" + "=" * 80)
    print("🎉 REGENERACIÓN COMPLETADA")
    print(f"📁 Imágenes guardadas en: {OUTPUT_DIR}")
    print("=" * 80)
    print("\n💡 Revisa las imágenes CORRECTED para verificar que:")
    print("   ✓ Luis mantiene su rostro exacto")
    print("   ✓ Carlos mantiene su rostro y pose exactos")
    print("   ✓ Las ediciones se ven naturales")
    print("\nSi las imágenes son correctas, reemplaza las originales.")

if __name__ == "__main__":
    main()
