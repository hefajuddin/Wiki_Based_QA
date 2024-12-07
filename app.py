from flask import Flask, render_template, request, jsonify
from transformers import pipeline
from data.context import get_aggregated_context

app = Flask(__name__)

# Load QA model pipeline
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def get_wikipedia_answer(question):
    context=get_aggregated_context(question)

    if not context.strip():
        return "Sorry, I couldn't find information about the topics."
    
    try:
        # Use the QA model to find the answer using the provided context
        qa_result = qa_pipeline(question=question, context=context)
        return qa_result['answer']
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