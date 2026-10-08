
import json
from app import analyze_inquiry

# Unsere vorbereiteten Testfälle laden
with open("test_cases.json", "r", encoding="utf-8") as file:
    test_cases = json.load(file)

correct = 0

# Jede Testanfrage einzeln überprüfen
for number, test in enumerate(test_cases, start=1):
    print(f"\nTest {number}: {test['inquiry']}")

    try:
        result = analyze_inquiry(test["inquiry"])

        # Die Funktion liefert Kategorie und Dringlichkeit zurück
        if isinstance(result, str):
            result = json.loads(result)

        category = result["category"]
        urgency = result["urgency"]

        category_ok = category == test["expected_category"]
        urgency_ok = urgency == test["expected_urgency"]

        if category_ok and urgency_ok:
            correct += 1
            print("BESTANDEN")
        else:
            print("ABWEICHUNG")

        print(f"Kategorie: {category}")
        print(f"Dringlichkeit: {urgency}")

    except Exception as error:
        print(f"FEHLER: {error}")

print(f"\nErgebnis: {correct} von {len(test_cases)} Tests bestanden")
