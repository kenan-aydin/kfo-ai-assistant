import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI (api_key=os.getenv("OPENAI_API_KEY"))

with open("practice_knowledge.txt", "r", encoding="utf-8") as file:
    practice_knowledge = file.read()

def analyze_inquiry(text):
    prompt = f"""
    Du analysierst Anfragen an eine kieferorthopädische Praxis.

    Ordne die Anfrage genau einer dieser Kategorien zu:
    - Termin
    - Kosten / Rechnung
    - Zahnspange / Behandlung
    - Neupatient
    - Sonstiges

    Bestimme zusätzlich die Dringlichkeit:
    - dringend
    - normal

    Dringend sind zum Beispiel:
    - starke oder plötzlich auftretende Schmerzen
    - starke Blutungen
    - Verletzungen oder Unfälle
    - starke Schwellungen
    - akute Probleme mit der Zahnspange

    Anfrage:
    {text}

    Antworte ausschließlich als JSON in diesem Format:
    {{
        "category": "Kategorie",
        "urgency": "normal oder dringend"
    }}
    """

    response = client.responses.create(
        model="gpt-5.1",
        input=prompt
    )

    return json.loads(response.output_text)

def generate_reply(inquiry, category):
    prompt = f"""
    Du bist ein Assistenzsystem für eine kieferorthopädische Praxis.

    Nutze für deine Antwort ausschließlich die folgende Wissensbasis:
    {practice_knowledge}

    Anfrage des Patienten:
    {inquiry}

    Kategorie:
    {category}

    Erstelle einen kurzen, freundlichen und professionellen Antwortentwurf
    für das Praxisteam.

    Regeln:
    - Keine Diagnosen stellen.
    - Keine medizinischen Behandlungsempfehlungen geben.
    - Bei medizinischen Beschwerden an das Praxisteam verweisen.
    - Keine Informationen erfinden.
    - Der Entwurf muss vor dem Versand von einem Menschen geprüft werden.
    - Praxisinformationen dürfen nur aus der Wissensbasis stammen.
    - Wenn eine benötigte Information nicht in der Wissensbasis steht, verweise auf das Praxisteam und erfinde keine Antwort.
    """

    response = client.responses.create(
        model="gpt-5.1",
        input=prompt
    )

    return response.output_text

