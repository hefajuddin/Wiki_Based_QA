import wikipediaapi
from extract_wiki import extract_topics

# Initialize Wikipedia API with user agent
wiki_wiki = wikipediaapi.Wikipedia(
    language="en",
    user_agent="WikiBasedQA/1.0 (https://my-wiki-project.com/; hefajuddin101@gmail.com)"
)

def get_aggregated_context(question):
    # Extract the topics from the question
    topics = extract_topics(question)
    print(f"Wikipedia topics are: {topics}")
    
    # Initialize an empty string for the aggregated context
    aggregated_context = ""
    
    # Query Wikipedia for each topic and aggregate summaries
    for topic in topics:
        page = wiki_wiki.page(topic)
        if page.exists():
            print(f"Found information for topic: {topic}")
            aggregated_context += page.summary + "\n"  # Add topic summary to context
        else:
            print(f"No information found for topic: {topic}")
    
    return aggregated_context