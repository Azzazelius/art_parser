#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# * __file__: Это встроенная переменная в Python, представляет путь к текущему файлу manage.py.
# * Функция os.path.abspath() возвращает абсолютный путь к файлу, основываясь на относительном пути из __file__. 
# Это позволяет убедиться, что путь абсолютный и содержит полную информацию о директории.
# * Функция os.path.dirname() возвращает путь к родительской директории файла.
sys.path.append(os.path.join(BASE_DIR, 'parser_main'))
# * Функция os.path.join() используется для объединения пути к BASE_DIR и относительного пути 'parser_main' 
#  Это позволяет указать на папку parser_main, находящуюся внутри корневой директории проекта.
# * sys.path.append(): sys.path - это список путей, в которых интерпретатор Python 
# ищет модули при выполнении программы. Метод append() используется для добавления нового пути в этот список.
# он добавляет путь к папке parser_main в список sys.path,
# чтобы интерпретатор мог найти и импортировать модули из этой папки.

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'parser_main.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

