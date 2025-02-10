from transformers import pipeline


def extract_information(preprocessed_files: dict, max_chunk_length: int = 500) -> dict:

    summarizer = pipeline("summarization", model="cointegrated/rut5-base-multitask")

    summaries = {}
    for file_name, text in preprocessed_files.items():
        try:
            # Разделяем текст на блоки
            chunks = [
                text[i:i + max_chunk_length]
                for i in range(0, len(text), max_chunk_length)
            ]

            summary = ""
            for chunk in chunks:
                #  max_new_tokens на основе длины текста
                max_tokens = min(300, len(chunk.split()))  # Максимум: 300 токенов

                result = summarizer(
                    chunk,
                    max_new_tokens=max_tokens,  # Только max_new_tokens
                    do_sample=True,
                    num_beams=4,  #  качество генерации
                )
                summary += result[0]["summary_text"] + " "

            summaries[file_name] = summary.strip()
        except Exception as e:
            print(f"Ошибка обработки файла {file_name}: {e}")

    return summaries
