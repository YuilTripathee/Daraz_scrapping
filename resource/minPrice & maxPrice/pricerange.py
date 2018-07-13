import json
def validatePriceRange(list_of_products, minPrice = None, maxPrice = None, fullPrice = False):
    new_product_list = []
    # for the list of products that comes with the list of prices
    if fullPrice == True:
        if minPrice:
            new_product_list = list(filter(lambda x : x['prices'][-1]['price'] >= minPrice, list_of_products))
        if maxPrice:
            new_product_list = list(filter(lambda x : x['prices'][-1]['price'] <= maxPrice, new_product_list))          
    # for the list of products that comes with single price
    else:
        if minPrice:
            new_product_list = list(filter(lambda x : x['prices']['price'] >= minPrice, list_of_products))
        if maxPrice:
            new_product_list = list(filter(lambda x : x['prices']['price'] <= maxPrice, new_product_list))          
        
    return new_product_list

def printPrices(list_of_products, fullPrice):
    if fullPrice:
        for product in list_of_products:
            print(product['prices'][-1]['price'])
    else:
        for product in list_of_products:
            print(product['prices']['price'])

def printList(list_of_products):
    print(json.dumps(list_of_products, indent = 4))

def monkey(list0, number):
    less_than_zero = list(filter(lambda x: x < number, list0))
    print(less_than_zero)          
    # return listA

