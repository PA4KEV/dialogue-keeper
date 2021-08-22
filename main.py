from dialog import Dialog
import version

if __name__ == "__main__":
    print(f"=== Start Dialogue Keeper {version.version} ===")

    Dialog.display(
        dialog="Question",
        choices=["A", "B", "C", "D"]
    )
