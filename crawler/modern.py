from models import Crawling

from bs4 import BeautifulSoup

class modern_able(Crawling):
    def __init__(self):
        collection_name = 'modern'
        super().__init__(collection_name)
        return
    def get_url(self,_url :list) -> list:
        return_list = list()
        get_url = self.s.get(_url).content
        soup_url = BeautifulSoup(get_url,'html.parser')
        get_goods = soup_url.find('div',{'class':'goods-list'})
        get_li = get_goods.find_all('li')
        for get_thumbnail in get_li:
            get_a = get_thumbnail.find('a').get('href')
            sub_url = f"https://www.the-modernable.com{get_a.replace('..','')}"
            self.logger.info(f"get suburl {sub_url}")
            return_list.append(sub_url)

        return return_list

    def get_suburl(self,_suburl : list) ->list:
        for get_suburl in _suburl:
            return_sublist = list()
            try:
                req_suburl = self.s.get(get_suburl).content
                soup_suburl = BeautifulSoup(req_suburl,'html.parser')
                get_info = soup_suburl.find('div',{'class':'info'})
                get_productname = get_info.find('div',{'class':'tit'}).text


                get_item = get_info.find('div',{'class':'item'})
                get_li = get_item.find_all('li')
                get_productcode = get_li[-2].find('div').text

                get_price = get_li[-1].find('div').text
                get_image = soup_suburl.find('div',{'class':'image'})
                get_imgurl = get_image.find('img').get('src')
                img = get_imgurl.split('/')[-1]
                self.logger.info(f"Main img file name {img}")

                img_url = f"https://www.the-modernable.com{get_imgurl}"
                content_imgurl = self.s.get(img_url).content
                img_path = f"img/modern/img/{img}"

                self.save_file(img_path,content_imgurl)
                get_style = soup_suburl.find('div',{'class':'txt-manual'})

                get_detailimg = get_style.find('img').get('src')
                self.logger.debug(f"get detail img {get_detailimg}")

                detail_img = get_detailimg.split('/')[-1]
                detailimg_url = f"https://www.the-modernable.com{get_detailimg}"
                content_detailimg = self.s.get(detailimg_url).content
                detailimg_path = f"img/modern/detail_img/{detail_img}"
                self.save_file(detailimg_path,content_detailimg)




                dict_data = {'product_name':get_productname,'product_code':get_productcode,'price':get_price,'img_path':img_path,'detail_path':detailimg_path}
                return_sublist.append(dict_data)


            except Exception as e:

                 self.logger.error(e)

        return return_sublist

