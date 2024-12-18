from db.database import get_user_data

def run_logic():
    user_id = 1
    user_data = get_user_data(user_id)
    print(f"User Data: {user_data}")
