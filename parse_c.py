import sys
from pycparser import parse_file, c_ast, c_generator
from pycparser.plyparser import ParseError
import os


def parse_c_file(c_source):
    # Path to the fake standard library
    fake_libc_include_path = os.path.join(os.path.dirname(__file__), 'pycparser', 'utils', 'fake_libc_include')

    # Parse the C file into an AST
    try:
        ast = parse_file(c_source, use_cpp=True, cpp_path='gcc', cpp_args=['-E', f'-I{fake_libc_include_path}'])
        return ast
    except ParseError as e:
        print(f"Parse error: {e}")
        sys.exit(1)

def print_ast(abstract_syntax_tree):
    # Print the AST
    abstract_syntax_tree.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python parse_c_file.py <path_to_c_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    ast = parse_c_file(file_path)
    print_ast(ast)