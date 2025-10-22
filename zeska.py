def translate(line):
    # change zeska words → python words (and add print brackets)
    line = line.strip()
    if line.startswith("printu "):
        # convert to print("text")
        content = line.replace("printu ", "", 1)
        return f"print({content})"
    line = line.replace("ifu", "if")
    line = line.replace("elseu", "else")
    return line

def run_zeska(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    py_code = ""
    for line in lines:
        py_code += translate(line) + "\n"

    print("=== Zeska running ===")
    exec(py_code)

run_zeska("hello.zeska")
