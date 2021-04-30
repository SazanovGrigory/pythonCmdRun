def askQuestionYN(question):
    positive=['y','Y','д','Д','YES','ДА','yes','да','Yes','Да']
    negative=['n','N','н','Н','НЕТ','NO','нет','no','Нет','No']
    tries=5
    for i in range(tries):
        try:
            tmpstr=(input(question+' (Y/N) '))
        except KeyboardInterrupt:
            return (False)
        position=[number for number in positive if number == tmpstr]
        if position: 
            return (True)
        position=[number for number in negative if number == tmpstr]
        if position: 
            return (False)
        print('Неверный ввод. Попробуйте еще раз.')
        print('Использовано '+str(i+1)+' попыток из '+str(tries))
    print(f"{TColors.TerminalColors.WARNING}Ответ не был получен :-( возвращаем (NO) {TColors.TerminalColors.ENDC}")
    return (False)