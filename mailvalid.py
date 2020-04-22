from src import SocialChecker
import json
import time
import datetime

alf = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

auth = SocialChecker.XingAuth("petara94@mail.ru", "Keyman228123321")
auth = auth.GetAuth()

print(json.dumps(auth, indent=4))