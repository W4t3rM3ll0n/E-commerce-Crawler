from crawler import duty
from crawler import hnhn
from crawler import remon
from crawler import modern
from crawler import vorakim

class CrawlerMain:
    def __init__(self):
        return
    def duty_main(self):
        duty.DutyFun().call_fun()
        return
    def hnhn_main(self):
        hnhn.hnhn().call_url("http://www.hn-hn.co.kr/shop/shopbrand.html?xcode=008&type=Y")
        return
    def remon_main(self):
        remon.ReMon().call_url()
        return
    def modern_main(self):
        modern.modern_able().call_url("https://www.the-modernable.com/goods/goods_list.php?cateCd=001")
        return

    def vorakim_main(self):
        vorakim.vorakim().call_url("http://www.vorakim.com/product/list.html?cate_no=65")
if __name__ == '__main__':
    app = CrawlerMain()
    app.vorakim_main()

