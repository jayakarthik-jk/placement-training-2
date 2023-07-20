while True:
    tokens = []
    expression = input("Enter the expreession: ")
    i = 0
    # tokenization
    while i < len(expression):
        if expression[i].isdigit():
            start = i
            while i < len(expression) and expression[i].isdigit():
                i += 1
            number = int(expression[start:i])
            tokens.append(number)
            continue
        match expression[i]:
            case ' ':
                i += 1
                continue
            case '+':
                tokens.append('+')
            case '-':
                tokens.append('-')
            case '*':
                tokens.append('*')
            case '/':
                tokens.append('/')
            case '%':
                tokens.append('%')
            case token:
                print(f"Invalid input {token}")
                break
        i += 1
    
    # evaluation
    while len(tokens) > 1:
        num2 = tokens.pop()
        operator = tokens.pop()
        num1 = tokens.pop()
        match operator:
            case '+': tokens.append(num1 + num2)
            case '-': tokens.append(num1 - num2)
            case '*': tokens.append(num1 * num2)
            case '/': tokens.append(num1 / num2)
            case '%': tokens.append(num1 % num2)
    if len(tokens) >= 1:
        print(f"{tokens[0]}")
        