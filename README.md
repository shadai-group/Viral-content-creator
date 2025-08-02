# Viral-content-creator con ShadAi

Aplicación web desarrollada en **FastAPI** que permite generar guiones para videos virales (TikTok, Reels) y publicaciones (Instagram, Twitter, LinkedIn) utilizando inteligencia artificial con **ShadAI**.

## 📂 Estructura del Proyecto

\`\`\`
.
├── crear_guion.py             # Lógica de conexión con ShadAI (Generación de guiones)
├── main.py                    # Backend FastAPI (Rutas y lógica principal)
├── static/
│   └── style.css              # Estilos de la interfaz web
├── templates/
│   └── index.html             # Plantilla HTML con formulario e historial
└── README.md                  # Este archivo
\`\`\`

## ⚙️ Requisitos Previos

Antes de ejecutar la aplicación, asegúrate de tener instalado:

- Python 3.9+
- Pip (gestor de paquetes de Python)

Instalación de las dependencias necesarias:


pip install fastapi uvicorn shadai


## 🚀 Cómo Ejecutar la Aplicación

Una vez instaladas las dependencias, puedes correr el proyecto localmente con el siguiente comando:


uvicorn main:app --reload


Esto levantará el servidor en:


http://127.0.0.1:8000/


Abre ese enlace en tu navegador para acceder a la aplicación.

## 📝 Uso de la Aplicación

1. Ingresa una tendencia o hashtag viral (ej: \`#BackToSchool\`, \`#LifeHacks\`).
2. Selecciona el tipo de contenido: **Video** o **Publicación**.
3. (Opcional) Sube una imagen para que la IA la use como contexto.
4. Haz clic en **Generar**.
5. El guion generado se mostrará en pantalla y se guardará en el historial lateral.

## 🧠 Tecnología Utilizada

- **FastAPI**: Framework backend para APIs rápidas y eficientes.
- **ShadAI SDK**: Para conexión y generación de contenido mediante inteligencia artificial.
- **HTML + CSS**: Frontend básico y responsivo.
- **Python Async/Await**: Para manejo de sesiones de IA de forma eficiente.

## 💡 Nota Importante
No es necesario configurar un entorno virtual para ejecutar este proyecto en local, pero es recomendable si planeas escalar o mantenerlo en el tiempo.

## 🛠 Mejoras Futuras
- Guardar historial de guiones en base de datos.
- Exportar guiones en formato PDF.
- Animaciones visuales para la interfaz.
- Autenticación de usuarios para gestionar proyectos.

---

### 🧪 ¡Pon a prueba tu creatividad!
Este proyecto es el punto de partida para que empieces a crear tus propios agentes y herramientas automatizadas con inteligencia artificial. 
**Los límites están en tu imaginación.**
