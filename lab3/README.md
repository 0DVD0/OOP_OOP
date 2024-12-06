# OOP Laboratory work nr.3

## Overview
The laboratory is a Python-based program that monitors a folder for changes in real time, allows users to commit folder states (snapshots), and provides functionality to restore the folder to a previous state (similar to Git's `checkout`).

The system operates through two main components:
- **Real-Time Monitoring:** Tracks changes (new, modified, and deleted files) in a specified folder and displays updates.
- **Command-Based Interface:** Provides commands for committing changes, retrieving file information, viewing status, and restoring previous states.

---

## Features
1. **Real-Time Monitoring:**
   - Detects new, deleted, and modified files.
   - Displays updates in real time every 5 seconds.

2. **Snapshot Management:**
   - Saves folder states (snapshots) during commits.
   - Each snapshot includes file names, content, and hashes for tracking changes.

3. **Restoration (`checkout`):**
   - Restores the folder to a specific snapshot (commit).
   - Clears the folder and recreates files from the snapshot.

4. **File Information and Status:**
   - Retrieves detailed information about a specific file.
   - Displays the current status of all files (e.g., `Changed`, `New file`, or `Unchanged`).

---

## How It Works

### Real-Time Monitoring
- A separate program (monitor_directory.py) continuously monitors the specified folder for changes.
- Updates are displayed for:
  - **New files:** Detected when a file is added to the folder.
  - **Deleted files:** Detected when a file is removed from the folder.
  - **Modified files:** Detected by comparing file hashes.

### Command Interface
Running the Lab_3.py lets the user interact with the program using the following commands:

#### 1. `commit`
- Saves the current state of the folder as a snapshot.
- Each snapshot includes:
  - File names.
  - File hashes.
  - File content.
- Snapshots are stored in memory (or optionally on disk for persistence).

#### 2. `info <filename>`
- Displays detailed information about the specified file, including:
  - File name.
  - Extension.
  - Creation date.

#### 3. `status`
- Displays the status of all files in the folder:
  - **New file:** Files added since the last snapshot.
  - **Changed:** Files modified since the last snapshot.
  - **Unchanged:** Files with no changes.

#### 4. `checkout <commit_id>`
- Restores the folder to a specific snapshot.
- Deletes all current files and recreates files from the selected snapshot.

#### 5. `exit`
- Terminates the program and stops monitoring.

---

## Implementation Details

### Key Classes

#### 1. `File`
- Represents a single file in the folder.
- Tracks file metadata (e.g., name, extension, creation date) and computes file hashes for change detection.

#### 2. `DocumentChangeDetectionSystem`
- Manages the folder state and snapshots.
- Key Methods:
  - **`commit`**: Saves the current folder state.
  - **`checkout`**: Restores a previous folder state.
  - **`status`**: Checks the current state of all files.
  - **`info`**: Retrieves metadata about a specific file.

### Snapshots
- Snapshots are stored as dictionaries in memory, with the commit ID as the key.
- Each snapshot includes file metadata and content.

---

## Usage

### Running the Program
1. **Start Monitoring:**
   - Run the monitor_directory.py to monitor the folder for changes every 5 seconds.

2. **Interact via Commands:**
   - Run lab_3.py and use commands (`commit`, `info`, `status`, `checkout`) to manage snapshots and view file details.

### Example Workflow
1. Add a new file to the folder.
   - **Output:** "New file detected: `<filename>`"

2. Modify a file in the folder.
   - **Output:** "File modified: `<filename>`"

3. Run `commit`.
   - **Output:** "Snapshot #0 saved successfully."

4. View file status with `status`.
   - **Output:**
     ```
     file1.txt: Unchanged
     file2.txt: Changed
     new_file.txt: New file
     ```

5. Restore the folder to a previous state with `checkout <commit_id>`.
   - **Output:** "Restored to snapshot #0."




