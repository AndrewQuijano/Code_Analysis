import sys
from clang.cindex import Index, Config

def parse_cpp_file(file_path):
    # Create an index for parsing
    index = Index.create()
    # Parse the C++ file into an AST
    translation_unit = index.parse(file_path)
    return translation_unit

def print_ast(node, indent=0):
    # Print the AST recursively
    print('  ' * indent + str(node.spelling or node.displayname) + ' (' + str(node.kind) + ')')
    for child in node.get_children():
        print_ast(child, indent + 1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python parse_cpp_file.py <path_to_cpp_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    translation_unit = parse_cpp_file(file_path)
    print_ast(translation_unit.cursor)