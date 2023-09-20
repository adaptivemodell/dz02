from selene.support.shared import browser
from selene import be, have


def test_siteopen(browser_open):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text("User-oriented Web UI browser tests in Python"))


def test_siteopen2(browser_open):
    browser.element('[name="q"]').should(be.blank).type('ergf43g3g43q3ggggg232').press_enter()
    browser.element('[class="mnr-c"]').should(have.text("По запросу ergf43g3g43q3ggggg232 ничего не найдено."))
    print('test_siteopen2')
