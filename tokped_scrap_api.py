import requests
import pandas as pd

url_target = 'https://gql.tokopedia.com/graphql/SearchProductQueryV4'

header = {
    'sec-ch-ua': 'Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'Tkpd-UserId': '3905748',
    'X-Version': 'bdbd9a3',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'content-type': 'application/json',
    'accept': '*/*',
    'Referer': 'https://www.tokopedia.com/search?navsource=&page=2&q=handphone&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&st=',
    'X-Source': 'tokopedia-lite',
    'x-device': 'desktop-0.0',
    'X-Tkpd-Lite-Service': 'zeus',
    'sec-ch-ua-platform': '"Windows"'
 }

# query = f'[{{"operationName":"SearchProductQueryV4","variables":{{"params":"device=desktop&navsource=&ob=23&page=1&q=handphone&related=true&rows=60&safe_search=false&scheme=https&shipping=&show_adult=false&source=search&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&st=product&start=0&topads_bucket=true&unique_id=802ea2b712dc54a209b139d7d9026c7a&user_addressId=&user_cityId=176&user_districtId=2274&user_id=&user_lat=&user_long=&user_postCode=&user_warehouseId=12210375&variants=&warehouses=12210375%232h%2C0%2315m"}},"query":"query SearchProductQueryV4($params: String\u0021) {{\\n  ace_search_product_v4(params: $params) {{\\n    header {{\\n      totalData\\n      totalDataText\\n      processTime\\n      responseCode\\n      errorMessage\\n      additionalParams\\n      keywordProcess\\n      componentId\\n      __typename\\n    }}\\n    data {{\\n      banner {{\\n        position\\n        text\\n        imageUrl\\n        url\\n        componentId\\n        trackingOption\\n        __typename\\n      }}\\n      backendFilters\\n      isQuerySafe\\n      ticker {{\\n        text\\n        query\\n        typeId\\n        componentId\\n        trackingOption\\n        __typename\\n      }}\\n      redirection {{\\n        redirectUrl\\n        departmentId\\n        __typename\\n      }}\\n      related {{\\n        position\\n        trackingOption\\n        relatedKeyword\\n        otherRelated {{\\n          keyword\\n          url\\n          product {{\\n            id\\n            name\\n            price\\n            imageUrl\\n            rating\\n            countReview\\n            url\\n            priceStr\\n            wishlist\\n            shop {{\\n              city\\n              isOfficial\\n              isPowerBadge\\n              __typename\\n            }}\\n            ads {{\\n              adsId: id\\n              productClickUrl\\n              productWishlistUrl\\n              shopClickUrl\\n              productViewUrl\\n              __typename\\n            }}\\n            badges {{\\n              title\\n              imageUrl\\n              show\\n              __typename\\n            }}\\n            ratingAverage\\n            labelGroups {{\\n              position\\n              type\\n              title\\n              url\\n              __typename\\n            }}\\n            componentId\\n            __typename\\n          }}\\n          componentId\\n          __typename\\n        }}\\n        __typename\\n      }}\\n      suggestion {{\\n        currentKeyword\\n        suggestion\\n        suggestionCount\\n        instead\\n        insteadCount\\n        query\\n        text\\n        componentId\\n        trackingOption\\n        __typename\\n      }}\\n      products {{\\n        id\\n        name\\n        ads {{\\n          adsId: id\\n          productClickUrl\\n          productWishlistUrl\\n          productViewUrl\\n          __typename\\n        }}\\n        badges {{\\n          title\\n          imageUrl\\n          show\\n          __typename\\n        }}\\n        category: departmentId\\n        categoryBreadcrumb\\n        categoryId\\n        categoryName\\n        countReview\\n        customVideoURL\\n        discountPercentage\\n        gaKey\\n        imageUrl\\n        labelGroups {{\\n          position\\n          title\\n          type\\n          url\\n          __typename\\n        }}\\n        originalPrice\\n        price\\n        priceRange\\n        rating\\n        ratingAverage\\n        shop {{\\n          shopId: id\\n          name\\n          url\\n          city\\n          isOfficial\\n          isPowerBadge\\n          __typename\\n        }}\\n        url\\n        wishlist\\n        sourceEngine: source_engine\\n        __typename\\n      }}\\n      violation {{\\n        headerText\\n        descriptionText\\n        imageURL\\n        ctaURL\\n        ctaApplink\\n        buttonText\\n        buttonType\\n        __typename\\n      }}\\n      __typename\\n    }}\\n    __typename\\n  }}\\n}}\\n"}}]'

