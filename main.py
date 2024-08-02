from src.parser import HH
from src.utils import sorting, creat_class
from src.creat_bd import WorkWithJson


def main():
    user_vacancy = input('Введите вакансию для поиска на сайте hh.ru: \n')
    hh = HH(user_vacancy)
    if hh.connect != 200:
        quit(f"Ошибка: {hh.connect}")
    hh.load_vacancies()
    vacancies = hh.vacancies
    fv = WorkWithJson()
    fv.save_file(vacancies)
    name_criterion = input('Введите критерий для отбора вакансий: \n')
    n = input('Введите количество вакансий для просмотра: \n')
    vac = creat_class()
    top_vacancies = sorting(vac, name_criterion, int(n))
    for top_vacancy in top_vacancies:
        print(top_vacancy)
    delete = input("Удалить список вакансий?(Y)").upper()
    if delete == "Y":
        fv.del_file()


if __name__ == '__main__':
    main()
