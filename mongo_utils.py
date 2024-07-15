from pymongo import MongoClient

class MongoDB:
    def __init__(self):
        self.client = MongoClient('mongodb+srv://<naima392>:<120401nm>@cluster0.3esjczc.mongodb.net/EMR?retryWrites=true&w=majority')
        self.db = self.client.EMR

    def get_patients_collection(self):
        return self.db.patients

    def get_med_history_info_collection(self):
        return self.db.medhistoryinfo
