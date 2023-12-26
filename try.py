import nltk


text_try = "SINGAPORE - Timothy Jenkins In an unprecedented overnight ruling, the Court of Appeal in the early hours on Friday (Aug 5) threw out a suit brought against the Attorney-General by 24 prisoners on death row alleging that their right to access to justice had been violated.One inmate, Abdul Rahim Shapiee, 45, who also brought a separate suit, failed in his last-minute bid to get_all_politician_names a stay of his execution.The court, comprising Chief Justice Sundaresh Menon and Justices Tay Yong Kwang and Woo Bih Li, delivered its judgment at about midnight, having deliberated for some seven hours after hearing arguments on Thursday afternoon.In a statement on Friday night, the Central Narcotics Bureau said the executions of Abdul Rahim and a co-accused, Ong Seow Ping, 49, were carried out that day.The two men were jointly tried and convicted in March 2018 of different heroin trafficking charges. Ong was not involved in the current proceedings.The 24 inmates were led by Iskandar Rahmat, the former policeman sentenced to death for the 2013 Kovan double murder."

def extract_entities(text):
    for sent in nltk.sent_tokenize(text):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'node'):
                 print (chunk.node, ' '.join(c[0] for c in chunk.leaves()))

extract_entities(text_try)