import os
import shutil
import sys
import re
import csv

def read_users_from_csv(csv_file='users.csv'):
    """
    Read users from a CSV file and return a list of dictionaries
    """
    users = []
    try:
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                users.append(row)
        return users
    except FileNotFoundError:
        print(f"Error: CSV file {csv_file} not found!")
        return []
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []

def create_competition_folder(participant_name):
    """
    Create a folder for a participant with all challenge templates
    """
    # Sanitize participant name to be a valid folder name
    safe_name = "".join(c for c in participant_name if c.isalnum() or c in " _-").strip()
    safe_name = safe_name.replace(" ", "_")
    
    # Create the participant directory
    participant_dir = os.path.join("participants", safe_name)
    if os.path.exists(participant_dir):
        print(f"Folder for {participant_name} already exists! Skipping...")
        return None
    
    # Create directory structure
    os.makedirs(participant_dir, exist_ok=True)
    
    # Copy template files to the participant directory
    template_dir = "templates"
    if not os.path.exists(template_dir):
        print(f"Error: Template directory {template_dir} not found!")
        return None
    
    # Copy all template files directly to participant directory
    for filename in os.listdir(template_dir):
        if filename.endswith(".py"):
            source = os.path.join(template_dir, filename)
            destination = os.path.join(participant_dir, filename)
            shutil.copy2(source, destination)
    
    print(f"Created competition folder for {participant_name} at {participant_dir}")
    return participant_dir

def create_custom_test_file(participant_name, participant_dir):
    """
    Create a custom test file for the participant
    """
    # Read the original test file
    with open('test_templates.py.txt', 'r') as f:
        test_content = f.read()
    
    # Replace imports to point to participant's directory
    folder_name = os.path.basename(participant_dir)
    test_content = test_content.replace('from templates.', f'from participants.{folder_name}.')
    
    # Change the class name to include participant name
    safe_name = "".join(c for c in participant_name if c.isalnum()).strip()
    test_content = test_content.replace('class TestTemplates', f'class Test{safe_name}')
    
    # Ensure the tests folder exists
    tests_dir = os.path.join('tests')
    os.makedirs(tests_dir, exist_ok=True)
    # Write the test content to a new file in the tests directory
    test_file_path = os.path.join(tests_dir, f'test_{folder_name}.py')
    with open(test_file_path, 'w') as f:
        f.write(test_content)
    
    return test_file_path

def main():
    print("=== Programming Competition Setup ===")
    
    # Create participants and tests directories if they don't exist
    os.makedirs("participants", exist_ok=True)
    os.makedirs("tests", exist_ok=True)
    
    # Read users from CSV file
    users = read_users_from_csv()
    if not users:
        print("No users found in CSV file or file could not be read.")
        response = input("Do you want to manually enter a participant name? (y/n): ")
        if response.lower() == 'y':
            participant_name = input("Enter participant's name: ")
            if not participant_name:
                print("Error: Name cannot be empty!")
                sys.exit(1)
            
            # Create competition folder for the participant
            participant_dir = create_competition_folder(participant_name)
            if participant_dir:
                # Create a custom test file for the participant
                test_file = create_custom_test_file(participant_name, participant_dir)
                print(f"\nSetup complete! Participant folder created at: {participant_dir}")
                print(f"Custom test file created: {test_file}")
        else:
            print("Operation cancelled.")
        return
    
    # Process all users from CSV
    processed_count = 0
    skipped_count = 0
    
    for user in users:
        # Using the full name (first_name + last_name) as the participant name
        participant_name = user['username']
        print(f"\nProcessing: {participant_name}")
        
        # Create competition folder for the participant
        participant_dir = create_competition_folder(participant_name)
        if participant_dir:
            # Create a custom test file for the participant
            test_file = create_custom_test_file(participant_name, participant_dir)
            print(f"Custom test file created: {test_file}")
            processed_count += 1
        else:
            skipped_count += 1
    
    print(f"\nSetup complete! Processed {processed_count} participants, skipped {skipped_count} existing participants.")
    print("Participants can now solve the challenges in their folders.")
    print("Run 'python -m tests.test_<folder_name>' to test their solutions.")

if __name__ == "__main__":
    main()
