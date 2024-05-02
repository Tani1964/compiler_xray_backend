from flask import Flask, request, jsonify, redirect, session
from flask_cors import CORS
from lexer import Lexer
from syntax_tree import Parser
from interpreter import Interpreter
from flask_session import Session

app = Flask(__name__)
app.secret_key = 'your_secret_key'
CORS(app, resources={r"/*": {"origins": "*"}})

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session["text"] = request.get_json().get('text')
        print(compiler(session["text"]))
        return {
            "lexemes": session["tokens"],
            "parse_tree": session["parse_tree"],
            "interpreter": session["result"]
        }

    if request.method == 'GET':
        if not session.get("text"):
            session["text"] = "2+3*9"
        return compiler(session["text"])
    
def compiler(text):
    tokenizer = Lexer(text)
    tokens = tokenizer.tokenize()
    session["tokens"] = str(tokens)
    
    parser = Parser(tokens)
    tree = parser.parse()
    print(tree)
    parse_tree = binary_tree_to_dict(tree)
    session["parse_tree"] = parse_tree
    
    interpreter = Interpreter(tree)
    result = interpreter.interpret()
    session["result"] = str(result)
    
    return {
            "lexemes": session["tokens"],
            "parse_tree": session["parse_tree"],
            "interpreter": session["result"]
        }

def binary_tree_to_dict(tree):
    if isinstance(tree, list):
        return {
            "left": binary_tree_to_dict(tree[0]),
            "operator": str(tree[1]),
            "right": binary_tree_to_dict(tree[2])
        }
    else:
        return str(tree)