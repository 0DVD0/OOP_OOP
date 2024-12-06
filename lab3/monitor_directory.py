import os
import time
import hashlib
from multiprocessing import Manager


def calculate_hash(file_path):
    hasher = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        return None


def monitor_folder(shared_state):
    folder_to_monitor = "./test_directory"
    monitored_files = {}

    print(f"[Monitoring] Monitoring folder: {folder_to_monitor}")

    while True:
        try:
            # Get the current state of the folder
            current_files = set(os.listdir(folder_to_monitor))

            # Check for new files
            new_files = current_files - monitored_files.keys()
            for new_file in new_files:
                file_path = os.path.join(folder_to_monitor, new_file)
                if os.path.isfile(file_path):
                    monitored_files[new_file] = calculate_hash(file_path)
                    print(f"[Monitoring] New file detected: {new_file}")

            # Check for deleted files
            deleted_files = set(monitored_files.keys()) - current_files
            for deleted_file in deleted_files:
                print(f"[Monitoring] File deleted: {deleted_file}")
                del monitored_files[deleted_file]

            # Check for modified files
            for file_name in current_files:
                file_path = os.path.join(folder_to_monitor, file_name)
                if os.path.isfile(file_path):
                    current_hash = calculate_hash(file_path)
                    if file_name in monitored_files and monitored_files[file_name] != current_hash:
                        print(f"[Monitoring] File modified: {file_name}")
                        monitored_files[file_name] = current_hash

            # Check for actions from shared state
            if shared_state.get("action"):
                print(f"[Action] {shared_state['action']}")
                shared_state["action"] = ""

            # Sleep for 5 seconds before checking again
            time.sleep(5)

        except KeyboardInterrupt:
            print("[Monitoring] Monitoring stopped.")
            break


if __name__ == "__main__":
    with Manager() as manager:
        shared_state = manager.dict()
        shared_state["action"] = ""

        monitor_folder(shared_state)
