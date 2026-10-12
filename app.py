import streamlit as st
from ai_logic import analyze_inquiry, generate_reply

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
        try:
            analysis = analyze_inquiry(inquiry)
            category = analysis["category"]
            urgency = analysis["urgency"]

            st.success("Anfrage wurde analysiert.")
            st.subheader("Ergebnis")
            st.write(f"**Kategorie:** {category}")
            st.write(f"**Dringlichkeit:** {urgency.capitalize()}")
            st.write(f"**Eingabe:** {inquiry}")
            reply = generate_reply(inquiry, category)
            st.subheader("KI-Antwortenentwurf")
            st.write(reply)
        except Exception as e:
            st.error(
                "Die Anfrage konnte momentan nicht verarbeitet werden. "
                "Bitte versuchen Sie es später erneut."
            )
    else:
        st.warning("Bitte zuerst eine Anfrage eingeben.")