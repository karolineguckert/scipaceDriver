import csv

class CsvHelper:
    def __init__(self):
        self.header = [
            "Titulo",
            "DOI",
            "Modelo",
            "Pré-processamento",
            "Resultados",
            "Resultados comparados com modelo empirico",
            "Trabalhos futuros"
        ]

    def create_file_with_header(self, file_path):
        with open(file_path, 'a+', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(self.header)

    def append_fields_to_file(self, file_path, fields):
        with open(file_path, 'a+', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)