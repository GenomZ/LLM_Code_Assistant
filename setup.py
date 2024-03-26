from setuptools import setup, find_packages

setup(
    name='LLM Code Assistant',
    version='0.0.1',
    packages=find_packages(),
    description='LLM Code Assistant Recruitment Project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Krzysztof Buzar',
    author_email='kbuzar@gmail.com',
    license='MIT',
    install_requires=[
        'transformers~=4.39.1',
        'torch~=1.11.0',
        'PySide6~=6.6.1',
        'setuptools~=58.1.0',
    ],
    url='https://github.com/GenomZ/LLM_Code_Assistant',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Opera AI Developer Recruitment Process',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='LLM Code Assistant',
)