
import os
import pandas as pd
from PyPDF2 import PdfReader, PdfWriter

# Rutas
base_dir = "C:/Informes"
excel_path = os.path.join(base_dir, "clinicos.xlsx")
output_dir = os.path.join(base_dir, "Protegidos")

# Crear carpeta de salida si no existe
os.makedirs(output_dir, exist_ok=True)

# Leer Excel
df = pd.read_excel(excel_path)
df.columns = [col.strip() for col in df.columns]  # Limpiar espacios

# Crear un diccionario para mapear número de paciente a (nombre, dni)
paciente_map = {
    str(row["Nº de paciente"]): (str(row["Nombre"]), str(row["DNI"]))
    for _, row in df.iterrows()
}

# Procesar PDFs
for filename in os.listdir(base_dir):
    if filename.lower().endswith(".pdf"):
        numero = filename.split(".")[0]
        if numero in paciente_map:
            nombre, dni = paciente_map[numero]
            input_path = os.path.join(base_dir, filename)
            output_filename = f"{nombre}.pdf"
            output_path = os.path.join(output_dir, output_filename)

            try:
                reader = PdfReader(input_path)
                writer = PdfWriter()

                for page in reader.pages:
                    writer.add_page(page)

                writer.encrypt(dni)
                with open(output_path, "wb") as f_out:
                    writer.write(f_out)

                print(f"Procesado: {filename} -> {output_filename} (clave: {dni})")
            except Exception as e:
                print(f"Error al procesar {filename}: {e}")
