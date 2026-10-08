from src.task_manager import TaskManager


def main():
    manager = TaskManager()

    while True:
        print("\n=== GERENCIADOR DE TAREFAS ===")
        print("1. Listar tarefas")
        print("2. Adicionar tarefa")
        print("3. Concluir tarefa")
        print("4. Remover tarefa")
        print("0. Sair")

        option = input("\nEscolha uma opção: ").strip()

        if option == "1":
            manager.list_tasks()
        elif option == "2":
            description = input("Descrição da tarefa: ").strip()
            if description:
                manager.add_task(description)
                print("Tarefa adicionada!")
            else:
                print("A descrição não pode ficar vazia.")
        elif option == "3":
            manager.list_tasks()
            try:
                task_id = int(input("ID da tarefa: "))
                manager.complete_task(task_id)
            except ValueError:
                print("Digite um ID válido.")
        elif option == "4":
            manager.list_tasks()
            try:
                task_id = int(input("ID da tarefa: "))
                manager.remove_task(task_id)
            except ValueError:
                print("Digite um ID válido.")
        elif option == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
