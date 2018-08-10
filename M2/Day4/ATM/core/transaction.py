
from conf import settings
from core import accounts

def make_transaction(log_obj,acc_data,tran_type,amount,**others):
    if acc_data['status'] > 0:
        print("\033[31;1mAccount [%s] is frozen.\033[0m" %acc_data['id'])
        return
    amount = float(amount)
    if tran_type in settings.TRANSACTION_TYPE:
        interest = amount * settings.TRANSACTION_TYPE[tran_type]['interest']
        old_balance = acc_data['balance']
        if settings.TRANSACTION_TYPE[tran_type]['action'] == 'plus':
            new_balance = old_balance + amount + interest
        elif settings.TRANSACTION_TYPE[tran_type]['action'] == 'minus':
            new_balance = old_balance - amount - interest
            if new_balance < 0:
                print('''\033[31;1mYour credit [%s] is not enough for this transaction [-%s], your current balance is
                    [%s]''' %(acc_data['credit'],(amount + interest), old_balance ))
                return
        acc_data['balance'] = new_balance
        accounts.dump_account(acc_data)
        log_obj.info("account:%s   action:%s    amount:%s   interest:%s  current_balance:%s" %
                          (acc_data['id'], tran_type, amount,interest,acc_data['balance']))
        return acc_data
    else:
        print("\033[31;1mTransaction type [%s] is not exist!\033[0m" % tran_type)




