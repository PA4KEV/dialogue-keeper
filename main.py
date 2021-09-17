import sys

import config
import database.config
from dialog import Dialog
import version

if __name__ == "__main__":
    print(f"=== Start Dialogue Keeper {version.version} ===")

    session = database.config.initialize()
    if not session:        
        sys.exit(1)
    else:               
        print("Loaded dialogue database")
        c = session.query(database.config.Character).one_or_none()
        for d in c.dialogs:
            print(f'{c.name}: {d.choice_path}')
        

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
