#!/usr/bin/env python3
"""
Generar nueva foto hero de Luis en escritorio asesorando
Usando Gemini 2.5 Flash Image (Nano Banana) via Runway API
VERSIÓN CORREGIDA con formato correcto de API
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
    
    # Formato correcto según documentación
    payload = {
        "model": "gemini_2.5_flash",
        "promptText": prompt,  # Cambio: prompt → promptText
        "ratio": "1024:1024",   # Cambio: width/height → ratio
        "referenceImages": [    # Cambio: array de objetos, no strings
            {
                "uri": reference_uri,
                "tag": "luis_original"
            }
        ]
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
            
            # Get task ID
            if 'id' in result:
                task_id = result['id']
                print(f"✅ Tarea creada: {task_id}")
                
                # Wait for completion
                print("⏳ Esperando generación...")
                time.sleep(10)  # Wait initial time
                
                # Check task status
                for i in range(30):  # Max 5 minutes
                    status_response = requests.get(
                        f"{BASE_URL}/v1/tasks/{task_id}",
                        headers=headers
                    )
                    
                    if status_response.status_code == 200:
                        status_data = status_response.json()
                        
                        if status_data.get('status') == 'SUCCEEDED':
                            # Get image URL
                            if 'output' in status_data and isinstance(status_data['output'], list) and len(status_data['output']) > 0:
                                image_url = status_data['output'][0]
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
                                print(f"❌ No se encontró output en respuesta: {status_data}")
                                return False
                        elif status_data.get('status') == 'FAILED':
                            print(f"❌ Generación falló: {status_data.get('failure')}")
                            return False
                        else:
                            print(f"⏳ Estado: {status_data.get('status')} ({i+1}/30)")
                            time.sleep(10)
                    else:
                        print(f"❌ Error consultando estado: {status_response.status_code}")
                        time.sleep(10)
                
                print("❌ Timeout esperando generación")
                return False
            else:
                print(f"❌ No se encontró ID en respuesta: {result}")
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
    
    # Prompt optimizado para Nano Banana (menos de 1000 caracteres)
    prompt = """Professional business consultant at desk. Hispanic man in coral sweater with C! logo, warm smile. Hands gesturing naturally while explaining. Laptop showing dashboard, notebook, phone on white desk. Modern office, iMac background. Natural lighting. Professional corporate photography, Sony A7III 50mm f/1.8. Preserve exact facial features @luis_original"""
    
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
