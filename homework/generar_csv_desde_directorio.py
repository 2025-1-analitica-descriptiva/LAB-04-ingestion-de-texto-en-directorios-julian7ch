import os
import csv

def generar_csv_desde_directorio(input_dir, output_path):
    if os.path.exists(output_path):
        print(f"El archivo '{output_path}' ya existe. No se volverá a generar.")
        return

    rows = []

    for sentimiento in ['positive', 'negative', 'neutral']:
        carpeta_sentimiento = os.path.join(input_dir, sentimiento)
        for nombre_archivo in os.listdir(carpeta_sentimiento):
            ruta_archivo = os.path.join(carpeta_sentimiento, nombre_archivo)
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                frase = archivo.read().strip()
                rows.append({'phrase': frase, 'target': sentimiento})

    # Asegura q la carpeta 'files/output' exista
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Escribe el archivo CSV
    with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['phrase', 'target'])
        writer.writeheader()
        writer.writerows(rows)

    print(f"Archivo generado correctamente: {output_path}")
