import nltk

def print_tree_sideways(tree, indent="", is_last=True):
    """Custom function to print trees without messing up the order."""
    # If it's a leaf node (terminal character)
    if isinstance(tree, str):
        print(indent + ("└── " if is_last else "├── ") + tree)
    # If it's a parent node (variable)
    else:
        print(indent + ("└── " if is_last else "├── ") + tree.label())
        # Adjust the indentation for the children
        indent += "    " if is_last else "│   "
        # Recursively print children
        for i, child in enumerate(tree):
            print_tree_sideways(child, indent, i == len(tree) - 1)

# 1. Define the Context-Free Grammar
grammar = nltk.CFG.fromstring("""
    E -> E '+' T | T
    T -> T 'x' F | F
    F -> '(' E ')' | 'a'
""")

# 2. Initialize the ChartParser
parser = nltk.ChartParser(grammar)

# 3. Define the strings
strings = {
    "a": "a",
    "b": "a+a",
    "c": "a+a+a",
    "d": "((a))"
}

# 4. Parse and display
for problem_letter, string in strings.items():
    print(f"\n--- Problem {problem_letter}: Parse tree for '{string}' ---")
    tokens = list(string)
    trees = list(parser.parse(tokens))
    
    for tree in trees:
        print_tree_sideways(tree)