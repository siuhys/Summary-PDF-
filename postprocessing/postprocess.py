import csv

def save_summaries(output_file, summaries):

    with open(output_file, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        
        for file_name, summary in summaries.items():
            writer.writerow([f"Название файла - {file_name}"])  # Первая строка с названием файла
            writer.writerow([f"Кратко резюме файла - {summary}"])  # Вторая строка с резюме
            writer.writerow([])  # Пустая строка для разделения записей
