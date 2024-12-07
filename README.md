# Wiki_Based_QA

1. Install requirment using following command-
pip install -r requirements.txt

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