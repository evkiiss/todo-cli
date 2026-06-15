import sys
from todo.commands import add_task
from todo.commands import add_task, list_tasks

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <command> [args]")
        return
    cmd = sys.argv
    if cmd == "add":
        if len(sys.argv) < 3:
            print("Need title: python main.py add 'купить хлеб'")
            return
        add_task(sys.argv)
    elif cmd == "list":  
        list_tasks()     
    else:               
        print(f"Unknown command: {cmd}")
if __name__ == "__main__":  
    main()                 