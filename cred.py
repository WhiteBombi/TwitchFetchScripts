# Some public credential information and checks used in Python scripts.
# By: WhiteBombo

client_id = 'qm7yhtp9i5h2785tjrkyh7a1lvsls3'

def checkId():
    try:
        if client_id == '':
            print('Missing client_id')
            exit()
    except(NameError):
        print('Missing client_id')
        exit()
