from dataclasses import dataclass


@dataclass
class Task:
    id: int
    description: str
    completed: bool = False


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, description: str):
        task = Task(self.next_id, description)
        self.tasks.append(task)
        self.next_id += 1

    def list_tasks(self):
        if not self.tasks:
            print("\nNenhuma tarefa cadastrada.")
            return

        print("\nTarefas:")
        for task in self.tasks:
            status = "✓" if task.completed else " "
            print(f"[{status}] {task.id} - {task.description}")

    def complete_task(self, task_id: int):
        task = self._find_task(task_id)
        if task:
            task.completed = True
            print("Tarefa concluída!")
        else:
            print("Tarefa não encontrada.")

    def remove_task(self, task_id: int):
        task = self._find_task(task_id)
        if task:
            self.tasks.remove(task)
            print("Tarefa removida!")
        else:
            print("Tarefa não encontrada.")

    def _find_task(self, task_id: int):
        return next((task for task in self.tasks if task.id == task_id), None)
