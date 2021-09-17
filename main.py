import sqlalchemy
import sys

import config
from dialog import Dialog
import version

if __name__ == "__main__":
    print(f"=== Start Dialogue Keeper {version.version} ===")

    if not config.verify_database():
        print("Error: unable to load dialogue database!")
        sys.exit(1)
    else:
        engine = sqlalchemy.create_engine(f"sqlite:///dialogues.db")
        connection = engine.connect()
        print("Loaded dialogue database")
    print("Loaded config.yaml" if config.load_config() else "Error loading config.yaml")
    

    Dialog.display(
        dialog="I don't know how to handle this by myself...\nPerhaps we can work together?",
        choices=[
            "No, you must muster strength within yourself.",
            "Yes, sure! You can follow us.", 
            "No, we only just met, we do not trust you.", 
            "Yes, we will take care of you."
        ]
    )
