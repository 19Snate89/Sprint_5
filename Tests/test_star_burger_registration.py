from locators import StarBurgerRegistration, StarBurgerLogin
from config import URL, registration_data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegBurger:

    def test_registration_page(self, driver):
        driver.get(f'{URL}register')
        name_title = driver.find_element(*StarBurgerRegistration.REG_TITLE)
        assert name_title.text == 'Регистрация', f'Неверный заголовок формы регистрации: {name_title.text}'

    def test_registration_positive_result(self, driver):
        driver.get(f'{URL}register')
        name_data, email_data, password_data = registration_data()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerRegistration.REG_BUTTON))
        name = driver.find_element(*StarBurgerRegistration.NAME_FIELD)
        name.send_keys(name_data)

        email = driver.find_element(*StarBurgerRegistration.EMAIL_FIELD)
        email.send_keys(email_data)

        password = driver.find_element(*StarBurgerRegistration.PASS_FIELD)
        password.send_keys(password_data)

        driver.find_element(*StarBurgerRegistration.REG_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerLogin.LOGIN_BUTTON))
        url = driver.current_url
        assert url == f'{URL}login'

    def test_registration_with_wrong_password(self, driver):
        driver.get(f'{URL}register')
        name_data, email_data, password_data = registration_data()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerRegistration.REG_BUTTON))
        name = driver.find_element(*StarBurgerRegistration.NAME_FIELD)
        name.send_keys(name_data)

        email = driver.find_element(*StarBurgerRegistration.EMAIL_FIELD)
        email.send_keys(email_data)

        password = driver.find_element(*StarBurgerRegistration.PASS_FIELD)
        password.send_keys('12345')

        driver.find_element(*StarBurgerRegistration.REG_BUTTON).click()

        error_text = driver.find_element(*StarBurgerRegistration.ERROR_TEXT)
        assert error_text





