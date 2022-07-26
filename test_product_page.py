import pytest

from .pages.product_page import ProductPage


def test_guest_see_add_to_cart_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_cart()
    page.solve_quiz_and_get_code()


@pytest.mark.parametrize('promo_offer', ["0","1", "3", "4", "5", pytest.param("7", marks=pytest.mark.xfail), "6", "8", "9"])
def test_product_info_is_the_same(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_cart()
    page.solve_quiz_and_get_code()
    page.product_info_should_be_the_same()






