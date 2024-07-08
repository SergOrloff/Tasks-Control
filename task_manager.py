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
    task_manager.add_task("Купить индюшку и сметану", "2024-07-07")
    task_manager.add_task("Закончить архитектурный проект", "2024-07-10")
    task_manager.add_task("Позвонить детям", "2024-07-06")
    task_manager.add_task("Изучить Python", "2024-08-31")
    task_manager.add_task("Слетать в космос", "2024-07-15")
    task_manager.add_task("Записать песню", "2024-07-20")

    print("Все задачи:")
    print(task_manager)

    # Отмечаем задачу как выполненную
    task_manager.mark_task_completed("Купить индюшку и сметану")
    task_manager.mark_task_completed("Позвонить детям")

    print("\nТекущие задачи:")
    for task in task_manager.list_current_tasks():
        print(task)