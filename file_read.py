def display_name(filename):
    try:
        with open("emp.txt", 'r') as file:
            for line in file:
                parts = line.strip().split(', ')
                name = parts[0]
                if name.startswith('S'):
                    print(name)
    except FileNotFoundError:
        print("The file does not exist.")

# Example usage:
display_name('emp.txt')

# display_names_above_salary.py

def display_names_above_salary(filename, salary_threshold=94000):
    try:
        with open("emp.txt", 'r') as file:
            for line in file:
                parts = line.strip().split(', ')
                name = parts[0]
                salary = int(parts[3])
                if salary > salary_threshold:
                    print(name)
    except FileNotFoundError:
        print("The file does not exist.")

# Example usage:
display_names_above_salary('emp.txt')

# find_hotmail_users.py

def find_hotmail_users(filename):
    try:
        with open('emp.txt', 'r') as file:
            for line in file:
                parts = line.strip().split(', ')
                name = parts[0]
                email = parts[1]
                if '@yahoo.com' in email:
                    print(name)
    except FileNotFoundError:
        print("The file does not exist.")

# Example usage:
find_hotmail_users('emp.txt')

def print_seventh_line(filename):
    try:
        with open('emp.txt', 'r') as file:
            # Move to the start of the 7th line
            for _ in range(6):  # 6 because Python is zero-indexed
                file.readline()
            # Read and print the 7th line
            seventh_line = file.readline()
            print(seventh_line.strip())
    except FileNotFoundError:
        print("The file does not exist.")

# Example usage:
print_seventh_line('emp.txt')

def count_names_in_file(file_path):
    name_counts = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                name = line.split(',')[0].strip()
                name_counts[name] = name_counts.get(name, 0) + 1
    except FileNotFoundError:
        print(f'The file {file_path} does not exist.')
    except Exception as e:
        print(f'An error occurred: {e}')
    return sum(name_counts.values())

file_path = 'emp.txt'
total_name_count = count_names_in_file(file_path)
print("Total number of names in the file:", total_name_count)

