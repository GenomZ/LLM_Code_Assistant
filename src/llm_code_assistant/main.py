from transformers import AutoTokenizer, AutoModelForCausalLM, GPTNeoForCausalLM, GPT2Tokenizer
import transformers
import torch

def model_predict_codellama(prompt: str) -> str:
    """
    Function calling a codellama/CodeLlama-7b-hf model from Hugging Face with a user provided prompt.
    The function returns a string that is a result of text generation. The model focuses on code completion
    and code commenting.
    Function is specifically designed to work with the defined model, providing a different model identifier may result
    with unexpected behaviour.

     Args:
        prompt: string which is a piece of code that should be completed with the specified model

    Returns:
        code_completion: string that is a continuation of the provided code in a form of text
    """

    # Defining model identifier to access and cache the model from Hugging Face Hub
    model_identifier = "codellama/CodeLlama-7b-hf"

    # Initialize tokenizer and model pipeline
    tokenizer = AutoTokenizer.from_pretrained(model_identifier)
    pipeline = transformers.pipeline(
        "text-generation",
        model=model_identifier,
        torch_dtype=torch.float64,
    )

    # Tokenize and process prompt
    sequences = pipeline(
        prompt,
        do_sample=True,
        top_k=10,
        temperature=0.1,
        top_p=0.95,
        num_return_sequences=1,
        eos_token_id=tokenizer.eos_token_id,
        max_length=200,
    )

    # Parse output and return completed code
    completed_code = ""
    for seq in sequences:
        completed_code += seq['generated_text']
        # print(f"Result: {seq['generated_text']}")

    return completed_code


def model_predict_gptneo(prompt: str) -> str:
    """
    Function calling a EleutherAI/gpt-neo-125m model from Hugging Face with a user provided prompt.
    The function returns a string that is a result of text generation. The model focuses on code completion
    and code commenting.
    Function is specifically designed to work with the defined model, providing a different model identifier may result
    with unexpected behaviour.

     Args:
        prompt: string which is a piece of code that should be completed with the specified model

    Returns:
        code_completion: string that is a continuation of the provided code in a form of text
    """

    # Check if GPU acceleration is available
    device = "cuda:0" if torch.cuda.is_available() else "cpu"

    # Specify the path to your local model directory
    mode_identifier = "EleutherAI/gpt-neo-125m"

    # Load the model and tokenizer from the local directory
    model = GPTNeoForCausalLM.from_pretrained(mode_identifier)
    tokenizer = GPT2Tokenizer.from_pretrained(mode_identifier)

    # Use GPU if possible
    model = model.to(device)

    # Ensure the tokenizer recognizes the EOS token as a pad token
    tokenizer.pad_token = tokenizer.eos_token

    # Tokenize the input prompt, ensuring to return tensors, attention mask, and apply padding
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True, max_length=512)
    input_ids = inputs.input_ids
    attention_mask = inputs.attention_mask

    # Generate a sequence of tokens following the prompt
    max_length = len(input_ids[0]) + 500  # You can adjust the max_length as needed
    output = model.generate(input_ids, attention_mask=attention_mask, max_length=max_length, no_repeat_ngram_size=2,
                            early_stopping=True, num_beams=5, pad_token_id=tokenizer.eos_token_id)

    # Decode the generated tokens to a string
    completed_code = tokenizer.decode(output[0], skip_special_tokens=True)

    return completed_code

def model_predict_codegen(prompt: str) -> str:
    """
    Function calling a EleutherAI/gpt-neo-125m model from Hugging Face with a user provided prompt.
    The function returns a string that is a result of text generation. The model focuses on code completion
    and code commenting.
    Function is specifically designed to work with the defined model, providing a different model identifier may result
    with unexpected behaviour.

     Args:
        prompt: string which is a piece of code that should be completed with the specified model

    Returns:
        code_completion: string that is a continuation of the provided code in a form of text
    """

    # Check if GPU acceleration is available
    device = "cuda:0" if torch.cuda.is_available() else "cpu"

    # Tokenize input
    tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen-350M-mono")
    model = AutoModelForCausalLM.from_pretrained("Salesforce/codegen-350M-mono")
    input_ids = tokenizer(prompt, return_tensors="pt").to(device).input_ids

    # Use GPU if applicable
    model = model.to(device)

    # Parse prompt, generate and return output
    generated_ids = model.generate(input_ids, max_length=1024)
    completed_code = tokenizer.decode(generated_ids[0], skip_special_tokens=True)

    return completed_code
