# Aplicación de Cifrado y Descifrado en Python

Este proyecto consiste en una aplicación de escritorio creada con **Python** y **PyQt5** que permite cifrar y descifrar números de 6 dígitos, de manera sencilla y con una interfaz gráfica amigable.

## Funcionalidades

- **Ventana Principal**: Muestra la información del autor y permite navegar a las otras ventanas.
- **Ventana de Cifrado**: El usuario ingresa un número de 6 dígitos, el cual se cifra aplicando un algoritmo de transformación.
- **Ventana de Descifrado**: Permite ingresar un número cifrado y recuperar el número original.
- **Validaciones**: Se verifican los datos de entrada (número de 6 dígitos, no vacío) y se muestran mensajes claros en caso de error.
- **Mensajes de Estado**: El icono de la aplicación aparece en la bandeja del sistema, indicando que la aplicación está en ejecución. Además, se muestra un mensaje al realizar cada operación.

## Tecnologías utilizadas

- **Python**: Lenguaje de programación utilizado para el desarrollo de la aplicación.
- **PyQt5**: Biblioteca de Python para crear interfaces gráficas.
- **Git**: Para el control de versiones del código fuente.

## Instalación

1. Clona el repositorio en tu máquina local:
   ```bash
   git clone https://github.com/EfraMonR/encryption-application

2. Asegúrate de tener **Python 3** instalado en tu máquina.

3. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt

4. Ejecuta la aplicación:
   ```bash
   python .\app\main.py

## Uso

1. Ventana Principal: Al iniciar la aplicación, verás dos botones para navegar a las ventanas de Cifrado y Descifrado.

2. Ventana de Cifrado: Ingresa un número de 6 dígitos, presiona "Cifrar", y se mostrará el número cifrado.

3. Ventana de Descifrado: Ingresa un número cifrado y presiona "Descifrar" para obtener el número original.

## Autor

Esta aplicación fue desarrollada por **Efrain Montealegre Raga** como parte de una actividad práctica para aprender a construir aplicaciones gráficas en Python utilizando PyQt5.

Si tienes preguntas o sugerencias, puedes contactarme a través de GitHub o por correo.