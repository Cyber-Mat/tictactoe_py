'''
A short program to automatically add bullets to copied lists
(e.g from wikipaedia) and then returns the
bulleted list to the clipboard
'''
import pyperclip


def get_list():
    '''
    Function to get list from clipboard
    '''
    text = pyperclip.paste()
    my_list = text.split('\n')
    return my_list


def bullet_list():
    '''
    Function to add bullets to list
    '''
    my_list = get_list()
    new_list = []

    for item in my_list:
        if item == '':
            continue
        new_list.append('* ' + item)
    return new_list


def return_list():
    '''
    Function to return list to clipboard
    '''
    new_list = bullet_list()
    pyperclip.copy('\n'.join(new_list))
    print('List bulleted')


if __name__ == '__main__':
    return_list()
