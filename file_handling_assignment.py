def write_to_file(filename, content_list):
  """
  Writes a list of lines to a text file in write mode.

  Args:
      filename: The name of the file to write to.
      content_list: A list containing the lines to be written.
  """
  try:
    with open(filename, 'w') as file_object:
      for line in content_list:
        file_object.write(line + "\n")  # Add newline character at the end
  except (IOError, OSError) as e:
    print(f"Error writing to file: {e}")

def read_from_file(filename):
  """
  Reads the contents of a text file and displays them on the console.

  Args:
      filename: The name of the file to read from.
  """
  try:
    with open(filename, 'r') as file_object:
      contents = file_object.read()
      print(contents.rstrip())  # Remove trailing newline
  except FileNotFoundError as e:
    print(f"Error reading file: {e}")

def append_to_file(filename, content_list):
  """
  Appends a list of lines to a text file in append mode.

  Args:
      filename: The name of the file to append to.
      content_list: A list containing the lines to be appended.
  """
  try:
    with open(filename, 'a') as file_object:
      for line in content_list:
        file_object.write(line + "\n")  # Add newline character at the end
  except (IOError, OSError) as e:
    print(f"Error appending to file: {e}")

# Initial content to write
content_to_write = [
  "This is the first line of text.\n",
  "Here's another line with a number: 42\n",
  "And a final line for now.\n"
]

# Write the initial content to the file
write_to_file("my_file.txt", content_to_write)

# Read the contents of the file and display them
print("\n--- Contents of the file ---")
read_from_file("my_file.txt")

# Additional content to append
content_to_append = [
  "\nAppending some more lines...\n",
  "This line is appended.\n",
  "The file now has more content.\n"
]

# Append the additional lines to the file
print("\n--- Appending content ---")
append_to_file("my_file.txt", content_to_append)

# Read the contents again to see the appended text
print("\n--- Contents after appending ---")
read_from_file("my_file.txt")

print("\n--- File handling completed successfully! ---")
