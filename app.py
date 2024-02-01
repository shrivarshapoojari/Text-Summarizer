from flask import Flask, render_template,request,jsonify
from textsummary import summarizer
import spacy
nlp=spacy.load("en_core_web_sm")
app = Flask(__name__)
def serialize_doc(doc_or_str):
    if isinstance(doc_or_str, spacy.tokens.Doc):
        return {'text': doc_or_str.text, 'tokens': [token.text for token in doc_or_str]}
    elif isinstance(doc_or_str, str):
        return {'text': doc_or_str, 'tokens': nlp(doc_or_str).text}
    else:
        raise ValueError("Invalid type for serialization")



@app.route('/')
def index():
    return render_template('index.html')
   

@app.route('/summarize',methods=["GET","POST"])
def summarize():
    if request.method=="POST":
        rawtext=request.form.get("rawtext")
        summary, original, lenorg, lensum = summarizer(rawtext)
        try:
            serialized_summary = serialize_doc(summary)
            
        except Exception as e:
            # Handle any exceptions or print the error for debugging
            print(f"Error in serialization: {str(e)}")
            return jsonify({'error': 'Serialization error'})

        return jsonify({'summary': serialized_summary})

         

        


if(__name__)=="__main__":
    app.run(debug=True)

