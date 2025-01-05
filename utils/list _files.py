import glob


def list_files(directory):
    return glob.glob(directory + "/*")


if __name__ == "__main__":
    files = list_files("pdf_input_files")
    for file in files:
        file = file.replace("pdf_input_files\\", "")
        print(file)
