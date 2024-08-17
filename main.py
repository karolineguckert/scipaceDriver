from ScispaceDriver import ScispaceDriver

def main():

    questions = [
        "Quais modelos de RNA foram utilizados? E de que forma foram utilizados?",
        "Quais os pré-processamentos foram utilizados? E de que forma foram utilizados?",
        "Quais os resultados obtidos?",
        "Quais comparações podem ser feitas com o modelo empírico?",
        "Quais os possíveis trabalhos futuros?"
    ]
    answers = []

    for question in questions:
        scispace = ScispaceDriver()
        scispace.file_upload()
        scispace.change_language()

        text_answer = scispace.write_and_submit_in_text_area(question)
        answers.append(text_answer)
        print(text_answer)
        scispace.close_window()

    print(answers)



main()