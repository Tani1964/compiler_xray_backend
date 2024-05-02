from flask import Flask, request, jsonify, redirect, flash
from flask_cors import CORS
from lexer import Lexer
from syntax_tree import Parser
from interpreter import Interpreter


app = Flask(__name__)
app.secret_key = 'your_secret_key'

CORS(app, allow_any_origin=True)


@app.route("/", methods=['GET', 'POST'])
def index():
    # text = request.form.get('text')
    text = "2+3"
    
    if request.method == 'POST':
        text = request.form.get('text')
        print(text)
        if not text:
            return jsonify({"error": "No text provided"}), 400

        return redirect("http://localhost:5173")
    
    tokenizer = Lexer(text)
    tokens = tokenizer.tokenize()
    parser = Parser(tokens)
    tree = parser.parse()
    interpreter = Interpreter(tree)
    result = interpreter.interpret()
    
    def binary_tree_to_dict(tree):
        if isinstance(tree, list):
            operator = tree[1]
            left = tree[0]
            right = tree[2]
        
            return {
                "left": binary_tree_to_dict(left),
                "operator": operator,
                "right": binary_tree_to_dict(right)
            }
        else:
            return tree

    # # Example usage
    # binary_tree = [1, "+", [5, "+", [6, "*", 8]]]
    result = binary_tree_to_dict(result)
    print(result)

    if request.method == 'GET':
        return jsonify({
            "lexemes": str(tokens),
            "parse_tree": str(tree),
            "interpreter": str(result)
        })