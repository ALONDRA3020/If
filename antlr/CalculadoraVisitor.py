# Generated from Calculadora.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CalculadoraParser import CalculadoraParser
else:
    from CalculadoraParser import CalculadoraParser

# This class defines a complete generic visitor for a parse tree produced by CalculadoraParser.

class CalculadoraVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalculadoraParser#program.
    def visitProgram(self, ctx:CalculadoraParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#statement.
    def visitStatement(self, ctx:CalculadoraParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#assign.
    def visitAssign(self, ctx:CalculadoraParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#print.
    def visitPrint(self, ctx:CalculadoraParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#ifStatement.
    def visitIfStatement(self, ctx:CalculadoraParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#condition.
    def visitCondition(self, ctx:CalculadoraParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#Variable.
    def visitVariable(self, ctx:CalculadoraParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#MulDiv.
    def visitMulDiv(self, ctx:CalculadoraParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#AddSub.
    def visitAddSub(self, ctx:CalculadoraParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#Parens.
    def visitParens(self, ctx:CalculadoraParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#Int.
    def visitInt(self, ctx:CalculadoraParser.IntContext):
        return self.visitChildren(ctx)



del CalculadoraParser