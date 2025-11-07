#!/usr/bin/env python3
"""
Generar nueva foto hero de Luis en escritorio asesorando
Usando Gemini 2.5 Flash Image (Nano Banana) via Runway API
"""

import requests
import json
import time
import base64
import os

# API Configuration
API_KEY = os.environ.get('RUNWAY_API_KEY', 'key_ba98b6472aac218bf1662def655be2c02d645a5e29bc5618a0794e8090f3e481aac2a42ab483f5937f0cf29a8cc2359d81b81510d3c2c8076a19ef187d3d7fa6')
BASE_URL = "https://api.dev.runwayml.com"

def image_to_data_uri(image_path):
    """Convert image to data URI for Runway API"""
    with open(image_path, 'rb') as f:
        image_data = f.read()
    base64_image = base64.b64encode(image_data).decode('utf-8')
    # Detect image format
    ext = image_path.lower().split('.')[-1]
    mime_type = f'image/{ext}' if ext in ['png', 'jpg', 'jpeg', 'webp'] else 'image/png'
    return f'data:{mime_type};base64,{base64_image}'

def generate_image(prompt, reference_image_path, output_path):
    """Generate image using Gemini 2.5 Flash with reference image"""
    
    print(f"\n🎨 Generando: {output_path}")
    print(f"📝 Prompt: {prompt[:100]}...")
    
    # Convert reference image to data URI
    reference_uri = image_to_data_uri(reference_image_path)
    
    # Prepare request
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "X-Runway-Version": "2024-11-06"
    }
    
    payload = {
        "model": "gemini_2.5_flash",
        "prompt": prompt,
        "referenceImages": [reference_uri],
        "width": 1024,
        "height": 1024
    }
    
    # Make request
    try:
        response = requests.post(
            f"{BASE_URL}/v1/text_to_image",
            headers=headers,
            json=payload,
            timeout=120
        )
        
        if response.status_code == 200:
            result = response.json()
            
            # Get image URL
            if 'url' in result:
                image_url = result['url']
                print(f"✅ Imagen generada: {image_url}")
                
                # Download image
                img_response = requests.get(image_url)
                if img_response.status_code == 200:
                    with open(output_path, 'wb') as f:
                        f.write(img_response.content)
                    print(f"💾 Guardada en: {output_path}")
                    return True
                else:
                    print(f"❌ Error descargando imagen: {img_response.status_code}")
                    return False
            else:
                print(f"❌ No se encontró URL en respuesta: {result}")
                return False
        else:
            print(f"❌ Error en API: {response.status_code}")
            print(f"Respuesta: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Excepción: {str(e)}")
        return False

# Main execution
if __name__ == "__main__":
    print("=" * 60)
    print("🎬 GENERACIÓN DE NUEVA FOTO HERO - LUIS ASESORANDO")
    print("=" * 60)
    
    # Reference image
    reference_image = "/home/ubuntu/c3-marketing-sistema-iman-local/assets/team-photos/luis-arroyo-desk.png"
    
    # Output path
    output_path = "/home/ubuntu/c3-marketing-sistema-iman-local/assets/generated/00_luis_hero_consulting.png"
    
    # Prompt optimizado para Nano Banana
    prompt = """Professional business consultant photo. Hispanic man in coral/salmon colored sweater with 'C!' logo, sitting at modern white desk in bright office. Warm smile, approachable expression. Hands gesturing naturally as if explaining something to a client. On desk: open laptop showing business dashboard, professional notebook, smartphone. Clean minimalist office background with iMac visible. Natural lighting from left side. Professional corporate photography style. Shot with Sony A7III, 50mm f/1.8, shallow depth of field. High resolution, sharp focus on face. Preserve exact facial features, skin tone, and body proportions. Nano-banana strength: 0.50. Photorealistic, professional headshot quality."""
    
    print(f"\n📸 Foto de referencia: {reference_image}")
    print(f"💾 Salida: {output_path}")
    print(f"\n🚀 Iniciando generación con Nano Banana...")
    
    success = generate_image(prompt, reference_image, output_path)
    
    if success:
        print("\n" + "=" * 60)
        print("✅ GENERACIÓN COMPLETADA EXITOSAMENTE")
        print("=" * 60)
        print(f"\n📊 Costo: 5 créditos ($0.05 USD)")
        print(f"📁 Archivo: {output_path}")
    else:
        print("\n" + "=" * 60)
        print("❌ ERROR EN LA GENERACIÓN")
        print("=" * 60)
