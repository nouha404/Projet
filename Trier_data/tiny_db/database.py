from textwrap import indent
from tinydb import TinyDB, where

db = TinyDB('data.json', indent=4)

Users = db.table('Users')

Users.insert_multiple([{"name":  "Teach","grade" : "Yonko" },
                       {"name":  "Akainu","grade" : "Amirale" },
                       {"name":  "Kizaru","grade" : "Amiral" },
                       ])
Users.upsert({"Xp" : 100}, where("grade") == "Yonko")   # type: ignore 