payload = [{
    "operationName": "SearchProductQueryV4",
    "variables" : {
        "params" : "device=desktop&navsource=&ob=23&page=2&q=handphone&related=true&rows=60&safe_search=false&scheme=https&shipping=&show_adult=false&source=search&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&st=product&start=60&topads_bucket=true&unique_id=6fcf44dbee09837c7ce5bc7ac79a61e4&user_addressId=4723103&user_cityId=178&user_districtId=2290&user_id=3905748&user_lat=-6.331467099999969&user_long=106.90458220000005&user_postCode=13870&user_warehouseId=13209377&variants=&warehouses=13209377%232h%2C0%2315m"
    },
    "query" : "query SearchProductQueryV4($params: String!) {\n  ace_search_product_v4(params: $params) {\n    header {\n      totalData\n      totalDataText\n      processTime\n      responseCode\n      errorMessage\n      additionalParams\n      keywordProcess\n      componentId\n      __typename\n    }\n    data {\n      banner {\n        position\n        text\n        imageUrl\n        url\n        componentId\n        trackingOption\n        __typename\n      }\n      backendFilters\n      isQuerySafe\n      ticker {\n        text\n        query\n        typeId\n        componentId\n        trackingOption\n        __typename\n      }\n      redirection {\n        redirectUrl\n        departmentId\n        __typename\n      }\n      related {\n        position\n        trackingOption\n        relatedKeyword\n        otherRelated {\n          keyword\n          url\n          product {\n            id\n            name\n            price\n            imageUrl\n            rating\n            countReview\n            url\n            priceStr\n            wishlist\n            shop {\n              city\n              isOfficial\n              isPowerBadge\n              __typename\n            }\n            ads {\n              adsId: id\n              productClickUrl\n              productWishlistUrl\n              shopClickUrl\n              productViewUrl\n              __typename\n            }\n            badges {\n              title\n              imageUrl\n              show\n              __typename\n            }\n            ratingAverage\n            labelGroups {\n              position\n              type\n              title\n              url\n              __typename\n            }\n            componentId\n            __typename\n          }\n          componentId\n          __typename\n        }\n        __typename\n      }\n      suggestion {\n        currentKeyword\n        suggestion\n        suggestionCount\n        instead\n        insteadCount\n        query\n        text\n        componentId\n        trackingOption\n        __typename\n      }\n      products {\n        id\n        name\n        ads {\n          adsId: id\n          productClickUrl\n          productWishlistUrl\n          productViewUrl\n          __typename\n        }\n        badges {\n          title\n          imageUrl\n          show\n          __typename\n        }\n        category: departmentId\n        categoryBreadcrumb\n        categoryId\n        categoryName\n        countReview\n        customVideoURL\n        discountPercentage\n        gaKey\n        imageUrl\n        labelGroups {\n          position\n          title\n          type\n          url\n          __typename\n        }\n        originalPrice\n        price\n        priceRange\n        rating\n        ratingAverage\n        shop {\n          shopId: id\n          name\n          url\n          city\n          isOfficial\n          isPowerBadge\n          __typename\n        }\n        url\n        wishlist\n        sourceEngine: source_engine\n        __typename\n      }\n      violation {\n        headerText\n        descriptionText\n        imageURL\n        ctaURL\n        ctaApplink\n        buttonText\n        buttonType\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
}]


print("Mulai Scrape Data ke Tokopedia....")
# response = requests.post(url_target, headers=header, data=query)
response = requests.post(url_target, headers=header, json=payload)
products = response.json()[0]['data']['ace_search_product_v4']['data']['products']
# print(products)
dtFrame = pd.DataFrame.from_dict(products)
dtFrame.to_excel('data_tokped.xlsx', index=False)
print("Selesai...")