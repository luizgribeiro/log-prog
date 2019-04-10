def find_open_close(expr):

    #get opening index
    open = expr.find('(')

    aux = 1 
    i = 0
    #get closing index
    for i in range(open+1, len(expr)):
        if expr[i] == '(':
            aux += 1
        elif expr[i] == ')':
            aux -= 1
        if aux == 0:
            return (open, i)


def sub_expr(expr, dict_expr):

    if expr.find('(') == -1:
        index = str(len(dict_expr))
        dict_expr[index] = expr
        return expr 
    else:
        open, close = find_open_close(expr)

        #chama com a parte de dentro
        sub_expr(expr[open+1:close], dict_expr)

        #coloca no dicionario
        sub_index = str(len(dict_expr) - 1)
        dict_expr[str(len(dict_expr))] = expr[:open] + sub_index + expr[close+1:]

        #chama com o restante da formula
        rest = expr[close+1:]
        if  rest != '':
            tolken_expr= dict_expr[str(len(dict_expr) -1)]
            sub_expr(tolken_expr , dict_expr)

        return dict_expr[str(len(dict_expr) -1)]
