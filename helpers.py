import random


class GenerationData:
    EMAIL = f"{random.randint(100, 999)}@mail.ru"
    PASSWORD = f"pass{random.randint(100, 999)}"
    AD_NAME = f"Велосипед bike{random.randint(100, 999)} Pro MAX"
    AD_DESCRIPTION = f"Просмотр по договорённости. Территориально - Уралмаш д{random.randint(1, 200)}"
    AD_PRICE = f"{random.randint(50000, 60000)}"    
