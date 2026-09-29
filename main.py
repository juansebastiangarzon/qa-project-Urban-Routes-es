import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    order_taxi_button = (By.CSS_SELECTOR, 'button.button.round')
    comfort_tariff = (By.XPATH, "//div[contains(@class, 'tcard')][.//div[text()='Comfort']]")
    phone_button = (By.CLASS_NAME, 'np-button')
    phone_field = (By.ID, 'phone')
    confirm_phone_button = (By.XPATH, "//button[text()='Confirmar']")
    phone_code_field = (By.ID, 'code')
    phone_next_button = (By.XPATH, "//button[text()='Siguiente']")
    payment_method_button = (By.CLASS_NAME, 'pp-button')
    add_card_button = (By.CLASS_NAME, 'pp-plus-container')
    card_number_field = (By.ID, 'number')
    card_code_field = (By.CSS_SELECTOR, 'input.card-input[name="code"]')
    confirm_add_card_button = (By.XPATH, "//button[text()='Agregar']")
    close_card_modal_button = (By.CSS_SELECTOR, 'div.section.active button.close-button.section-close')
    message_field = (By.ID, 'comment')
    blanket_tissues_switch = (By.XPATH, "//div[contains(@class, 'r-type-switch')][.//div[text()='Manta y pañuelos']]//span[contains(@class, 'slider')]")
    ice_cream_plus = (By.XPATH, "//div[contains(@class, 'r-counter-container')][.//div[text()='Helado']]//div[contains(@class, 'counter-plus')]")
    ice_cream_counter = (By.XPATH, "//div[contains(@class, 'r-counter-container')][.//div[text()='Helado']]//div[contains(@class, 'counter-value')]")
    reserve_taxi_button = (By.CLASS_NAME, 'smart-button')
    search_car_title = (By.CLASS_NAME, 'order-header-title')
    driver_car_number = (By.CLASS_NAME, 'number')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # Llenando "Desde"
    def set_from(self, from_address):
        element = self.wait.until(expected_conditions.visibility_of_element_located(self.from_field))
        element.send_keys(from_address)

    # Llenando "Hasta"
    def set_to(self, to_address):
        element = self.wait.until(expected_conditions.visibility_of_element_located(self.to_field))
        element.send_keys(to_address)

    # Verficamos campos
    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    # Juntamos en un paso las acciones ya creadas, escribir dirección origen y la dirección de destino
    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    #Damos primero el click en el botón "pedir taxi"
    def click_order_taxi(self):
        element = self.wait.until(expected_conditions.element_to_be_clickable(self.order_taxi_button))
        element.click()

    #Damos click en el segundo botón confort
    def select_comfort(self):
        self.driver.find_element(*self.comfort_tariff).click()

    # Damos click en el botón "Aregar número"
    def click_phone_button(self):
        element = self.wait.until(expected_conditions.element_to_be_clickable(self.phone_button))
        element.click()

    # Rellenamos el número de teléfono
    def set_phone(self, phone):
        element = self.wait.until(expected_conditions.visibility_of_element_located(self.phone_field))
        element.send_keys(phone)

    # Damos click en el botón siguiente
    def click_phone_next(self):
        element = self.wait.until(expected_conditions.element_to_be_clickable(self.phone_next_button))
        element.click()

    # Código del SMS
    def set_phone_code(self):
        code = retrieve_phone_code(self.driver)
        element = self.wait.until(expected_conditions.visibility_of_element_located(self.phone_code_field))
        element.send_keys(code)

    # Damos click al botón de confirmación del código SMS
    def confirm_phone(self):
        element = self.wait.until(expected_conditions.element_to_be_clickable(self.confirm_phone_button))
        element.click()

    # Damos click al botón metodo de pago
    def click_payment_method(self):
        element = self.wait.until(expected_conditions.element_to_be_clickable(self.payment_method_button))
        element.click()

    # Damos click al botón agregar tarjeta de la ventana modal
    def click_add_card(self):
        element = self.wait.until(expected_conditions.element_to_be_clickable(self.add_card_button))
        element.click()

    # Llenamos número de tarjeta
    def set_card_number(self, card_number):
        element = self.wait.until(expected_conditions.visibility_of_element_located(self.card_number_field))
        element.send_keys(card_number)

    # Llenamos número de cvc
    def set_card_code(self, card_code):
        element = self.wait.until(expected_conditions.visibility_of_element_located(self.card_code_field))
        element.send_keys(card_code)
        element.send_keys(Keys.TAB)

    # Damos click al botón "Agregar" de la ventana modal "Agregar tarjeta"
    def click_confirm_add_card(self):
        element = self.wait.until(expected_conditions.element_to_be_clickable(self.confirm_add_card_button))
        element.click()

    # Damos click al botón "X" en la ventana con la lista de las tarjetas guardadas
    def close_card_modal(self):
        buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button.close-button.section-close')

        for button in buttons:
            if button.is_displayed():
                button.click()
                break

    # Mensaje al conductor o "Controlador XD"
    def set_message(self, message):
        element = self.wait.until(expected_conditions.visibility_of_element_located(self.message_field))
        element.send_keys(message)

    # Agregar manta y pañuelos
    def select_blanket_tissues(self):
        element = self.wait.until(expected_conditions.element_to_be_clickable(self.blanket_tissues_switch))
        element.click()

    # Agregar dos helados
    def add_ice_cream(self):
        element = self.wait.until(expected_conditions.element_to_be_clickable(self.ice_cream_plus))
        element.click()

    # Comprobamos si el metodo es dos helados porque todo pasa muy rapido auxilio
    def get_ice_cream_count(self):
        element = self.wait.until(expected_conditions.visibility_of_element_located(self.ice_cream_counter))
        return element.text

    # Damos click al botón de reservar taxi
    def click_reserve_taxi(self):
        element = self.wait.until(expected_conditions.element_to_be_clickable(self.reserve_taxi_button))
        element.click()

    # Comprobamos que si abra la modal de "Buscar..."
    def get_search_car_title(self):
        element = self.wait.until(expected_conditions.visibility_of_element_located(self.search_car_title))
        return element.text

    # Esperando para que el elemento cambie
    def get_driver_car_number(self):
        wait = WebDriverWait(self.driver, 45)
        element = wait.until(expected_conditions.visibility_of_element_located(self.driver_car_number))
        return element.text

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono

        # necesitamos los registros de Chrome para recuperar el código de confirmación del teléfono
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        cls.driver = webdriver.Chrome(options=options)
        # necesitamos los registros de Chrome para recuperar el código de confirmación del teléfono

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

        routes_page.click_order_taxi()
        routes_page.select_comfort()

        routes_page.click_phone_button()
        routes_page.set_phone(data.phone_number)
        routes_page.click_phone_next()
        routes_page.set_phone_code()
        routes_page.confirm_phone()

        routes_page.click_payment_method()
        routes_page.click_add_card()

        routes_page.set_card_number(data.card_number)
        routes_page.set_card_code(data.card_code)

        routes_page.click_confirm_add_card()
        routes_page.close_card_modal()

        routes_page.set_message(data.message_for_driver)
        routes_page.select_blanket_tissues()

        routes_page.add_ice_cream()
        routes_page.add_ice_cream()

        assert routes_page.get_ice_cream_count() == '2'

        routes_page.click_reserve_taxi()

        assert routes_page.get_search_car_title() == 'Buscar automóvil'

        assert routes_page.get_driver_car_number() != ''

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
