
# 🤖 Chatbot de Atención al Cliente – Backend con FastAPI

Este proyecto es un **backend para un chatbot inteligente**, desarrollado en Python con **FastAPI**, diseñado para integrarse con plataformas de conversación como **Dialogflow**. El bot responde automáticamente a múltiples consultas de usuarios, como horarios, precios, ubicación, requisitos y turnos.

---

## 🎯 Funcionalidades

El chatbot entiende las siguientes intenciones:

| Intent              | Descripción                                                  |
|---------------------|--------------------------------------------------------------|
| `ConsultarHorario`  | Devuelve el horario disponible para un servicio              |
| `ConsultarPrecio`   | Informa el precio de un servicio                             |
| `ConsultarUbicacion`| Indica la ubicación de un área o instalación                 |
| `ConsultarRequisitos`| Informa requisitos de un trámite o servicio                 |
| `ConsultarDocente`  | Proporciona información sobre docentes (modo ejemplo)        |
| `AgendarTurno`      | Permite registrar un turno usando nombre y fecha             |

También se procesan parámetros como:
- `servicio`
- `nombre`
- `fecha`
- `lugar`
- `carrera`

---

## 🛠️ Tecnologías utilizadas

- [FastAPI](https://fastapi.tiangolo.com/) – Framework moderno y rápido para APIs
- Python 3.8+
- Pydantic – Validación de datos
- Postman – Para pruebas de intents simulados

---

## 📂 Estructura del proyecto

```
chatbot-backend/
├── main.py                        # Código principal del webhook
├── postman/                       # Colección de pruebas en Postman
│   └── webhook_chatbot_test_collection.json
├── requirements.txt               # Dependencias del proyecto
└── README.md
```

---

## 🚀 Cómo probarlo localmente

1. Cloná el repositorio
2. Instalá dependencias y ejecutá FastAPI:

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

3. Accedé a la documentación interactiva:
```
http://127.0.0.1:8000/docs
```

4. Usá Postman para probar los intents disponibles o integralo con Dialogflow.

---

## 🔗 Integración con Dialogflow

Podés publicar el webhook con [ngrok](https://ngrok.com/) o [Render](https://render.com/) y vincularlo como fulfillment en un agente de Dialogflow para respuestas dinámicas.

---

## 📌 Licencia

MIT – libre para usar, modificar y compartir.
