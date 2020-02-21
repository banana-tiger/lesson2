"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
    """
    Замените pass на ваш код
    """
    conversation = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую"}
    while True:
        try:    
            question = input("Задайте свой вопрос или попрощайтесь: ")
            if question in conversation:
                question_key = question
                print(conversation[question_key])
            elif question == "Пока":
                print("До свидания!")
                break
            else:
                print("Сложно, непонятно, попробуйте снова")
        except KeyboardInterrupt:
            print("Пока!")
            break

if __name__ == "__main__":
    ask_user()
