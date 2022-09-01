#	CPI.py

#	~ Enzo Zavorski Delevatti
#	Aug 2022

''' UNIVALI – Arquitetura e Organização de Computadores II
    Prof. Douglas Rossi de Melo
    Avaliação 01 – Desempenho                               '''

import os


def checkFile(path: str):
    try:
        open(path, 'rb')
        return True
    except FileNotFoundError:
        return False
    except IsADirectoryError:
        return False

class CPI:
    def __init__(self, filepath = ''):
        if(filepath):
            self.filepath = filepath
        else:
            self.filepath = filepath = input('Insira o arquivo que deseja abrir\n« ')
        
        try:
            with open(filepath, 'rb') as self.file:
                print('Arquivo carregado.\n')
                
        except FileNotFoundError:
            input('Arquivo não encontrado!\n')
            self.__init__()