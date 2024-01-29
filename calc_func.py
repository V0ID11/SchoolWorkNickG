def calc(operations, operand1, operand2):
    operations = operations.upper()
    if operations == 'ADD':
        return operand1+operand2
    elif operations == "SUB":
        return operand1-operand2
    elif operations == "MUL":
        return operand1*operand2
    