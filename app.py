import os
from decouple import config

listAscii = ['Â','Ã³', 'Ã¡', '�']
routeProject = config('ROUTE_PROJECT')


def read_file(file, search):
    message = ''
    with open(file, 'r', encoding='UTF-8', errors="ignore") as file:
        for i, line in enumerate(file):
            if search in line:
                message = message + " \t\t\n - \"{}\" en la linea {}".format(search, i + 1)
    return message


def list_files(startpath):
    print(startpath)
    for root, dirs, files in os.walk(startpath):
        for f in files:
            file = '{}{}{}'.format(root, '/', f)
            for ascii in listAscii:
                existCodeAscii = read_file(file, ascii)
                if existCodeAscii != '':
                    separator = '-' * 100
                    print('\n{}'.format(separator))
                    print('\n{}:\t\t\n - {}'.format('RUTAS DE ARCHIVOS', file.replace("\\", "/")))
                    print('\n{}:{}'.format('CARACTERES ENCONTRADOS', existCodeAscii))
    print('\n{}'.format(separator))  

list_files(routeProject)
