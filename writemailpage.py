import json
from bs4 import BeautifulSoup as bs4
if __name__ == '__main__':
    html_page = """"""
    # content i HTML5 head
    head_content = """<!--
Coded with 💙 by Yuil Tripathee
-->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
    """
    # adding to html page
    html_page = html_page + head_content
    # header in HTML body tag
    header_in_body = """<body style="font-family: 'Roboto', 'sans-serif'; background-color: #f1f1f1; font-size: 15px; line-height: 1.5; margin: 0; ">
    <!-- header -->
    <div style="background-color: #2196F3; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2),0 6px 20px 0 rgba(0,0,0,0.19); padding: 0.01em 16px; text-align: center;">
        <p style="color: #fff; font-size: 24px; font-family: 'Roboto', sans-serif; margin: 1em; ">Today's best picks for online shopping</p>
    </div>"""
    # adding to html page
    html_page = html_page + header_in_body

    # HTML body section (other than header)
    html_body_head = """
    <!-- body -->
    <div style="padding: 5px;">
        <div style="content : ''; display : table; clear : both">
        <!-- items to render -->
    """
    # adding to HTML file
    html_page = html_page + html_body_head

    # open JSON file to get the data
    with open('data_to_send.json', 'r', encoding='utf-8') as fp:
        json_list = json.load(fp)

    # iteration through the products
    product_content = """"""
    for product in json_list:
        product_head = """
        <div style="width: 30%; float: left; font-family: 'Roboto', sans-serif;">
            <div style="min-height: 266px; background-color: #fff; box-shadow: 0 2px 4px 0 rgba(0,0,0,0.16),0 2px 10px 0 rgba(0,0,0,0.12); border-radius: 4px; ">
                <p style="text-align: center; font-size: 18px; font-family: 'Roboto', sans-serif;"><b>"""
        product_name = product['name']
        close_prduct_head = """</b>
                </p>
                <div style="max-height: 135px; overflow: hidden; width: 49.99%; float: left;"><img style="text-align: center; max-width: 100%; height: auto; margin-bottom: -5px; border-style: none;" src='"""
        product_image = product['image_url']
        close_image = """' alt='img'></div>
                <div style="width: 49.99%; float: left;">
                    <p>Rs. 
        """
        new_price = str(product['new_price'])
        close_new_price = """ <strike>Rs. 
        """
        old_price = str(product['old_price'])
        close_old_price = """</strike></p>
                        <p><b>
        """
        discount = product['discount']
        close_discount = """ off</b></p>
        <a href='
        """
        product_link = product['link']
        close_product_link = """'><button style="background-color: #2196F3; border-radius: 4px; display: inline-block; padding: 6px 16px; overflow: hidden; text-decoration: none; cursor: pointer; white-space: nowrap; border: none; color: #fff; ">Buy</button><br><br></a>
            </div>
            </div> 
            </div>
        """
        close_product = "</div>"
        product_whole = product_head + product_name + close_prduct_head + product_image + close_image + new_price + close_new_price + old_price + close_old_price + discount + close_discount + product_link + close_product_link
        html_page = html_page + product_whole
        pass

    # writing whole string to HTML file
    with open('mail.html', 'w', encoding='utf-8') as fp:
        fp.write(html_page)
        fp.close()
    pass