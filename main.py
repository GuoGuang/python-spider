# -*- coding: utf-8 -*-
__author__ = 'GuoGuang'

"""
主函数 指定运行哪个脚本
debug使用
"""
from scrapy.cmdline import execute

import sys
import os
if __name__ == "__main__":
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    # execute(["scrapy", "crawl", "FangTianXia"])
    execute(["scrapy", "crawl", "zhipin"])
# execute(["scrapy", "crawl", "lagou"])

# import scrapy
# from scrapy.crawler import CrawlerProcess
# from spiders.jobbole import JobboleSpider
# from spiders.lagou import LagouSpider
# from twisted.internet import reactor, defer
# from scrapy.crawler import CrawlerRunner
# from scrapy.utils.log import configure_logging
#
# configure_logging()
# runner = CrawlerRunner()
#
# @defer.inlineCallbacks
# def crawl():
#     yield runner.crawl(JobboleSpider)
#     yield runner.crawl(LagouSpider)
#     reactor.stop()
#
# crawl()
# reactor.run() # the script will block here until the last crawl call is finished