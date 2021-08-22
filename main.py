import config
from dialog import Dialog
import version

if __name__ == "__main__":
    print(f"=== Start Dialogue Keeper {version.version} ===")

    print("Loaded config.yaml" if config.load_config() else "Error loading config.yaml")

    Dialog.display(
        dialog="Question",
        choices=["A", "B", "C", "D"]
    )
