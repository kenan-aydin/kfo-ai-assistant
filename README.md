# 🦷 KFO AI Assistant

AI-powered assistant for processing inquiries in an orthodontic practice.

The application analyzes incoming patient inquiries, classifies them by topic and urgency, and generates context-aware response drafts using a Large Language Model (LLM).

> **Note:** This is a demo project. No real patient data should be entered or processed.

## Features

- AI-based classification of patient inquiries
- Automatic urgency detection
- LLM-generated response drafts
- Knowledge-grounded responses using a practice knowledge base
- Safety rules to prevent medical diagnoses and treatment recommendations
- Human-in-the-loop approach: generated responses must be reviewed before sending
- Error handling for API or processing failures
- Interactive web interface built with Streamlit

## Example Workflow

Patient inquiry:

> "I have severe pain from my braces and my gums are bleeding."

The application analyzes the inquiry and returns:

- **Category:** Braces / Treatment
- **Urgency:** Urgent
- **Response draft:** A context-aware draft that refers the patient to the practice without providing a diagnosis.

## How It Works

1. The user enters an inquiry in the Streamlit interface.
2. An LLM analyzes the inquiry.
3. The model returns a structured category and urgency level.
4. A local practice knowledge base provides context for the response.
5. The LLM generates a professional response draft.
6. The draft must be reviewed by practice staff before being sent.

## Tech Stack

- Python
- OpenAI API
- Large Language Models (LLMs)
- Streamlit
- JSON
- python-dotenv
- Git / GitHub

## Project Structure

```text
kfo-ai-assistant/
├── app.py
├── practice_knowledge.txt
├── requirements.txt
├── README.md
└── .gitignore
```
## Installation

Clone the repository:
```bash
git clone https://github.com/kenan-aydin/kfo-ai-assistant.git
cd kfo-ai-assistant

Create and activate a virtual environment:
python3 -m venv .venv
source .venv/bin/activate

Install the dependencies:
pip install -r requirements.txt

Create a .env file and add your OpenAI API key:
OPENAI_API_KEY=your_api_key_here

Start the application:
streamlit run app.py
```

## Safety & Privacy
This project is intended for demonstration and educational purposes.
- Do not enter real patient data.
- The assistant does not provide medical diagnoses.
- The assistant does not provide individual treatment recommendations.
- Generated responses require human review.
- API keys are stored locally and excluded from Git using .gitignore.

## Future Improvements
- Retrieval-Augmented Generation (RAG)
- Vector-based knowledge retrieval
- Extended practice knowledge base
- More detailed urgency assessment
- Automated testing and evaluation
- Improved user interface

## Author
Kenan Aydin
B.Sc. AI Engineering
Mannheim University of Applied Sciences
