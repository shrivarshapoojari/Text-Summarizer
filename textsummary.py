import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import  nlargest

text="Mahendra Singh Dhoni  is an Indian professional cricketer. He is a right handed batter and a wicket-keeper. Widely regarded as one of the most prolific wicket-keeper-batsmen and captains, he represented the Indian cricket team and was the captain of the side in limited-overs formats from 2007 to 2017 and in test cricket from 2008 to 2014. Dhoni has captained the most international matches and is the most successful Indian captain with wins in the 2007 ICC World Twenty20, the 2011 Cricket World Cup, the 2013 ICC Champions Trophy and the Asia Cup in 2010, 2016 and 2018. He plays for and captains Chennai Super Kings in the Indian Premier League (IPL).Born in Ranchi, Dhoni made his first class debut for Bihar in 1999. He made his debut for the Indian cricket team on 23 December 2004 in an ODI against Bangladesh and played his first test a year later against Sri Lanka. In 2007, he became the captain of the ODI side before taking over in all formats by 2008. Dhoni retired from test cricket in 2014, but continued playing in limited overs cricket till 2019. He has scored 17,266 runs in international cricket including 10,000 plus runs at an average of more than 50 in ODIs.Dhoni plays for Chennai Super Kings in the IPL, leading them to the final on ten occasions and winning it five times (2010, 2011, 2018, 2021 and 2023). He has also led CSK to two Champions League T20 titles in 2010 and 2014. He is amongst the few batsmen to have scored more than five thousand runs in the IPL, as well as being the first wicket-keeper to do so.In 2008, Dhoni was awarded India's highest sport honor Major Dhyan Chand Khel Ratna Award by Government of India. He received the fourth highest civilian award Padma Shri in 2009 and third highest civilian award Padma Bhushan in 2018. Dhoni holds an honorary rank of Lieutenant Colonel in the Parachute Regiment of the Indian Territorial Army which was presented to him by the Indian Army in 2011. He is one of the most popular cricketers in the world."
def summarizer(text):
    stopwords=list(STOP_WORDS)
    # print(stopwords)

    nlp=spacy.load("en_core_web_sm")
    doc= nlp(text)
    # print(doc)

    tokens=[token.text for token in doc]
    # print(tokens)

    word_freq={}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text]=1
            else:
                word_freq[word.text]+=1
    # print(word_freq)
    max_freq=max(word_freq.values())
    # print(max_freq)

    for word in word_freq.keys():
        word_freq[word]=word_freq[word]/max_freq
    # print(word_freq)

    sent_tokens=[sent for sent in doc.sents]
    # print(sent_tokens)

    sent_scores={}
    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent]=word_freq[word.text]
                else:
                    sent_scores[sent]+=word_freq[word.text]
    # print(sent_scores)


    select_len =int(len(sent_tokens)*0.4)

    summary=nlargest(select_len,sent_scores,key=sent_scores.get)

    final_summary=[word.text for word in summary]

    summary= ' '.join(final_summary)

    # print(summary)

    # print(text)

    # print("Length of original text = ",len(text.split(" ")))
    # print("Length of summary = ",len(summary.split(" ")))
    return summary,doc,len(text.split(' ')),len(summary.split(' '))

















