import requests
import json
import pandas as pd
import random
import time

url = 'https://gql.tokopedia.com/graphql/SearchProductQueryV4'

header = {
    'origin': 'https://www.tokopedia.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
 }

cari = 'handphone'

def get_params() :
    params = []
    for i in range(1, 5):
        param = "device=desktop&navsource=&ob=23&page={}&q={}&related=true&rows=60&safe_search=false&scheme=https&shipping=&show_adult=false&source=search&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&st=product&start={}&topads_bucket=true&unique_id=802ea2b712dc54a209b139d7d9026c7a&user_addressId=&user_cityId=176&user_districtId=2274&user_id=&user_lat=&user_long=&user_postCode=&user_warehouseId=12210375&variants=&warehouses=12210375%232h%2C0%2315m".format(i, cari, (i - 1) * 60)
        params.append(param)

    return params

def scrape_data(param) :
    payload = [{
        "operationName": "SearchProductQueryV4",
        "variables" : {
            "params" : param
        },
        "query" : "query SearchProductQueryV4($params: String!) {\n  ace_search_product_v4(params: $params) {\n    header {\n      totalData\n      totalDataText\n      processTime\n      responseCode\n      errorMessage\n      additionalParams\n      keywordProcess\n      componentId\n      __typename\n    }\n    data {\n      banner {\n        position\n        text\n        imageUrl\n        url\n        componentId\n        trackingOption\n        __typename\n      }\n      backendFilters\n      isQuerySafe\n      ticker {\n        text\n        query\n        typeId\n        componentId\n        trackingOption\n        __typename\n      }\n      redirection {\n        redirectUrl\n        departmentId\n        __typename\n      }\n      related {\n        position\n        trackingOption\n        relatedKeyword\n        otherRelated {\n          keyword\n          url\n          product {\n            id\n            name\n            price\n            imageUrl\n            rating\n            countReview\n            url\n            priceStr\n            wishlist\n            shop {\n              city\n              isOfficial\n              isPowerBadge\n              __typename\n            }\n            ads {\n              adsId: id\n              productClickUrl\n              productWishlistUrl\n              shopClickUrl\n              productViewUrl\n              __typename\n            }\n            badges {\n              title\n              imageUrl\n              show\n              __typename\n            }\n            ratingAverage\n            labelGroups {\n              position\n              type\n              title\n              url\n              __typename\n            }\n            componentId\n            __typename\n          }\n          componentId\n          __typename\n        }\n        __typename\n      }\n      suggestion {\n        currentKeyword\n        suggestion\n        suggestionCount\n        instead\n        insteadCount\n        query\n        text\n        componentId\n        trackingOption\n        __typename\n      }\n      products {\n        id\n        name\n        ads {\n          adsId: id\n          productClickUrl\n          productWishlistUrl\n          productViewUrl\n          __typename\n        }\n        badges {\n          title\n          imageUrl\n          show\n          __typename\n        }\n        category: departmentId\n        categoryBreadcrumb\n        categoryId\n        categoryName\n        countReview\n        customVideoURL\n        discountPercentage\n        gaKey\n        imageUrl\n        labelGroups {\n          position\n          title\n          type\n          url\n          __typename\n        }\n        originalPrice\n        price\n        priceRange\n        rating\n        ratingAverage\n        shop {\n          shopId: id\n          name\n          url\n          city\n          isOfficial\n          isPowerBadge\n          __typename\n        }\n        url\n        wishlist\n        sourceEngine: source_engine\n        __typename\n      }\n      violation {\n        headerText\n        descriptionText\n        imageURL\n        ctaURL\n        ctaApplink\n        buttonText\n        buttonType\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
    }]

    req = requests.post(url, headers=header, json=payload).json()
    # LIHAT DI PREVIEW NETWORK UNTUK URUTAN JSON NYA
    rows = req[0]['data']['ace_search_product_v4']['data']['products']
    # print(len(rows))

    scrape_data = []
    for i  in range(0, len(rows)):
        no = i
        nama_product = rows[i]['name']
        harga = rows[i]['price']
        rating = rows[i]['ratingAverage']
        toko = rows[i]['shop']['name']
        lokasi = rows[i]['shop']['city']
        scrape_data.append(
            (toko, lokasi, nama_product, harga, rating)
        )

        # print(no, nama_product, harga, rating, toko, lokasi)
    return scrape_data


if __name__ == '__main__' :
    params = get_params()
    all_data = []
    for i in range(0, len(params)):
        # param = params[i]
        data = scrape_data(params[i])

        ## PAKAI INI KALAU ADA PROTEKSI SAAT AKSES API
        # time.sleep(random.randint(2, 9))

        all_data.extend(data)

    df = pd.DataFrame(all_data, columns=['Nama Toko', 'Lokasi', 'Nama Barang', 'Harga Barang', 'Rating Barang'])

    df.to_excel('data_handphone_tokped_api.xlsx', index=False)
    print('Data Berhasil Tersimpan')