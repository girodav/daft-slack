import requests
import logging
from daft_slack import config


def _get_slack_message(daft_ad):
    slack_message = {
        'attachments': [
            {
                "color": "#36a64f",
                "pretext": "Hey, I found a new property!",
                "title": daft_ad.formalised_address,
                "title_link": daft_ad.daft_link,
                "fields": [
                    {
                        "title": "Price",
                        "value": daft_ad.price
                    },
                    {
                        "title": "Beds",
                        "value": daft_ad.bedrooms
                    }

                ],
                "image_url": daft_ad.images[0] if daft_ad.images is not None else ''
            }
        ]
    }
    return slack_message


def send_errors(error):
    logging.error(error)
    requests.post(config.SLACK_URL_ERRORS, json={
        'attachments': [
            {
                "title": error
            }
        ]
    })


def send_new_property_found_notification(daft_ad):
    requests.post(config.SLACK_URL, json=_get_slack_message(daft_ad))
