from flask import Flask, request, jsonify

from src.llm_code_assistant.main import (model_predict_codellama,
                                         model_predict_gptneo,
                                         model_predict_codegen)


app = Flask(__name__)


@app.route('/codellama', methods=['POST'])
def codellama():
    """
    Function that returns output for  prompt with the use of codellama/CodeLlama-7b-hf model from Hugging Face
    :return:
    """
    data = request.json
    prompt = data['prompt']
    suggestion = model_predict_codellama(prompt)
    return jsonify(suggestion=suggestion)


@app.route('/gptneo', methods=['POST'])
def gptneo():
    """
    Function that returns output for  prompt with the use of codellama/CodeLlama-7b-hf model from Hugging Face
    :return:
    """
    data = request.json
    prompt = data['prompt']
    suggestion = model_predict_gptneo(prompt)
    return jsonify(suggestion=suggestion)


@app.route('/codegen', methods=['POST'])
def codegen():
    data = request.json
    prompt = data['prompt']
    suggestion = model_predict_codegen(prompt)
    return jsonify(suggestion=suggestion)


def run_flask_app():
    app.run(debug=True, use_reloader=False)  # use_reloader=False is important to avoid starting the app twice


if __name__ == '__main__':
    run_flask_app()
