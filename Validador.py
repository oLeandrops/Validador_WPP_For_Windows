from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from funcoesBD import consulta,update, updateParaConsulta


options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
browser = Chrome(r'C:/Users/leandro.silva/DRIVERS/chromedriver.exe',options=options)
browser.implicitly_wait(1)
urlprincipal = 'https://web.whatsapp.com/'
browser.get(urlprincipal)
resposta = input('Você já escaneou o QRCODE?')
ddi= 55
while resposta == 'SIM':
    telefone = consulta()
    updateParaConsulta(telefone)
    url = f'https://web.whatsapp.com/send?phone={ddi}{telefone}&text='
    browser.get(url)
    carregando = browser.find_elements(By.CSS_SELECTOR,'div[class="QgIWN"]')
    while len(carregando) <=0:
        carregando = browser.find_elements(By.CSS_SELECTOR,'div[class="QgIWN"]')
        carregando = browser.find_elements(By.CSS_SELECTOR,'div[class="QgIWN"]')
    while len(carregando) >0:
        carregando = browser.find_elements(By.CSS_SELECTOR,'div[class="QgIWN"]')
        #whats lento para iniciar conversar --TRATAMENTO
    carregando_conversa = browser.find_elements(By.CSS_SELECTOR,'div[data-testid="popup-title"]')
    while len(carregando_conversa) >0:
        carregando_conversa = browser.find_elements(By.CSS_SELECTOR,'div[data-testid="popup-title"]')
    if len(browser.find_elements(By.CSS_SELECTOR,'div[title="Mensagem"]')) > 0:
        #whats lento para carregando tela de msg --TRATAMENTO
        carregando_mensagem = browser.find_elements(By.CSS_SELECTOR,'div[title="Carregando mensagens..."]')
        while len(carregando_mensagem) >0:
            carregando_mensagem = browser.find_elements(By.CSS_SELECTOR,'div[title="Carregando mensagens..."]')
        update(telefone,status='VALIDO')
        #PROCESSO DE APAGAR CONVERSA
        if len(browser.find_elements(By.CSS_SELECTOR, '#main')) > 0:
            menu = browser.find_element(By.CSS_SELECTOR, '#main')
            menu.find_element(By.CSS_SELECTOR, 'div[data-testid="conversation-menu-button"] ').click()
            sleep(0.5)
            browser.find_elements(By.CSS_SELECTOR, 'li')[-3].click()
            sleep(0.5)
            if browser.find_elements(By.CSS_SELECTOR, 'div[class*="_2Zdgs"]'):
                browser.find_element(By.CSS_SELECTOR, 'div[class*="_2Zdgs"]').click()
            elif browser.find_elements(By.CSS_SELECTOR,'div[class*="tvf2evcx"]'):
                browser.find_element(By.CSS_SELECTOR,'div[class*="tvf2evcx"] div[data-testid*="ok"').click()
            elif browser.find_elements(By.CSS_SELECTOR,'div[class*="p357zi0d"]'):
                browser.find_element(By.CSS_SELECTOR,'div[class*="p357zi0d"]').click()
            else:
                print('não encontrei nenhum elemento')
            sleep(0.5)
            if len(browser.find_elements(By.CSS_SELECTOR, 'div[class*="_2Zdgs"]')) >0:
                browser.find_element(By.CSS_SELECTOR, 'div[class*="_2Zdgs"]').click()
    elif len(browser.find_elements(By.CSS_SELECTOR, 'div[data-animate-modal-popup="true"]')) > 0:
        update(telefone,'INVALIDO')
