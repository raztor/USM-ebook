from time import sleep

from webbot import Browser

web = Browser()
web.go_to('https://bibliotecadigital.usm.cl/')
sleep(2)
web.click(' Rechazar cookies ')
web.click('IDENTIFICARSE')
sleep(5)
web.type('*******.******@usm.cl' , into='Email')
sleep(1)
web.click('Siguiente' , tag='span')
sleep(2)
web.type('**************' , into='Password' , id='i0118')
sleep(1)
web.click('Iniciar sesión' , tag='span') # you are logged in . woohoooo
web.find_elements(text="Quiere mantener la sesión iniciada")
if web.exists('Quiere mantener la sesión iniciada'):
    print('Loged in')
    web.click('No')
web.go_to('https://bibliotecadigital.usm.cl/info/algorithms-in-c-parts-1-4-fundamentals-data-structure-sorting-searching-00640961')
sleep(4)
web.find_elements(text="Prestar")
if web.exists('Prestar'):
    print('Found')
    web.click('PRESTAR')
    sleep(4)
web.find_elements(text="Leer")
web.click("Leer")
sleep(10)
web.find_elements(id="pageNumber_copy")
web.type("1", id="pageNumber_copy")
sleep(0.5)