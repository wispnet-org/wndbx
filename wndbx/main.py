from ui.menu import show_menu
from logic.core import run_logic
from db.database import initialize_db

def main():
    initialize_db()
    show_menu()
    run_logic()

if __name__ == "__main__":
    main()
