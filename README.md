# Управление списком задач на Python

Этот проект реализует простую программу для управления списком задач на языке Python. Программа позволяет добавлять новые задачи, отмечать их как выполненные и выводить текущие (не выполненные) задачи.

## Описание классов

### Класс `Task`

Класс `Task` представляет собой задачу и включает в себя:

- **Атрибуты:**
  - `description` (строка): описание задачи.
  - `due_date` (строка): срок выполнения задачи.
  - `completed` (логическое значение): статус выполнения задачи (по умолчанию `False`).
  
- **Методы:**
  - `mark_completed()`: отмечает задачу как выполненную.
  - `__str__()`: возвращает строковое представление задачи.

### Класс `TaskManager`

Класс `TaskManager` управляет списком задач и включает в себя:

- **Атрибуты:**
  - `tasks` (список): список задач.
  
- **Методы:**
  - `add_task(description, due_date)`: добавляет новую задачу в список задач.
  - `mark_task_completed(description)`: отмечает задачу как выполненную по её описанию.
  - `list_current_tasks()`: возвращает список текущих (не выполненных) задач.
  - `__str__()`: возвращает строковое представление всех задач.

## Пример использования

```python
from datetime import datetime

class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок выполнения: {self.due_date}, Статус: {status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        task = Task(description, due_date)
        self.tasks.append(task)

    def mark_task_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_completed()
                break

    def list_current_tasks(self):
        current_tasks = [task for task in self.tasks if not task.completed]
        return current_tasks

    def __str__(self):
        if not self.tasks:
            return "Список задач пуст"
        return "\n".join(str(task) for task in self.tasks)

# Пример использования
if __name__ == "__main__":
    task_manager = TaskManager()
    
    # Добавляем задачи
    task_manager.add_task("Купить продукты", "2023-10-15")
    task_manager.add_task("Закончить проект", "2023-10-20")
    task_manager.add_task("Позвонить родителям", "2023-10-17")

    print("Все задачи:")
    print(task_manager)

    # Отмечаем задачу как выполненную
    task_manager.mark_task_completed("Купить продукты")

    print("\nТекущие задачи:")
    for task in task_manager.list_current_tasks():
        print(task)
```

## Запуск программы

1. Убедитесь, что у вас установлен Python (рекомендуется версия 3.6 и выше).
2. Сохраните код в файл с расширением `.py`, например, `task_manager.py`.
3. Запустите файл с помощью команды:
    ```bash
    python task_manager.py
    ```
## Лицензия
Этот проект лицензирован под лицензией MIT. См. файл `LICENSE` для получения дополнительной информации.