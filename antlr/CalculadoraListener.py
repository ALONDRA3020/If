# Generated from Calculadora.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CalculadoraParser import CalculadoraParser
else:
    from CalculadoraParser import CalculadoraParser

# This class defines a complete listener for a parse tree produced by CalculadoraParser.
class CalculadoraListener(ParseTreeListener):

    # Enter a parse tree produced by CalculadoraParser#program.
    def enterProgram(self, ctx:CalculadoraParser.ProgramContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#program.
    def exitProgram(self, ctx:CalculadoraParser.ProgramContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#statement.
    def enterStatement(self, ctx:CalculadoraParser.StatementContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#statement.
    def exitStatement(self, ctx:CalculadoraParser.StatementContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#assign.
    def enterAssign(self, ctx:CalculadoraParser.AssignContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#assign.
    def exitAssign(self, ctx:CalculadoraParser.AssignContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#print.
    def enterPrint(self, ctx:CalculadoraParser.PrintContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#print.
    def exitPrint(self, ctx:CalculadoraParser.PrintContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#ifStatement.
    def enterIfStatement(self, ctx:CalculadoraParser.IfStatementContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#ifStatement.
    def exitIfStatement(self, ctx:CalculadoraParser.IfStatementContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#condition.
    def enterCondition(self, ctx:CalculadoraParser.ConditionContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#condition.
    def exitCondition(self, ctx:CalculadoraParser.ConditionContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#Variable.
    def enterVariable(self, ctx:CalculadoraParser.VariableContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#Variable.
    def exitVariable(self, ctx:CalculadoraParser.VariableContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#MulDiv.
    def enterMulDiv(self, ctx:CalculadoraParser.MulDivContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#MulDiv.
    def exitMulDiv(self, ctx:CalculadoraParser.MulDivContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#AddSub.
    def enterAddSub(self, ctx:CalculadoraParser.AddSubContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#AddSub.
    def exitAddSub(self, ctx:CalculadoraParser.AddSubContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#Parens.
    def enterParens(self, ctx:CalculadoraParser.ParensContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#Parens.
    def exitParens(self, ctx:CalculadoraParser.ParensContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#Int.
    def enterInt(self, ctx:CalculadoraParser.IntContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#Int.
    def exitInt(self, ctx:CalculadoraParser.IntContext):
        pass



del CalculadoraParser