def operate(operation, *args):
    def add(*args):
        return sum(args)

    def subtract(*args):
        return sum(-x for x in args)

    def multiply(*args):
        result = 1
        for x in args:
            result *= x
        return result

    def divide(*args):
        result = 1
        for x in args:
            result /= x
        return result

    if operation == '+':
        return add(*args)
    elif operation == '-':
        return subtract(*args)
    elif operation == '*':
        return multiply(*args)
    elif operation == "/":
        return divide(*args)
    else:
        return 'Wrong operator'



print(operate(".", 3, 4))
