#!/usr/bin/env python3
"""
Regenerar foto de Carlos con logo C3 bordado en naranja
Usando Gemini 2.5 Flash + Nano Banana para preservar identidad
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
    
    with open(image_path, 'rb') as f:
        image_data = f.read()
    
    ext = image_path.suffix.lower()
    mime_types = {
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.webp': 'image/webp'
    }
    mime_type = mime_types.get(ext, 'image/jpeg')
    
    base64_data = base64.b64encode(image_data).decode('utf-8')
    data_uri = f"data:{mime_type};base64,{base64_data}"
    
    size_kb = len(image_data) / 1024
    print(f"  ✅ Data URI creado ({size_kb:.0f} KB)")
    
    return data_uri

def generate_image_with_reference(prompt, reference_image_path, reference_tag, output_filename):
    """Generar imagen con Gemini usando imagen de referencia"""
    print(f"\n🎨 Generando: {output_filename}")
    print(f"   Tag de referencia: @{reference_tag}")
    
    data_uri = image_to_data_uri(reference_image_path)
    
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
        return False
    
    print(f"  ⏳ Task ID: {task_id}")
    print(f"  ⏳ Esperando generación...")
    
    max_attempts = 60
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
            output = status_data.get('output')
            if isinstance(output, list) and len(output) > 0:
                image_url = output[0]
            elif isinstance(output, str):
                image_url = output
            else:
                print(f"  ❌ Formato de output inesperado: {output}")
                return False
            
            if image_url:
                print(f"  📥 Descargando imagen...")
                img_response = requests.get(image_url)
                
                if img_response.status_code == 200:
                    output_path = OUTPUT_DIR / output_filename
                    with open(output_path, 'wb') as f:
                        f.write(img_response.content)
                    
                    file_size = len(img_response.content) / 1024
                    print(f"  ✅ Guardada: {output_path} ({file_size:.0f} KB)")
                    return True
                else:
                    print(f"  ❌ Error descargando imagen")
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
    print("🎬 REGENERACIÓN DE CARLOS - LOGO C3 BORDADO NARANJA")
    print("Proyecto: Sistema Imán Local - C3 Marketing")
    print("=" * 80)
    
    if not API_KEY:
        print("❌ Error: RUNWAY_API_KEY no configurada")
        sys.exit(1)
    
    print(f"✅ API Key configurada")
    print(f"✅ Directorio de salida: {OUTPUT_DIR}")
    print(f"✅ Modelo: gemini_2.5_flash con Nano Banana")
    
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    print("\n" + "=" * 80)
    print("CARLOS - CAMISA BLANCA + LOGO C3 BORDADO NARANJA")
    print("=" * 80)
    
    carlos_photo = TEAM_PHOTOS_DIR / "carlos-cordero.jpg"
    
    # Prompt optimizado (< 1000 caracteres)
    # Especifica: C3 (letra C y número 3), sin círculo, naranja/dorado, textura bordada
    carlos_prompt = """Using @carlos as base: PRESERVE @carlos face, expression, arms-crossed pose EXACTLY (100% Nano Banana). CHANGE: Replace gray shirt with crisp white button-down shirt. ADD: Embroidered "C3" logo (letter C + number 3, NO circle) on left chest in orange/golden color (#F9B718). Logo style: same size and embroidered texture as reference, professional, subtle. KEEP: Facebook lanyard, watch unchanged. BACKGROUND: Professional office, horizontal aluminum blinds, off-white wall, natural lighting, soft focus. Precise edges, high resolution, warm tone. DO NOT modify @carlos face/pose."""
    
    success = generate_image_with_reference(
        prompt=carlos_prompt,
        reference_image_path=carlos_photo,
        reference_tag="carlos",
        output_filename="01_carlos_white_shirt_c3_orange_FINAL.png"
    )
    
    if success:
        print("\n✅ Imagen de Carlos con logo C3 naranja generada exitosamente")
    else:
        print("\n❌ Error generando imagen de Carlos")
    
    print("\n" + "=" * 80)
    print("🎉 GENERACIÓN COMPLETADA")
    print(f"📁 Imagen guardada en: {OUTPUT_DIR}")
    print("=" * 80)
    print("\n💡 Revisa la imagen para verificar que:")
    print("   ✓ Carlos mantiene su rostro y pose exactos")
    print("   ✓ Camisa blanca profesional")
    print("   ✓ Logo 'C3' bordado (sin círculo) en pecho izquierdo")
    print("   ✓ Color naranja/dorado (#F9B718)")
    print("   ✓ Textura bordada similar a la de Luis")
    print("   ✓ Tamaño profesional y sutil")
    print("   ✓ Lanyard y reloj preservados")
    print("   ✓ Fondo oficina profesional")
    print("\nCosto: 1 imagen × 5 créditos = 5 créditos = $0.05 USD")
    print("Balance restante: ~60 créditos ($0.60 USD)")

if __name__ == "__main__":
    main()
