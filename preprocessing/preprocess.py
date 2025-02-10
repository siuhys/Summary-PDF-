import os
import pdfplumber


def preprocess_files(input_folder: str) -> dict:
    preprocessed_files = {}
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".pdf"):
            file_path = os.path.join(input_folder, file_name)
            try:
                with pdfplumber.open(file_path) as pdf:
                    text = " ".join(
                        page.extract_text() or "" for page in pdf.pages
                    ).strip()
                preprocessed_files[file_name] = text
            except Exception as e:
                print(f"Ошибка при обработке файла {file_name}: {e}")
    return preprocessed_files