if __name__ == '__main__':
    recieved_data_WpriceList = {
        "type": 200, 
        "status_code": 1, 
        "status_message": "Everything's working properly", 
        "data": {
            "category": [
            {
                "id": 1, 
                "category": "Accessories", 
                "sub_category": "Cables"
            }, 
            {
                "id": 2, 
                "category": "Gadgets", 
                "sub_category": "Smartwatches"
            }, 
            {
                "id": 3, 
                "category": "Gadgets", 
                "sub_category": "Wireless Speakers"
            }, 
            {
                "id": 4, 
                "category": "Gadgets", 
                "sub_category": "VR Headsets"
            }, 
            {
                "id": 5, 
                "category": "Mobile phones", 
                "sub_category": "Smartphones"
            }
            ], 
            "products": [
            {
                "id": 114, 
                "sku": "OT776EL0USKY8NAFAMZ", 
                "brand": "\u00a0", 
                "name": "Black Smartwatch - Gt08", 
                "category": 2, 
                "link": "https://www.daraz.com.np/other-black-smartwatch-gt08-22715.html", 
                "image_link": "https://np.daraz.io/bb4QHf2Qsr0H175YUUn42fT60qU=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/51/722/1.jpg?2085", 
                "reviews": 12, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jun 24 16:02:36 2018", 
                "prices": [
                {
                    "id": 114, 
                    "price": 1249, 
                    "discount": 43, 
                    "date": "Sun Jun 24 15:53:46 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 239, 
                    "price": 1249, 
                    "discount": 43, 
                    "date": "Sun Jun 24 16:02:36 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 183, 
                "sku": "GI401EL14SORGNAFAMZ", 
                "brand": "Gionee\u00a0", 
                "name": "S11 Lite (4GB RAM, 32GB ROM) 5.7\"-Black", 
                "category": 5, 
                "link": "https://www.daraz.com.np/gionee-s11-lite-4gb-ram-32gb-rom-5.7-black-132586.html", 
                "image_link": "https://np.daraz.io/Uv4PIlpeWdp90RHZP6ESPaEU_Ik=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/68/5231/1.jpg?6125", 
                "reviews": 1, 
                "date_issued": "Sun Jul  1 14:02:28 2018", 
                "date_updated": "Sun Jul  1 17:17:16 2018", 
                "prices": [
                {
                    "id": 774, 
                    "price": 18500, 
                    "discount": 29, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 927, 
                    "price": 18500, 
                    "discount": 29, 
                    "date": "Sun Jul  1 15:14:15 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1050, 
                    "price": 18500, 
                    "discount": 29, 
                    "date": "Sun Jul  1 17:17:16 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 176, 
                "sku": "OT776OT07QF5CNAFAMZ", 
                "brand": "\u00a0", 
                "name": "Laptop Power Cable", 
                "category": 1, 
                "link": "https://www.daraz.com.np/other-laptop-power-cable-9921.html", 
                "image_link": "https://np.daraz.io/mJDauNcWO1BXIDg8I8qtMQatBaI=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/12/99/1.jpg?5554", 
                "reviews": 0, 
                "date_issued": "Sun Jul  1 14:02:28 2018", 
                "date_updated": "Sun Jul  1 17:17:16 2018", 
                "prices": [
                {
                    "id": 764, 
                    "price": 99, 
                    "discount": 50, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 925, 
                    "price": 99, 
                    "discount": 50, 
                    "date": "Sun Jul  1 15:14:15 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1069, 
                    "price": 99, 
                    "discount": 50, 
                    "date": "Sun Jul  1 17:17:16 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 26, 
                "sku": "OT776EL06TNFWNAFAMZ", 
                "brand": "\u00a0", 
                "name": "3 In 1 HDMI Switch- Black", 
                "category": 1, 
                "link": "https://www.daraz.com.np/other-3-in-1-hdmi-switch-black-116411.html", 
                "image_link": "https://np.daraz.io/savGui9YU02dqfG4G24TqUAqmAE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/11/4611/1.jpg?5541", 
                "reviews": 0, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": [
                {
                    "id": 26, 
                    "price": 1649, 
                    "discount": 34, 
                    "date": "Sun Jun 24 15:53:46 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 149, 
                    "price": 1649, 
                    "discount": 34, 
                    "date": "Sun Jun 24 16:02:36 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 276, 
                    "price": 1649, 
                    "discount": 34, 
                    "date": "Wed Jun 27 18:28:30 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 357, 
                    "price": 1649, 
                    "discount": 34, 
                    "date": "Thu Jun 28 11:30:16 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 461, 
                    "price": 1649, 
                    "discount": 34, 
                    "date": "Thu Jun 28 11:33:05 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 523, 
                    "price": 1649, 
                    "discount": 34, 
                    "date": "Thu Jun 28 11:33:22 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 674, 
                    "price": 1649, 
                    "discount": 34, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 818, 
                    "price": 1649, 
                    "discount": 34, 
                    "date": "Sun Jul  1 15:14:14 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 983, 
                    "price": 1649, 
                    "discount": 34, 
                    "date": "Sun Jul  1 17:17:16 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1141, 
                    "price": 1649, 
                    "discount": 34, 
                    "date": "Sun Jul  1 18:11:48 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 5, 
                "sku": "OT776EL1B3028NAFAMZ", 
                "brand": "\u00a0", 
                "name": "JY-25 USB Bluetooth Portable Speaker Support TF Card + FM Radio", 
                "category": 3, 
                "link": "https://www.daraz.com.np/other-jy-25-usb-bluetooth-portable-speaker-support-tf-card-fm-radio-28097.html", 
                "image_link": "https://np.daraz.io/-bspGELOuUOKaAqpydgq4aRFcc4=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/79/082/1.jpg?2235", 
                "reviews": 5, 
                "date_issued": "Sun Jun 24 15:53:45 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": [
                {
                    "id": 5, 
                    "price": 1019, 
                    "discount": 29, 
                    "date": "Sun Jun 24 15:53:45 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 132, 
                    "price": 1019, 
                    "discount": 29, 
                    "date": "Sun Jun 24 16:02:36 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 255, 
                    "price": 1019, 
                    "discount": 29, 
                    "date": "Wed Jun 27 18:28:30 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 358, 
                    "price": 1019, 
                    "discount": 29, 
                    "date": "Thu Jun 28 11:30:16 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 426, 
                    "price": 1019, 
                    "discount": 29, 
                    "date": "Thu Jun 28 11:33:05 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 574, 
                    "price": 1019, 
                    "discount": 29, 
                    "date": "Thu Jun 28 11:33:27 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 630, 
                    "price": 1019, 
                    "discount": 29, 
                    "date": "Sun Jul  1 14:02:27 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 788, 
                    "price": 1019, 
                    "discount": 29, 
                    "date": "Sun Jul  1 15:14:13 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 960, 
                    "price": 1019, 
                    "discount": 29, 
                    "date": "Sun Jul  1 17:17:15 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1103, 
                    "price": 1019, 
                    "discount": 29, 
                    "date": "Sun Jul  1 18:11:48 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 52, 
                "sku": "OT776EL0ZDSK4NAFAMZ", 
                "brand": "\u00a0", 
                "name": "Apple Macbook Pro Type-C Hub Adapter 7 in 1 With HDMI", 
                "category": 1, 
                "link": "https://www.daraz.com.np/other-apple-macbook-pro-type-c-hub-adapter-7-in-1-with-hdmi-103495.html", 
                "image_link": "https://np.daraz.io/NsGiPsWa7ygxlJB_ttcOHUkbwZA=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/59/4301/1.jpg?5538", 
                "reviews": 0, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": [
                {
                    "id": 52, 
                    "price": 4199, 
                    "discount": 16, 
                    "date": "Sun Jun 24 15:53:46 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 179, 
                    "price": 4199, 
                    "discount": 16, 
                    "date": "Sun Jun 24 16:02:36 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 315, 
                    "price": 4199, 
                    "discount": 16, 
                    "date": "Wed Jun 27 18:28:30 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 380, 
                    "price": 4199, 
                    "discount": 16, 
                    "date": "Thu Jun 28 11:30:17 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 490, 
                    "price": 4199, 
                    "discount": 16, 
                    "date": "Thu Jun 28 11:33:06 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 548, 
                    "price": 4199, 
                    "discount": 16, 
                    "date": "Thu Jun 28 11:33:22 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 710, 
                    "price": 4199, 
                    "discount": 16, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 862, 
                    "price": 4199, 
                    "discount": 16, 
                    "date": "Sun Jul  1 15:14:15 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1017, 
                    "price": 4199, 
                    "discount": 16, 
                    "date": "Sun Jul  1 17:17:16 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1184, 
                    "price": 4199, 
                    "discount": 16, 
                    "date": "Sun Jul  1 18:11:48 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 167, 
                "sku": "ON440SP0XUZKCNAFAMZ", 
                "brand": "\u00a0", 
                "name": "Smart Heart Rate Monitor Bluetooth 4.0 Sports Fitness Tracker -  K18S", 
                "category": 2, 
                "link": "https://www.daraz.com.np/onlineshopgroup-smart-heart-rate-monitor-bluetooth-4.0-sports-fitness-tracker-k18s-137865.html", 
                "image_link": "https://np.daraz.io/yHa1lT5rRmR9UzPGlYvrOA0qRcU=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/56/8731/1.jpg?6141", 
                "reviews": 0, 
                "date_issued": "Sun Jul  1 14:02:28 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": [
                {
                    "id": 737, 
                    "price": 2999, 
                    "discount": 40, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 899, 
                    "price": 2999, 
                    "discount": 40, 
                    "date": "Sun Jul  1 15:14:15 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1087, 
                    "price": 2999, 
                    "discount": 40, 
                    "date": "Sun Jul  1 17:17:16 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1238, 
                    "price": 2999, 
                    "discount": 40, 
                    "date": "Sun Jul  1 18:11:48 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 150, 
                "sku": "OT776EL19FVA4NAFAMZ", 
                "brand": "\u00a0", 
                "name": "5m 15 Pin Male To Male VGA Cable - White", 
                "category": 1, 
                "link": "https://www.daraz.com.np/other-5m-15-pin-male-to-male-vga-cable-white-132367.html", 
                "image_link": "https://np.daraz.io/_vHh944TIUXA-IfAKCdkiFEXRJ0=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/76/3231/1.jpg?1206", 
                "reviews": 0, 
                "date_issued": "Sun Jul  1 14:02:28 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": [
                {
                    "id": 665, 
                    "price": 475, 
                    "discount": 5, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 810, 
                    "price": 475, 
                    "discount": 5, 
                    "date": "Sun Jul  1 15:14:14 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 978, 
                    "price": 475, 
                    "discount": 5, 
                    "date": "Sun Jul  1 17:17:16 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1137, 
                    "price": 475, 
                    "discount": 5, 
                    "date": "Sun Jul  1 18:11:48 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 188, 
                "sku": "LE594EL0O6VXGNAFAMZ", 
                "brand": "Leagoo\u00a0", 
                "name": "T1 (2 GB RAM, 16 GB ROM) 5.0\"- Gray (4G)", 
                "category": 5, 
                "link": "https://www.daraz.com.np/leagoo-t1-2-gb-ram-16-gb-rom-5.0-gray-4g-123604.html", 
                "image_link": "https://np.daraz.io/0QOsxk-ZkdYM2365qnITd7rVmzo=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/40/6321/1.jpg?5817", 
                "reviews": 0, 
                "date_issued": "Sun Jul  1 14:02:28 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": [
                {
                    "id": 781, 
                    "price": 8500, 
                    "discount": 50, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 937, 
                    "price": 8500, 
                    "discount": 50, 
                    "date": "Sun Jul  1 15:14:15 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1070, 
                    "price": 8500, 
                    "discount": 50, 
                    "date": "Sun Jul  1 17:17:16 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1216, 
                    "price": 8500, 
                    "discount": 50, 
                    "date": "Sun Jul  1 18:11:48 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 71, 
                "sku": "OT776EL0BSUTWNAFAMZ", 
                "brand": "\u00a0", 
                "name": "F07 Waterproof Heart Rate Monitor Wrist Watch-Black", 
                "category": 2, 
                "link": "https://www.daraz.com.np/other-f07-waterproof-heart-rate-monitor-wrist-watch-black-122891.html", 
                "image_link": "https://np.daraz.io/xPh11_eqD9nVH4CrSCzZo1NGNqo=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/19/8221/1.jpg?7111", 
                "reviews": 0, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": [
                {
                    "id": 72, 
                    "price": 4479, 
                    "discount": 15, 
                    "date": "Sun Jun 24 15:53:46 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 210, 
                    "price": 4479, 
                    "discount": 15, 
                    "date": "Sun Jun 24 16:02:36 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 296, 
                    "price": 4479, 
                    "discount": 15, 
                    "date": "Wed Jun 27 18:28:30 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 534, 
                    "price": 4479, 
                    "discount": 15, 
                    "date": "Thu Jun 28 11:33:22 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 715, 
                    "price": 4479, 
                    "discount": 15, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 880, 
                    "price": 4479, 
                    "discount": 15, 
                    "date": "Sun Jul  1 15:14:15 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1077, 
                    "price": 4479, 
                    "discount": 15, 
                    "date": "Sun Jul  1 17:17:16 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1225, 
                    "price": 4479, 
                    "discount": 15, 
                    "date": "Sun Jul  1 18:11:48 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 101, 
                "sku": "OT776EL062JA8NAFAMZ", 
                "brand": "\u00a0", 
                "name": "Combo of VR Box With Gaming Remote Controller and  Earphone", 
                "category": 4, 
                "link": "https://www.daraz.com.np/other-combo-of-vr-box-with-gaming-remote-controller-and-earphone-69101.html", 
                "image_link": "https://np.daraz.io/S2ldOvluhBl7Wrk9uEu57AoG3uA=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/10/196/1.jpg?3447", 
                "reviews": 0, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": [
                {
                    "id": 101, 
                    "price": 1450, 
                    "discount": 19, 
                    "date": "Sun Jun 24 15:53:46 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 205, 
                    "price": 1450, 
                    "discount": 19, 
                    "date": "Sun Jun 24 16:02:36 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 620, 
                    "price": 1450, 
                    "discount": 19, 
                    "date": "Thu Jun 28 11:33:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 748, 
                    "price": 1450, 
                    "discount": 19, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 896, 
                    "price": 1450, 
                    "discount": 19, 
                    "date": "Sun Jul  1 15:14:15 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1015, 
                    "price": 1450, 
                    "discount": 19, 
                    "date": "Sun Jul  1 17:17:16 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1231, 
                    "price": 1450, 
                    "discount": 19, 
                    "date": "Sun Jul  1 18:11:48 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 48, 
                "sku": "OT776EL19AKM8NAFAMZ", 
                "brand": "\u00a0", 
                "name": "Waterproof Portable Bluetooth Speakers", 
                "category": 3, 
                "link": "https://www.daraz.com.np/other-waterproof-portable-bluetooth-speakers-67067.html", 
                "image_link": "https://np.daraz.io/QrYt8qaLDOvq_GSQ62jtbx8lquo=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/76/076/1.jpg?9887", 
                "reviews": 1, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": [
                {
                    "id": 48, 
                    "price": 2200, 
                    "discount": 21, 
                    "date": "Sun Jun 24 15:53:46 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 177, 
                    "price": 2200, 
                    "discount": 21, 
                    "date": "Sun Jun 24 16:02:36 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 304, 
                    "price": 2200, 
                    "discount": 21, 
                    "date": "Wed Jun 27 18:28:30 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 409, 
                    "price": 2200, 
                    "discount": 21, 
                    "date": "Thu Jun 28 11:30:17 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 468, 
                    "price": 2200, 
                    "discount": 21, 
                    "date": "Thu Jun 28 11:33:06 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 590, 
                    "price": 2200, 
                    "discount": 21, 
                    "date": "Thu Jun 28 11:33:27 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 655, 
                    "price": 2200, 
                    "discount": 21, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 811, 
                    "price": 2200, 
                    "discount": 21, 
                    "date": "Sun Jul  1 15:14:14 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1001, 
                    "price": 2200, 
                    "discount": 21, 
                    "date": "Sun Jul  1 17:17:16 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1135, 
                    "price": 2200, 
                    "discount": 21, 
                    "date": "Sun Jul  1 18:11:48 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 184, 
                "sku": "MO694EL128ADGNAFAMZ", 
                "brand": "Motorola\u00a0", 
                "name": "Moto E4 (2GB RAM, 16GB ROM) - Irony Grey", 
                "category": 5, 
                "link": "https://www.daraz.com.np/motorola-moto-e4-2gb-ram-16gb-rom-irony-grey-121246.html", 
                "image_link": "https://np.daraz.io/UvoZFoQrJRz1cHp2SqeB8gUKE6c=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/64/2121/1.jpg?4348", 
                "reviews": 0, 
                "date_issued": "Sun Jul  1 14:02:28 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": [
                {
                    "id": 776, 
                    "price": 14335, 
                    "discount": 12, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 931, 
                    "price": 14335, 
                    "discount": 12, 
                    "date": "Sun Jul  1 15:14:15 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1054, 
                    "price": 14335, 
                    "discount": 12, 
                    "date": "Sun Jul  1 17:17:16 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1200, 
                    "price": 14335, 
                    "discount": 12, 
                    "date": "Sun Jul  1 18:11:48 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 136, 
                "sku": "OT776EL0RMLK0NAFAMZ", 
                "brand": "\u00a0", 
                "name": "Smartwatch Supporting Sim & Tf Card Slot", 
                "category": 2, 
                "link": "https://www.daraz.com.np/other-smartwatch-supporting-sim-tf-card-slot-40464.html", 
                "image_link": "https://np.daraz.io/OdMktfefPNTLqV_pfN53z1kniPU=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/46/404/1.jpg?3704", 
                "reviews": 1, 
                "date_issued": "Thu Jun 28 11:30:17 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": [
                {
                    "id": 407, 
                    "price": 2199, 
                    "discount": 12, 
                    "date": "Thu Jun 28 11:30:17 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 462, 
                    "price": 2199, 
                    "discount": 12, 
                    "date": "Thu Jun 28 11:33:05 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 514, 
                    "price": 2199, 
                    "discount": 12, 
                    "date": "Thu Jun 28 11:33:22 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 668, 
                    "price": 2199, 
                    "discount": 12, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 835, 
                    "price": 2199, 
                    "discount": 12, 
                    "date": "Sun Jul  1 15:14:15 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1034, 
                    "price": 2199, 
                    "discount": 12, 
                    "date": "Sun Jul  1 17:17:16 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1166, 
                    "price": 2199, 
                    "discount": 12, 
                    "date": "Sun Jul  1 18:11:48 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 21, 
                "sku": "OT776EL18VF3CNAFAMZ", 
                "brand": "\u00a0", 
                "name": "SD Support Bluetooth Portable Speaker (Color Varied)", 
                "category": 3, 
                "link": "https://www.daraz.com.np/other-sd-support-bluetooth-portable-speaker-color-varied-96357.html", 
                "image_link": "https://np.daraz.io/BwaSKVBm43RTUK2Ov4skgLXrN8I=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/75/369/1.jpg?4365", 
                "reviews": 1, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": [
                {
                    "id": 21, 
                    "price": 339, 
                    "discount": 48, 
                    "date": "Sun Jun 24 15:53:46 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 151, 
                    "price": 339, 
                    "discount": 48, 
                    "date": "Sun Jun 24 16:02:36 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 275, 
                    "price": 339, 
                    "discount": 48, 
                    "date": "Wed Jun 27 18:28:30 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 379, 
                    "price": 339, 
                    "discount": 48, 
                    "date": "Thu Jun 28 11:30:17 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 438, 
                    "price": 339, 
                    "discount": 48, 
                    "date": "Thu Jun 28 11:33:05 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 580, 
                    "price": 339, 
                    "discount": 48, 
                    "date": "Thu Jun 28 11:33:27 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 641, 
                    "price": 339, 
                    "discount": 48, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 800, 
                    "price": 339, 
                    "discount": 48, 
                    "date": "Sun Jul  1 15:14:14 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 985, 
                    "price": 339, 
                    "discount": 48, 
                    "date": "Sun Jul  1 17:17:16 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1123, 
                    "price": 339, 
                    "discount": 48, 
                    "date": "Sun Jul  1 18:11:48 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 171, 
                "sku": "LE594EL0CA7TWNAFAMZ", 
                "brand": "Leagoo\u00a0", 
                "name": "M8 (2 GB RAM, 16 GB ROM) 5.7\"- Gold", 
                "category": 5, 
                "link": "https://www.daraz.com.np/leagoo-m8-2-gb-ram-16-gb-rom-5.7-gold-123602.html", 
                "image_link": "https://np.daraz.io/u51VcoUSa9G_I0HR3PQHxyOnF0Y=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/20/6321/1.jpg?5696", 
                "reviews": 1, 
                "date_issued": "Sun Jul  1 14:02:28 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": [
                {
                    "id": 751, 
                    "price": 8500, 
                    "discount": 39, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 894, 
                    "price": 8500, 
                    "discount": 39, 
                    "date": "Sun Jul  1 15:14:15 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1018, 
                    "price": 8500, 
                    "discount": 39, 
                    "date": "Sun Jul  1 17:17:16 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1174, 
                    "price": 8500, 
                    "discount": 39, 
                    "date": "Sun Jul  1 18:11:48 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 164, 
                "sku": "ZT122EL07MEUWNAFAMZ", 
                "brand": "ZTE\u00a0", 
                "name": "Blade S6 Smart Mobile Phone - [16GB, 2GB - Silver]", 
                "category": 5, 
                "link": "https://www.daraz.com.np/zte-blade-s6-smart-mobile-phone-16gb-2gb-silver-30821.html", 
                "image_link": "https://np.daraz.io/G_A6KkRhWLOVcH82VOakH-lLdrs=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/12/803/1.jpg?3725", 
                "reviews": 0, 
                "date_issued": "Sun Jul  1 14:02:28 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": [
                {
                    "id": 730, 
                    "price": 14055, 
                    "discount": 3, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 878, 
                    "price": 14055, 
                    "discount": 3, 
                    "date": "Sun Jul  1 15:14:15 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1007, 
                    "price": 14055, 
                    "discount": 3, 
                    "date": "Sun Jul  1 17:17:16 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1159, 
                    "price": 14055, 
                    "discount": 3, 
                    "date": "Sun Jul  1 18:11:48 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 99, 
                "sku": "AA370EL1KRC6ONAFAMZ", 
                "brand": "\u00a0", 
                "name": "6ft 1.8M 1080P HDMI Gold Male To VGA HD-15 Male 15Pin Adapter Cable", 
                "category": 1, 
                "link": "https://www.daraz.com.np/other-6ft-1.8m-1080p-hdmi-gold-male-to-vga-hd-15-male-15pin-adapter-cable-43359.html", 
                "image_link": "https://np.daraz.io/VbL2ODNZ53r_AMtpAKKdMtkPmcE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/95/334/1.jpg?7124", 
                "reviews": 0, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": [
                {
                    "id": 99, 
                    "price": 999, 
                    "discount": 33, 
                    "date": "Sun Jun 24 15:53:46 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 221, 
                    "price": 999, 
                    "discount": 33, 
                    "date": "Sun Jun 24 16:02:36 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 335, 
                    "price": 999, 
                    "discount": 33, 
                    "date": "Wed Jun 27 18:28:30 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 399, 
                    "price": 999, 
                    "discount": 33, 
                    "date": "Thu Jun 28 11:30:17 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 500, 
                    "price": 999, 
                    "discount": 33, 
                    "date": "Thu Jun 28 11:33:06 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 566, 
                    "price": 999, 
                    "discount": 33, 
                    "date": "Thu Jun 28 11:33:22 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 738, 
                    "price": 999, 
                    "discount": 33, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 892, 
                    "price": 999, 
                    "discount": 33, 
                    "date": "Sun Jul  1 15:14:15 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1038, 
                    "price": 999, 
                    "discount": 33, 
                    "date": "Sun Jul  1 17:17:16 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1229, 
                    "price": 999, 
                    "discount": 33, 
                    "date": "Sun Jul  1 18:11:48 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 109, 
                "sku": "AA370EL1AI650NAFAMZ", 
                "brand": "\u00a0", 
                "name": "OTG Cable, Pofesun 0.5ft USB C OTG Cable", 
                "category": 1, 
                "link": "https://www.daraz.com.np/other-otg-cable-pofesun-0.5ft-usb-c-otg-cable-101187.html", 
                "image_link": "https://np.daraz.io/RhsRFCRLr-6LiZDi4KhICI-2Jas=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/78/1101/1.jpg?4484", 
                "reviews": 0, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jun 24 16:02:36 2018", 
                "prices": [
                {
                    "id": 110, 
                    "price": 449, 
                    "discount": 55, 
                    "date": "Sun Jun 24 15:53:46 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 229, 
                    "price": 449, 
                    "discount": 55, 
                    "date": "Sun Jun 24 16:02:36 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 122, 
                "sku": "OT776EL1B4E7SNAFAMZ", 
                "brand": "\u00a0", 
                "name": "X6 Bluetooth Smart Watch With Camera SIM Memory Card - (White/Black)", 
                "category": 2, 
                "link": "https://www.daraz.com.np/other-x6-bluetooth-smart-watch-with-camera-sim-memory-card-whiteblack-74197.html", 
                "image_link": "https://np.daraz.io/Rbu6yCJV-EarDY3sSQOqzLuRyvQ=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/79/147/1.jpg?8287", 
                "reviews": 2, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jun 24 16:02:36 2018", 
                "prices": [
                {
                    "id": 122, 
                    "price": 2500, 
                    "discount": 29, 
                    "date": "Sun Jun 24 15:53:46 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 245, 
                    "price": 2500, 
                    "discount": 29, 
                    "date": "Sun Jun 24 16:02:36 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 156, 
                "sku": "SO640EL1C1XUSNAFAMZ", 
                "brand": "SOMHO\u00a0", 
                "name": "S-311 Portable Bluetooth Speaker-Red", 
                "category": 3, 
                "link": "https://www.daraz.com.np/somho-s-311-portable-bluetooth-speaker-red-121708.html", 
                "image_link": "https://np.daraz.io/WXZFO02T_6Ae9_zaFqYgfCMI_Gw=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/80/7121/1.jpg?9397", 
                "reviews": 0, 
                "date_issued": "Sun Jul  1 14:02:28 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": [
                {
                    "id": 696, 
                    "price": 1699, 
                    "discount": 4, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 860, 
                    "price": 1699, 
                    "discount": 4, 
                    "date": "Sun Jul  1 15:14:15 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1047, 
                    "price": 1699, 
                    "discount": 4, 
                    "date": "Sun Jul  1 17:17:16 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1178, 
                    "price": 1699, 
                    "discount": 4, 
                    "date": "Sun Jul  1 18:11:48 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 47, 
                "sku": "OT776EL0I7OXSNAFAMZ", 
                "brand": "\u00a0", 
                "name": "Bluetooth Smartwatch - D3 New", 
                "category": 2, 
                "link": "https://www.daraz.com.np/other-bluetooth-smartwatch-d3-new-29503.html", 
                "image_link": "https://np.daraz.io/DQ-CIGqQm2hoz_ST40WHOO8qrHM=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/30/592/1.jpg?7286", 
                "reviews": 8, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": [
                {
                    "id": 47, 
                    "price": 1299, 
                    "discount": 37, 
                    "date": "Sun Jun 24 15:53:46 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 178, 
                    "price": 1299, 
                    "discount": 37, 
                    "date": "Sun Jun 24 16:02:36 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 277, 
                    "price": 1299, 
                    "discount": 37, 
                    "date": "Wed Jun 27 18:28:30 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 528, 
                    "price": 1299, 
                    "discount": 37, 
                    "date": "Thu Jun 28 11:33:22 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 703, 
                    "price": 1299, 
                    "discount": 37, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 867, 
                    "price": 1299, 
                    "discount": 37, 
                    "date": "Sun Jul  1 15:14:15 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1068, 
                    "price": 1299, 
                    "discount": 37, 
                    "date": "Sun Jul  1 17:17:16 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1208, 
                    "price": 1299, 
                    "discount": 37, 
                    "date": "Sun Jul  1 18:11:48 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 13, 
                "sku": "OT776EL0KP5M8NAFAMZ", 
                "brand": "\u00a0", 
                "name": "HDMI To VGA Converter", 
                "category": 1, 
                "link": "https://www.daraz.com.np/other-hdmi-to-vga-converter-66743.html", 
                "image_link": "https://np.daraz.io/YHyFj4q_wx94p2Jw0rNdEvGc27M=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/34/766/1.jpg?4424", 
                "reviews": 0, 
                "date_issued": "Sun Jun 24 15:53:45 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": [
                {
                    "id": 13, 
                    "price": 359, 
                    "discount": 64, 
                    "date": "Sun Jun 24 15:53:46 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 136, 
                    "price": 359, 
                    "discount": 64, 
                    "date": "Sun Jun 24 16:02:36 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 341, 
                    "price": 359, 
                    "discount": 64, 
                    "date": "Wed Jun 27 18:28:30 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 346, 
                    "price": 359, 
                    "discount": 64, 
                    "date": "Thu Jun 28 11:30:16 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 447, 
                    "price": 359, 
                    "discount": 64, 
                    "date": "Thu Jun 28 11:33:05 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 515, 
                    "price": 359, 
                    "discount": 64, 
                    "date": "Thu Jun 28 11:33:22 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 647, 
                    "price": 359, 
                    "discount": 64, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 793, 
                    "price": 359, 
                    "discount": 64, 
                    "date": "Sun Jul  1 15:14:14 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 959, 
                    "price": 359, 
                    "discount": 64, 
                    "date": "Sun Jul  1 17:17:15 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1115, 
                    "price": 359, 
                    "discount": 64, 
                    "date": "Sun Jul  1 18:11:48 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 130, 
                "sku": "AA370SP1CHTM4NAFAMZ", 
                "brand": "", 
                "name": "KW18 Smartwatch Phone support TF SIM Card Heart Rate", 
                "category": 0, 
                "link": "https://www.daraz.com.np/aafno-pasal-kw18-smartwatch-phone-support-tf-sim-card-heart-rate-135418.html", 
                "image_link": "https://np.daraz.io/ysogQZyIQE2SaeWLpNIthdQhgQ8=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/81/4531/1.jpg?8322", 
                "reviews": 0, 
                "date_issued": "Wed Jun 27 18:28:30 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": [
                {
                    "id": 317, 
                    "price": 6999, 
                    "discount": 53, 
                    "date": "Wed Jun 27 18:28:30 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 549, 
                    "price": 6999, 
                    "discount": 53, 
                    "date": "Thu Jun 28 11:33:22 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 640, 
                    "price": 6999, 
                    "discount": 53, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 805, 
                    "price": 6999, 
                    "discount": 53, 
                    "date": "Sun Jul  1 15:14:14 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 979, 
                    "price": 6999, 
                    "discount": 53, 
                    "date": "Sun Jul  1 17:17:16 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1127, 
                    "price": 6999, 
                    "discount": 53, 
                    "date": "Sun Jul  1 18:11:48 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 129, 
                "sku": "OT776EL0I94MWNAFAMZ", 
                "brand": "", 
                "name": "USB 2.0 Type A Male to A Female Extension Cable 3 Meter - Black", 
                "category": 1, 
                "link": "https://www.daraz.com.np/other-usb-2.0-type-a-male-to-a-female-extension-cable-3-meter-black-95603.html", 
                "image_link": "https://np.daraz.io/a5uzgsRy6G7CAWuRcCFTC9AkFBM=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/30/659/1.jpg?1285", 
                "reviews": 0, 
                "date_issued": "Wed Jun 27 18:28:30 2018", 
                "date_updated": "Thu Jun 28 11:33:22 2018", 
                "prices": [
                {
                    "id": 313, 
                    "price": 149, 
                    "discount": 25, 
                    "date": "Wed Jun 27 18:28:30 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 378, 
                    "price": 149, 
                    "discount": 25, 
                    "date": "Thu Jun 28 11:30:17 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 489, 
                    "price": 149, 
                    "discount": 25, 
                    "date": "Thu Jun 28 11:33:06 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 546, 
                    "price": 149, 
                    "discount": 25, 
                    "date": "Thu Jun 28 11:33:22 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 22, 
                "sku": "OT776EL0Q3ZI8NAFAMZ", 
                "brand": "\u00a0", 
                "name": "VR Box Pro - 3D Glasses Virtual Reality With Remote", 
                "category": 4, 
                "link": "https://www.daraz.com.np/other-vr-box-pro-3d-glasses-virtual-reality-with-remote-65834.html", 
                "image_link": "https://np.daraz.io/vQ8dkKWM5ZZTlul2Ba5TBya2lwE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/43/856/1.jpg?4484", 
                "reviews": 0, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": [
                {
                    "id": 22, 
                    "price": 619, 
                    "discount": 31, 
                    "date": "Sun Jun 24 15:53:46 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 138, 
                    "price": 619, 
                    "discount": 31, 
                    "date": "Sun Jun 24 16:02:36 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 254, 
                    "price": 619, 
                    "discount": 31, 
                    "date": "Wed Jun 27 18:28:30 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 356, 
                    "price": 619, 
                    "discount": 31, 
                    "date": "Thu Jun 28 11:30:16 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 439, 
                    "price": 619, 
                    "discount": 31, 
                    "date": "Thu Jun 28 11:33:05 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 604, 
                    "price": 619, 
                    "discount": 31, 
                    "date": "Thu Jun 28 11:33:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 660, 
                    "price": 619, 
                    "discount": 31, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 806, 
                    "price": 619, 
                    "discount": 31, 
                    "date": "Sun Jul  1 15:14:14 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 951, 
                    "price": 619, 
                    "discount": 31, 
                    "date": "Sun Jul  1 17:17:15 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1131, 
                    "price": 619, 
                    "discount": 31, 
                    "date": "Sun Jul  1 18:11:48 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 181, 
                "sku": "MO694EL01FP6SNAFAMZ", 
                "brand": "Motorola\u00a0", 
                "name": "Moto C (1GB RAM, 16GB ROM) - Black", 
                "category": 5, 
                "link": "https://www.daraz.com.np/motorola-moto-c-1gb-ram-16gb-rom-black-121420.html", 
                "image_link": "https://np.daraz.io/nWnMgyO4cHkyfnHtkyYWCeZJuxE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/02/4121/1.jpg?9229", 
                "reviews": 0, 
                "date_issued": "Sun Jul  1 14:02:28 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": [
                {
                    "id": 772, 
                    "price": 9671, 
                    "discount": 12, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 923, 
                    "price": 9671, 
                    "discount": 12, 
                    "date": "Sun Jul  1 15:14:15 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1040, 
                    "price": 9671, 
                    "discount": 12, 
                    "date": "Sun Jul  1 17:17:16 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1191, 
                    "price": 9671, 
                    "discount": 12, 
                    "date": "Sun Jul  1 18:11:48 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 194, 
                "sku": "MI671EL014J6KNAFAMZ", 
                "brand": "Micromax\u00a0", 
                "name": "Canvas Ultra M1 [3 GB RAM, 32 GB ROM] - Gold", 
                "category": 5, 
                "link": "https://www.daraz.com.np/micromax-canvas-ultra-m1-3-gb-ram-32-gb-rom-gold-119810.html", 
                "image_link": "https://np.daraz.io/2aJUfI3YolpEjFcUovvi2kU5tKM=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/01/8911/1.jpg?1809", 
                "reviews": 1, 
                "date_issued": "Sun Jul  1 18:11:48 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": [
                {
                    "id": 1179, 
                    "price": 12200, 
                    "discount": 46, 
                    "date": "Sun Jul  1 18:11:48 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 106, 
                "sku": "OT776EL069O88NAFAMZ", 
                "brand": "\u00a0", 
                "name": "Desktop Power Cable 0.68 (1.5m)", 
                "category": 1, 
                "link": "https://www.daraz.com.np/other-desktop-power-cable-0.68-1.5m-92501.html", 
                "image_link": "https://np.daraz.io/31UQCWw-fT4BCTHbm08qJrBla-s=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/10/529/1.jpg?8684", 
                "reviews": 0, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": [
                {
                    "id": 106, 
                    "price": 75, 
                    "discount": 25, 
                    "date": "Sun Jun 24 15:53:46 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 227, 
                    "price": 75, 
                    "discount": 25, 
                    "date": "Sun Jun 24 16:02:36 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 337, 
                    "price": 75, 
                    "discount": 25, 
                    "date": "Wed Jun 27 18:28:30 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 403, 
                    "price": 75, 
                    "discount": 25, 
                    "date": "Thu Jun 28 11:30:17 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 502, 
                    "price": 75, 
                    "discount": 25, 
                    "date": "Thu Jun 28 11:33:06 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 568, 
                    "price": 75, 
                    "discount": 25, 
                    "date": "Thu Jun 28 11:33:22 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 731, 
                    "price": 75, 
                    "discount": 25, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 882, 
                    "price": 75, 
                    "discount": 25, 
                    "date": "Sun Jul  1 15:14:15 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1033, 
                    "price": 75, 
                    "discount": 25, 
                    "date": "Sun Jul  1 17:17:16 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1192, 
                    "price": 75, 
                    "discount": 25, 
                    "date": "Sun Jul  1 18:11:48 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 119, 
                "sku": "OT776EL0HKBYSNAFAMZ", 
                "brand": "\u00a0", 
                "name": "Samsung Gear S3 Tempered Glass Screen Protecto 2.5D High Definition 9H", 
                "category": 2, 
                "link": "https://www.daraz.com.np/other-samsung-gear-s3-tempered-glass-screen-protecto-2.5d-high-definition-9h-120592.html", 
                "image_link": "https://np.daraz.io/X266OtOLq2w8p5evYKzjBqWq5fE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/29/5021/1.jpg?5156", 
                "reviews": 0, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": [
                {
                    "id": 119, 
                    "price": 500, 
                    "discount": 38, 
                    "date": "Sun Jun 24 15:53:46 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 242, 
                    "price": 500, 
                    "discount": 38, 
                    "date": "Sun Jun 24 16:02:36 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 555, 
                    "price": 500, 
                    "discount": 38, 
                    "date": "Thu Jun 28 11:33:22 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 760, 
                    "price": 500, 
                    "discount": 38, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 921, 
                    "price": 500, 
                    "discount": 38, 
                    "date": "Sun Jul  1 15:14:15 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1093, 
                    "price": 500, 
                    "discount": 38, 
                    "date": "Sun Jul  1 17:17:16 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1245, 
                    "price": 500, 
                    "discount": 38, 
                    "date": "Sun Jul  1 18:11:48 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 6, 
                "sku": "OT776OT02Z6SONAFAMZ", 
                "brand": "\u00a0", 
                "name": "Printer Cable 10 Meter", 
                "category": 1, 
                "link": "https://www.daraz.com.np/other-printer-cable-10-meter-10050.html", 
                "image_link": "https://np.daraz.io/Euv_hKy1WFxRxRDLZifWzklub7I=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/05/001/1.jpg?5552", 
                "reviews": 0, 
                "date_issued": "Sun Jun 24 15:53:45 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": [
                {
                    "id": 6, 
                    "price": 899, 
                    "discount": 40, 
                    "date": "Sun Jun 24 15:53:45 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 126, 
                    "price": 899, 
                    "discount": 40, 
                    "date": "Sun Jun 24 16:02:35 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 256, 
                    "price": 899, 
                    "discount": 40, 
                    "date": "Wed Jun 27 18:28:30 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 344, 
                    "price": 899, 
                    "discount": 40, 
                    "date": "Thu Jun 28 11:30:16 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 437, 
                    "price": 899, 
                    "discount": 40, 
                    "date": "Thu Jun 28 11:33:05 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 511, 
                    "price": 899, 
                    "discount": 40, 
                    "date": "Thu Jun 28 11:33:22 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 639, 
                    "price": 899, 
                    "discount": 40, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 789, 
                    "price": 899, 
                    "discount": 40, 
                    "date": "Sun Jul  1 15:14:13 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 953, 
                    "price": 899, 
                    "discount": 40, 
                    "date": "Sun Jul  1 17:17:15 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1106, 
                    "price": 899, 
                    "discount": 40, 
                    "date": "Sun Jul  1 18:11:48 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 93, 
                "sku": "OT776EL1JI138NAFAMZ", 
                "brand": "\u00a0", 
                "name": "X2 Smart Watch Bluetooth Sport Fitness Tracker Heart Rate", 
                "category": 2, 
                "link": "https://www.daraz.com.np/other-x2-smart-watch-bluetooth-sport-fitness-tracker-heart-rate-102239.html", 
                "image_link": "https://np.daraz.io/7Cb-Vq1XdMAXmU0c_kgSI7DsAos=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/93/2201/1.jpg?3696", 
                "reviews": 0, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jun 24 16:02:36 2018", 
                "prices": [
                {
                    "id": 93, 
                    "price": 4499, 
                    "discount": 20, 
                    "date": "Sun Jun 24 15:53:46 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 231, 
                    "price": 4499, 
                    "discount": 20, 
                    "date": "Sun Jun 24 16:02:36 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 88, 
                "sku": "OT776EL1ESQ6KNAFAMZ", 
                "brand": "\u00a0", 
                "name": "VGA to HDMI Video & Audio Converter Adapter", 
                "category": 1, 
                "link": "https://www.daraz.com.np/other-vga-to-hdmi-video-audio-converter-adapter-112358.html", 
                "image_link": "https://np.daraz.io/KuLpiVXUVCj1zQxqvhUJ8Z2H83w=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/85/3211/1.jpg?3647", 
                "reviews": 0, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": [
                {
                    "id": 87, 
                    "price": 1300, 
                    "discount": 30, 
                    "date": "Sun Jun 24 15:53:46 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 211, 
                    "price": 1300, 
                    "discount": 30, 
                    "date": "Sun Jun 24 16:02:36 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 332, 
                    "price": 1300, 
                    "discount": 30, 
                    "date": "Wed Jun 27 18:28:30 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 393, 
                    "price": 1300, 
                    "discount": 30, 
                    "date": "Thu Jun 28 11:30:17 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 497, 
                    "price": 1300, 
                    "discount": 30, 
                    "date": "Thu Jun 28 11:33:06 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 562, 
                    "price": 1300, 
                    "discount": 30, 
                    "date": "Thu Jun 28 11:33:22 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 747, 
                    "price": 1300, 
                    "discount": 30, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 909, 
                    "price": 1300, 
                    "discount": 30, 
                    "date": "Sun Jul  1 15:14:15 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1051, 
                    "price": 1300, 
                    "discount": 30, 
                    "date": "Sun Jul  1 17:17:16 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1211, 
                    "price": 1300, 
                    "discount": 30, 
                    "date": "Sun Jul  1 18:11:48 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 42, 
                "sku": "OT776EL07MZOWNAFAMZ", 
                "brand": "\u00a0", 
                "name": "Portable Bluetooth Speaker With USB + TF Card + FM Radio (JY-25)", 
                "category": 3, 
                "link": "https://www.daraz.com.np/other-portable-bluetooth-speaker-with-usb-tf-card-fm-radio-jy-25-3821.html", 
                "image_link": "https://np.daraz.io/ywMDE6cqb4yoT8_ahIMtQ4YXJ-8=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/12/83/1.jpg?1917", 
                "reviews": 1, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": [
                {
                    "id": 43, 
                    "price": 1199, 
                    "discount": 39, 
                    "date": "Sun Jun 24 15:53:46 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 173, 
                    "price": 1199, 
                    "discount": 39, 
                    "date": "Sun Jun 24 16:02:36 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 302, 
                    "price": 1199, 
                    "discount": 39, 
                    "date": "Wed Jun 27 18:28:30 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 406, 
                    "price": 1199, 
                    "discount": 39, 
                    "date": "Thu Jun 28 11:30:17 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 465, 
                    "price": 1199, 
                    "discount": 39, 
                    "date": "Thu Jun 28 11:33:05 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 589, 
                    "price": 1199, 
                    "discount": 39, 
                    "date": "Thu Jun 28 11:33:27 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 671, 
                    "price": 1199, 
                    "discount": 39, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 832, 
                    "price": 1199, 
                    "discount": 39, 
                    "date": "Sun Jul  1 15:14:15 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1031, 
                    "price": 1199, 
                    "discount": 39, 
                    "date": "Sun Jul  1 17:17:16 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1165, 
                    "price": 1199, 
                    "discount": 39, 
                    "date": "Sun Jul  1 18:11:48 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 103, 
                "sku": "OT776OT05YCTKNAFAMZ", 
                "brand": "\u00a0", 
                "name": "HDMI Male to VGA + Audio Converter Cable For PC/Laptop", 
                "category": 1, 
                "link": "https://www.daraz.com.np/other-hdmi-male-to-vga-audio-converter-cable-for-pclaptop-10001.html", 
                "image_link": "https://np.daraz.io/2AH5oGzwgsdll8LfOMBB5siacHI=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/10/001/1.jpg?5553", 
                "reviews": 0, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Thu Jun 28 11:33:22 2018", 
                "prices": [
                {
                    "id": 104, 
                    "price": 499, 
                    "discount": 50, 
                    "date": "Sun Jun 24 15:53:46 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 225, 
                    "price": 499, 
                    "discount": 50, 
                    "date": "Sun Jun 24 16:02:36 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 336, 
                    "price": 499, 
                    "discount": 50, 
                    "date": "Wed Jun 27 18:28:30 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 401, 
                    "price": 499, 
                    "discount": 50, 
                    "date": "Thu Jun 28 11:30:17 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 501, 
                    "price": 499, 
                    "discount": 50, 
                    "date": "Thu Jun 28 11:33:06 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 567, 
                    "price": 499, 
                    "discount": 50, 
                    "date": "Thu Jun 28 11:33:22 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 32, 
                "sku": "OT776EL1LW8HGNAFAMZ", 
                "brand": "\u00a0", 
                "name": "All-in-1 Combo Hub With Card Readers & USB Ports", 
                "category": 1, 
                "link": "https://www.daraz.com.np/other-all-in-1-combo-hub-with-card-readers-usb-ports-124279.html", 
                "image_link": "https://np.daraz.io/GKKwE3Ki4G3wx20nJZx5PXuGx0I=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/97/2421/1.jpg?1597", 
                "reviews": 0, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": [
                {
                    "id": 33, 
                    "price": 380, 
                    "discount": 11, 
                    "date": "Sun Jun 24 15:53:46 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 159, 
                    "price": 380, 
                    "discount": 11, 
                    "date": "Sun Jun 24 16:02:36 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 282, 
                    "price": 380, 
                    "discount": 11, 
                    "date": "Wed Jun 27 18:28:30 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 364, 
                    "price": 380, 
                    "discount": 11, 
                    "date": "Thu Jun 28 11:30:16 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 467, 
                    "price": 380, 
                    "discount": 11, 
                    "date": "Thu Jun 28 11:33:06 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 527, 
                    "price": 380, 
                    "discount": 11, 
                    "date": "Thu Jun 28 11:33:22 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 744, 
                    "price": 380, 
                    "discount": 11, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 903, 
                    "price": 380, 
                    "discount": 11, 
                    "date": "Sun Jul  1 15:14:15 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1046, 
                    "price": 380, 
                    "discount": 11, 
                    "date": "Sun Jul  1 17:17:16 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1205, 
                    "price": 380, 
                    "discount": 11, 
                    "date": "Sun Jul  1 18:11:48 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 85, 
                "sku": "OT776EL09WQLCNAFAMZ", 
                "brand": "\u00a0", 
                "name": "Super Loud & Super Bass Bluetooth Sound Bar w/LCD- Grey", 
                "category": 3, 
                "link": "https://www.daraz.com.np/other-super-loud-super-bass-bluetooth-sound-bar-wlcd-grey-44661.html", 
                "image_link": "https://np.daraz.io/7m1c-7kM1gtrXK7B3UMi68SkWuU=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/16/644/1.jpg?3644", 
                "reviews": 0, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jul  1 15:14:15 2018", 
                "prices": [
                {
                    "id": 86, 
                    "price": 1899, 
                    "discount": 37, 
                    "date": "Sun Jun 24 15:53:46 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 215, 
                    "price": 1899, 
                    "discount": 37, 
                    "date": "Sun Jun 24 16:02:36 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 328, 
                    "price": 1899, 
                    "discount": 37, 
                    "date": "Wed Jun 27 18:28:30 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 422, 
                    "price": 1899, 
                    "discount": 37, 
                    "date": "Thu Jun 28 11:30:17 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 486, 
                    "price": 1899, 
                    "discount": 37, 
                    "date": "Thu Jun 28 11:33:06 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 599, 
                    "price": 1899, 
                    "discount": 37, 
                    "date": "Thu Jun 28 11:33:27 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 728, 
                    "price": 1899, 
                    "discount": 37, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 898, 
                    "price": 1899, 
                    "discount": 37, 
                    "date": "Sun Jul  1 15:14:15 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 137, 
                "sku": "OT776EL1CLQQONAFAMZ", 
                "brand": "\u00a0", 
                "name": "JY-25 Digital Screen Display Bluetooth Pill Wireless  Speaker with Mic Support Hands-free Call/FM/TF Card/USB", 
                "category": 3, 
                "link": "https://www.daraz.com.np/other-jy-25-digital-screen-display-bluetooth-pill-wireless-speaker-with-mic-support-hands-free-callfmtf-cardusb-63618.html", 
                "image_link": "https://np.daraz.io/ziYMsLnBokx9E1vlgHvpRbpwW4c=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/81/636/1.jpg?9964", 
                "reviews": 1, 
                "date_issued": "Thu Jun 28 11:30:17 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": [
                {
                    "id": 423, 
                    "price": 1075, 
                    "discount": 33, 
                    "date": "Thu Jun 28 11:30:17 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 488, 
                    "price": 1075, 
                    "discount": 33, 
                    "date": "Thu Jun 28 11:33:06 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 600, 
                    "price": 1075, 
                    "discount": 33, 
                    "date": "Thu Jun 28 11:33:27 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 736, 
                    "price": 1075, 
                    "discount": 33, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 906, 
                    "price": 1075, 
                    "discount": 33, 
                    "date": "Sun Jul  1 15:14:15 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1088, 
                    "price": 1075, 
                    "discount": 33, 
                    "date": "Sun Jul  1 17:17:16 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1221, 
                    "price": 1075, 
                    "discount": 33, 
                    "date": "Sun Jul  1 18:11:48 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 108, 
                "sku": "AA370SP0UE13WNAFAMZ", 
                "brand": "\u00a0", 
                "name": "K18S Smart Heart Rate Monitor Bluetooth 4.0 Sports Fitness Tracker ", 
                "category": 2, 
                "link": "https://www.daraz.com.np/aafno-pasal-k18s-smart-heart-rate-monitor-bluetooth-4.0-sports-fitness-tracker-134015.html", 
                "image_link": "https://np.daraz.io/vE1ucJIpvDIfm4lyYznPpPHoysk=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/51/0431/1.jpg?8574", 
                "reviews": 1, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": [
                {
                    "id": 108, 
                    "price": 2999, 
                    "discount": 63, 
                    "date": "Sun Jun 24 15:53:46 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 236, 
                    "price": 2999, 
                    "discount": 63, 
                    "date": "Sun Jun 24 16:02:36 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 540, 
                    "price": 2999, 
                    "discount": 63, 
                    "date": "Thu Jun 28 11:33:22 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 750, 
                    "price": 2999, 
                    "discount": 63, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 911, 
                    "price": 2999, 
                    "discount": 63, 
                    "date": "Sun Jul  1 15:14:15 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1090, 
                    "price": 2999, 
                    "discount": 63, 
                    "date": "Sun Jul  1 17:17:16 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1242, 
                    "price": 2999, 
                    "discount": 63, 
                    "date": "Sun Jul  1 18:11:48 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 89, 
                "sku": "AA370SP03GLF0NAFAMZ", 
                "brand": "\u00a0", 
                "name": "Goral Y5 Smartwatch Water Resistant Pulse Activity Sports Xiaomi Miband VS 2", 
                "category": 2, 
                "link": "https://www.daraz.com.np/aafno-pasal-goral-y5-smartwatch-water-resistant-pulse-activity-sports-xiaomi-miband-vs-2-131850.html", 
                "image_link": "https://np.daraz.io/-csO0XRv8G4suiBk209qbrnz-r0=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/05/8131/1.jpg?7472", 
                "reviews": 1, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Thu Jun 28 11:33:22 2018", 
                "prices": [
                {
                    "id": 89, 
                    "price": 2499, 
                    "discount": 50, 
                    "date": "Sun Jun 24 15:53:46 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 230, 
                    "price": 2499, 
                    "discount": 50, 
                    "date": "Sun Jun 24 16:02:36 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 557, 
                    "price": 2499, 
                    "discount": 50, 
                    "date": "Thu Jun 28 11:33:22 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 159, 
                "sku": "XI094EL06QWLKNAFAMZ", 
                "brand": "Xiaomi\u00a0", 
                "name": "Redmi Note 4 [3GB RAM, 32GB ROM] - Dark Grey", 
                "category": 5, 
                "link": "https://www.daraz.com.np/xiaomi-redmi-note-4-3gb-ram-32gb-rom-dark-grey-33311.html", 
                "image_link": "https://np.daraz.io/pdUO8mOuKDesePC5zAJ0t0iQl68=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/11/333/1.jpg?9009", 
                "reviews": 1, 
                "date_issued": "Sun Jul  1 14:02:28 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": [
                {
                    "id": 714, 
                    "price": 18199, 
                    "discount": 4, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 859, 
                    "price": 18199, 
                    "discount": 4, 
                    "date": "Sun Jul  1 15:14:15 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 984, 
                    "price": 18199, 
                    "discount": 4, 
                    "date": "Sun Jul  1 17:17:16 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1140, 
                    "price": 18199, 
                    "discount": 4, 
                    "date": "Sun Jul  1 18:11:48 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 151, 
                "sku": "IN072EL0WL20KNAFAMZ", 
                "brand": "Infocus \u00a0", 
                "name": "M535 (3GB RAM,16GB ROM) - Gold", 
                "category": 5, 
                "link": "https://www.daraz.com.np/infocus-m535-3gb-ram16gb-rom-gold-103745.html", 
                "image_link": "https://np.daraz.io/jI71HPnLL2iC7AqzfHSHDvbPY4c=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/54/7301/1.jpg?9093", 
                "reviews": 2, 
                "date_issued": "Sun Jul  1 14:02:28 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": [
                {
                    "id": 669, 
                    "price": 9500, 
                    "discount": 52, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 824, 
                    "price": 9500, 
                    "discount": 52, 
                    "date": "Sun Jul  1 15:14:14 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1105, 
                    "price": 9500, 
                    "discount": 52, 
                    "date": "Sun Jul  1 18:11:48 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 115, 
                "sku": "OT776EL0GFTK0NAFAMZ", 
                "brand": "\u00a0", 
                "name": "VR Shinecon Virtual Reality Headset 3D Glasses", 
                "category": 4, 
                "link": "https://www.daraz.com.np/other-vr-shinecon-virtual-reality-headset-3d-glasses-21672.html", 
                "image_link": "https://np.daraz.io/XKRAFmRykKtLGfQ6HATe-s4NFCc=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/27/612/1.jpg?5947", 
                "reviews": 0, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Thu Jun 28 11:33:28 2018", 
                "prices": [
                {
                    "id": 115, 
                    "price": 899, 
                    "discount": 14, 
                    "date": "Sun Jun 24 15:53:46 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 224, 
                    "price": 899, 
                    "discount": 14, 
                    "date": "Sun Jun 24 16:02:36 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 628, 
                    "price": 899, 
                    "discount": 14, 
                    "date": "Thu Jun 28 11:33:28 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 131, 
                "sku": "AA370SP01GKTONAFAMZ", 
                "brand": "", 
                "name": "K5 Smart Watch IP68 Waterproof Military Watch", 
                "category": 0, 
                "link": "https://www.daraz.com.np/aafno-pasal-k5-smart-watch-ip68-waterproof-military-watch-135420.html", 
                "image_link": "https://np.daraz.io/lVkndR4fSpL3Vi9DFs7QjnJ7RI0=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/02/4531/1.jpg?8404", 
                "reviews": 0, 
                "date_issued": "Wed Jun 27 18:28:30 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": [
                {
                    "id": 320, 
                    "price": 5999, 
                    "discount": 50, 
                    "date": "Wed Jun 27 18:28:30 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 551, 
                    "price": 5999, 
                    "discount": 50, 
                    "date": "Thu Jun 28 11:33:22 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 762, 
                    "price": 5999, 
                    "discount": 50, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 924, 
                    "price": 5999, 
                    "discount": 50, 
                    "date": "Sun Jul  1 15:14:15 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1094, 
                    "price": 5999, 
                    "discount": 50, 
                    "date": "Sun Jul  1 17:17:16 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1247, 
                    "price": 5999, 
                    "discount": 50, 
                    "date": "Sun Jul  1 18:11:48 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 12, 
                "sku": "OT776EL1KVD8WNAFAMZ", 
                "brand": "\u00a0", 
                "name": "Combo of VR Box + Earphone And Gaming Remote", 
                "category": 4, 
                "link": "https://www.daraz.com.np/other-combo-of-vr-box-earphone-and-gaming-remote-22559.html", 
                "image_link": "https://np.daraz.io/1TP1ThoB8F17UCsSoxGAh-saNyE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/95/522/1.jpg?6254", 
                "reviews": 4, 
                "date_issued": "Sun Jun 24 15:53:45 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": [
                {
                    "id": 12, 
                    "price": 749, 
                    "discount": 25, 
                    "date": "Sun Jun 24 15:53:45 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 128, 
                    "price": 749, 
                    "discount": 25, 
                    "date": "Sun Jun 24 16:02:36 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 247, 
                    "price": 749, 
                    "discount": 25, 
                    "date": "Wed Jun 27 18:28:30 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 347, 
                    "price": 749, 
                    "discount": 25, 
                    "date": "Thu Jun 28 11:30:16 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 428, 
                    "price": 749, 
                    "discount": 25, 
                    "date": "Thu Jun 28 11:33:05 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 601, 
                    "price": 749, 
                    "discount": 25, 
                    "date": "Thu Jun 28 11:33:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 642, 
                    "price": 749, 
                    "discount": 25, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 796, 
                    "price": 749, 
                    "discount": 25, 
                    "date": "Sun Jul  1 15:14:14 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 942, 
                    "price": 749, 
                    "discount": 25, 
                    "date": "Sun Jul  1 17:17:15 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1114, 
                    "price": 749, 
                    "discount": 25, 
                    "date": "Sun Jul  1 18:11:48 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 170, 
                "sku": "AA370SP07EWVGNAFAMZ", 
                "brand": "\u00a0", 
                "name": "N88 Smartwatch Support Heart Rate Blood Pressure Calorie Step Watch IP67 Waterproof ", 
                "category": 2, 
                "link": "https://www.daraz.com.np/aafno-pasal-n88-smartwatch-support-heart-rate-blood-pressure-calorie-step-watch-ip67-waterproof-135421.html", 
                "image_link": "https://np.daraz.io/AyE5uBWfmNi3P294VqC21XlTlJE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/12/4531/1.jpg?8522", 
                "reviews": 0, 
                "date_issued": "Sun Jul  1 14:02:28 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": [
                {
                    "id": 746, 
                    "price": 5499, 
                    "discount": 45, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 907, 
                    "price": 5499, 
                    "discount": 45, 
                    "date": "Sun Jul  1 15:14:15 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1089, 
                    "price": 5499, 
                    "discount": 45, 
                    "date": "Sun Jul  1 17:17:16 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1240, 
                    "price": 5499, 
                    "discount": 45, 
                    "date": "Sun Jul  1 18:11:48 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 185, 
                "sku": "MO694EL186MF8NAFAMZ", 
                "brand": "Motorola\u00a0", 
                "name": "Moto E4 (2GB RAM, 16GB ROM) - Gold", 
                "category": 5, 
                "link": "https://www.daraz.com.np/motorola-moto-e4-2gb-ram-16gb-rom-gold-121247.html", 
                "image_link": "https://np.daraz.io/7UQGe5SBn_FXQSQmZXUZ51H57Z0=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/74/2121/1.jpg?4389", 
                "reviews": 0, 
                "date_issued": "Sun Jul  1 14:02:28 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": [
                {
                    "id": 778, 
                    "price": 14335, 
                    "discount": 12, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 933, 
                    "price": 14335, 
                    "discount": 12, 
                    "date": "Sun Jul  1 15:14:15 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1057, 
                    "price": 14335, 
                    "discount": 12, 
                    "date": "Sun Jul  1 17:17:16 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1204, 
                    "price": 14335, 
                    "discount": 12, 
                    "date": "Sun Jul  1 18:11:48 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 175, 
                "sku": "OT776EL010WPCNAFAMZ", 
                "brand": "\u00a0", 
                "name": "Combo of VR Box & Yunteng YT 1288 Selfie Stick", 
                "category": 4, 
                "link": "https://www.daraz.com.np/other-combo-of-vr-box-yunteng-yt-1288-selfie-stick-22710.html", 
                "image_link": "https://np.daraz.io/kUdR4DQBS_PaoYmM3V0PN1wdwqo=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/01/722/1.jpg?6237", 
                "reviews": 0, 
                "date_issued": "Sun Jul  1 14:02:28 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": [
                {
                    "id": 763, 
                    "price": 849, 
                    "discount": 23, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 910, 
                    "price": 849, 
                    "discount": 23, 
                    "date": "Sun Jul  1 15:14:15 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1029, 
                    "price": 849, 
                    "discount": 23, 
                    "date": "Sun Jul  1 17:17:16 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1235, 
                    "price": 849, 
                    "discount": 23, 
                    "date": "Sun Jul  1 18:11:48 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 8, 
                "sku": "OT776EL0YYM6ONAFAMZ", 
                "brand": "\u00a0", 
                "name": "Black OTG Cable for Mobile Phones", 
                "category": 1, 
                "link": "https://www.daraz.com.np/other-black-otg-cable-for-mobile-phones-22785.html", 
                "image_link": "https://np.daraz.io/di2I0SVsVIpUvclbcr1cBqqhvuU=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/58/722/1.jpg?7454", 
                "reviews": 2, 
                "date_issued": "Sun Jun 24 15:53:45 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": [
                {
                    "id": 8, 
                    "price": 69, 
                    "discount": 66, 
                    "date": "Sun Jun 24 15:53:45 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 129, 
                    "price": 69, 
                    "discount": 66, 
                    "date": "Sun Jun 24 16:02:36 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 259, 
                    "price": 69, 
                    "discount": 66, 
                    "date": "Wed Jun 27 18:28:30 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 345, 
                    "price": 69, 
                    "discount": 66, 
                    "date": "Thu Jun 28 11:30:16 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 441, 
                    "price": 69, 
                    "discount": 66, 
                    "date": "Thu Jun 28 11:33:05 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 513, 
                    "price": 69, 
                    "discount": 66, 
                    "date": "Thu Jun 28 11:33:22 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 643, 
                    "price": 69, 
                    "discount": 66, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 791, 
                    "price": 69, 
                    "discount": 66, 
                    "date": "Sun Jul  1 15:14:14 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 956, 
                    "price": 69, 
                    "discount": 66, 
                    "date": "Sun Jul  1 17:17:15 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1110, 
                    "price": 69, 
                    "discount": 66, 
                    "date": "Sun Jul  1 18:11:48 2018", 
                    "currency": "NPR"
                }
                ]
            }, 
            {
                "id": 34, 
                "sku": "OT776EL0NIO0KNAFAMZ", 
                "brand": "\u00a0", 
                "name": "Samsung Gear S2 Gear Sport Tempered Glass Screen Protector High Definition", 
                "category": 2, 
                "link": "https://www.daraz.com.np/other-samsung-gear-s2-gear-sport-tempered-glass-screen-protector-high-definition-120593.html", 
                "image_link": "https://np.daraz.io/uASfn9glBj813C1xtexs14Vfjzw=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/39/5021/1.jpg?5276", 
                "reviews": 0, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": [
                {
                    "id": 34, 
                    "price": 500, 
                    "discount": 38, 
                    "date": "Sun Jun 24 15:53:46 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 156, 
                    "price": 500, 
                    "discount": 38, 
                    "date": "Sun Jun 24 16:02:36 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 271, 
                    "price": 500, 
                    "discount": 38, 
                    "date": "Wed Jun 27 18:28:30 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 410, 
                    "price": 500, 
                    "discount": 38, 
                    "date": "Thu Jun 28 11:30:17 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 463, 
                    "price": 500, 
                    "discount": 38, 
                    "date": "Thu Jun 28 11:33:05 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 516, 
                    "price": 500, 
                    "discount": 38, 
                    "date": "Thu Jun 28 11:33:22 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 679, 
                    "price": 500, 
                    "discount": 38, 
                    "date": "Sun Jul  1 14:02:28 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 845, 
                    "price": 500, 
                    "discount": 38, 
                    "date": "Sun Jul  1 15:14:15 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1048, 
                    "price": 500, 
                    "discount": 38, 
                    "date": "Sun Jul  1 17:17:16 2018", 
                    "currency": "NPR"
                }, 
                {
                    "id": 1177, 
                    "price": 500, 
                    "discount": 38, 
                    "date": "Sun Jul  1 18:11:48 2018", 
                    "currency": "NPR"
                }
                ]
            }
            ]
        }
    }

    recieved_data_WonePrice = {
        "type": 200, 
        "status_code": 1, 
        "status_message": "Everything's working properly", 
        "data": {
            "category": [
            {
                "id": 1, 
                "category": "Accessories", 
                "sub_category": "Cables"
            }, 
            {
                "id": 2, 
                "category": "Gadgets", 
                "sub_category": "Smartwatches"
            }, 
            {
                "id": 3, 
                "category": "Gadgets", 
                "sub_category": "Wireless Speakers"
            }, 
            {
                "id": 4, 
                "category": "Gadgets", 
                "sub_category": "VR Headsets"
            }, 
            {
                "id": 5, 
                "category": "Mobile phones", 
                "sub_category": "Smartphones"
            }
            ], 
            "products": [
            {
                "id": 141, 
                "sku": "OT776SP0BRDL8NAFAMZ", 
                "brand": "\u00a0", 
                "name": "K2 Bluetooth Smart Watch-Black", 
                "category": 2, 
                "link": "https://www.daraz.com.np/other-k2-bluetooth-smart-watch-black-135791.html", 
                "image_link": "https://np.daraz.io/d3zcH25E-LNr1wGT4MlilplB9gU=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/19/7531/1.jpg?2057", 
                "reviews": 0, 
                "date_issued": "Sun Jul  1 14:02:28 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": {
                "price": 3499, 
                "discount": 65, 
                "date": "Sun Jul  1 18:11:48 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 31, 
                "sku": "OT776OT1AFLGWNAFAMZ", 
                "brand": "\u00a0", 
                "name": "USB To Ethernet Converter Cable", 
                "category": 1, 
                "link": "https://www.daraz.com.np/other-usb-to-ethernet-converter-cable-9977.html", 
                "image_link": "https://np.daraz.io/CXc_ER2FbXqJZSitFAChKPh5E30=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/77/99/1.jpg?4186", 
                "reviews": 0, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": {
                "price": 335, 
                "discount": 33, 
                "date": "Sun Jul  1 18:11:48 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 172, 
                "sku": "OB756EL1IRYQONAFAMZ", 
                "brand": "OBI\u00a0", 
                "name": "SF1 (3GB RAM, 32GB ROM) -Black", 
                "category": 5, 
                "link": "https://www.daraz.com.np/sf1-smartphone-3gb-ram-32gb-rom-black-obi-mpg25.html", 
                "image_link": "https://np.daraz.io/kXHAKMuTEm7XnzsVsr5JV_y2T3A=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/92/004/1.jpg?2703", 
                "reviews": 13, 
                "date_issued": "Sun Jul  1 14:02:28 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": {
                "price": 12000, 
                "discount": 49, 
                "date": "Sun Jul  1 18:11:48 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 101, 
                "sku": "OT776EL062JA8NAFAMZ", 
                "brand": "\u00a0", 
                "name": "Combo of VR Box With Gaming Remote Controller and  Earphone", 
                "category": 4, 
                "link": "https://www.daraz.com.np/other-combo-of-vr-box-with-gaming-remote-controller-and-earphone-69101.html", 
                "image_link": "https://np.daraz.io/S2ldOvluhBl7Wrk9uEu57AoG3uA=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/10/196/1.jpg?3447", 
                "reviews": 0, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": {
                "price": 1450, 
                "discount": 19, 
                "date": "Sun Jul  1 18:11:48 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 176, 
                "sku": "OT776OT07QF5CNAFAMZ", 
                "brand": "\u00a0", 
                "name": "Laptop Power Cable", 
                "category": 1, 
                "link": "https://www.daraz.com.np/other-laptop-power-cable-9921.html", 
                "image_link": "https://np.daraz.io/mJDauNcWO1BXIDg8I8qtMQatBaI=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/12/99/1.jpg?5554", 
                "reviews": 0, 
                "date_issued": "Sun Jul  1 14:02:28 2018", 
                "date_updated": "Sun Jul  1 17:17:16 2018", 
                "prices": {
                "price": 99, 
                "discount": 50, 
                "date": "Sun Jul  1 17:17:16 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 10, 
                "sku": "OT776EL101CH4NAFAMZ", 
                "brand": "\u00a0", 
                "name": "HDMI Cable (1.5m)", 
                "category": 1, 
                "link": "https://www.daraz.com.np/other-hdmi-cable-1.5m-92506.html", 
                "image_link": "https://np.daraz.io/0Vy0v_Pm1hvAmvTkWI3qKDOS6xE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/60/529/1.jpg?8924", 
                "reviews": 0, 
                "date_issued": "Sun Jun 24 15:53:45 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": {
                "price": 125, 
                "discount": 17, 
                "date": "Sun Jul  1 18:11:48 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 156, 
                "sku": "SO640EL1C1XUSNAFAMZ", 
                "brand": "SOMHO\u00a0", 
                "name": "S-311 Portable Bluetooth Speaker-Red", 
                "category": 3, 
                "link": "https://www.daraz.com.np/somho-s-311-portable-bluetooth-speaker-red-121708.html", 
                "image_link": "https://np.daraz.io/WXZFO02T_6Ae9_zaFqYgfCMI_Gw=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/80/7121/1.jpg?9397", 
                "reviews": 0, 
                "date_issued": "Sun Jul  1 14:02:28 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": {
                "price": 1699, 
                "discount": 4, 
                "date": "Sun Jul  1 18:11:48 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 52, 
                "sku": "OT776EL0ZDSK4NAFAMZ", 
                "brand": "\u00a0", 
                "name": "Apple Macbook Pro Type-C Hub Adapter 7 in 1 With HDMI", 
                "category": 1, 
                "link": "https://www.daraz.com.np/other-apple-macbook-pro-type-c-hub-adapter-7-in-1-with-hdmi-103495.html", 
                "image_link": "https://np.daraz.io/NsGiPsWa7ygxlJB_ttcOHUkbwZA=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/59/4301/1.jpg?5538", 
                "reviews": 0, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": {
                "price": 4199, 
                "discount": 16, 
                "date": "Sun Jul  1 18:11:48 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 41, 
                "sku": "OT776EL1D8P4ONAFAMZ", 
                "brand": "\u00a0", 
                "name": "VR Box Shinecon , Bluetooth Gaming Remote & Earphone", 
                "category": 4, 
                "link": "https://www.daraz.com.np/other-vr-box-shinecon-bluetooth-gaming-remote-earphone-70728.html", 
                "image_link": "https://np.daraz.io/yNIihngH3UmMFd5rLym4l7OxCVI=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/82/707/1.jpg?7046", 
                "reviews": 1, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": {
                "price": 1449, 
                "discount": 24, 
                "date": "Sun Jul  1 18:11:48 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 140, 
                "sku": "XI094EL1CMIIONAFAMZ", 
                "brand": "Xiaomi\u00a0", 
                "name": "Redmi Note 4 [4GB RAM, 64GB ROM] - Black", 
                "category": 5, 
                "link": "https://www.daraz.com.np/xiaomi-redmi-note-4-4gb-ram-64gb-rom-black-27618.html", 
                "image_link": "https://np.daraz.io/bS-uqm1Pp4sXPKhSj0bOSFPRr8w=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/81/672/1.jpg?4589", 
                "reviews": 8, 
                "date_issued": "Sun Jul  1 14:02:28 2018", 
                "date_updated": "Sun Jul  1 18:11:47 2018", 
                "prices": {
                "price": 20115, 
                "discount": 4, 
                "date": "Sun Jul  1 18:11:47 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 129, 
                "sku": "OT776EL0I94MWNAFAMZ", 
                "brand": "", 
                "name": "USB 2.0 Type A Male to A Female Extension Cable 3 Meter - Black", 
                "category": 1, 
                "link": "https://www.daraz.com.np/other-usb-2.0-type-a-male-to-a-female-extension-cable-3-meter-black-95603.html", 
                "image_link": "https://np.daraz.io/a5uzgsRy6G7CAWuRcCFTC9AkFBM=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/30/659/1.jpg?1285", 
                "reviews": 0, 
                "date_issued": "Wed Jun 27 18:28:30 2018", 
                "date_updated": "Thu Jun 28 11:33:22 2018", 
                "prices": {
                "price": 149, 
                "discount": 25, 
                "date": "Thu Jun 28 11:33:22 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 78, 
                "sku": "OT776EL0NE6O8NAFAMZ", 
                "brand": "\u00a0", 
                "name": "RJ45 Ethernet cable connector, F-to-F type, Almond color", 
                "category": 1, 
                "link": "https://www.daraz.com.np/other-rj45-ethernet-cable-connector-f-to-f-type-almond-color-39293.html", 
                "image_link": "https://np.daraz.io/_fW-AnlBnO5yZd1hhuGH1q89H-k=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/39/293/1.jpg?6464", 
                "reviews": 0, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": {
                "price": 149, 
                "discount": 70, 
                "date": "Sun Jul  1 18:11:48 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 64, 
                "sku": "OT776EL0XD3YWNAFAMZ", 
                "brand": "\u00a0", 
                "name": "New Design WS-Y66B Portable Bluetooth Speaker", 
                "category": 3, 
                "link": "https://www.daraz.com.np/other-new-design-ws-y66b-portable-bluetooth-speaker-93065.html", 
                "image_link": "https://np.daraz.io/9ueIZm4QtbQfA_m1ubJ__soiM7Q=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/56/039/1.jpg?1887", 
                "reviews": 0, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": {
                "price": 899, 
                "discount": 10, 
                "date": "Sun Jul  1 18:11:48 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 183, 
                "sku": "GI401EL14SORGNAFAMZ", 
                "brand": "Gionee\u00a0", 
                "name": "S11 Lite (4GB RAM, 32GB ROM) 5.7\"-Black", 
                "category": 5, 
                "link": "https://www.daraz.com.np/gionee-s11-lite-4gb-ram-32gb-rom-5.7-black-132586.html", 
                "image_link": "https://np.daraz.io/Uv4PIlpeWdp90RHZP6ESPaEU_Ik=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/68/5231/1.jpg?6125", 
                "reviews": 1, 
                "date_issued": "Sun Jul  1 14:02:28 2018", 
                "date_updated": "Sun Jul  1 17:17:16 2018", 
                "prices": {
                "price": 18500, 
                "discount": 29, 
                "date": "Sun Jul  1 17:17:16 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 40, 
                "sku": "AA370FA09EXGSNAFAMZ", 
                "brand": "\u00a0", 
                "name": "S2 Smart Watch", 
                "category": 2, 
                "link": "https://www.daraz.com.np/aafno-pasal-s2-smart-watch-131851.html", 
                "image_link": "https://np.daraz.io/2CEx_tcxFl2xWd5PssrecFtVi9U=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/15/8131/1.jpg?7670", 
                "reviews": 0, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jun 24 16:02:36 2018", 
                "prices": {
                "price": 6999, 
                "discount": 53, 
                "date": "Sun Jun 24 16:02:36 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 174, 
                "sku": "ZO121EL19CBW0NAFAMZ", 
                "brand": "Zopo\u00a0", 
                "name": "Speed X Dual Camera Smartphone (3GB RAM, 32GB ROM)- Gold", 
                "category": 5, 
                "link": "https://www.daraz.com.np/zopo-speed-x-dual-camera-smartphone-3gb-ram-32gb-rom-gold-85167.html", 
                "image_link": "https://np.daraz.io/Zd-ylnQ_KlveITNaO2e0SZX4ce0=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/76/158/1.jpg?4191", 
                "reviews": 5, 
                "date_issued": "Sun Jul  1 14:02:28 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": {
                "price": 11900, 
                "discount": 43, 
                "date": "Sun Jul  1 18:11:48 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 124, 
                "sku": "OT776EL15DO5WNAFAMZ", 
                "brand": "", 
                "name": "Citizen Watch BM8475 Tempered Glass Screen Protector", 
                "category": 0, 
                "link": "https://www.daraz.com.np/other-citizen-watch-bm8475-tempered-glass-screen-protector-120596.html", 
                "image_link": "https://np.daraz.io/EuvwMA2hUn3NjmRULjjueVyjwRg=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/69/5021/1.jpg?5396", 
                "reviews": 0, 
                "date_issued": "Wed Jun 27 18:28:30 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": {
                "price": 500, 
                "discount": 38, 
                "date": "Sun Jul  1 18:11:48 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 121, 
                "sku": "OT776EL0TH02CNAFAMZ", 
                "brand": "\u00a0", 
                "name": "Garmin Fenix Chronos Tempered Glass Screen Protector 2.5D High Definition 9H", 
                "category": 2, 
                "link": "https://www.daraz.com.np/other-garmin-fenix-chronos-tempered-glass-screen-protector-2.5d-high-definition-9h-120594.html", 
                "image_link": "https://np.daraz.io/lfTqZV0f94MEr_N5tEWzpXY6QyU=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/49/5021/1.jpg?5315", 
                "reviews": 0, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jun 24 16:02:36 2018", 
                "prices": {
                "price": 500, 
                "discount": 38, 
                "date": "Sun Jun 24 16:02:36 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 73, 
                "sku": "OT776EL0GIOY8NAFAMZ", 
                "brand": "\u00a0", 
                "name": "HF - Q3 Speaker Wireless Bluetooth 2.1", 
                "category": 3, 
                "link": "https://www.daraz.com.np/other-hf-q3-speaker-wireless-bluetooth-2.1-64772.html", 
                "image_link": "https://np.daraz.io/tSW3WJE6FmVhsbyw5Nih4Mrjda4=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/27/746/1.jpg?3266", 
                "reviews": 0, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": {
                "price": 1150, 
                "discount": 21, 
                "date": "Sun Jul  1 18:11:48 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 33, 
                "sku": "WS638EL1EYIIKNAFAMZ", 
                "brand": "WSTER\u00a0", 
                "name": "WS Y66B Portable Speaker Box-Grey", 
                "category": 3, 
                "link": "https://www.daraz.com.np/wster-ws-y66b-portable-speaker-box-grey-119558.html", 
                "image_link": "https://np.daraz.io/m53cKM8ltVD3uWVsuWJCGy4HgbA=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/85/5911/1.jpg?0113", 
                "reviews": 0, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": {
                "price": 899, 
                "discount": 10, 
                "date": "Sun Jul  1 18:11:48 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 120, 
                "sku": "OT776EL0C9KOKNAFAMZ", 
                "brand": "\u00a0", 
                "name": "Citizen Watch NY0040-09EE Tempered Glass Screen Protector", 
                "category": 2, 
                "link": "https://www.daraz.com.np/other-citizen-watch-ny0040-09ee-tempered-glass-screen-protector-120602.html", 
                "image_link": "https://np.daraz.io/p2AAc5SCTyr3gNQ5M4DXqogDW7E=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/20/6021/1.jpg?5516", 
                "reviews": 0, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Thu Jun 28 11:33:22 2018", 
                "prices": {
                "price": 500, 
                "discount": 38, 
                "date": "Thu Jun 28 11:33:22 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 154, 
                "sku": "GI401EL0EYLNSNAFAMZ", 
                "brand": "Gionee\u00a0", 
                "name": "A1 Lite Smart Mobile Phone (32GB ROM + 3GB RAM) 5.3\" - Gold", 
                "category": 5, 
                "link": "https://www.daraz.com.np/gionee-a1-lite-smart-mobile-phone-32gb-rom-3gb-ram-5.3-gold-92152.html", 
                "image_link": "https://np.daraz.io/HX9pNeja1rQN_7x0Qh1cndiSiFg=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/25/129/1.jpg?4929", 
                "reviews": 3, 
                "date_issued": "Sun Jul  1 14:02:28 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": {
                "price": 16400, 
                "discount": 37, 
                "date": "Sun Jul  1 18:11:48 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 112, 
                "sku": "WA285EL0J7Z9KNAFAMZ", 
                "brand": "\u00a0", 
                "name": "Apple Watch Strap With Metal Cover & Adjustable Magnetic Closure Clasp", 
                "category": 2, 
                "link": "https://www.daraz.com.np/waiwaiparts-apple-watch-strap-with-metal-cover-adjustable-magnetic-closure-clasp-58223.html", 
                "image_link": "https://np.daraz.io/zZCGoUdvjIrmry0cl4xJVX8rtow=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/32/285/1.jpg?1353", 
                "reviews": 0, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": {
                "price": 1800, 
                "discount": 40, 
                "date": "Sun Jul  1 18:11:48 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 118, 
                "sku": "GE203EL0EJ1H4NAFAMZ", 
                "brand": "\u00a0", 
                "name": "GT08 Bluetooth 3.0 Smart Watch with Camera SIM", 
                "category": 2, 
                "link": "https://www.daraz.com.np/bestdeals-gt08-bluetooth-3.0-smart-watch-with-camera-sim-30442.html", 
                "image_link": "https://np.daraz.io/BuSrcbpP81n-EMQ-3eCKQuRaPSc=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/24/403/1.jpg?4145", 
                "reviews": 5, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jun 24 16:02:36 2018", 
                "prices": {
                "price": 1099, 
                "discount": 50, 
                "date": "Sun Jun 24 16:02:36 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 110, 
                "sku": "ON440EL0VE0MSNAFAMZ", 
                "brand": "\u00a0", 
                "name": "X6 Bluetooth Smartwatch With Camera Support SIM Card", 
                "category": 2, 
                "link": "https://www.daraz.com.np/onlineshopgroup-x6-bluetooth-smartwatch-with-camera-support-sim-card-122725.html", 
                "image_link": "https://np.daraz.io/rKLKH1-y9hOp5CdLuqhBDnrNstI=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/52/7221/1.jpg?8429", 
                "reviews": 0, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Thu Jun 28 11:33:22 2018", 
                "prices": {
                "price": 1699, 
                "discount": 55, 
                "date": "Thu Jun 28 11:33:22 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 170, 
                "sku": "AA370SP07EWVGNAFAMZ", 
                "brand": "\u00a0", 
                "name": "N88 Smartwatch Support Heart Rate Blood Pressure Calorie Step Watch IP67 Waterproof ", 
                "category": 2, 
                "link": "https://www.daraz.com.np/aafno-pasal-n88-smartwatch-support-heart-rate-blood-pressure-calorie-step-watch-ip67-waterproof-135421.html", 
                "image_link": "https://np.daraz.io/AyE5uBWfmNi3P294VqC21XlTlJE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/12/4531/1.jpg?8522", 
                "reviews": 0, 
                "date_issued": "Sun Jul  1 14:02:28 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": {
                "price": 5499, 
                "discount": 45, 
                "date": "Sun Jul  1 18:11:48 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 53, 
                "sku": "OT776EL0UOGVONAFAMZ", 
                "brand": "\u00a0", 
                "name": "Mini Bluetooth Speaker - White", 
                "category": 3, 
                "link": "https://www.daraz.com.np/other-mini-bluetooth-speaker-white-103515.html", 
                "image_link": "https://np.daraz.io/7RfeBuBuGz-yRhOSEcVIG9BMw6Q=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/51/5301/1.jpg?7938", 
                "reviews": 1, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Thu Jun 28 11:33:27 2018", 
                "prices": {
                "price": 377, 
                "discount": 46, 
                "date": "Thu Jun 28 11:33:27 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 56, 
                "sku": "OT776OT0W5FFSNAFAMZ", 
                "brand": "\u00a0", 
                "name": "HDMI-HDMI 10 Meter Cable", 
                "category": 1, 
                "link": "https://www.daraz.com.np/other-hdmi-hdmi-10-meter-cable-10045.html", 
                "image_link": "https://np.daraz.io/xiEiWQ2TIi49_9csF_2suZYWPqw=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/54/001/1.jpg?1087", 
                "reviews": 1, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": {
                "price": 599, 
                "discount": 8, 
                "date": "Sun Jul  1 18:11:48 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 18, 
                "sku": "JB523EL135AN8NAFAMZ", 
                "brand": "JBL\u00a0", 
                "name": "JBLGO2BLU Portable Bluetooth Speaker - Blue", 
                "category": 3, 
                "link": "https://www.daraz.com.np/jbl-jblgo2blu-portable-bluetooth-speaker-blue-125756.html", 
                "image_link": "https://np.daraz.io/juQuOHu8aJbxN4R5Wiu-av9-sg8=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/65/7521/1.jpg?3649", 
                "reviews": 0, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": {
                "price": 4225, 
                "discount": 6, 
                "date": "Sun Jul  1 18:11:48 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 169, 
                "sku": "MI094EL01RAMKNAFAMZ", 
                "brand": "Xiaomi\u00a0", 
                "name": "Redmi 4A [2GB RAM, 32GB ROM] - Gold", 
                "category": 5, 
                "link": "https://www.daraz.com.np/xiaomi-redmi-4a-2gb-ram-32gb-rom-gold-135920.html", 
                "image_link": "https://np.daraz.io/6uh0_qZllFUPLBTAsEVfHOgqH_Y=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/02/9531/1.jpg?4864", 
                "reviews": 0, 
                "date_issued": "Sun Jul  1 14:02:28 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": {
                "price": 12725, 
                "discount": 2, 
                "date": "Sun Jul  1 18:11:48 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 58, 
                "sku": "OT776OT1IRWFCNAFAMZ", 
                "brand": "\u00a0", 
                "name": "VGA-VGA Cable 10 meter", 
                "category": 1, 
                "link": "https://www.daraz.com.np/other-vga-vga-cable-10-meter-10029.html", 
                "image_link": "https://np.daraz.io/H1LP6ZfVAOhLPab2Z1UG48Owwqw=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/92/001/1.jpg?3952", 
                "reviews": 0, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": {
                "price": 899, 
                "discount": 29, 
                "date": "Sun Jul  1 18:11:48 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 190, 
                "sku": "LE599EL16114WNAFAMZ", 
                "brand": "Lenovo\u00a0", 
                "name": "RocStar A319 (4GB ROM, 512MB RAM)- Black", 
                "category": 5, 
                "link": "https://www.daraz.com.np/lenovo-rocstar-a319-4gb-rom-512mb-ram-black-29507.html", 
                "image_link": "https://np.daraz.io/j7qPvoLHV3XuzgP_h7a-ZzNfJ4I=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/70/592/1.jpg?9431", 
                "reviews": 1, 
                "date_issued": "Sun Jul  1 14:02:28 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": {
                "price": 4120, 
                "discount": 39, 
                "date": "Sun Jul  1 18:11:48 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 98, 
                "sku": "OT776EL0WFWR4NAFAMZ", 
                "brand": "\u00a0", 
                "name": "VR Box With Bluetooth Control Gamepad", 
                "category": 4, 
                "link": "https://www.daraz.com.np/other-vr-box-with-bluetooth-control-gamepad-9445.html", 
                "image_link": "https://np.daraz.io/PUYlGVIm2ll3UF-9xS1_Wonq_mg=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/54/49/1.jpg?7450", 
                "reviews": 0, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": {
                "price": 799, 
                "discount": 43, 
                "date": "Sun Jul  1 18:11:48 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 17, 
                "sku": "ON440EL0GHR2SNAFAMZ", 
                "brand": "\u00a0", 
                "name": "Lightning 8-Pin To HDMI Female Video Adapter With Micro USB Charging Cable", 
                "category": 1, 
                "link": "https://www.daraz.com.np/onlineshopgroup-lightning-8-pin-to-hdmi-female-video-adapter-with-micro-usb-charging-cable-120772.html", 
                "image_link": "https://np.daraz.io/Ro0sbdOVotlM-CegLl4c8oUMJDE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/27/7021/1.jpg?8515", 
                "reviews": 0, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": {
                "price": 1499, 
                "discount": 32, 
                "date": "Sun Jul  1 18:11:48 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 130, 
                "sku": "AA370SP1CHTM4NAFAMZ", 
                "brand": "", 
                "name": "KW18 Smartwatch Phone support TF SIM Card Heart Rate", 
                "category": 0, 
                "link": "https://www.daraz.com.np/aafno-pasal-kw18-smartwatch-phone-support-tf-sim-card-heart-rate-135418.html", 
                "image_link": "https://np.daraz.io/ysogQZyIQE2SaeWLpNIthdQhgQ8=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/81/4531/1.jpg?8322", 
                "reviews": 0, 
                "date_issued": "Wed Jun 27 18:28:30 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": {
                "price": 6999, 
                "discount": 53, 
                "date": "Sun Jul  1 18:11:48 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 161, 
                "sku": "SA884EL10C34KNAFAMZ", 
                "brand": "Samsung\u00a0", 
                "name": "SM-G965F Galaxy S9+ (6GB RAM, 64GB ROM) - Black", 
                "category": 5, 
                "link": "https://www.daraz.com.np/samsung-sm-g965f-galaxy-s9-6gb-ram-64gb-rom-black-103016.html", 
                "image_link": "https://np.daraz.io/dG63dn5szDUmgqPbhdpdh3oojOc=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/61/0301/1.jpg?8956", 
                "reviews": 1, 
                "date_issued": "Sun Jul  1 14:02:28 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": {
                "price": 96000, 
                "discount": 4, 
                "date": "Sun Jul  1 18:11:48 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 44, 
                "sku": "OT776EL17AGXSNAFAMZ", 
                "brand": "\u00a0", 
                "name": "I6 Smartwatch With Sim And Micro Sd Slot", 
                "category": 2, 
                "link": "https://www.daraz.com.np/other-i6-smartwatch-with-sim-and-micro-sd-slot-21727.html", 
                "image_link": "https://np.daraz.io/ZDGDj8x3XluFG2rDauGqvm84NYY=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/72/712/1.jpg?5975", 
                "reviews": 16, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": {
                "price": 1088, 
                "discount": 56, 
                "date": "Sun Jul  1 18:11:48 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 63, 
                "sku": "OT776EL13L5K0NAFAMZ", 
                "brand": "\u00a0", 
                "name": "I7 Bluetooth Smartwatch", 
                "category": 2, 
                "link": "https://www.daraz.com.np/other-i7-bluetooth-smartwatch-29466.html", 
                "image_link": "https://np.daraz.io/ybxI-3UXx-Sc-meU5GQSkK5bugE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/66/492/1.jpg?6748", 
                "reviews": 11, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": {
                "price": 1099, 
                "discount": 56, 
                "date": "Sun Jul  1 18:11:48 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 182, 
                "sku": "OT776EL1A9MYONAFAMZ", 
                "brand": "\u00a0", 
                "name": "VR Shinecon 3D Glasses + Wireless Remote Control Gamepad", 
                "category": 4, 
                "link": "https://www.daraz.com.np/bestdeals-vr-shinecon-3d-glasses-wireless-remote-control-gamepad-21777.html", 
                "image_link": "https://np.daraz.io/xctprPaSOnDFnqO-FEtHjeWvsoM=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/77/712/1.jpg?6130", 
                "reviews": 0, 
                "date_issued": "Sun Jul  1 14:02:28 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": {
                "price": 1149, 
                "discount": 35, 
                "date": "Sun Jul  1 18:11:48 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 122, 
                "sku": "OT776EL1B4E7SNAFAMZ", 
                "brand": "\u00a0", 
                "name": "X6 Bluetooth Smart Watch With Camera SIM Memory Card - (White/Black)", 
                "category": 2, 
                "link": "https://www.daraz.com.np/other-x6-bluetooth-smart-watch-with-camera-sim-memory-card-whiteblack-74197.html", 
                "image_link": "https://np.daraz.io/Rbu6yCJV-EarDY3sSQOqzLuRyvQ=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/79/147/1.jpg?8287", 
                "reviews": 2, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jun 24 16:02:36 2018", 
                "prices": {
                "price": 2500, 
                "discount": 29, 
                "date": "Sun Jun 24 16:02:36 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 93, 
                "sku": "OT776EL1JI138NAFAMZ", 
                "brand": "\u00a0", 
                "name": "X2 Smart Watch Bluetooth Sport Fitness Tracker Heart Rate", 
                "category": 2, 
                "link": "https://www.daraz.com.np/other-x2-smart-watch-bluetooth-sport-fitness-tracker-heart-rate-102239.html", 
                "image_link": "https://np.daraz.io/7Cb-Vq1XdMAXmU0c_kgSI7DsAos=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/93/2201/1.jpg?3696", 
                "reviews": 0, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jun 24 16:02:36 2018", 
                "prices": {
                "price": 4499, 
                "discount": 20, 
                "date": "Sun Jun 24 16:02:36 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 32, 
                "sku": "OT776EL1LW8HGNAFAMZ", 
                "brand": "\u00a0", 
                "name": "All-in-1 Combo Hub With Card Readers & USB Ports", 
                "category": 1, 
                "link": "https://www.daraz.com.np/other-all-in-1-combo-hub-with-card-readers-usb-ports-124279.html", 
                "image_link": "https://np.daraz.io/GKKwE3Ki4G3wx20nJZx5PXuGx0I=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/97/2421/1.jpg?1597", 
                "reviews": 0, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": {
                "price": 380, 
                "discount": 11, 
                "date": "Sun Jul  1 18:11:48 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 185, 
                "sku": "MO694EL186MF8NAFAMZ", 
                "brand": "Motorola\u00a0", 
                "name": "Moto E4 (2GB RAM, 16GB ROM) - Gold", 
                "category": 5, 
                "link": "https://www.daraz.com.np/motorola-moto-e4-2gb-ram-16gb-rom-gold-121247.html", 
                "image_link": "https://np.daraz.io/7UQGe5SBn_FXQSQmZXUZ51H57Z0=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/74/2121/1.jpg?4389", 
                "reviews": 0, 
                "date_issued": "Sun Jul  1 14:02:28 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": {
                "price": 14335, 
                "discount": 12, 
                "date": "Sun Jul  1 18:11:48 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 173, 
                "sku": "ZO121EL1DYQPGNAFAMZ", 
                "brand": "Zopo\u00a0", 
                "name": "Flash X Plus (3GB RAM, 32GB ROM)- Gold", 
                "category": 5, 
                "link": "https://www.daraz.com.np/zopo-flash-x-plus-3gb-ram-32gb-rom-gold-122938.html", 
                "image_link": "https://np.daraz.io/5O2gpkRMAQth0RPzcx2bL-iM6u8=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/83/9221/1.jpg?6666", 
                "reviews": 1, 
                "date_issued": "Sun Jul  1 14:02:28 2018", 
                "date_updated": "Sun Jul  1 17:17:16 2018", 
                "prices": {
                "price": 11999, 
                "discount": 47, 
                "date": "Sun Jul  1 17:17:16 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 19, 
                "sku": "OT776EL0JLF28NAFAMZ", 
                "brand": "\u00a0", 
                "name": "VR Box Pro-3D Glasses Virtual Reality With Remote", 
                "category": 4, 
                "link": "https://www.daraz.com.np/other-vr-box-pro-3d-glasses-virtual-reality-with-remote-21923.html", 
                "image_link": "https://np.daraz.io/pXi9zfRaMJKHNYkaKkHBb-w9oLE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/32/912/1.jpg?6101", 
                "reviews": 0, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": {
                "price": 750, 
                "discount": 63, 
                "date": "Sun Jul  1 18:11:48 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 180, 
                "sku": "OT776EL1MATVCNAFAMZ", 
                "brand": "\u00a0", 
                "name": "DZ09 Smart Mobile Watch-Silver with VR Box and Remote", 
                "category": 4, 
                "link": "https://www.daraz.com.np/other-dz09-smart-mobile-watch-silver-with-vr-box-and-remote-32979.html", 
                "image_link": "https://np.daraz.io/U1lmWOnwfCLH5Hrw_Hh19bhtXNI=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/97/923/1.jpg?8464", 
                "reviews": 1, 
                "date_issued": "Sun Jul  1 14:02:28 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": {
                "price": 1800, 
                "discount": 28, 
                "date": "Sun Jul  1 18:11:48 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 138, 
                "sku": "OT776EL1FR27SNAFAMZ", 
                "brand": "\u00a0", 
                "name": "VR 2.0 Pack of 3 - VR Box 2 3D With Bluetooth Joystick Remote & Zipper Earphone", 
                "category": 4, 
                "link": "https://www.daraz.com.np/other-vr-2.0-pack-of-3-vr-box-2-3d-with-bluetooth-joystick-remote-zipper-earphone-32968.html", 
                "image_link": "https://np.daraz.io/KCghevF4Yxy4kZmH66X6V8tXUX0=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/86/923/1.jpg?8163", 
                "reviews": 3, 
                "date_issued": "Thu Jun 28 11:33:28 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": {
                "price": 850, 
                "discount": 43, 
                "date": "Sun Jul  1 18:11:48 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 66, 
                "sku": "ON440EL0YL2LWNAFAMZ", 
                "brand": "\u00a0", 
                "name": "Smartwatch - IOS/Android - White", 
                "category": 2, 
                "link": "https://www.daraz.com.np/onlineshopgroup-smartwatch-iosandroid-white-109085.html", 
                "image_link": "https://np.daraz.io/Gf7CYoY5pfzzKteLDQN5vfrMHJE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/58/0901/1.jpg?1676", 
                "reviews": 2, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": {
                "price": 1499, 
                "discount": 35, 
                "date": "Sun Jul  1 18:11:48 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 143, 
                "sku": "WK851EL06EGDGNAFAMZ", 
                "brand": "W-KING\u00a0", 
                "name": "S20 Portable Waterproof Bluetooth Super Bass Loudspeaker- Blue", 
                "category": 3, 
                "link": "https://www.daraz.com.np/w-king-s20-portable-waterproof-bluetooth-super-bass-loudspeaker-blue-125701.html", 
                "image_link": "https://np.daraz.io/ebgVJpNvE7Rmw_yqRQ-SMBqwTeY=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/10/7521/1.jpg?0130", 
                "reviews": 1, 
                "date_issued": "Sun Jul  1 14:02:28 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": {
                "price": 2599, 
                "discount": 38, 
                "date": "Sun Jul  1 18:11:48 2018", 
                "currency": "NPR"
                }
            }, 
            {
                "id": 88, 
                "sku": "OT776EL1ESQ6KNAFAMZ", 
                "brand": "\u00a0", 
                "name": "VGA to HDMI Video & Audio Converter Adapter", 
                "category": 1, 
                "link": "https://www.daraz.com.np/other-vga-to-hdmi-video-audio-converter-adapter-112358.html", 
                "image_link": "https://np.daraz.io/KuLpiVXUVCj1zQxqvhUJ8Z2H83w=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/85/3211/1.jpg?3647", 
                "reviews": 0, 
                "date_issued": "Sun Jun 24 15:53:46 2018", 
                "date_updated": "Sun Jul  1 18:11:48 2018", 
                "prices": {
                "price": 1300, 
                "discount": 30, 
                "date": "Sun Jul  1 18:11:48 2018", 
                "currency": "NPR"
                }
            }
            ]
        }
    }
    productsWP = recieved_data_WpriceList['data']['products']
    productsNP = recieved_data_WonePrice['data']['products']
    a = validatePriceRange(productsWP, minPrice=100, maxPrice=500, fullPrice=True)
    b = validatePriceRange(productsNP, minPrice=100, maxPrice=500, fullPrice=False)