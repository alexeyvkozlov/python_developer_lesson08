#~ USAGE
# cd c:\python_developer
# cd d:\python_developer
# .\pydev\Scripts\activate
# cd c:\python_developer\python_developer_lesson07_task2
# cd d:\python_developer\python_developer_lesson07_task2
#~~~~~~~~~~~~~~~~~~~~~~~~
# python console_file_manager.py
#~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import os
import platform
import getpass
import random

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
famous_people = [
  ("Александр Сергеевич Пушкин", "06.06.1799"),
  ("Альберт Эйнштейн", "14.03.1879"),
  ("Махатма Ганди", "02.10.1869"),
  ("Мартин Лютер Кинг", "15.01.1929"),
  ("Стив Джобс", "24.02.1955"),
  ("Леонардо да Винчи", "15.04.1452"),
  ("Мэри Кюри", "07.11.1867"),
  ("Нельсон Мандела", "18.07.1918"),
  ("Вольфганг Амадей Моцарт", "27.01.1756"),
  ("Майя Анжелу", "04.04.1928")
]
#~~~~~~~~~~~~~~~~~~~~~~~~
bill_sum = 0
history = []
#~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 01 
# - создать папку
# после выбора пользователь вводит название папки, создаем её в рабочей директории;
def create_folder_01(folder_name: str) -> bool:
  retVal = False
  # folder_name = input("Введите название папки для создания: ")
  try:
    os.mkdir(folder_name)
    print(f"Папка создана: `{folder_name}`")
    retVal = True
  except FileExistsError:
    print(f"Ошибка. Папка уже существует: `{folder_name}`")
  return retVal

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ 02
# - удалить (файл/папку)
# после выбора пользователь вводит название папки или файла, удаляем из рабочей директории если такой есть;
def delete_file_or_folder_02(item_name: str) -> bool:
  retVal = False
  # item_name = input("Введите название файла или папки для удаления: ")
  try:
    os.remove(item_name) if os.path.isfile(item_name) else os.rmdir(item_name)
    print(f"Удален(а): `{item_name}`")
    retVal = True
  except FileNotFoundError:
    print("Файл или папка не найдены.")
  return retVal

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ 03
# - копировать (файл/папку)
# после выбора пользователь вводит название папки/файла и новое название папки/файла. Копируем;
def copy_file_or_folder_03(name1: str, name2: str) -> bool:
  retVal = False
  #~ путь к папке из которой запустили программу
  prog_path = os.getcwd()
  fname1 = os.path.join(prog_path, name1)
  fname2 = os.path.join(prog_path, name2)
  print(f"Файл/папка-1: `{fname1}`")
  print(f"Файл/папка-2: `{fname2}`")
  try:
    if os.path.isfile(fname1):
      os.system(f'copy {fname1} {fname2}')
    else:
      os.system(f'xcopy {fname1} {fname2} /E /I')
    print(f"Скопирован(а) : `{fname1}` -> `{fname2}`")
    retVal = True
  except FileNotFoundError:
    print("Файл или папка не найдены")
  return retVal

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ 04
# - просмотр содержимого рабочей директории
# вывод всех объектов в рабочей папке;
def list_directory_contents_04() -> list[str]:
  retVal = []
  for item in os.listdir():
    retVal.append(item)
  return retVal 

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ 05
# - посмотреть только папки
# вывод только папок которые находятся в рабочей папке;
def list_only_folders_05() -> list[str]:
  retVal = []
  for item in os.listdir():
    if os.path.isdir(item):
      retVal.append(item)
  return retVal

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ 06
# - посмотреть только файлы
# вывод только файлов которые находятся в рабочей папке;
def list_only_files_06() -> list[str]:
  retVal = []
  for item in os.listdir():
    if os.path.isfile(item):
      retVal.append(item)
  return retVal

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ 07
# - просмотр информации об операционной системе
# вывести информацию об операционной системе (можно использовать пример из 1-го урока);
def get_system_info_07() -> str:
  retVal = f"Операционная система: {platform.system()} {platform.release()}, Имя пользователя: {getpass.getuser()}"
  return retVal

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ 08
# - создатель программы
# вывод информации о создателе программы;
def get_creator_info_08():
  retVal = "Создатель программы: Алексей Козлов"
  return retVal

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ 09
# - играть в викторину
# запуск игры викторина из предыдущего дз;
#~~~~~~~~~~~~~~~~~~~~~~~~
def format_date(date):
  day, month, year = date.split('.')
  months = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"]
  return f"{int(day)} {months[int(month) - 1]} {year} года"
