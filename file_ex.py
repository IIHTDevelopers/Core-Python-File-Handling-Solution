import os

def get_file_root_and_extension(filename):
    split_tup = os.path.splitext(filename)
    file_name = split_tup[0]
    file_extension = split_tup[1]
    return file_name, file_extension


def get_file_size(filename):
    return os.path.getsize(filename)

def count_words(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            num_words = len(words)
            return num_words
    except FileNotFoundError:
        print("File not found.")
        return -1
    except Exception as e:
        print("An error occurred:", e)
        return -1

def check_file_permissions(filename):
    if os.access(filename, os.W_OK):
        print(f"Write permission is granted for {filename}.")
    else:
        print(f"No write permission for {filename}.")

# Example usage:
filename = "inventory.txt"
print(get_file_root_and_extension(filename))
print(get_file_size(filename))
word_count = count_words(filename)
if word_count != -1:
    print(f"The file '{filename}' contains {word_count} words.")
check_file_permissions(filename)


def get_image_size(image_filename):
    try:
        # Get the size of the image file in bytes
        size_bytes = os.path.getsize(image_filename)
        # Convert bytes to kilobytes (1 KB = 1024 bytes)
        size_kb = size_bytes / 1024
        return size_kb
    except FileNotFoundError:
        print("File not found.")
        return -1

# Example usage:
image_filename = 'flower.jpg'
size_kb = get_image_size(image_filename)
if size_kb != -1:
    print(f"The size of the image file '{image_filename}' is {size_kb:.2f} KB.")

