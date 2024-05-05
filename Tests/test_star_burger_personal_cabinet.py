from locators import StarBurgerMain, StarBurgerLogin, StarBurgerRegistration, StarBurgerPersonalCabinet
from config import URL, USER_DATA, USER
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TestPersonalCabinet:

    def test_personal_cabinet_page(self, driver):
        driver.get(f'{URL}login')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerLogin.LOGIN_BUTTON))

        email = driver.find_element(*StarBurgerLogin.EMAIL_FIELD)
        email.send_keys(USER_DATA['email'])
        password = driver.find_element(*StarBurgerLogin.PASS_FIELD)
        password.send_keys(USER_DATA['password'])
        driver.find_element(*StarBurgerLogin.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerMain.INGRIDIENTS_SECTION))
        url = driver.current_url
        assert url == URL

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerMain.PERSONAL_CABINET_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerPersonalCabinet.ACCOUNT_TEXT))
        url = driver.current_url
        assert url == f'{URL}account/profile'


    def test_logout(self, driver):
        driver.get(f'{URL}login')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerLogin.LOGIN_BUTTON))

        email = driver.find_element(*StarBurgerLogin.EMAIL_FIELD)
        email.send_keys(USER_DATA['email'])
        password = driver.find_element(*StarBurgerLogin.PASS_FIELD)
        password.send_keys(USER_DATA['password'])
        driver.find_element(*StarBurgerLogin.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerMain.INGRIDIENTS_SECTION))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerMain.PERSONAL_CABINET_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerPersonalCabinet.ACCOUNT_TEXT))
        driver.find_element(*StarBurgerPersonalCabinet.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerLogin.LOGIN_BUTTON))
        url = driver.current_url
        assert url == f'{URL}login'


    def test_transition_to_constructor(self, driver):
        driver.get(f'{URL}login')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerLogin.LOGIN_BUTTON))

        email = driver.find_element(*StarBurgerLogin.EMAIL_FIELD)
        email.send_keys(USER_DATA['email'])
        password = driver.find_element(*StarBurgerLogin.PASS_FIELD)
        password.send_keys(USER_DATA['password'])
        driver.find_element(*StarBurgerLogin.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerMain.INGRIDIENTS_SECTION))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerMain.PERSONAL_CABINET_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerPersonalCabinet.ACCOUNT_TEXT))
        driver.find_element(*StarBurgerMain.CONSTRUCTOR).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerMain.INGRIDIENTS_SECTION))
        url = driver.current_url
        assert url == URL

    def test_transition_to_logo(self, driver):
        driver.get(f'{URL}login')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerLogin.LOGIN_BUTTON))

        email = driver.find_element(*StarBurgerLogin.EMAIL_FIELD)
        email.send_keys(USER_DATA['email'])
        password = driver.find_element(*StarBurgerLogin.PASS_FIELD)
        password.send_keys(USER_DATA['password'])
        driver.find_element(*StarBurgerLogin.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerMain.INGRIDIENTS_SECTION))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerMain.PERSONAL_CABINET_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerPersonalCabinet.ACCOUNT_TEXT))

        driver.find_element(*StarBurgerMain.LOGO).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerMain.INGRIDIENTS_SECTION))
        url = driver.current_url
        assert url == URL