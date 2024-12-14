from setings.data_base import DB

def save_data_in_db(list_data):
    DB.insert_quests_data(list_data)

def check_user(id):
    return DB.check_id(id)