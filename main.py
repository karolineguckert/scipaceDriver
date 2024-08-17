from ScispaceDriver import ScispaceDriver

def main():

    questions = [
        "Quais modelos de RNA foram utilizados? E de que forma foram utilizados?",
        "Quais os pré-processamentos foram utilizados? E de que forma foram utilizados?",
        "Quais os resultados obtidos?",
        "Quais comparações podem ser feitas com o modelo empírico?",
        "Quais os possíveis trabalhos futuros?"
    ]

    root_path = "C:/Users/karol/Desktop/mestrado andrigo/TCC-3-karoline_souza_guckert_compressed.pdf"

    scispace = ScispaceDriver()
    scispace.make_questions(questions, root_path)




main()