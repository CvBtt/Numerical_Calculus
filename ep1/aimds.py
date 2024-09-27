def arithmetic_arranger(problems, show_answers=False):
    #Usefull variables
    first_line = ''
    second_line = ''
    third_line = ''
    fourth_line = ''

    #Running exception cases

    if len(problems) > 5:
        return 'Error: Too many problems.'
    for operation in problems:
        if '*' in operation or '/' in operation:
            return "Error: Operator must be '+' or '-'."

        if operation.find('+') > 0:

            if not operation[:operation.find('+')].rstrip(' ').isnumeric() or not operation[operation.find('+'):].lstrip('+ ').isnumeric():
                return 'Error: Numbers must only contain digits.'

            if len(operation[:operation.find('+')].rstrip(' ')) > 4 or len(operation[operation.find('+'):].lstrip('+ ')) > 4:
                return "Error: Numbers cannot be more than four digits."

        else:
            if not operation[:operation.find('-')].rstrip(' ').isnumeric() or not operation[operation.find('-'):].lstrip('- ').isnumeric():
                return 'Error: Numbers must only contain digits.'

            if len(operation[:operation.find('-')].rstrip(' ')) > 4 or len(operation[operation.find('-'):].lstrip('- ')) > 4:
                return "Error: Numbers cannot be more than four digits."
                
    
    #Going over each element
    for element in problems:

        
        #Here I made a mistake,  I  can do it better, no repeating code
        operator_position_plus, operator_position_minus = element.find('+'), element.find('-')
        
        #The operation is a sum
        if operator_position_plus > 0:
            first_int = element[:operator_position_plus].rstrip(' ') #parte numérica do primeiro número
            second_int = element[operator_position_plus:].lstrip('+ ') #parte numérica do segundo númedo
            difference_len = len(first_int) - len(second_int)
            soma = str(int(first_int) + int(second_int))

            if difference_len > 0:
                first_line += '  ' + first_int + '    '
                second_line += '+ ' + difference_len * ' ' + second_int + '    '
                third_line += len('+ ' + len(first_int) * ' ') * '-' + '    '
                fourth_line += ((len('+ ' + len(first_int) * ' ')) - len(soma))*' '+ soma + '    '
            
            

            elif difference_len < 0:
                first_line += '  ' + abs(difference_len) * ' ' + first_int + '    '
                second_line += '+ ' + second_int + '    '
                third_line += len('  ' + len(second_int) * ' ') * '-' + '    '
                fourth_line += (len('  ' + len(second_int) * ' ') - len(soma)) * ' ' + soma + '    '
                

            else:
                first_line += '  ' + first_int + '    '
                second_line += '+ ' + second_int + '    '
                third_line += len('  ' + first_int) * '-' + '    '
                fourth_line += (len('  ' + first_int) -len(soma)) * ' '+ soma + '    '

        #The operation is a subtraction
        else:
            first_int = element[:operator_position_minus].rstrip(' ') #parte numérica primeiro número
            second_int = element[operator_position_minus:].lstrip('- ')  #parte numérica segundo númerp
            difference_len = len(first_int) - len(second_int)
            diff = str(int(first_int) - int(second_int))

            if difference_len > 0:
                first_line += '  ' + first_int + '    '
                second_line += '- ' + difference_len * ' ' + second_int + '    '
                third_line += len('- ' + len(first_int) * ' ') * '-' + '    '
                fourth_line += (len('- ' + len(first_int) * ' ') -len(diff))*' '+ diff + '    '

            elif difference_len < 0:
                first_line += '  ' + abs(difference_len) * ' ' + first_int + '    '
                second_line += '- ' + second_int + '    '
                third_line += len('  ' + len(second_int) * ' ') * '-' + '    '
                fourth_line += (len('  ' + len(second_int) * ' ') -len(diff)) * ' '+ diff + '    '

            else:
                first_line += '  ' + first_int + '    '
                second_line += '- ' + second_int + '    '
                third_line += len('  ' + first_int) * '-' + '    '
                fourth_line += ((len('  ' + first_int) * '-') -len(diff))*' '+ diff + '    '
            


    first_line_correct = first_line.rstrip(' ')
    second_line_correct = second_line.rstrip(' ')
    third_line_correct = third_line.lstrip(' ')
    fourth_line_correct = fourth_line.rstrip(' ')

    
    print(repr('  3801      123\n-    2    +  49\n------    -----'))

    if show_answers:
        return f'{first_line_correct}\n-{second_line_correct}\n-{third_line_correct}\n-{fourth_line_correct}'

    else:
        return f'{first_line_correct}\n{second_line_correct}\n{third_line_correct}'
    
    

print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')