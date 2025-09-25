# start.py
import sys
import os

# Добавляем src/ в PYTHONPATH
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Теперь можно импортировать server
from server import main  # или from server.__main__ import main

if __name__ == "__main__":
    main()