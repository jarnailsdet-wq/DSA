#context manager
import os
from contextlib import contextmanager
@contextmanager
def temporary_test_file(filename, content):
    """Context manager to create a temporary test file."""
    print(f"Creating temporary file: {filename}")
    with open(filename, 'w') as f:
        f.write(content)
    try:
        yield filename
    finally:
        print(f"Cleaning up temporary file: {filename}")
        if  os.path.exists(filename):
            os.remove(filename)

print("Testing temporary file creation and cleanup")            
try:
    with temporary_test_file('test_file.txt', 'This is a test file.') as temp_file:
        print(f"test selleinum uploaded successfully: {temp_file}")
        print("submit button is missing")
        raise Exception("Simulating an error during file processing")
except Exception as e:
    print(f"An error occurred: {e}")
    
