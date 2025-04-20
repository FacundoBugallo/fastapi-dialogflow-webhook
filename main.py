
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any

app = FastAPI()


class Intent(BaseModel):
    displayName: str

class QueryResult(BaseModel):
    intent: Intent
    parameters: Dict[str, Any]

class WebhookRequest(BaseModel):
    queryResult: QueryResult


servicio_aliases = {
    "consultoría": ["consultoría", "asesoramiento", "entrevista académica"],
    "certificación": ["certificación", "certificado", "trámite de certificado"],
    "oficina central": ["oficina central", "sede principal", "administración"],
    "secretaría académica": ["secretaría académica", "secretaría", "oficina de alumnos"],
    "carrera de psicología": ["carrera de psicología", "psicología", "psico"],
    "docente": ["profesor", "docente", "profe"],
    "turno": ["turno", "cita", "reunión"]
}

def normalizar_servicio(nombre_usuario: str) -> str:
    for clave, alias_list in servicio_aliases.items():
        if nombre_usuario.lower() in [a.lower() for a in alias_list]:
            return clave
    return nombre_usuario.lower()

def manejar_consultar_horario(servicio: str) -> str:
    servicio = normalizar_servicio(servicio)
    horarios = {
        "consultoría": "El horario disponible para consultoría es de 9am a 6pm.",
        "certificación": "La oficina de certificación atiende de 10am a 4pm.",
        "turno": "Podés pedir turno de lunes a viernes entre 8am y 12pm."
    }
    return horarios.get(servicio, f"No tengo horarios registrados para {servicio}.")

def manejar_consultar_precio(servicio: str) -> str:
    servicio = normalizar_servicio(servicio)
    precios = {
        "consultoría": "$1500",
        "certificación": "$2000"
    }
    if servicio in precios:
        return f"El precio de {servicio} es {precios[servicio]}."
    return f"No tengo registrado el precio de {servicio}."

def manejar_consultar_ubicacion(servicio: str, lugar: str = None) -> str:
    servicio = normalizar_servicio(servicio)
    ubicaciones = {
        "oficina central": "La oficina central está en Av. Siempre Viva 123.",
        "secretaría académica": "Está en el primer piso del edificio principal."
    }
    if lugar:
        return f"La ubicación de {lugar} será confirmada próximamente."
    return ubicaciones.get(servicio, f"No tengo ubicación registrada para {servicio}.")

def manejar_consultar_requisitos(servicio: str, carrera: str = None) -> str:
    servicio = normalizar_servicio(servicio)
    if carrera:
        return f"Los requisitos para la carrera {carrera} incluyen título secundario, DNI y formulario de inscripción."
    if servicio == "carrera de psicología":
        return "Para inscribirte a Psicología necesitás tu título secundario, DNI y formulario completo."
    return f"Los requisitos para {servicio} pueden consultarse en la web oficial o presencialmente."

def manejar_consultar_docente() -> str:
    return "Podés consultar el listado de docentes por carrera en el portal del estudiante."

def manejar_agendar_turno(nombre: str = None, fecha: str = None) -> str:
    if nombre and fecha:
        return f"{nombre}, tu turno fue agendado para el {fecha}."
    elif nombre:
        return f"{nombre}, indicame la fecha para agendar tu turno."
    elif fecha:
        return f"Tu turno fue agendado para el {fecha}, por favor indicame tu nombre."
    return "Para agendar un turno necesito tu nombre y la fecha deseada."

# WEBHOOK
@app.post("/webhook")
async def dialogflow_webhook(req: WebhookRequest):
    intent = req.queryResult.intent.displayName
    parameters = req.queryResult.parameters

    servicio = parameters.get("servicio", "")
    fecha = parameters.get("fecha", None)
    nombre = parameters.get("nombre", None)
    lugar = parameters.get("lugar", None)
    carrera = parameters.get("carrera", None)

    if intent == "ConsultarHorario":
        respuesta = manejar_consultar_horario(servicio)
    elif intent == "ConsultarPrecio":
        respuesta = manejar_consultar_precio(servicio)
    elif intent == "ConsultarUbicacion":
        respuesta = manejar_consultar_ubicacion(servicio, lugar)
    elif intent == "ConsultarRequisitos":
        respuesta = manejar_consultar_requisitos(servicio, carrera)
    elif intent == "ConsultarDocente":
        respuesta = manejar_consultar_docente()
    elif intent == "AgendarTurno":
        respuesta = manejar_agendar_turno(nombre, fecha)
    else:
        respuesta = "Lo siento, no entendí tu solicitud."

    return {"fulfillmentText": respuesta}
