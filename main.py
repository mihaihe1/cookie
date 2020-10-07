from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('https://orteil.dashnet.org/cookieclicker/')

driver.implicitly_wait(5)

cookie = driver.find_element_by_id('bigCookie')
cookie_count = driver.find_element_by_id('cookies')
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1,-1,-1)]

actions = ActionChains(driver)
actions.click(cookie)



for i in range(5000):
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
    cps = float(cookie_count.text.split(" ")[4])
    best = 1
    cnt = 1
    ok = False
    for item in items:
        #print(item.text)
        if item.text != '':
            aux = item.text.split(',')
            if len(aux) > 1:
                num = str(aux[0]) + str(aux[1])
            else:
                num = str(aux[0])

            if num != '':
                value = int(num)
                #print(value)
                if cps < 0.5 and cnt == 2:
                    #print(str(best) + "a")
                    bestItem = item
                    price = value
                elif cnt == 1 and cps >= 0.5:
                    bestItem = item
                    price = value

        cnt += 1
    if count >= price:
        upgrade_actions = ActionChains(driver)
        upgrade_actions.move_to_element(bestItem)
        upgrade_actions.click()
        upgrade_actions.perform()
