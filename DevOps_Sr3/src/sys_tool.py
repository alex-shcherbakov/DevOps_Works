import sys

def main():
    """Основна функція, що обробляє аргументи командного рядка."""
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg in ("--help", "-h"):
            print("Використання: python src/sys_tool.py")
            print("Друкує рядок 'командна строка', коли запущено безпосередньо.")
            return
        else:
            print(f"Невідомий аргумент: {arg}")
            print("Спробуйте --help для підказки.")
            return
    print("командна строка")


if __name__ == "__main__":
    main()