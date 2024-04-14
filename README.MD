# Proyecto compresor de comunicación mediante algoritmo de Huffman

## Autores

- Pablo Emilio Troncoso Romero
- Andrés Quintero Pedraza

## Estructura sugerida

- Carpeta src: Codigo fuente de la logica de la aplicación asi como también menú de    usuario
- Carpeta tests: Pruebas Unitarias 

## Funcionalidad y uso

Este programa implementa el algoritmo de codificación Huffman para comprimir y descomprimir texto ingresado por el usuario.

### Ejecución del Programa

Para ejecutar el programa y codificar un texto, sigue los siguientes pasos:

- Clona el repositorio o descarga los archivos del programa.
- Asegúrate de tener Python instalado en tu sistema.
- Abre una terminal en la carpeta donde se encuentran los archivos del programa.
- Ejecuta el siguiente comando para iniciar el programa: 

    `python src\GUI\menu_GUI.py`

- Se mostrará un menú donde puedes elegir entre codificar un texto o decodificar un texto:

    1. Si eliges codificar un texto, ingresa el texto a codificar cuando se solicite.
    2. Si eliges decodificar un texto, ingresa el texto codificado cuando se solicite.
    3. Si eliges salir, el programa se cerrará.

- El programa mostrará el texto original, el texto codificado y el texto decodificado respectivamente.

### Ejecución de Pruebas Unitarias
El programa incluye pruebas unitarias para verificar su correcto funcionamiento. Para ejecutar las pruebas unitarias, sigue estos pasos:

- Asegúrate de tener instalado pytest en tu entorno de Python. Si no lo tienes instalado, puedes hacerlo con el siguiente comando:

    `pip install pytest`

- Abre una terminal en la carpeta donde se encuentran los archivos del programa.
- Ejecuta el siguiente comando para correr las pruebas unitarias:

    `pytest test_huffman_coding.py`

- Se ejecutarán las pruebas y se mostrará el resultado en la terminal.






