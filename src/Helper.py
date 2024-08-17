from src.ScispaceDriver import ScispaceDriver
from src.BibtextHelper import BibtextHelper
from src.CsvHelper import CsvHelper


class Helper():

    def __init__(self):
        self.questions = [
            "Quais modelos de RNA foram utilizados? E de que forma foram utilizados?",
            "Quais os pré-processamentos foram utilizados? E de que forma foram utilizados?",
            "Quais os resultados obtidos?",
            "Quais comparações podem ser feitas com o modelo empírico?",
            "Quais os possíveis trabalhos futuros?"
        ]

        self.absolute_path = "C:/Users/karol/Desktop/YOLO/seleniumMestrado/src/in/"

    def create_all_infos_by_articles(self):
        csv_helper = CsvHelper()
        scispace = ScispaceDriver()

        bibtex_helper = BibtextHelper()
        articles_infos = bibtex_helper.get_infos_from_file()

        for i in range(2, len(articles_infos)):
            print("Iniciando artigo {}\n".format(i))
            answers = None
            file = articles_infos[i]["file"]
            title = articles_infos[i]["title"]
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


            file_path = "src/out/artigos.csv"
            csv_helper.append_fields_to_file(file_path, fields)
            print("Finalizado\n")