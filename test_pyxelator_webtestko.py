from playwright.sync_api import sync_playwright
from pyxelator import find, click, fill 
import pytest
import cred
import time

def test_pyxelator_ft_test_ko():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://test.kelasotomesyen.com")
        # page.wait_for_selector("//h2[contains(text(),'Semua Produk')]").is_visible()
        # assert page.title() == "Kelas Otomesyen Test App"

        fill(page, 'ss/email.png', cred.EMAIL)
        fill(page, 'ss/password.png', cred.PASSWORD)
        click(page,'ss/masuk.png')
        # assert page.url == "https://test.kelasotomesyen.com/products"

        time.sleep(5)
        click(page, 'ss/tambah_produk.png')
        fill(page, 'ss/nama_produk.png', 'anak emas')
        fill(page, 'ss/harga.png', '70000')
        fill(page, 'ss/stok.png', '17')
        page.locator("//select[@id='category']*//option[@value='Home']").click()
        # page.get_by_test_id("product-category-input").select_option("Home")
        fill(page, 'ss/deskripsi_produk.png', 'anak emas yang nanti klo udah gede bisa jadi biang emas')
        # click(page, 'ss/submit_produk.png')

        time.sleep(10)
        browser.close()