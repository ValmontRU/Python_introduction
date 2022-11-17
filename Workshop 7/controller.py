import logger
import model
import ui

def do_it():
    choice = ui.first_request()
    if choice == '1':
        a = ui.ask_fraction_num1()
        b = ui.ask_fraction_num2()
    else:
        a = ui.compl1()
        b = ui.compl2()
    operator = ui.ask_operation()
    result = model.calc(a, b, operator)
    print(result)
    logger.calc_logger(a, b, operator, result)