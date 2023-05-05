# web_features_automation
## Test automation of web features found at "https://the-internet.herokuapp.com"
### To run this project locally, follow these steps:
 * Make sure these are installed to your computer:
   * Python
   * Git
 * In your terminal, run:
   > git clone https://github.com/nbcraig/web_features_automation/
 * Open your project folder in the terminal make sure you activate the virtual environment(optional) and run:
   > pip install -r requirements.txt
 * Finally, run this command:
   > pytest
  
### Features:
  * Tests are wrote in Python with the Selenium and Pytest libraries
  * A HTML report with is made each time tests are ran
  * Covered tests cases:
    1. Login with a valid user.
    Expected: Validate the user navigates to the products page when logged in.
    
    2. Login with an invalid user.
    Expected: Validate error message is displayed.
    
    3. Logout from the home page.
    Expected: Validate the user navigates to the login page.
    
    4. Sort products by Price (low to high).
    Expected: Validate the products have been sorted by price correctly
    
    5. Add multiple items to the shopping cart.
    Expected: Validate all the items that have been added to the shopping cart.
    
    6. Add the specific product ‘Sauce Labs Onesie’ to the shopping cart.
    Expected: Validate the correct product was added to the cart.
    
    7. Complete a purchase.
    Expected: Validate the user navigates to the order confirmation page.