''' Some public credential information and checks used in Python scripts.

By: WhiteBombo
'''

CLIENT_ID = 'qm7yhtp9i5h2785tjrkyh7a1lvsls3'

def check_id():
    ''' Checks whether a Client-ID exists and throws a tantrum if it doesn't. '''
    try:
        if CLIENT_ID == '':
            print('Missing Client-ID. A tantrum has been thrown.')
            exit()
    except NameError:
        print('Missing Client-ID. A tantrum has been thrown.')
        exit()
