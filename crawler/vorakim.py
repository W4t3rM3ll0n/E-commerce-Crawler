from models import Crawling
from bs4 import BeautifulSoup

class vorakim(Crawling):
    def __init__(self):
        collection_name = 'vorakim'
        super().__init__(collection_name)
        return

    def get_url(self,_url :list) -> list:
        return_list = list()
        get_url = self.s.get(_url).content
        soup_url = BeautifulSoup(get_url,'html.parser')
        get_id = soup_url.find('div',{'id':'container'})
        get_elements = get_id.find('div',{'class':'xans-element- xans-product xans-product-listnormal ec-base-product'})
        get_grid4 = get_elements.find('ul',{'class':'prdList grid4'})
        get_li = get_grid4.find_all('div',{'class':'thumbnail'})

        for get_thumbnail in get_li:
            get_suburl = f"http://www.vorakim.com{get_thumbnail.find('a').get('href')}"
            return_list.append(get_suburl)
        return return_list

    def get_suburl(self,_suburl : list) ->list:
        return_sublist =list()
        for get_suburl in _suburl:
            content_suburl = self.s.get(get_suburl).content
            soup_suburl = BeautifulSoup(content_suburl,'html.parser')
            get_productdetail = soup_suburl.find('div',{'class':'xans-element- xans-product xans-product-detail'})
            get_design = get_productdetail.find('div',{'class':'xans-element- xans-product xans-product-detaildesign'})
            get_tbody = get_design.find('tbody')

            get_tr = get_tbody.find_all('tr',{'class':'xans-record-'})
            get_namestyle = get_tr[0]
            get_nametd = get_namestyle.find('td')
            get_name = get_nametd.find('span',{'style':'font-size:16px;color:#333333;'}).text

            get_pricestyle = get_tr[2]
            get_pricetd = get_pricestyle.find('td')
            get_price = get_pricetd.find('strong',{'id':'span_product_price_text'}).text

            get_keyimg = get_productdetail.find('div',{'class':'keyImg'})
            get_imgthumbnail = get_keyimg.find('div',{'class':'thumbnail'})
            get_imgurl = f"http://{get_imgthumbnail.find('img').get('src').replace('//','')}"
            content_imgurl = self.s.get(get_imgurl).content
            img = get_imgurl.split('/')[-1]
            img_path = f"img/vorakim/img/{img}"

            # self.save_file(img_path,content_imgurl)

            get_center = soup_suburl.find('div',{'id':'prdDetail'})
            get_color = get_center.find_all('img')


            detail_list = list()
            detail_path = list()
            for get_detailurl in get_color:
                get_detaillist =list()
                if get_detailurl.get('src'):
                    get_detaillist = f"http://www.vorakim.com{get_detailurl.get('src')}"
                    detail_list.append(get_detaillist)
                else:
                    pass
                for detail_url in detail_list:
                    # TODO: have to fix get detail img 
                    detailpath_list = list()
                    detail_img = detail_url.split('/')[-1]

                    detailimg_path = f"img/vorakim/detail_img/{detail_img}"
                    content_detailurl = self.s.get(detail_url).content
                    self.save_file(detailimg_path,content_detailurl)
                    detailpath_list.append(detailimg_path)
            dict_data = {'product_name':get_name,'product_price':get_price,'imgpath':img_path,'detail_img':detailpath_list}
            return_sublist.append(dict_data)
        return return_sublist







