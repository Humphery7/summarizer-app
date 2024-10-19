from flask import Flask, request, jsonify
from transformers import pipeline, BartTokenizer


app = Flask(__name__)

pipe = pipeline("summarization", model="facebook/bart-large-cnn")
tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")

@app.route('/', methods=['GET'])
def summarize():
    input_text = request.args.get('input_text')
    if not input_text:
        return jsonify({"error": "No input text provided"}), 400
    else:
        tokens = tokenizer.encode(input_text, truncation=False)
        if len(tokens) > 1024:
            print("Input is too long. Consider breaking it into chunks.")
            tokens = tokenizer.encode(input_text, truncation=True, max_length=1024)
            input_text = tokenizer.decode(tokens, skip_special_tokens=True)

    try:
        summary = pipe(input_text, do_sample=False)[0]['summary_text']
        return jsonify({"summary": summary})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)