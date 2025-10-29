from django.shortcuts import render
def index(request):
    result = ""
    if request.method == "POST":
        code = request.POST.get("code", "")
        try:
            from antlr4 import InputStream, CommonTokenStream
            from antlr.CalculadoraLexer import CalculadoraLexer
            from antlr.CalculadoraParser import CalculadoraParser
            from antlr.EvalVisitor import EvalVisitor

            input_stream = InputStream(code)
            lexer = CalculadoraLexer(input_stream)
            tokens = CommonTokenStream(lexer)
            parser = CalculadoraParser(tokens)
            tree = parser.program()

            visitor = EvalVisitor()
            visitor.visit(tree)
            result = visitor.memory
        except Exception as e:
            result = f"Error: {e}"

    return render(request, "index.html", {"result": result})