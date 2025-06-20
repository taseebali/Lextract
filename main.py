from scripts.contract_parser import extract_contract_text
from scripts.llm_analyzer import analyze_contract_ollama

if __name__ == "__main__":
    file_path = "../marketing-agreement.pdf" #CHANGE THIS TO FILE PATH

    try:
        contract_text = extract_contract_text(file_path)
        # print("Extracted Contract Text:")
        # print(contract_text)

        analysis_result = analyze_contract_ollama(contract_text)
        print("\nAnalysis Result:")
        print(analysis_result)
    except Exception as e:
        print(f"An error occurred: {e}")