from crawler import duty
from crawler import hnhn
from crawler import remon
from crawler import modern
from crawler import vorakim
import argparse
class CrawlerMain:
    def __init__(self):
        return
    def duty_main(self):
        duty.DutyFun().call_fun()
        return
    def hnhn_main(self):
        hnhn.Hnhn().call_url("http://www.hn-hn.co.kr/shop/shopbrand.html?xcode=008&type=Y")
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
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', required=True, help='사이트 이름')
    args = parser.parse_args()
    if args.url == 'hnhn':
        app.hnhn_main()
    if args.url == 'remon':
        app.remon_main()
    if args.url == 'modern':
        app.modern_main()
    if args.url == 'vorakim':
        app.vorakim_main()
    if args.url == 'duty':
        app.duty_main()
