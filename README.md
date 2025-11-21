<div align="center">
   
# ⚙️ PDF Renamer Security (PDF-RS)   
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Windows](https://img.shields.io/badge/Platform-Windows%2010%2B-success)](https://www.microsoft.com/windows)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)


</div>

## 🌟 Resumen del Proyecto

Pequeña utilidad para automatizar el proceso de **renombrar archivos PDF** utilizando un número de identificador y **protegerlos con contraseña** utilizando su DNI (Documento Nacional de Identidad) o contraseñas.


---

## ✨ Características Principales

* **Renombrado Automático:** Renombra archivos PDF basándose en un número de identificador.
* **Protección con Contraseña:** Protege los PDFs con una contraseña específica (por ejemplo, el DNI del paciente).
* **Uso de Excel:** Utiliza un archivo Excel (`clinicos.xlsx`) como fuente de datos para los identificadores y contraseñas.
* **Flujo de Trabajo Automatizado:** Procesa los archivos desde una carpeta origen y los guarda protegidos en una carpeta destino.
* **Conservación de Archivos Originales:** Los archivos PDF originales no son eliminados durante el proceso.

## 🛠️ Tecnologías Utilizadas

| Tecnología | Propósito |
| :--- | :--- |
| **Python** | Lenguaje de programación principal. |
| **PyPDF2 ** | Módulo de Python para la manipulación general de archivos PDF (lectura, división, fusión, cifrado/descifrado). |
| **PdfReader** | Clase de PyPDF2 utilizada específicamente para leer y acceder al contenido de un archivo PDF existente. |
| **PdfWriter** | Clase de PyPDF2 utilizada específicamente para escribir, crear, o modificar (añadir páginas, cifrar) un nuevo archivo PDF. |

---

## 💡 Información General y Propósito

| Detalle | Descripción |
| :--- | :--- |
| **Creador** | LSCF |
| **Propósito** | Optimizar y asegurar el proceso de renombrado y cifrado de documentos PDF por lotes. |

## 🚀 Instalación y Uso
### Prerrequisitos
- Python 3.8 o superior
- Windows 10/11 (o cualquier sistema compatible con Tkinter)
---


## Instalación y Uso

### 1. Instalación de Dependencias

1.  **Clona el repositorio**
    ```bash
    git clone https://github.com/LSCF84/PDF-Renamer-Security-PDF-RS.git
    cd PDF-Renamer-Security
    ```
2.  **Instala dependencias**
    ```bash
    pip install -r requirements.txt
    ```
  ### 2. Ejecución

1.  Descarga o clona el archivo principal (ej: `renombra_protege_pdf.py`).
2.  Ejecuta el *script* desde tu terminal:

    ```bash
    python renombra_protege_pdf.py
    ```

### 3. Guía de Uso Rápido

1. Coloca el archivo 'clinicos.xlsx' en la carpeta C:\Informes
2. Asegúrate de que los archivos PDF estén en esa misma carpeta. Deben llamarse como el número de paciente (ej: 222.pdf)
3. Ejecuta el archivo 'renombra_protege_pdf.exe'
4. Los nuevos archivos renombrados y protegidos se guardarán en: C:\Informes\Protegidos
Contraseña de cada PDF = el DNI del paciente correspondiente.

IMPORTANTE:
- Los archivos originales NO se borran.
- Si hay errores, aparecerán mensajes en la consola.

---

## 👨‍💻 Autor

**LSCF**

## 🤝 ¿Quieres contribuir?

¡Claro! Abre un Issue o un Pull Request para ayudar a mejorar esta suite. Usa la plantilla al crear un Issue.

---

⭐️ Si te sirvió, ¡dale una estrella al repositorio!