#~~~~~~~~~~~~~~~~~~~~~~~~
def play_quiz_09(selected_people, answer_lst) -> int:
  correct_answers = 0
  incorrect_answers = 0
  for i in range(len(selected_people)):
    # print(f'{i}: {selected_people[i]}, {answer_lst[i]}')
    # print(f'  {selected_people[i][0]}, {selected_people[i][1]}')
    # 0: ('Вольфганг Амадей Моцарт', '27.01.1756'), 27.01.1756
    #   Вольфганг Амадей Моцарт, 27.01.1756
    if selected_people[i][1] == answer_lst[i]:
      correct_answers += 1
    else:
      print(f"Неверно! Правильный ответ: {format_date(selected_people[i][1])}")
  return correct_answers

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ 11
# 6. Добавить пункт "сохранить содержимое рабочей директории в файл";
# Функция для сохранения содержимого рабочей директории в файл listdir.txt
def save_directory_contents_to_file():
  prog_path = os.getcwd()
  fname = os.path.join(prog_path, "listdir.txt")
  #~~~~~~~~~~~~~~~~~~~~~~~~
  files = []
  dirs = []
  #~~~~~~~~~~~~~~~~~~~~~~~~
  #~ получаем список файлов и папок в рабочей директории
  for item in os.listdir():
    if os.path.isfile(item):
      files.append(item)
    elif os.path.isdir(item):
      dirs.append(item)
  #~~~~~~~~~~~~~~~~~~~~~~~~
  #~ Записываем содержимое в файл listdir.txt
  with open(fname, "w") as file:
    file.write("files: " + ", ".join(files) + "\n")
    file.write("dirs: " + ", ".join(dirs))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
  while True:
    print()
    print('~'*70)
    print('1. Создать папку')
    print('2. Удалить файл/папку')
    print('3. Копировать файл/папку')
    print('4. Просмотр содержимого рабочей директории')
    print('5. Посмотреть только папки')
    print('6. Посмотреть только файлы')
    print('7. Просмотр информации об операционной системе')
    print('8. Создатель программы')
    print('9. Играть в викторину')
    print('10. Мой банковский счет')
    print('11. Cохранить содержимое рабочей директории в файл')
    print('12. Выход')
    #~~~~~~~~~~~~~~~~~~~~~~~~
    choice = input("Выберите пункт меню: ")
    if choice == '1':
      folder_name = input("Введите название папки для создания: ")
      create_folder_01()
    elif choice == '2':
      item_name = input("Введите название файла или папки для удаления: ")
      delete_file_or_folder_02(item_name)
    elif choice == '3':
      src1 = input("Введите название файла или папки для копирования: ")
      dst2 = input("Введите название нового/ой файла или папки для копирования: ")
      copy_file_or_folder_03(src1, dst2)
    elif choice == '4':
      dir_lst = list_directory_contents_04()
      print("Содержимое рабочей директории:")
      print(dir_lst)
    elif choice == '5':
      dir_lst5 = list_only_folders_05()
      print("Папки в рабочей директории:")
      print(dir_lst5)
    elif choice == '6':
      file_lst6 = list_only_files_06()
      print("Файлы в рабочей директории:")
      print(file_lst6)
    elif choice == '7':
      sys_info = get_system_info_07()
      print(sys_info)
    elif choice == '8':
      creator_info = get_creator_info_08()
      print(creator_info)
    elif choice == '9':
      selected_people = random.sample(famous_people, 3)
      answer_lst = []
      for famous_person, birth_date in selected_people:
        answer = input(f"Введите дату рождения {famous_person} (в формате 'dd.mm.yyyy'): ")
        answer_lst.append(answer)
      correct_answers = play_quiz_09(selected_people, answer_lst)
      print(f"Количество правильных ответов: {correct_answers} из {len(answer_lst)}")
    elif choice == '10':
      print('  1. пополнение счета')
      print('  2. покупка')
      print('  3. история покупок')
      print(f'    Ваш счет {bill_sum}')
      choice10 = input('Выберите пункт меню: ')
      if choice10 == '1':
        purchase_cost = int(input('Введите сумму: '))
        bill_sum += purchase_cost
      elif choice10 == '2':
        purchase_cost = int(input('Введите сумму покупки: '))
        if purchase_cost > bill_sum:
          print('Недостаточно средств')
        else:
          purchase_name = input('Введит название покупки: ')
          bill_sum -= purchase_cost
          history.append((purchase_name, purchase_cost))
      elif choice10 == '3':
        print(f'История покупок: {history}')
    elif choice == '11':
      save_directory_contents_to_file()
    elif choice == '12':
      break
    else:
      print('Неверный пункт меню')