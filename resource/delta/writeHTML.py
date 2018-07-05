<<<<<<< HEAD
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
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Top picks for today</title>
    <link rel="stylesheet" href="https://www.w3schools.com/lib/w3.css">
    <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    <style>
        rbt,p, .w3-btn {
            font-family: 'Roboto', sans-serif;
        }
        .w3-third {
            padding: 8px 8px!important;
        }
        .img_container {
            max-height: 135px;
            overflow: hidden;
        }
        .w3-card-2 {
            min-height : 266px;
        }
    </style>
</head>
    """
    # adding to html page
    html_page = html_page + head_content
    # header in HTML body tag
    header_in_body = """<body class="w3-light-grey">
    <!-- header -->
    <div class="w3-container w3-center w3-card-4 w3-top w3-white">
        <p class="w3-xlarge w3-text-grey">Today's best picks for online shopping</p>
    </div>"""
    # adding to html page
    html_page = html_page + header_in_body

    # HTML body section (other than header)
    html_body_head = """
    <!-- body -->
    <div class="w3-container w3-animate-bottom" style="margin-top: 130px">
        <div class="w3-row">
        <!-- items to render -->
    """
    # adding to HTML file
    html_page = html_page + html_body_head

    # open JSON file to get the data
    with open('data_to_send.json', 'r', encoding='utf-8') as fp:
        json_list = json.load(fp)
        json_list.reverse()

    # iteration through the products
    product_content = """"""
    for product in json_list:
        product_head = """
        <div class="w3-third">
            <div class="w3-card-2 w3-white w3-container w3-round">
                <p class="w3-large w3-center"><b>"""
        product_name = product['name']
        close_prduct_head = """</b>
                </p>
                <div class="w3-half img_container"><img class="w3-image w3-center" src='"""
        product_image = product['image_url']
        close_image = """' alt='img'></div>
                <div class="w3-half w3-container">
                    <p>Rs. 
        """
        new_price = str(product['new_price'])
        close_new_price = """ <strike class="w3-text-grey w3-small">Rs. 
        """
        old_price = str(product['old_price'])
        close_old_price = """</strike></p>
                        <p class="w3-text-green w3-small"><b>
        """
        discount = product['discount']
        close_discount = """ off</b></p>
        <a href='
        """
        product_link = product['link']
        close_product_link = """'><button class="w3-btn w3-blue w3-round w3-ripple middle_thing"><i class="material-icons">&#xe8cc;</i> Buy</button><br><br></a>
            </div>
            </div> 
            </div>
        """
        close_product = "</div>"
        product_whole = product_head + product_name + close_prduct_head + product_image + close_image + new_price + close_new_price + old_price + close_old_price + discount + close_discount + product_link + close_product_link
        html_page = html_page + product_whole
        pass

    # writing footer content
    html_footer = """
        </div> 
    </div> 
    <br><br>
    <!-- footer -->
    <div class="w3-footer w3-padding-24 w3-container w3-border-top w3-border-light-grey w3-text-grey w3-white">
        <div class="w3-center">
            <p>Sent from Yuil Tripathee <br> Software Engineer Intern at Dynamics Softech Computer Solutions</p>
            <p>Copyright &copy; 2018 <br>All rights reserved</p>
        </div>
        <div>
            <p class="w3-left"><a href="#">Unsubscribe</a>&nbsp;&nbsp;<a href="#">Terms of use</a><br></p>
            <p class="w3-right"><a href="#">Source Code</a></p>
        </div>
    </div>
</body>
</html>
    """
    html_page = html_page + html_footer
    # writing whole string to HTML file
    with open('index.html', 'w', encoding='utf-8') as fp:
        fp.write(html_page)
        fp.close()
=======
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
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Top picks for today</title>
    <link rel="stylesheet" href="https://www.w3schools.com/lib/w3.css">
    <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    <style>
        rbt,p, .w3-btn {
            font-family: 'Roboto', sans-serif;
        }
        .w3-third {
            padding: 8px 8px!important;
        }
        .img_container {
            max-height: 135px;
            overflow: hidden;
        }
        .w3-card-2 {
            min-height : 266px;
        }
    </style>
</head>
    """
    # adding to html page
    html_page = html_page + head_content
    # header in HTML body tag
    header_in_body = """<body class="w3-light-grey">
    <!-- header -->
    <div class="w3-container w3-center w3-card-4 w3-top w3-white">
        <p class="w3-xlarge w3-text-grey">Today's best picks for online shopping</p>
    </div>"""
    # adding to html page
    html_page = html_page + header_in_body

    # HTML body section (other than header)
    html_body_head = """
    <!-- body -->
    <div class="w3-container w3-animate-bottom" style="margin-top: 130px">
        <div class="w3-row">
        <!-- items to render -->
    """
    # adding to HTML file
    html_page = html_page + html_body_head

    # open JSON file to get the data
    with open('data_to_send.json', 'r', encoding='utf-8') as fp:
        json_list = json.load(fp)
        json_list.reverse()

    # iteration through the products
    product_content = """"""
    for product in json_list:
        product_head = """
        <div class="w3-third">
            <div class="w3-card-2 w3-white w3-container w3-round">
                <p class="w3-large w3-center"><b>"""
        product_name = product['name']
        close_prduct_head = """</b>
                </p>
                <div class="w3-half img_container"><img class="w3-image w3-center" src='"""
        product_image = product['image_url']
        close_image = """' alt='img'></div>
                <div class="w3-half w3-container">
                    <p>Rs. 
        """
        new_price = str(product['new_price'])
        close_new_price = """ <strike class="w3-text-grey w3-small">Rs. 
        """
        old_price = str(product['old_price'])
        close_old_price = """</strike></p>
                        <p class="w3-text-green w3-small"><b>
        """
        discount = product['discount']
        close_discount = """ off</b></p>
        <a href='
        """
        product_link = product['link']
        close_product_link = """'><button class="w3-btn w3-blue w3-round w3-ripple middle_thing"><i class="material-icons">&#xe8cc;</i> Buy</button><br><br></a>
            </div>
            </div> 
            </div>
        """
        close_product = "</div>"
        product_whole = product_head + product_name + close_prduct_head + product_image + close_image + new_price + close_new_price + old_price + close_old_price + discount + close_discount + product_link + close_product_link
        html_page = html_page + product_whole
        pass

    # writing footer content
    html_footer = """
        </div> 
    </div> 
    <br><br>
    <!-- footer -->
    <div class="w3-footer w3-padding-24 w3-container w3-border-top w3-border-light-grey w3-text-grey w3-white">
        <div class="w3-center">
            <p>Sent from Yuil Tripathee <br> Software Engineer Intern at Dynamics Softech Computer Solutions</p>
            <p>Copyright &copy; 2018 <br>All rights reserved</p>
        </div>
        <div>
            <p class="w3-left"><a href="#">Unsubscribe</a>&nbsp;&nbsp;<a href="#">Terms of use</a><br></p>
            <p class="w3-right"><a href="#">Source Code</a></p>
        </div>
    </div>
</body>
</html>
    """
    html_page = html_page + html_footer
    # writing whole string to HTML file
    with open('index.html', 'w', encoding='utf-8') as fp:
        fp.write(html_page)
        fp.close()
>>>>>>> 8e27e40220dc8794da2e3e1fff5967c53eafa9d5
    pass