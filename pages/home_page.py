from pages.common_operations import CommonOps
from selenium.webdriver.common.by import By

class HomePage(CommonOps):
    title_element = (By.CLASS_NAME, 'title')
    menu_button = (By.ID, 'react-burger-menu-btn')
    logout_button = (By.ID, 'logout_sidebar_link')
    reset_app_button = (By.ID, 'reset_sidebar_link')
    sort_button = (By.CLASS_NAME, 'select_container')
    low_to_high_option = (By.CSS_SELECTOR, 'option[value="lohi"]')
    inventory_list = (By.CLASS_NAME, 'inventory_list')
    cart_button = (By.CLASS_NAME, 'shopping_cart_link')

    def logout(self):
        self.wait_for(self.menu_button).click()
        self.get_element(self.logout_button).click()

    def navigate_to_cart(self):
        self.get_element(self.cart_button).click()
    def sort_low_to_high(self):
        self.wait_to_be_clickable(self.sort_button).click()
        self.get_element(self.low_to_high_option).click()

    def get_inventory_prices_list(self):
        inventory_items_price = (self.get_elements((By.CLASS_NAME, 'inventory_item_price')))
        inventory_price_list = []
        for i in inventory_items_price:
            # The follwing line will extract text from the web element,
            # remove the dollar sign and append a float decimal to the price list
            inventory_price_list.append(float((i.text)[1:]))
        return inventory_price_list
    
    def add_to_cart(self):
        inventory_list = (self.get_element((By.CLASS_NAME, 'inventory_list')))
        inventory_items = (inventory_list.find_elements(By.CLASS_NAME, 'inventory_item'))[:4]
        for i in inventory_items:
            add_to_cart_button = i.find_element(By.CLASS_NAME, 'btn')
            add_to_cart_button.click()

    def inventory_items_titles(self):
        inventory_list = (self.get_element((By.CLASS_NAME, 'inventory_list')))
        inventory_items = (inventory_list.find_elements(By.CLASS_NAME, 'inventory_item'))[:4]
        inventory_titles = []
        for i in inventory_items:
            item_name = (i.find_element(By.CLASS_NAME, 'inventory_item_name')).text
            inventory_titles.append(item_name)
        print(inventory_titles)
        return inventory_titles
    
    def cart_titles(self):
        self.navigate_to_cart()
        cart_list = (self.get_element((By.CLASS_NAME, 'cart_list')))
        cart_items = (cart_list.find_elements(By.CLASS_NAME, 'cart_item'))
        cart_titles = []
        for i in cart_items:
            item_name = (i.find_element(By.CLASS_NAME, 'inventory_item_name')).text
            cart_titles.append(item_name)
        return cart_titles
    
    # The parameter `button_id` below refers to the add to cart button id of the 
    # concerned item
    def add_specific_item_to_cart(self, button_id):
        self.wait_for((By.ID, button_id)).click()

    def complete_purchase(self):
        self.navigate_to_cart()
        self.wait_for((By.ID, 'checkout')).click()
        self.wait_for((By.ID, 'first-name')).send_keys('John')
        self.get_element((By.ID, 'last-name')).send_keys('Doe')
        self.get_element((By.ID, 'postal-code')).send_keys('99999')
        self.get_element((By.ID, 'continue')).click()
        self.wait_for((By.ID, 'finish')).click()