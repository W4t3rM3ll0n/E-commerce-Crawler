import requests
from pymongo import MongoClient
import os
import logging
class Crawling:
    def __init__(self,collection_name):
        self.s = requests.Session()
        self.s.headers.update({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'})
        self.db = MongoClient("localhost",27017).localdev
        self.collection = self.db[collection_name]
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(fmt="[*] %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

        f'''
        make directory 'img','collection_name','path/img'.'path/detail_img'
        
        '''
        try:
            os.makedirs('img', exist_ok=True)
            os.makedirs(f"img/{collection_name}", exist_ok=True)
            path = f"img/{collection_name}/"
            os.makedirs(f"{path}img", exist_ok=True)
            os.makedirs(f"{path}detail_img", exist_ok=True)
        except Exception as e:
            self.logger.error(e)
            pass


    def get_url(self,_url :list)-> list:
        raise NotImplementedError("get_url does not define")

    def get_suburl(self,_suburl : list) ->list:
        raise NotImplementedError("get_suburl does not define")
    def save_file(self,img:str,content_img:bytes):
        '''
        file open,write and close
        save img_data
        '''
        img_file = open(img,'wb')
        img_file.write(content_img)
        img_file.close()
        return

    def save_url(self, _data: list):
        '''
        insert data in database
        '''
        self.collection.insert_many(_data)
        return


    def call_url(self,_url:str):
        '''
        crawling url
        if crawling has been failed
        show about error
        '''
        try:
            sub_url = self.get_url(_url)
            save_url = self.get_suburl(sub_url)
            self.save_url(save_url)
            self.logger.info(f"crawling is complete")
        except Exception as e:
            self.logger.error(e)
