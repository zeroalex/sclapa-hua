from pycep_correios import get_address_from_cep, WebService

cep = input()

address = get_address_from_cep(cep, webservice=WebService.APICEP)
print(address)
