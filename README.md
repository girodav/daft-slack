# Daft-Slack

A simple tool that leverages [the unofficial Python APIs for Daft.ie](https://github.com/AnthonyBloomer/daftlistings) (credits to [AnthonyBloomer](https://github.com/AnthonyBloomer))
to search for properties that match your criteria, and automatically reach out to the estate agent/landlord with a pre-defined message. If a new property is found, the tool also sends a notification
through [Slack](https://slack.com).

The tool is meant to be run as a cronjob on an Unix machine, but can be run ad-hoc.

# Installation Steps

Install the required dependencies with `pip` (either locally or in a [Python virtual environment](https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv))

`pip install -r requirements.txt`

# How to Run

1 - Change the configuration file `config.py`  
2 - Execute `python daft_slack/daft_slack.py`

