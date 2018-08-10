import json
import os
from conf import settings

def dump_account(acc_data):
    account_file = '%s/db/accounts/%s.json' % (settings.BASE_DIR, acc_data['id'])
    with open(account_file,'w') as f:
        json.dump(acc_data,f)

def load_account(id):
    account_file = '%s/db/accounts/%s.json' % (settings.BASE_DIR, id)
    if os.path.isfile(account_file):
        with open(account_file, 'r') as f:
            acc_data = json.load(f)
        return acc_data
    else:
        print("\033[31;1mAccount [%s] does not exist!\033[0m" %id)