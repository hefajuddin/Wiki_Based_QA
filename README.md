# Wiki_Based_QA

1. Install requirment using following commands-
pip install -r requirements.txt
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.6.0/en_core_web_sm-3.6.0-py3-none-any.whl
python -m spacy download en_core_web_sm

3. Run cmd on your project directory and execute the project using following command-
python app.py

4. Server will run on http://127.0.0.1:5002/, ensure that this port is not runnig in another instance

5. Go to browser, hit http://127.0.0.1:5002/ now UI is displaying

6. Input any question you think it's answer is available in any Wikipedia(English) link and hit enter, if the answer is available in Widipedia-text you will get answer

7. If you will not get desired answer check terminal where you can see what Wikipedia topics are extracted (like- Wikipedia topics are: ['president', 'America']) then you can check that Wikipedia manually

=============How the project works===============
1. When user input his/her question or statement, extract_topics() read the question and extract possible topics and return
2. Then get_aggregated_context() call the wikipedeaapi on given topics and aggregated texts get from those pages and return
3. get_wikipedia_answer() takes all texts from Wikipedea pages and apply question-answer model to get answer

* Project will not work if wikipediaapi does not provide data, then you have to work on following code in data/context.py -

wiki_wiki = wikipediaapi.Wikipedia(
    language="en",
    user_agent="WikiBasedQA/1.0 (https://my-wiki-project.com/; hefajuddin101@gmail.com)"
)