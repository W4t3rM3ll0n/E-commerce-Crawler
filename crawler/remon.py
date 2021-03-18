from models import Crawling
from bs4 import BeautifulSoup


class ReMon(Crawling):
    def __init__(self):
        collection_name = 'remon'
        super().__init__(collection_name)
        return

    def get_url(self,_url :list)-> list:
        return_list = list()
        get_url = self.s.get(_url).text
        soup_url = BeautifulSoup(get_url,'html.parser')
        get_ul = soup_url.find('ul',{'id':'search-result-items'})
        get_productimg = get_ul.find_all('div',{'class':'product-image'})
        for get_href in get_productimg:
            sub_url = get_href.find('a',{'class':'thumb-link'}).get('href')
            return_list.append(sub_url)
        return return_list

    def get_suburl(self,_suburl : list) ->list:
        return_sublist = list()

        for get_suburl in _suburl:
            detail_list = list()
            text_suburl = self.s.get(get_suburl).text
            soup_suburl = BeautifulSoup(text_suburl,'html.parser')
            get_detail = soup_suburl.find('div',{'class':'product-col-2 product-detail'})
            get_name = get_detail.find('h1',{'class':'product-name'}).text
            get_price = get_detail.find('div',{'class':'product-price'}).text

            get_div = soup_suburl.find('div',{'class':'product-col-1 product-image-container'})
            get_href = get_div.find('a').get('href')
            get_img = get_href.split('/')[-1]
            img_file = get_img.split('?')[0]
            get_jpg = f"{img_file}.jpg"
            content_img = self.s.get(get_href).content
            img_path = f"img/remon/img/{get_jpg}"
            self.save_file(img_path,content_img)


            get_li = get_div.find_all('li')
            for get_a in get_li:
                get_href = get_a.find('a').get('href')
                sub_imgurl = self.s.get(get_href).content
                sub_img = f"{get_href.split('/')[-1].split('?')[0]}.jpg"
                sub_imgpath = f"img/remon/detail_img/{sub_img}"
                self.save_file(sub_imgpath,sub_imgurl)
                detail_list.append(f"remon/detail_img/{sub_img}")

            dict_data = {'product_name':get_name,'price':get_price,'img_path':f"remon/img/{get_jpg}",'detailimg_path':detail_list}
            return_sublist.append(dict_data)
        return return_sublist

    def call_url(self):
        url = ("https://www.lululemon.co.kr/men/?CID=ps_sem_google_pc_Q42020_SEM_Men%27s%20Clothing_%EB%82%A8%EC%9E%90%EC%98%B7&gclid=CjwKCAiAhbeCBhBcEiwAkv2cY2DNOW9I-k5IZEoLhsVB2h6ndZ6XG6LZJ66l_Zl4Pvaw5tBRlUcLtBoC6gMQAvD_BwE")
        sub_url = self.get_url(url)
        get_data = self.get_suburl(sub_url)
        self.save_url(get_data)
