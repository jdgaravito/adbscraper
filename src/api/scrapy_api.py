from fastapi import APIRouter, BackgroundTasks
from pydantic import BaseModel
from typing import List
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from src.db.df import update_dataframe, get_dataframe


class UrlList(BaseModel):
    urls: List[str]


scrapy_router = APIRouter()


class AdobeSpider(scrapy.Spider):
    name = "adobecr"

    def __init__(self, urls, *args, **kwargs):
        super(AdobeSpider, self).__init__(*args, **kwargs)
        self.start_urls = urls

    def parse(self, response):
        images_links = response.css("div.thumb-frame > a::attr(href)").extract()
        descriptions = response.css(
            "div.thumb-frame > a > picture > img::attr(alt)"
        ).extract()

        for image_link, description in zip(images_links, descriptions):
            update_dataframe(image_link, description)


def run_spider(urls):
    process = CrawlerProcess(get_project_settings())
    process.crawl(AdobeSpider, urls=urls)
    process.start()


@scrapy_router.post("/scrape")
async def scrape_urls(url_list: UrlList, background_tasks: BackgroundTasks):
    background_tasks.add_task(run_spider, url_list.urls)
    return {"message": "Scraping task started"}


@scrapy_router.get("/results")
async def get_results():
    df = get_dataframe()
    return df.to_dict(orient="records")
