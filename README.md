# Lextract

**Tagline:**
Extract, analyze, and automate insights from legal contracts with ease.

## Overview
Lextract is a Python-based toolkit for extracting text from legal contract files (PDF, DOCX, TXT) and performing automated analysis using LLMs. It is designed to help legal professionals, researchers, and developers quickly parse, analyze, and process large volumes of contract documents.

## Features
- Extracts text from PDF, DOCX, and TXT contract files
- Easily extensible for additional file types
- Automated tests for reliability
- Ready for integration with LLM-based analysis tools
- Clean project structure and easy setup

## Project Structure
```
scripts/                     # Core logic modules
    contract_parser.py       # Text extraction logic for contracts
    llm_analyzer.py          # LLM-based contract analysis logic
    __init__.py
tests/                       # Unit tests for contract parsing
    test_contract_parser.py
    __init__.py
main.py                      # Entry point for running the app
requirements.txt             # Python dependencies
.gitignore                   # Git ignore rules
README.md                    # Project documentation
```

## Ollama Setup (for LLM Analysis)

This project uses [Ollama](https://ollama.com/) to run local LLMs for contract analysis. To use the LLM features:

1. **Install Ollama:**
   - Download and install from https://ollama.com/download

2. **Start the Ollama server:**
   ```sh
   ollama serve
   ```

3. **Pull the Mistral model (or your preferred model):**
   ```sh
   ollama pull mistral
   ```

4. **Ensure the server is running on `localhost:11434` (default).**

5. **Run the main script as usual:**
   ```sh
   python main.py
   ```

The script will send contract text to the Ollama API for analysis using the selected model.

## Installation
1. **Clone the repository:**
   ```sh
   git clone https://github.com/taseebali/Lextract.git
   cd lextract
   ```
2. **Create and activate a virtual environment:**
   ```sh
   python -m venv .venv
   .venv\Scripts\activate   # On Windows
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
   *(If `requirements.txt` is missing, install manually: `pip install python-docx PyMuPDF`)*

## Usage
- **Extract contract text:**
  ```python
  from contract_parser import extract_contract_text
  text = extract_contract_text('path/to/contract.pdf')
  print(text)
  ```
- **Run the main script:**
  ```sh
  python main.py
  ```
- **Run tests:**
  ```sh
  python -m unittest discover tests
  ```

## Example
```python
from contract_parser import extract_contract_text
contract_text = extract_contract_text('marketing-agreement.pdf')
print(contract_text)
```

## Roadmap & Next Improvements
- Development of a robust full-stack web application for seamless user interaction and contract management
- Integration of a custom-trained language model based on Mistral 3B for advanced contract analysis and summarization
- Enhanced support for additional document formats (e.g., XLSX, PPTX)
- Implementation of a user authentication and role-based access system
- Real-time collaboration features for legal teams
- Advanced search and filtering capabilities across large contract repositories
- Automated clause extraction and risk assessment modules
- API endpoints for third-party integration
- Comprehensive documentation and deployment guides

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
MIT License

## Authors
- [Your Name](https://github.com/yourusername)

