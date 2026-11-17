import re

from playwright.sync_api import Page, expect

URL = "https://local-eats-unisenac.vercel.app/"
EMAIL = "teste2@gmail.com"
SENHA = "abc"


# Responsável: Luis
def test_login_com_credenciais_validas(page: Page):
    page.goto(URL)

    page.get_by_placeholder("teste@teste.com").fill(EMAIL)
    page.get_by_placeholder("Sua senha secreta").fill(SENHA)
    page.get_by_role("button", name="Entrar").last.click()

    expect(page).to_have_url(re.compile(r"index\.html"))
    expect(
    page.get_by_role("heading", name="Descubra sabores incríveis na sua cidade")).to_be_visible()