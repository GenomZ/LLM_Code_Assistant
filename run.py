import sys
import argparse

from PySide6.QtWidgets import QApplication

from gui.main_window import LLMGUI  # Adjust this import based on your actual GUI file and class name
from src.llm_code_assistant.main import (model_predict_codegen,
                                                       model_predict_gptneo,
                                                       model_predict_codellama)


# Custom validation function for the --prompt argument
def non_empty_string(s):
    if not s:
        raise argparse.ArgumentTypeError("The prompt cannot be an empty string.")
    return s

# Function to execute the model in console mode
def main():
    # Argument parser setup with detailed descriptions
    parser = argparse.ArgumentParser(
        description="Launch the Language Model (LLM) application in GUI or console mode.",
        epilog="Example usage: \npython run.py --gui --prompt 'Hello, world!' --model codellama\npython run.py --prompt 'Hello, world!' --model gptneo",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("--prompt", type=non_empty_string, help="Initial prompt to use for generating suggestions.", default="")
    parser.add_argument("--model", type=str, choices=['codellama', 'gptneo', 'codegen'], help="Specifies the model to use for suggestions. Options: 'codellama', 'gptneo', 'codegen'. Default is 'codellama'.", default="codellama")
    parser.add_argument("--gui", action="store_true", help="Launches the GUI application. If not specified, executes in console mode.")

    # Parse command-line arguments
    args = parser.parse_args()

    # Conditionally launch GUI or execute model based on the arguments
    if args.gui:
        app = QApplication(sys.argv)
        ex = LLMGUI()
        ex.show()
        sys.exit(app.exec())
    else:
        if args.model == "gptneo":
            print(model_predict_gptneo(args.prompt))
        elif args.model == "gptneo":
            print(model_predict_codegen(args.prompt))
        elif args.model == "codellama":
            print(model_predict_codellama(args.prompt))


if __name__ == "__main__":
    main()