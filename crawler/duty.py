from models import Crawling
from bs4 import BeautifulSoup
class DutyFun(Crawling):
    def __init__(self):
        collection_name = 'duty'
        super().__init__(collection_name)
        return

    def get_url(self,_url):
        return_list = list()
        get_url = self.s.get(_url).content
        soup_url = BeautifulSoup(get_url,'html.parser')
        get_table = soup_url.find('table',{'class':'brd_list_n'})
        get_td = get_table.find_all('td',{'class':'title t-alignLt pl10px'})
        for get_a in get_td:
            get_url = get_a.find('a').get('href')
            return_list.append(f"https://work.mma.go.kr/{get_url}")
        return return_list

    def get_suburl(self,_suburl):
        return_suburl = list()

        for get_suburl in _suburl:
            res_url = self.s.get(get_suburl).content
            soup_suburl = BeautifulSoup(res_url,'html.parser')
            get_table = soup_suburl.find('table',{'class':'table_row'})
            get_tbody = get_table.find('tbody')
            get_td = get_tbody.find('td').text
            get_div = soup_suburl.find_all('div',{'class':'step1'})
            find_div = get_div[0]
            find_colspan = find_div.find_all('td',{'colspan':'3'})

            find_company = find_colspan[0].text

            find_address = find_colspan[1].text

            find_secdiv = get_div[1]

            find_td = find_secdiv.find_all('td')
            find_fee = find_td[3].text

            dict_duty = {'company_name':find_company,'company_address':find_address,'fee':find_fee}
            return_suburl.append(dict_duty)
        return return_suburl






    def call_fun(self):
        url = "https://work.mma.go.kr/caisBYIS/search/cygonggogeomsaek.do"
        try:

            sub_url = self.get_url(url)
            save_url = self.get_suburl(sub_url)
            self.save_url(save_url)
            self.logger.info("crawling has been completed")
        except Exception as e:
            self.logger.error(e)




