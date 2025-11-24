from pages.login_page import LoginPage

def test_login_success(driver, base_url):
    driver.get(base_url)
    lp = LoginPage(driver)
    lp.login('standard_user', 'secret_sauce')
    assert 'inventory' in driver.current_url