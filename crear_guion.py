import os
import re
import shutil
import tempfile
from shadai.core.session import Session
from shadai.core.enums import AIModels

def clean_code_block(text):
    return re.sub(r'```[a-zA-Z]*', '', text).replace('```', '').strip()

async def crear_guion_viral(tendencia: str, tipo: str, imagen_path: str = None) -> str:
    async with Session(
        type="standard",
        language="es",
        llm_model=AIModels.GEMINI_2_0_FLASH,
        delete=False
    ) as session:

        # 👉 Ingestar SOLO si la imagen es válida y está presente
        if imagen_path and imagen_path.lower().endswith((".png", ".jpg", ".jpeg")):
            with tempfile.TemporaryDirectory() as temp_dir:
                destino = os.path.join(temp_dir, os.path.basename(imagen_path))
                shutil.copy(imagen_path, destino)
                await session.ingest(input_dir=temp_dir)

        prompt_tipo = {
            "video": """
Eres un guionista viral especializado en contenido para TikTok o Reels. 

Recibirás un hashtag o temática y deberás generar un guion corto que incluya:
1. Un hook inicial impactante.
2. Desarrollo emocional, curioso o potente.
3. Un llamado a la acción para comentar o seguir.
""",
            "post": """
Eres un redactor viral para Instagram/Twitter/LinkedIn. 

Recibirás un hashtag o temática y deberás crear un post llamativo con:
- Primer línea fuerte.
- Desarrollo interesante o emocional.
- Frase final que incite a compartir o reflexionar.
"""
        }

        prompt = f"""{prompt_tipo.get(tipo, prompt_tipo['video'])}

Hashtag o tendencia: **{tendencia}**

Responde con un guion así:

```markdown
# Hook impactante

Desarrollo breve


[Llamado a la acción que invite a comentar o seguir]
"""

        response = await session.chat(prompt)

        if not response or not str(response).strip():
            return "⚠️ No se pudo generar un guion para esta temática. Intenta con otra."

        return clean_code_block(str(response))
