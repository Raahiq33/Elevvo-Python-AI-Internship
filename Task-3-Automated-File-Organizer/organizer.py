
from pathlib import Path
import shutil

# File categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "PDFs": [".pdf"],
    "Documents": [".doc", ".docx", ".txt"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z"],
    "Code": [".py", ".html", ".css", ".js"]
}


def get_category(file):
    extension = file.suffix.lower()

    for category, extensions in FILE_TYPES.items():
        if extension in extensions:
            return category

    return "Others"


def get_unique_destination(destination):
    if not destination.exists():
        return destination

    counter = 1

    while True:
        new_name = (
            f"{destination.stem}_{counter}{destination.suffix}"
        )
        new_path = destination.with_name(new_name)

        if not new_path.exists():
            return new_path

        counter += 1


def organize_files(folder_path):
    folder = Path(folder_path).expanduser()

    if not folder.is_dir():
        print("Error: Folder not found!")
        return

    try:
        files = [item for item in folder.iterdir()
                 if item.is_file()]
    except OSError as error:
        print(f"Cannot access folder: {error}")
        return

    if not files:
        print("The folder is empty!")
        return

    moved_count = 0

    for file in files:
        category = get_category(file)
        destination_folder = folder / category

        try:
            destination_folder.mkdir(exist_ok=True)

            destination = get_unique_destination(
                destination_folder / file.name
            )

            shutil.move(str(file), str(destination))

            print(f"MOVED: {file.name}")
            print(f"FROM: {file}")
            print(f"TO:   {destination}")
            print("-" * 40)

            moved_count += 1

        except (OSError, shutil.Error) as error:
            print(f"Error moving {file.name}: {error}")

    print(f"\nCompleted! {moved_count} files organized.")


if __name__ == "__main__":
    print("===== AUTOMATED FILE ORGANIZER =====")

    folder_path = input("Enter folder path: ").strip().strip('"')

    if folder_path:
        confirm = input(
            "Files will be moved. Continue? (yes/no): "
        ).strip().lower()

        if confirm == "yes":
            organize_files(folder_path)
        else:
            print("Operation cancelled.")
    else:
        print("Error: No folder path entered.")
