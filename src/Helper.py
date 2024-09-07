from src.ScispaceDriver import ScispaceDriver
from src.BibtextHelper import BibtextHelper
from src.CsvHelper import CsvHelper
import time

class Helper():

    def __init__(self, questions, absolute_path_of_project):
        self.questions = questions
        self.absolute_path = "{}/src/in/".format(absolute_path_of_project)

    # file_out_name name of the out file that contains the results
    # index_begin_of_loop is the position to start the loop in articles lists
    def create_all_infos_by_articles(
            self,
            file_out_name: str,
            file_bib_in_name: str,
            index_begin_of_loop: int,
            bibtex_fields_to_be_in_csv,
            header_of_csv
    ):
        csv_helper = CsvHelper(header_of_csv)

        bibtex_helper = BibtextHelper(file_bib_in_name)
        articles_infos = bibtex_helper.get_infos_from_file()

        file_path = "src/out/{}.csv".format(file_out_name)
        csv_helper.create_file_with_header(file_path)

        for i in range(index_begin_of_loop, len(articles_infos)):
            start_time = time.perf_counter()
            print("Iniciando artigo {}\n".format(i))

            file = articles_infos[i]["file"]
            title = articles_infos[i]["title"]
            doi = articles_infos[i]["doi"]

            fields = self._get_infos_in_articles(articles_infos[i], bibtex_fields_to_be_in_csv)

            print("Incluindo o artigo.... {}".format(title))
            fields = self._get_answers_for_questions(file, fields, doi)

            print("Incluindo no csv....")
            csv_helper.append_fields_to_file(file_path, fields)

            end_time = time.perf_counter()
            run_time = end_time - start_time
            print("Finalizado - {}\n".format(run_time))

    def _get_infos_in_articles(self, article_info, bibtex_fields_to_be_in_csv):
        fields = []
        for bibtex_field in bibtex_fields_to_be_in_csv:
            try:
                fields.append(article_info[bibtex_field])
            except KeyError:
                fields.append("")
        return fields

    def _get_answers_for_questions(self, file, fields, doi):
        scispace = ScispaceDriver()

        if file and doi is not None:
            absolute_path_formatted = "{}/{}".format(self.absolute_path, file)
            answers = scispace.make_questions(self.questions, absolute_path_formatted)

            for answer in answers:
                fields.append(answer)

        return fields
