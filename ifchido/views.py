from django.shortcuts import render
from antlr4 import *
from antlr.CalculadoraLexer import CalculadoraLexer
from antlr.CalculadoraParser import CalculadoraParser
from antlr.EvalVisitor import EvalVisitor

def index(request):
    result = None
    if request.method == "POST":
        code = request.POST.get("code", "")
        try:
            input_stream = InputStream(code)
            lexer = CalculadoraLexer(input_stream)
            token_stream = CommonTokenStream(lexer)
            parser = CalculadoraParser(token_stream)
            tree = parser.program()

            evaluator = EvalVisitor()
            evaluator.visit(tree)
            result = evaluator.memory
        except Exception as e:
            result = f"Error: {e}"
    return render(request, "index.html", {"result": result})