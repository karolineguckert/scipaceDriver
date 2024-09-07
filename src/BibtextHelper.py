import bibtexparser

class BibtextHelper:
    def __init__(self, file_bib_in_name):
        self.articles_library = bibtexparser.parse_file("src/in/{}.bib".format(file_bib_in_name))

    def get_infos_from_file(self):
        infos = []
        for entry in self.articles_library.entries:
            title = None
            doi = None
            file = None
            year = None
            author = None

            for field in entry.fields:

                if field.key == "title":
                    title = field.value

                if field.key == "doi":
                    doi = field.value

                if field.key == "file":
                    file = field.value.split(":")[1]

                if field.key == "year":
                    year = field.value

                if field.key == "author":
                    author = field.value

            infos.append({
                "title": title,
                "doi": doi,
                "file": file,
                "year": year,
                "author": author
            })

        return infos
