class NIF():
    def __init__(self, DNI, letra = None):
        self.DNI = DNI
        self.letra = letra

    def get_letra(self):
        dic_letra = {'0':'T', '1':'R', '2':'W', '3':'A', '4':'G', '5':'M', '6':'Y', '7':'F', '8':'P', '9':'D', '10':'X', '11':'B', '12':'N', '13':'J', '14':'Z', '15':'S', '16':'Q', '17':'V', '18':'H', '19':'L', '20':'C', '21':'K', '22':'E'}

        resto = str(self.DNI%23)
        letra = dic_letra[resto]
        return letra


numero = NIF(04865577)
print(numero.get_letra())
