import streamlit as st


def classify_inquiry(text):
    text = text.lower()

    categories = {
        "Termin": [
            "termin", "verschieben", "absagen", "uhrzeit",
            "montag", "dienstag", "mittwoch", "donnerstag", "freitag"
        ],
        "Kosten / Rechnung": [
            "rechnung", "kosten", "bezahlen", "zahlung",
            "preis", "versicherung"
        ],
        "Zahnspange / Behandlung": [
            "zahnspange", "bracket", "draht", "schiene",
            "retainer", "gummi"
        ],
        "Neupatient": [
            "neupatient", "erster termin", "ersttermin",
            "neuer patient", "aufnahme"
        ]
    }

    for category, keywords in categories.items():
        if any(keyword in text for keyword in keywords):
            return category

    return "Sonstiges"


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

    else:
        st.warning("Bitte zuerst eine Anfrage eingeben.")