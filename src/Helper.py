from src.ScispaceDriver import ScispaceDriver
from src.BibtextHelper import BibtextHelper
from src.CsvHelper import CsvHelper
import time

class Helper():

    def __init__(self):
        self.questions = [
            "Quais modelos de aprendizado de máquina foram utilizados neste trabalho? E de que forma foram utilizados?",
            "Quais os pré-processamentos foram utilizados nos modelos de aprendizado de máquina apresentados neste trabalho? E de que forma foram utilizados?",
            "Quais os resultados obtidos pelos modelos de aprendizado de máquina utilizados neste trabalho?",
            "Quais comparações foram feitas pelo autor entre os modelos de aprendizado de máquina utilizados neste trabalho e o modelo empírico (físico-matemático)?",
            "Quais os possíveis trabalhos futuros são apresentados pelo autor neste trabalho?"
        ]

        self.absolute_path = "C:/Users/karol/Desktop/YOLO/seleniumMestrado/src/in/"

    def create_all_infos_by_articles(self):
        csv_helper = CsvHelper()
        scispace = ScispaceDriver()

        bibtex_helper = BibtextHelper()
        articles_infos = bibtex_helper.get_infos_from_file()

        file_path = "src/out/artigos2.csv"
        csv_helper.create_file_with_header(file_path)

        for i in range(35, len(articles_infos)):
            start_time = time.perf_counter()
            print("Iniciando artigo {}\n".format(i))

            answers = None
            file = articles_infos[i]["file"]
            title = articles_infos[i]["title"].replace("{", "").replace("}", "")
            doi = articles_infos[i]["doi"]

            print("Incluindo o artigo.... {}".format(title))

            if file and doi is not None:
                absolute_path_formated = "{}/{}".format(self.absolute_path, file)
                answers = scispace.make_questions(self.questions, absolute_path_formated)

            fields = [title, doi]

            if answers is not None:
                for answer in answers:
                    fields.append(answer)
            print("Incluindo no csv....")

            csv_helper.append_fields_to_file(file_path, fields)

            end_time = time.perf_counter()
            run_time = end_time - start_time
            print("Finalizado - {}\n".format(run_time))