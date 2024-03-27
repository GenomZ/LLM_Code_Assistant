from transformers import AutoTokenizer, AutoModelForCausalLM
import torch


def model_retrain_gptneo():
    """
    something
    :return:
    """
    pass

def model_predict_codellama():
    """
    something
    :return:
    """
    pass


def model_predict_gptneo():
    """
    something
    :return:
    """
    pass


def model_predict_codegen():
    """
    something
    :return:
    """


    device = "cuda:0" if torch.cuda.is_available() else "cpu"

    tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen-350M-mono")
    model = AutoModelForCausalLM.from_pretrained("Salesforce/codegen-350M-mono")

    prompt = "import math\n\ndef fibonacci_sequence(num_of_numbers):"
    # prompt = "write sql get all tables and import as pandas dataframe"

    input_ids = tokenizer(prompt, return_tensors="pt").to(device).input_ids

    # Use GPU if applicable
    model = model.to(device)

    generated_ids = model.generate(input_ids, max_length=1024)
    output = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
    # print(output)

    print(output.split("\n\n"))

