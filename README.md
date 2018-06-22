Google Analytics Segment Pusher
===============================

version number: 0.0.1
author: Rok Mihevc

Overview
--------

A python package to push user segmentation mapped to google analytics ID to google analytics.

Installation / Usage
--------------------

To install use pip:

    $ pip install ga_segment_pusher


Or clone the repo:

    $ git clone https://github.com/rok/ga_segment_pusher.git
    $ python setup.py install
    
Contributing
------------

TBD

Example
-------
```python
import ga_segment_pusher

key_file_location = 'credentials.json'
csv_file_location = 'segments.csv'

upload_params = {
    'account_id': 'XXXXXXXX',
    'web_property_id': 'UA-XXXXXXXX-1',
    'custom_data_source_id': 'XXXXXXXXXXXXXXXXXXXXXX'
}

analytics = ga_segment_pusher.get_service(key_file_location)

ga_segment_pusher.upload_csv(csv_file_location, analytics, **upload_params)
```
