from providers.scrapers.base import Scraper
from providers.scrapers.radboudumc import ScraperRadboudumc
from providers.scrapers.stepwork import ScraperStepwork
from providers.scrapers.umcg import ScraperUMCG
from providers.scrapers.vumc import ScraperVUmc


def test(scraper_name: str):
    scraper: Scraper

    if scraper_name == 'radboudumc':
        scraper = ScraperRadboudumc()
    elif scraper_name == 'stepwork':
        scraper = ScraperStepwork()
    elif scraper_name == 'umcg':
        scraper = ScraperUMCG()
    elif scraper_name == 'vumc':
        scraper = ScraperVUmc()
    else:
        raise Exception(f'Unknown scraper "{scraper_name}"')

    scraper.scrape()


test('stepwork')
