import bibtexparser

class BibtextHelper:
    def __init__(self):
        self.articles_library = bibtexparser.parse_file("src/in/artigos.bib")


    def get_infos_from_file(self):
        infos = []
        for entry in self.articles_library.entries:
            title = None
            doi = None
            file = None

            for field in entry.fields:

                if field.key == "title":
                    title = field.value

                if field.key == "doi":
                    doi = field.value

                if field.key == "file":
                    file = field.value.split(":")[1]

            infos.append({
                "title": title,
                "doi": doi,
                "file": file
            })

        return infos
