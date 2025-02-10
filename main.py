import os
import json
from preprocessing.preprocess import preprocess_files
from extraction.extract import extract_information
from postprocessing.postprocess import save_summaries


def main():
    # Загрузка конфигурации
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    input_folder = config.get("data_dir", "data")
    output_file = os.path.join(config.get("output_dir", "output"), "summaries.csv")

    # Проверка пути
    os.makedirs(config.get("output_dir", "output"), exist_ok=True)

    # Шаг 1: Предобработка файлов
    preprocessed_files = preprocess_files(input_folder)
    if not preprocessed_files:
        print("Нет файлов для обработки.")
        return

    # Шаг 2: Извлечение информации
    summaries = extract_information(preprocessed_files)

    # Шаг 3: Сохранение результатов
    save_summaries(output_file, summaries)
    print(f"Результаты сохранены в {output_file}")


if __name__ == "__main__":
    main()
