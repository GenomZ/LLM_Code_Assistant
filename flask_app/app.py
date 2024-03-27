from flask import Flask, render_template, request, jsonify
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

app = Flask(__name__)

device = "cuda:0" if torch.cuda.is_available() else "cpu"

tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen-350M-mono")
model = AutoModelForCausalLM.from_pretrained("Salesforce/codegen-350M-mono")

# Use GPU if applicable
model = model.to(device)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/complete', methods=['POST'])
def complete():
    prompt = request.form['prompt']
    input_ids = tokenizer(prompt, return_tensors="pt").to(device).input_ids

    generated_ids = model.generate(input_ids, max_length=1024)
    completions = tokenizer.decode(generated_ids[0], skip_special_tokens=True)

    return jsonify(completions=completions)


if __name__ == '__main__':
    app.run(debug=True)