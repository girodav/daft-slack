from daftlistings import Daft
from daft_slack import config
import logging


def initialize_daft_api_client():
    daft_client = Daft()
    daft_client.set_county(config.COUNTY)
    daft_client.set_listing_type(config.LISTING_TYPE)
    daft_client.set_min_price(config.MIN_PRICE)
    daft_client.set_max_price(config.MAX_PRICE)
    daft_client.set_with_photos(config.WITH_PHOTOS)
    daft_client.set_added_since(config.ADDED_SINCE)
    daft_client.set_area(config.AREAS)
    daft_client.set_sort_order(config.SORT_ORDER)
    daft_client.set_sort_by(config.SORT_BY)
    daft_client.set_furnished(config.FURNISHED)
    daft_client.set_min_beds(config.MIN_BEDS)
    daft_client.set_min_lease(config.MIN_LEASE)
    return daft_client


def contact_advertiser(daft_ad):
    logging.info(f"Contacting advertiser for ad {daft_ad.id}")
    return daft_ad.contact_advertiser(
        name=config.NAME,
        contact_number=config.PHONE_NUMBER,
        email=config.EMAIL,
        message=config.MESSAGE
    )
