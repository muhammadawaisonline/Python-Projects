import os
import shutil
import time
from datetime import datetime

class VersionControlSystem:
    def __init__(self, directory):
        self.directory = directory
        if not os.path.exists(directory):
            os.makedirs(directory)

    # Save a new version of the file
    def save_version(self, file_path):
        if not os.path.exists(file_path):
            print(f"File {file_path} does not exist.")
            return

        # Create a version directory if it doesn't exist
        version_dir = self._get_version_directory(file_path)
        if not os.path.exists(version_dir):
            os.makedirs(version_dir)

        # Copy the file with a timestamp to the version directory
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_name = os.path.basename(file_path)
        versioned_file_name = f"{base_name}_version_{timestamp}"
        shutil.copy(file_path, os.path.join(version_dir, versioned_file_name))
        print(f"Saved version: {versioned_file_name}")

    # Load a specific version of the file
    def load_version(self, file_path, version_name):
        version_dir = self._get_version_directory(file_path)
        version_file_path = os.path.join(version_dir, version_name)

        if not os.path.exists(version_file_path):
            print(f"Version {version_name} does not exist.")
            return

        # Copy the versioned file back to the original location
        shutil.copy(version_file_path, file_path)
        print(f"Restored {file_path} to version {version_name}.")

    # List all versions of the file
    def list_versions(self, file_path):
        version_dir = self._get_version_directory(file_path)
        if not os.path.exists(version_dir):
            print(f"No versions available for {file_path}.")
            return

        print(f"Versions of {file_path}:")
        for version in os.listdir(version_dir):
            print(f" - {version}")

    # Private method to get the version directory for a file
    def _get_version_directory(self, file_path):
        base_name = os.path.basename(file_path)
        version_dir = os.path.join(self.directory, f"{base_name}_versions")
        return version_dir

# Example usage
def main():
    vc_system = VersionControlSystem(directory="file_versions")

    # File you want to track
    file_to_track = "example.txt"

    while True:
        print("\n1. Save new version")
        print("2. List all versions")
        print("3. Load a specific version")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            vc_system.save_version(file_to_track)
        elif choice == "2":
            vc_system.list_versions(file_to_track)
        elif choice == "3":
            version_name = input("Enter the version name to load: ")
            vc_system.load_version(file_to_track, version_name)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
