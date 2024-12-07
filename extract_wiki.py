import spacy

# Load spaCy's English NLP model
nlp = spacy.load("en_core_web_sm")

def extract_topics(question):
    # Process the question with spaCy
    doc = nlp(question)
    
    topics = []

    # Collect all prepositional objects (pobj)
    for token in doc:
        if token.dep_ == "pobj":  # Prepositional object
            topics.append(token.text)

    # Collect all named entities matching specific labels
    for ent in doc.ents:
        if ent.label_ in {"PERSON", "ORG", "GPE", "EVENT", "WORK_OF_ART"}:
            topics.append(ent.text)

    # If no topics found, collect all nouns or proper nouns as fallback
    if not topics:
        topics = [token.text for token in doc if token.pos_ in {"NOUN", "PROPN"}]

    # Ensure uniqueness and return
    return list(set(topics))  # Remove duplicates and return as an array