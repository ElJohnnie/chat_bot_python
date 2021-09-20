from selenium import webdriver
#pip install selenium
#arquivo webdrive foi baixado de acordo com a versão do navegador
import time
#pip install times
from selenium.webdriver.common.keys import Keys
#pip install key



#bibliotecas que foram instaladas acima
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
time.sleep(10)
#concatenar com webwhatsapp

#função do bot
def bot():
    try:
        lBall = driver.find_element_by_class_name('_23LrM')
        lBall = driver.find_elements_by_class_name('_23LrM')
        lball_click = lBall[-1]
        action_ball = webdriver.common.action_chains.ActionChains(driver)
        action_ball.move_to_element_with_offset(lball_click, 0, -20)
        action_ball.click()
        action_ball.perform()
        action_ball.click()
        action_ball.perform()
        contact = driver.find_element_by_xpath('//*[@id="main"]/header/div[2]/div/div/span')
        contact_ok = contact.text
        print(contact_ok)
        # clicando exatamente em cima da mensagem nova e absorvendo o contato
        all_messages = driver.find_elements_by_class_name('_1Gy50')
        all_messages_text = [e.text for e in all_messages]
        message = all_messages_text[-1]
        print(message)
        #respondendo a mensagem
        textfield = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]')
        textfield.click()
        time.sleep(3)
        textfield.send_keys('No momento estou testando um chatbot, não poderei responder mensagens. Retorne daqui algumas horas.', Keys.ENTER)
        #voltar para o fixado obrigatório
        #_1pJ9J _2XH9R classes
        fixed_ico = driver.find_element_by_class_name('_1pJ9J')
        fixed_action = webdriver.common.action_chains.ActionChains(driver)
        fixed_action.move_to_element_with_offset(fixed_ico, 0, -20)
        fixed_action.click()
        fixed_action.perform()
        fixed_action.click()
        fixed_action.perform()
    except:
        print('Buscando novas mensagens')
        time.sleep(3)
while True:
    bot()


