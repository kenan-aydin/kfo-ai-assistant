import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI (api_key=os.getenv("OPENAI_API_KEY"))

def classify_inquiry(text):
    prompt = f"""
    Du klassifizierst Anfragen an eine kieferorthopädische Praxis.

    Ordne die folgende Anfrage genau einer dieser Kategorien zu:
    - Termin
    - Kosten / Rechnung
    - Zahnspange / Behandlung
    - Neupatient
    - Sonstiges

    Anfrage:
    {text}

    Antworte ausschließlich mit dem Namen der Kategorie.
    """

    response = client.responses.create(
        model="gpt-5.1",
        input=prompt
    )

    return response.output_text.strip()

def generate_reply(inquiry, category):
    prompt = f"""
    Du bist ein Assistenzsystem für eine kieferorthopädische Praxis.

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
    """

    response = client.responses.create(
        model="gpt-5.1",
        input=prompt
    )

    return response.output_text

st.set_page_config(
    page_title="KFO AI Assistant",
    page_icon="🦷",
    layout="centered"
)

st.title("🦷 KFO AI Assistant")

st.write(
    "KI-Assistent zur Klassifikation von Praxisanfragen "
    "und zur Erstellung von Antwortentwürfen."
)

st.info("Demo-Projekt – bitte keine echten Patientendaten eingeben.")

inquiry = st.text_area(
    "Praxisanfrage",
    placeholder="Beispiel: Ich kann meinen Termin am Donnerstag leider nicht wahrnehmen. Kann ich ihn verschieben?",
    height=150
)

if st.button("Anfrage analysieren"):
    if inquiry.strip():
        category = classify_inquiry(inquiry)

        st.success("Anfrage wurde analysiert.")
        st.subheader("Ergebnis")
        st.write(f"**Kategorie:** {category}")
        st.write(f"**Eingabe:** {inquiry}")
        reply = generate_reply(inquiry, category)
        st.subheader("KI-Antwortenentwurf")
        st.write(reply)
    else:
        st.warning("Bitte zuerst eine Anfrage eingeben.")