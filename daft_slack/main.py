#!/usr/bin/env python3
import pickledb
import logging
from daft_slack import config
from daft_slack.utils import daft_utils, slack_utils


def initialize_db():
    logging.info(f"Initializing local DB at path {config.DB_PATH}")
    return pickledb.load(config.DB_PATH, True)


def main():
    logging.basicConfig(format='%(asctime)s - [%(levelname)s]:%(message)s', level=config.LOG_LEVEL)
    db = initialize_db()
    daft_client = daft_utils.initialize_daft_api_client()
    listings = daft_client.search()
    for listing in listings:
        if not db.get(listing.id):
            response = daft_utils.contact_advertiser(listing)
            if response is not None:
                slack_utils.send_new_property_found_notification(listing)
            else:
                slack_utils.send_errors(f"Errors contacting the advertiser for this property {listing.daft_link}")
            if not db.set(listing.id, 'Seen'):
                slack_utils.send_errors(f"Errors saving {listing.daft_link}")


if __name__ == "__main__":
    main()
