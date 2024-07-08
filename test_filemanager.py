import os
import pytest
from console_file_manager import create_folder_01, delete_file_or_folder_02, copy_file_or_folder_03, list_directory_contents_04, list_only_folders_05, list_only_files_06, get_system_info_07, get_creator_info_08
from console_file_manager import format_date
from console_file_manager import play_quiz_09

def test_create_folder():
  assert create_folder_01('a') == True

def test_delete_file_or_folder():
  assert delete_file_or_folder_02('a') == True

def test_copy_file_or_folder():
  assert copy_file_or_folder_03("t1.txt", "t2.txt") == True

def test_list_directory_contents():
  assert isinstance(list_directory_contents_04(), list)

def test_list_only_folders():
  assert isinstance(list_only_folders_05(), list)

def test_list_only_files():
  assert isinstance(list_only_files_06(), list)

def test_get_system_info():
  assert isinstance(get_system_info_07(), str)

def test_get_creator_info():
  assert isinstance(get_creator_info_08(), str)

#~ Добавляем assert для проверки форматирования даты
assert format_date("25.12.2022") == "25 декабря 2022 года"

selected_people = [
    ("Вольфганг Амадей Моцарт", "27.01.1756")
]

answer_lst = ["27.01.1756"]

#~ Добавляем assert для проверки функции play_quiz_09
assert play_quiz_09(selected_people, answer_lst) == 1

#~ Проверяем, что файл listdir.txt был создан
assert os.path.exists("listdir.txt")