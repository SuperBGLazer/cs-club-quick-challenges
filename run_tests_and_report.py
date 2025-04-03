import unittest
import os
import sys
import csv
import inspect
import importlib.util
from io import StringIO
import argparse

def load_test_module(filepath):
    """Load a test module from a file path."""
    module_name = os.path.splitext(os.path.basename(filepath))[0]
    spec = importlib.util.spec_from_file_location(module_name, filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def get_test_classes(module):
    """Get all unittest.TestCase classes from a module."""
    test_classes = []
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and issubclass(obj, unittest.TestCase) and obj != unittest.TestCase:
            test_classes.append(obj)
    return test_classes

def extract_participant_name(test_class_name):
    """Extract participant name from the test class name."""
    # Assuming test classes are named like Test<ParticipantName>
    name = test_class_name.lower()
    if name.startswith('test'):
        return name[4:]
    return name

def run_tests_for_participant(test_class):
    """Run tests for a participant and return pass/fail counts."""
    # Redirect stdout to suppress test output
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    
    # Create and run a test suite for this class
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    result = unittest.TextTestRunner().run(suite)
    
    # Restore stdout
    sys.stdout = old_stdout
    
    # Count passed and failed tests
    passed = result.testsRun - len(result.errors) - len(result.failures)
    failed = len(result.errors) + len(result.failures)
    
    return passed, failed

def find_test_files(tests_dir):
    """Find all Python test files in the tests directory."""
    test_files = []
    for root, _, files in os.walk(tests_dir):
        for file in files:
            if file.startswith('test_') and file.endswith('.py'):
                test_files.append(os.path.join(root, file))
    return test_files

def main():
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description='Run tests and generate results CSV.')
    parser.add_argument('--participant', '-p', type=str, help='Only run tests for a specific participant')
    args = parser.parse_args()
    
    # Find the tests directory relative to the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(script_dir, 'tests')
    
    # Find all test files
    test_files = find_test_files(tests_dir)
    
    results = []
    
    # Process each test file
    for test_file in test_files:
        try:
            # Load the module
            module = load_test_module(test_file)
            
            # Get test classes from the module
            test_classes = get_test_classes(module)
            
            # Run tests for each class
            for test_class in test_classes:
                participant_name = extract_participant_name(test_class.__name__)
                
                # Skip if a specific participant was requested and this isn't them
                if args.participant and args.participant.lower() != participant_name.lower():
                    continue
                
                passed, failed = run_tests_for_participant(test_class)
                
                results.append({
                    'participant': participant_name,
                    'tests_passed': passed,
                    'tests_failed': failed
                })
                
                print(f"Processed {participant_name}: {passed} passed, {failed} failed")
        except Exception as e:
            print(f"Error processing {test_file}: {e}")
    
    if not results:
        if args.participant:
            print(f"No tests found for participant: {args.participant}")
        else:
            print("No test results generated.")
        return
    
    # Write results to CSV
    output_path = os.path.join(script_dir, 'test_results.csv')
    with open(output_path, 'w', newline='') as csvfile:
        fieldnames = ['participant', 'tests_passed', 'tests_failed']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for result in results:
            writer.writerow(result)
    
    print(f"\nResults written to {output_path}")

if __name__ == '__main__':
    main()
