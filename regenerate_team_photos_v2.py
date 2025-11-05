#!/usr/bin/env python3
"""
Regenerar fotos del equipo con Gemini 2.5 Flash + Nano Banana
Usando referenceImages correctamente según documentación de Runway API
"""

import os
import sys
import time
import json
import base64
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
    "Content-Type": "application/json",
    "X-Runway-Version": "2024-11-06"
}

def image_to_data_uri(image_path):
    """Convertir imagen a data URI para usar como referencia"""
    print(f"  📤 Convirtiendo imagen a data URI: {image_path}")
    
    # Leer la imagen
    with open(image_path, 'rb') as f:
        image_data = f.read()
    
    # Determinar el tipo MIME
    ext = image_path.suffix.lower()
    mime_types = {
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.webp': 'image/webp'
    }
    mime_type = mime_types.get(ext, 'image/jpeg')
    
    # Convertir a base64
    base64_data = base64.b64encode(image_data).decode('utf-8')
    
    # Crear data URI
    data_uri = f"data:{mime_type};base64,{base64_data}"
    
    size_kb = len(image_data) / 1024
    print(f"  ✅ Data URI creado ({size_kb:.0f} KB)")
    
    return data_uri

def generate_image_with_reference(prompt, reference_image_path, reference_tag, output_filename):
    """Generar imagen con Gemini usando imagen de referencia"""
    print(f"\n🎨 Generando: {output_filename}")
    print(f"   Tag de referencia: @{reference_tag}")
    
    # Convertir imagen a data URI
    data_uri = image_to_data_uri(reference_image_path)
    
    # Payload para la API
    payload = {
        "model": "gemini_2.5_flash",
        "promptText": prompt,
        "ratio": "1920:1080",
        "referenceImages": [
            {
                "uri": data_uri,
                "tag": reference_tag
            }
        ]
    }
    
    print(f"  🚀 Enviando request a Runway API...")
    
    # Hacer request
    response = requests.post(
        f"{BASE_URL}/v1/text_to_image",
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
        print(f"  Response: {json.dumps(result, indent=2)}")
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
            # Obtener URL de la imagen
            output = status_data.get('output')
            if isinstance(output, list) and len(output) > 0:
                image_url = output[0]
            elif isinstance(output, str):
                image_url = output
            else:
                print(f"  ❌ Formato de output inesperado: {output}")
                return False
            
            if image_url:
                # Descargar imagen
                print(f"  📥 Descargando imagen desde: {image_url[:80]}...")
                img_response = requests.get(image_url)
                
                if img_response.status_code == 200:
                    output_path = OUTPUT_DIR / output_filename
                    with open(output_path, 'wb') as f:
                        f.write(img_response.content)
                    
                    file_size = len(img_response.content) / 1024  # KB
                    print(f"  ✅ Guardada: {output_path} ({file_size:.0f} KB)")
                    return True
                else:
                    print(f"  ❌ Error descargando imagen: {img_response.status_code}")
                    return False
            else:
                print(f"  ❌ No se recibió URL de imagen")
                return False
        
        elif status == 'FAILED':
            error = status_data.get('failure')
            print(f"  ❌ Generación falló: {error}")
            return False
    
    print(f"  ❌ Timeout esperando generación")
    return False

def main():
    print("=" * 80)
    print("🎬 REGENERACIÓN DE FOTOS DEL EQUIPO - NANO BANANA V2")
    print("Proyecto: Sistema Imán Local - C3 Marketing")
    print("=" * 80)
    
    if not API_KEY:
        print("❌ Error: RUNWAY_API_KEY no configurada")
        sys.exit(1)
    
    print(f"✅ API Key configurada")
    print(f"✅ Directorio de salida: {OUTPUT_DIR}")
    print(f"✅ Modelo: gemini_2_5_flash con Nano Banana")
    print(f"✅ Método: referenceImages con data URI")
    
    # Crear directorio de salida si no existe
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    print("\n" + "=" * 80)
    print("IMAGEN 1: LUIS CON IPAD MOSTRANDO GBP")
    print("=" * 80)
    
    # Foto de Luis
    luis_photo = TEAM_PHOTOS_DIR / "luis-arroyo.png"
    
    # Prompt para Luis con referencia @luis (< 1000 caracteres)
    luis_prompt = """Using @luis as base: PRESERVE @luis face, body, pose, C3 coral shirt, and office background EXACTLY (100% Nano Banana preservation). ADD ONLY: iPad Pro 12.9" Space Gray held naturally at torso, 45° angle. Right hand grips side, left supports bottom. Screen shows Google Business Profile: "Garcia Landscaping" with 5.0★★★★★ rating, San Luis Obispo CA, professional landscaping photos, stats visible. Natural shadows, seamless integration, 1920x1080 professional quality. DO NOT modify @luis in any way."""
    
    success = generate_image_with_reference(
        prompt=luis_prompt,
        reference_image_path=luis_photo,
        reference_tag="luis",
        output_filename="02_luis_tablet_gbp_CORRECTED.png"
    )
    
    if not success:
        print("❌ Error generando imagen de Luis")
    else:
        print("✅ Imagen de Luis generada exitosamente")
    
    # Esperar un poco entre requests
    print("\n⏳ Esperando 10 segundos antes de la siguiente generación...")
    time.sleep(10)
    
    print("\n" + "=" * 80)
    print("IMAGEN 2: CARLOS - TRANSFORMACIÓN DE FONDO")
    print("=" * 80)
    
    # Foto de Carlos
    carlos_photo = TEAM_PHOTOS_DIR / "carlos-cordero.jpg"
    
    # Prompt para Carlos con referencia @carlos (< 1000 caracteres)
    carlos_prompt = """Using @carlos as base: PRESERVE @carlos face, expression, arms-crossed pose, gray shirt, Facebook lanyard, and watch EXACTLY (100% Nano Banana preservation). CHANGE ONLY BACKGROUND: Replace blue Facebook background with professional office - horizontal aluminum blinds, off-white wall, natural lighting from left, soft focus (f/2.8). Precise edge masking, no blue spill, no halos. Subtle shadow on wall. High resolution, warm professional tone. DO NOT modify @carlos in any way."""
    
    success = generate_image_with_reference(
        prompt=carlos_prompt,
        reference_image_path=carlos_photo,
        reference_tag="carlos",
        output_filename="01_carlos_office_background_CORRECTED.png"
    )
    
    if not success:
        print("❌ Error generando imagen de Carlos")
    else:
        print("✅ Imagen de Carlos generada exitosamente")
    
    print("\n" + "=" * 80)
    print("🎉 REGENERACIÓN COMPLETADA")
    print(f"📁 Imágenes guardadas en: {OUTPUT_DIR}")
    print("=" * 80)
    print("\n💡 Revisa las imágenes *_CORRECTED.png para verificar que:")
    print("   ✓ Luis mantiene su rostro exacto (Nano Banana preservó identidad)")
    print("   ✓ iPad se ve natural en sus manos")
    print("   ✓ Carlos mantiene su rostro y pose exactos")
    print("   ✓ Fondo de Carlos cambió a oficina profesional")
    print("   ✓ Las ediciones se ven naturales y profesionales")
    print("\nSi las imágenes son correctas, reemplaza las originales.")
    print("\nCosto: 2 imágenes × 5 créditos = 10 créditos = $0.10 USD")

if __name__ == "__main__":
    main()
