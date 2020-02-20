"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    #Практика 1
    #homework_range = [element for element in range(0, 10)]
    #for element in homework_range:
        #print(element + 1)
    
    #Практика 2
    #homework_string = input()
    #for letter in homework_string:
        #print(letter)

    #Задача Оценки
    
    import random
    import string


    def generate_grades():
        grades_list = []
        for element in range(random.randrange(5, 10), random.randrange(10, 20)):
            element = random.randrange(1, 6)
            grades_list.append(element)
        return grades_list

    def evaluate_scores_avg(scores_list):
        if type(scores_list) == list:
            scores_sum = 0
            for score in scores_list:
                scores_sum += score
            scores_avg = scores_sum / len(scores_list)
            return scores_avg
        else:
            return ValueError
    


    school_grades_list = []
    for element in range(0, 5): 
      grades_dict = {'school_class': f"{random.randrange(1, 11)}{random.choice(string.ascii_letters[0:4]).lower()}", 'scores': generate_grades()}
      school_grades_list.append(grades_dict)
    
    all_school_grades = []
    each_class_scores = []
    for element in school_grades_list:
        scores_list = element['scores']
        all_school_grades += scores_list
        each_class_scores.append(scores_list)
    print(f"Средний балл по всей школе равен {round(evaluate_scores_avg(all_school_grades), 1)}")
    print(f"Средние баллы по каждому классу: {[round(evaluate_scores_avg(element), 1) for element in each_class_scores]}")

    
if __name__ == "__main__":
    main()
