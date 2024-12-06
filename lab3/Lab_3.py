import os
import hashlib
from datetime import datetime
from multiprocessing import Process, Queue
import time


class File:
    def __init__(self, path):
        self.path = path
        self.name = os.path.basename(path)
        self.extension = self.get_extension()
        self.creation_date = datetime.fromtimestamp(os.path.getctime(path))
        self.last_hash = self.calculate_hash()
        self.status = "Unchanged"

    def calculate_hash(self):
        hasher = hashlib.sha256()
        try:
            with open(self.path, 'rb') as f:
                while chunk := f.read(8192):
                    hasher.update(chunk)
            return hasher.hexdigest()
        except FileNotFoundError:
            return None

    def get_extension(self):
        try:
            return os.path.splitext(self.path)[1]
        except IndexError:
            return "Unknown"

    def get_info(self):
        return f"Filename: {self.name}, Extension: {self.extension}, Creation Date: {self.creation_date}"

    def has_changed(self):
        current_hash = self.calculate_hash()
        if self.last_hash != current_hash:
            self.status = "Changed"
        else:
            self.status = "Unchanged"
        return self.status == "Changed"

    def update_snapshot(self):
        self.last_hash = self.calculate_hash()
        self.status = "Unchanged"


class DocumentChangeDetectionSystem:
    def __init__(self, folder_path, log_queue):
        self.folder_path = folder_path
        self.files = {}  # Track files with snapshot information
        self.snapshots = {}  # Store snapshots for commits
        self.commit_id = 0  # Commit counter
        self.log_queue = log_queue
        self.update_snapshot()

    def update_snapshot(self):
        current_files = os.listdir(self.folder_path)
        current_files_set = set(current_files)
        existing_files_set = set(self.files.keys())

        new_files = current_files_set - existing_files_set
        for filename in new_files:
            path = os.path.join(self.folder_path, filename)
            if os.path.isfile(path):
                self.files[filename] = File(path)
                self.files[filename].status = "New file"
                self.log_queue.put(f"New file added: {filename}")

        deleted_files = existing_files_set - current_files_set
        for deleted_file in deleted_files:
            del self.files[deleted_file]
            self.log_queue.put(f"File deleted: {deleted_file}")

    def commit(self):
        snapshot = {}
        for file_name, file_obj in self.files.items():
            snapshot[file_name] = {
                "hash": file_obj.calculate_hash(),
                "path": file_obj.path,
                "content": self.read_file(file_obj.path)
            }
        self.snapshots[self.commit_id] = snapshot
        self.commit_id += 1
        self.log_queue.put(f"Snapshot #{self.commit_id - 1} saved successfully.")

    def read_file(self, path):
        try:
            with open(path, 'rb') as f:
                return f.read()
        except FileNotFoundError:
            return None

    def write_file(self, path, content):
        with open(path, 'wb') as f:
            f.write(content)

    def checkout(self, commit_id):
        if commit_id not in self.snapshots:
            print(f"Commit #{commit_id} does not exist.")
            return

        # Clear current folder
        for filename in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, filename)
            os.remove(file_path)

        # Restore files from snapshot
        snapshot = self.snapshots[commit_id]
        for file_name, file_data in snapshot.items():
            restored_path = os.path.join(self.folder_path, file_name)
            self.write_file(restored_path, file_data["content"])
        self.log_queue.put(f"Restored to snapshot #{commit_id}.")

    def info(self, filename):
        file = self.files.get(filename)
        if file:
            print(file.get_info())
        else:
            print("File not found in the current folder.")

    def status(self):
        for file in self.files.values():
            if file.status != "New file":
                file.has_changed()
            print(f"{file.name}: {file.status}")


def monitor_folder(folder_to_monitor, log_queue):
    monitored_files = set()

    while True:
        try:
            # Get the current state of the folder
            current_files = set(os.listdir(folder_to_monitor))

            # Check for new files
            new_files = current_files - monitored_files
            for new_file in new_files:
                log_queue.put(f"New file detected: {new_file}")

            # Check for deleted files
            deleted_files = monitored_files - current_files
            for deleted_file in deleted_files:
                log_queue.put(f"File deleted: {deleted_file}")

            monitored_files = current_files
            time.sleep(5)
        except KeyboardInterrupt:
            log_queue.put("[Monitoring] Monitoring stopped.")
            break


if __name__ == "__main__":
    folder_to_monitor = "./test_directory"
    log_queue = Queue()

    # Start monitoring process
    monitor_process = Process(target=monitor_folder, args=(folder_to_monitor, log_queue))
    monitor_process.start()

    # Start user interface
    system = DocumentChangeDetectionSystem(folder_to_monitor, log_queue)

    try:
        while True:
            # Display logs from the monitoring process
            while not log_queue.empty():
                print(log_queue.get())

            # Get user commands
            command = input("Enter a command (commit/info/status/checkout/exit): ").strip().lower()
            if command == "commit":
                system.commit()
            elif command.startswith("info"):
                parts = command.split()
                if len(parts) > 1:
                    filename = parts[1]
                    system.info(filename)
                else:
                    print("Please provide a filename for the info command.")
            elif command == "status":
                system.status()
            elif command.startswith("checkout"):
                parts = command.split()
                if len(parts) > 1 and parts[1].isdigit():
                    system.checkout(int(parts[1]))
                else:
                    print("Please provide a valid commit ID for the checkout command.")
            elif command == "exit":
                print("Exiting program.")
                break
            else:
                print("Invalid command.")
    finally:
        monitor_process.terminate()
