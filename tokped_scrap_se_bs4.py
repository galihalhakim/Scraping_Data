import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://www.tokopedia.com/search?st=&q=rtx%204090&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&navsource='

# Menghilangkan tampilan Chromium
options = Options()
options.add_argument('--headless=new')
driver = webdriver.Chrome(options=options)

# # Menampilkan Chromium
# driver = webdriver.Chrome()

driver.get(url)

data = []
# LOOPING JUMLAH PAGE YANG MAU DI SCRAP
for i in range(2):
    # UNTUK AKALIN PAGINATION NYA TOKPED, SCROLL OTOMATIS KE BAWAH
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#zeus-root")))
    time.sleep(2)

    #  LOOPING SCROLL KE BAWAH SEBANYAK RANGE
    for j in range(20):
        # FUNGSI UNTUK SCROLL KEBAWAH
        driver.execute_script("window.scrollBy(0, 250)")
        time.sleep(1)

    # FUNGSI UNTUK SCROLL KEKANAN UNTUK TRIGGER PAGE
    driver.execute_script("window.scrollBy(50, 0)")
    time.sleep(1)

    soup = BeautifulSoup(driver.page_source, "html.parser")

    for item in soup.findAll('div', class_ = 'css-974ipl'):
        nama_product = item.find('div', class_ = 'css-3um8ox').text
        harga = item.find('div', class_ = 'css-1ksb19c').text
        
        rtg = item.findAll('span', class_ = 'css-t70v7i')
        if len(rtg) > 0:
            rating = item.find('span', class_ = 'css-t70v7i').text
        else:
            rating = ''

        tjl = item.findAll('span', class_ = 'css-1duhs3e')
        if len(rtg) > 0:
            terjual = item.find('span', class_ = 'css-1duhs3e').text
        else:
            terjual = ''

        for item2 in item.findAll('div', class_ = 'css-1rn0irl'):
            lokasi = item2.findAll('span', class_ = 'css-1kdc32b')[0].text
            toko = item2.findAll('span', class_ = 'css-1kdc32b')[1].text

            data.append(
                (toko, lokasi, nama_product, harga, terjual, rating)
            )

    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "button[aria-label='Laman berikutnya']").click()
    time.sleep(3)


df = pd.DataFrame(data, columns=['Toko', 'Lokasi', 'Nama Product', 'Harga', 'Terjual', 'Rating'])
print(df)

df.to_excel('Data_Tokped_RTX4090_BS4.xlsx', index=False)
print('Data Telah Disimpan')

driver.close()