# ==========================================
# Generador de Códigos QR fácil y rápido
# Tu amigo programador
# ==========================================
# Requisitos:
# pip install qrcode Pillow

import qrcode
from PIL import Image

def generar_qr():
    # 1. Solicitar los datos al usuario
    datos = input("Ingrese la URL o el texto para el QR: ")
    
    # 2. Configurar la estructura del código QR
    qr = qrcode.QRCode(
        version=3,      # Controla el tamaño del QR (1 a 40)(Dependiendo la cantidad de texto)
        box_size=8,     # Tamaño en píxeles de cada cuadro
        border=4        # Grosor del borde blanco
    )
    
    # 3. Añadir la información y procesar
    qr.add_data(datos)
    qr.make(fit=True) # Aumenta la version del Qr automaticamente
    
    # 4. Crear la imagen con colores personalizados
    # Puedes cambiar "Orange" por "White" si prefieres el clásico
    imagen_qr = qr.make_image(fill_color="black", back_color="orange")
    
    # 5. Guardar y mostrar el resultado
    nombre_archivo = "qr_generado.png"
    imagen_qr.save(nombre_archivo)
    imagen_qr.show()
    
    print(f"¡Éxito! Tu código QR se ha guardado como '{nombre_archivo}'")

# Ejecutar la función principal
if __name__ == "__main__":
    generar_qr()

