from src.Helper import Helper

def main():
    # questions = [
    #     "Quais modelos de aprendizado de máquina foram utilizados neste trabalho? E de que forma foram utilizados?",
    #     "Quais os pré-processamentos foram utilizados nos modelos de aprendizado de máquina apresentados neste trabalho? E de que forma foram utilizados?",
    #     "Quais os resultados obtidos pelos modelos de aprendizado de máquina utilizados neste trabalho?",
    #     "Quais comparações foram feitas pelo autor entre os modelos de aprendizado de máquina utilizados neste trabalho e o modelo empírico (físico-matemático)?",
    #     "Quais os possíveis trabalhos futuros são apresentados pelo autor neste trabalho?"
    # ]

    questions2 = [
        "Quais os nomes dos satélites ou quais os sensores utilizados como entrada nos modelos apresentados neste trabalho?"
    ]
    bibtex_fields_to_be_in_csv = [
        "title",
        "doi",
        "year",
        "author"
    ]

    # header_of_csv = [
    #     "Titulo",
    #     "DOI",
    #     "Ano",
    #     "Autor(es)",
    #     "Modelo",
    #     "Pré-processamento",
    #     "Resultados",
    #     "Resultados comparados com modelo empirico",
    #     "Trabalhos futuros"
    # ]

    header_of_csv2 = [
        "Titulo",
        "DOI",
        "Ano",
        "Autor(es)",
        "Satélite",
    ]

    absolute_path_of_project = "C:/Users/karol/Desktop/YOLO/seleniumMestrado"

    helper = Helper(questions2, absolute_path_of_project)
    helper.create_all_infos_by_articles("artigos4", "Intermares 35 itens", 0, bibtex_fields_to_be_in_csv, header_of_csv2)

main()