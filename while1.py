"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def ask_user():
    """
    Замените pass на ваш код
    """
    def ask_user():
        question = "Как дела?"
        right_answer = "Хорошо"
        while True:
          print(question)
          user_answer = input()
          if user_answer == right_answer:
              print("И это правильный ответ!")
              break
    
    ask_user()
    
if __name__ == "__main__":
    ask_user()
