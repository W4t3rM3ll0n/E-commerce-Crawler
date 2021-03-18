from models import Crawling
from bs4 import BeautifulSoup
from lxml import html
import time
import random


class Hnhn (Crawling):
    def __init__(self):
        collection_name = 'hn_hn'
        super().__init__(collection_name)
        return
    def get_url(self,_url :list) -> list:
        return_list = list()
        get_url = self.s.get(_url).text
        soup_url = BeautifulSoup(get_url,'html.parser')
        get_div = soup_url.find_all('div',{'class':'thumb'})
        for get_href in get_div:
            get_a = get_href.find('a').get('href')
            sub_url = f"http://www.hn-hn.co.kr{get_a}"
            self.logger.info(f"Get{sub_url}")
            return_list.append(sub_url)
        return return_list

    def get_suburl(self,_suburl : list) ->list:


        return_suburl = list()
        for get_suburl in _suburl:

            try:
                return_detailimg = list()
                req_suburl = self.s.get(get_suburl).content
                rand_int = random.randint(1, 5)
                self.logger.info(f"sleep {rand_int} sec...")
                sleep = time.sleep(rand_int)
                soup_suburl = BeautifulSoup(req_suburl,'html.parser')
                get_tableopt = soup_suburl.find('div',{'class':'table-opt'})
                get_name = get_tableopt.find('h3').text

                get_td = get_tableopt.find('td',{'class':'price'})
                get_tbleft = get_td.find('div',{'class':'tb-left'})

                if get_tbleft.find('strike'):
                    get_price = get_tbleft.text.strip().split('\t')[-1]
                else:
                    get_price = get_tbleft.text.strip()

                get_thumb = soup_suburl.find('div',{'class':'thumb'})

                get_jpg = get_thumb.find('img').get('src')

                jpg_url = f"http://www.hn-hn.co.kr/{get_jpg}"

                jpg = get_jpg.split('/')[-1].split('?')[0]

                open_jpg = self.s.get(jpg_url,verify=False).content
                img_path = f"img/hn_hn/img/{jpg}"
                self.save_file(img_path,open_jpg)

                data = html.fromstring(req_suburl)
                data_path = data.xpath('//*[@id="productDetail"]/div[2]/div[6]')[0]
                div_path = html.tostring(data_path)
                soup_div = BeautifulSoup(div_path,'html.parser')

                detail_url = soup_div.find_all('img')


                for sub_src in detail_url:

                    sub_img = sub_src.get('src')
                    if sub_img.find('Copyright') != -1:
                        continue
                    sub_jpg = sub_img.split('/')[-1]
                    open_detailimg = self.s.get(sub_img,verify=False).content
                    detail_path = f"img/hn_hn/detail_img/{sub_jpg}"
                    self.save_file(detail_path,open_detailimg)
                    return_detailimg.append(f"hn_hn/detail_img/{sub_jpg}")

                dict_data = {'product_name':get_name,'product_price':get_price,'img_path':f"hn_hn/img/{jpg}",'detail_imgpath':return_detailimg}

                return_suburl.append(dict_data)
            except Exception as e:
                self.logger.error(e)

                self.logger.info(f"Crawling fail url is {get_suburl}")

        return return_suburl





