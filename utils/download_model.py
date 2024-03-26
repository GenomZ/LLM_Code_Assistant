import subprocess
import os

def clone_huggingface_model_repo(model_name, models_dir="models"):
    """
    Clone a Hugging Face model repository into the specified ./models/ directory.
    Models downloaded with the function:
        - EleutherAI/gpt-neo-125M
        - Salesforce/codegen-350M-mono
        - codellama/CodeLlama-7b-hf

    Parameters:
    model_name (str): The name of the Hugging Face model (e.g., 'EleutherAI/gpt-neo-125M').
    models_dir (str): The local directory where the model repositories should be cloned.
                      Defaults to a 'models' directory in the current working directory.
    """
    # Ensure the models directory exists
    if not os.path.exists(models_dir):
        os.makedirs(models_dir, exist_ok=True)
    else:
        print("MODEL ALREADY DOWNLOADED!")
        return

    # Construct the GitHub URL for the model's repository
    # Hugging Face model URLs typically follow this pattern
    repo_url = f"https://huggingface.co/{model_name}"

    # The local path to clone the model repository into
    # This creates a subdirectory under models_dir with the model's name
    model_dir = os.path.join(models_dir, model_name.split("/")[1])

    # Execute the git clone command
    try:
        print(f"Cloning {model_name} into {model_dir}...")
        subprocess.run(["git", "clone", repo_url, model_dir], check=True)
        print("Clone successful.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to clone repository. Error: {e}")