<div align="center">
   
# Version REPDFSEC (Renamer_PDF_Security)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Windows](https://img.shields.io/badge/Platform-Windows%2010%2B-success)](https://www.microsoft.com/windows)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5%2B-orange)](https://openai.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)


</div>

##  Resumen del Proyecto

Renombra y Protege PDFs 

Pequeña utilidad para automatizar el proceso de **renombrar archivos PDF** utilizando un número de identificador y **protegerlos con contraseña** utilizando su DNI (Documento Nacional de Identidad) o contraseñas.


INSTRUCCIONES - Renombrar y proteger PDFs con datos de pacientes

1. Coloca el archivo 'clinicos.xlsx' en la carpeta C:\Informes
2. Asegúrate de que los archivos PDF estén en esa misma carpeta. Deben llamarse como el número de paciente (ej: 222.pdf)
3. Ejecuta el archivo 'renombra_protege_pdf.exe'
4. Los nuevos archivos renombrados y protegidos se guardarán en: C:\Informes\Protegidos

Contraseña de cada PDF = el DNI del paciente correspondiente.

IMPORTANTE:
- Los archivos originales NO se borran.
- Si hay errores, aparecerán mensajes en la consola.
Esta en modificacion, ya que la primera version estaba diseñada para pacientes.
