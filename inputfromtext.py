def read_input_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            input_data = file.read()
            return input_data
    except FileNotFoundError:
        return "File not found"
if __name__ == "__main__":
    file_path = "textfile.txt"
    input_data = read_input_from_file(file_path)
    print("Input from file: ")
    print(input_data)

