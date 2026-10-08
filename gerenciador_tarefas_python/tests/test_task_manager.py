import unittest

from src.task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        self.manager.add_task("Estudar Python")
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(self.manager.tasks[0].description, "Estudar Python")

    def test_complete_task(self):
        self.manager.add_task("Fazer exercício")
        self.manager.complete_task(1)
        self.assertTrue(self.manager.tasks[0].completed)

    def test_remove_task(self):
        self.manager.add_task("Tarefa temporária")
        self.manager.remove_task(1)
        self.assertEqual(len(self.manager.tasks), 0)


if __name__ == "__main__":
    unittest.main()
