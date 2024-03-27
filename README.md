<p align="center">
  <img src="docs/code_assistant_logo.png" width="350" title="hover text" alt="MUZG logo">
</p>

# Table of contents
- [Table of contents](#table-of-contents)
  - [General info](#general-info)
  - [Technologies](#technologies)
  - [Prerequirements](#prerequirements)
  - [Setup](#setup)
    - [Unique\_config](#unique_config)
  - [Documentation](#documentation)

## General info
This project is a recruitment task for Opera recruitment process for a position of AI Python Developer.

**To read the full code documentation go to: ```docs/build/html/index.html```**

In this project I have tested most popular LLM models available with non-limiting 
licenses (MIT, Apache 2.0, bsd-3-clause):

* `CodeLlama-7b-hf`
* `CodeGen-350M`
* `Neo-GPT-125M`

Usage of any mentioned models requires downloading them from Hugging Face, which will be done automatically before the first prediction.
Make note that the CodeLlama model requires more than 30GB of download and about 53GB of non system restricted VRAM (GPU)
or RAM and it takes more than 10min for a single prediction without the use of GPU or M2 type chip on Mac.

The suggestions from `CodeGen-350M` and `Neo-GPT-125M` were deemed of lesser quality and an approach of fine-tuning 
was applied to `Neo-GPT-125M` as it was smaller and it would be performed faster live.



## Technologies
Project is created with:
* Python
* PyQt6
* transformers
* pytorch

## Prerequisites
Downloading and cloning of models from Hugging Face will require a registered account on the site and installing git lsf.

To install git lfs execute command:

```git lfs install```

## Setup
To use this project, run using python:
**Python 3.10**

```
$ python llm_code_assistant.py
```

### Unique_config

To install any missing requirements and dependencies execute:

```pip install -r requirements.txt```

To resolve any issues with imports of internal functions execute:

```pip install -e .```

## Documentation

Documentation created with sphinx.

To recreate the process You will have to execute following commands from the root directory:

```pip install sphinx```

```sphinx-quickstart```

```sphinx-apidoc -f --no-toc -d 1 --separate --module-first --output-dir docs/build .\src\llm_code_assistant\```

```sphinx-build -M html docs docs/build/```

