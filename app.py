import os
from decouple import config

listAscii = ['Â', 'Ã¡', '�', 'Ã', 'Ã‰',
             'Ã', 'Ã­', 'Ã“', 'Ãš', 'Ãº', 'Ã‘', 'Ã±',
             'Â¡', 'Â¢', 'Â£', 'Â¤', 'Â¥', 'Â¦',
             'Â§', 'Â¨', 'Â©', 'Âª', 'Â«', 'Â¬', 'Â®',
             'Â¯', 'Â°', 'Â±', 'Â²', 'Â³', 'Â´', 'Âµ', 'Â¶',
             'Â·', 'Â¸', 'Â¹', 'Âº', 'Â»', 'Â¼', 'Â½', 'Â¾',
             'Â¿', 'Ã€', 'Ã‚', 'Ãƒ', 'Ã„', 'Ã…', 'Ã†',
             'Ã‡', 'Ãˆ', 'Ã‹', 'ÃŒ', 'ÃŽ',
             'Ã', 'Ã', 'Ã’', 'Ã”', 'Ã•', 'Ã–',
             'Ã—', 'Ã˜', 'Ã™', 'Ã›', 'Ãœ', 'Ã', 'Ãž',
             'ÃŸ', 'Ã', 'Ã¢', 'Ã£', 'Ã¤', 'Ã¥', 'Ã¦',
             'Ã§', 'Ã¨', 'Ã©', 'Ãª', 'Ã«', 'Ã¬', 'Ã®',
             'Ã¯', 'Ã°',  'Ã²', 'Ã³', 'Ã´', 'Ãµ', 'Ã¶',
             'Ã·', 'Ã¸', 'Ã¹', 'Ã»', 'Ã¼', 'Ã½', 'Ã¾', 'Ã¿']

routeProject = config('ROUTE_PROJECT')


def read_file(file, search):
    message = ''
    with open(file, 'r', encoding='UTF-8', errors="ignore") as file:
        for i, line in enumerate(file):
            if search in line:
                message = message + \
                    " \t\t\n - \"{}\" en la linea {}".format(search, i + 1)
    return message


def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        for f in files:
            file = '{}{}{}'.format(root, '/', f)
            for ascii in listAscii:
                existCodeAscii = read_file(file, ascii)
                if existCodeAscii != '':
                    separator = '-' * 100
                    print('\n{}'.format(separator))
                    print('\n{}:\t\t\n - {}'.format('RUTAS DE ARCHIVOS',
                          file.replace("\\", "/")))
                    print('\n{}:{}'.format('CARACTERES ENCONTRADOS', existCodeAscii))
    print('\n{}'.format(separator))


list_files(routeProject)
