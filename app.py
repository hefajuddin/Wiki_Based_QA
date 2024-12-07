from flask import Flask, render_template, request, jsonify
import wikipediaapi
import spacy
from transformers import pipeline

app = Flask(__name__)

# Load QA model pipeline
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# Initialize Wikipedia API with user agent
wiki_wiki = wikipediaapi.Wikipedia(
    language="en",
    user_agent="WikiBasedQA/1.0 (https://example.com/; contact@example.com)"
)

# Load spaCy's English NLP model
nlp = spacy.load("en_core_web_sm")

def extract_topic(question):
    # Process the question with spaCy
    doc = nlp(question)
    
    # Look for named entities (e.g., PERSON, ORG, GPE) or nouns as fallback
    for ent in doc.ents:
        if ent.label_ in {"PERSON", "ORG", "GPE", "EVENT", "WORK_OF_ART"}:
            return ent.text
    
    # Fallback: Use the first noun or proper noun
    for token in doc:
        if token.pos_ in {"NOUN", "PROPN"}:
            return token.text
    
    # Default to the entire question if no topic is extracted
    return question.strip()

def get_wikipedia_answer(question):
    # Extract the topic from the question
    topic = extract_topic(question)
    
    # Query Wikipedia for the topic
    page = wiki_wiki.page(topic)
    
    if not page.exists():
        return f"Sorry, I couldn't find information about '{topic}'."
    
    # Use the Wikipedia summary as context
    context = page.summary
    
    try:
        # Use the QA model to find the answer
        qa_result = qa_pipeline(question=question, context=context)
        answer = qa_result['answer']
        return answer
    except Exception as e:
        return f"Unable to process the question due to: {str(e)}"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = get_wikipedia_answer(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    print("\033[92m" + "Server is running successfully on http://127.0.0.1:5002" + "\033[0m")
    app.run(debug=True, port=5002)