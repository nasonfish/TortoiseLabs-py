# TortoiseLabs-py

Like [TortoiseLabs-php](/nasonfish/TortoiseLabs-php), TortoiseLabs-py is a very small library made for accessing [TortoiseLabs](http://tortois.es/)'s [API](http://wiki.tortois.es/index/API) so you don't have to handle the requests.

This small library will allow you to use simple function names to grab data from TortoiseLabs' panel.

## Installation

To use, first, you need to install `requests`:

    # pip install requests

Requests allows us to use very simple statements to send different requests to the api.

After that, as long as you've imported the file, you should be good to go:
```python
from tortoiselabs import TortoiseLabs
```

## Usage

First, you need to create a `TortoiseLabs` object with your user information (username and API key):
```python
from tortoiselabs import TortoiseLabs

my_tl = TortoiseLabs('my_username', 'api_key_from_my_profile')

```

After that, we have four classes for four different categories of api functions, matching the ones on the [API page](http://wiki.tortois.es/index/API):

```python
my_tl.vps
my_tl.support
my_tl.billing
my_tl.dns
```

Each one of these contains the functions within the header on the page, and returns the values specified as a dict.

## Examples

```python
from tortoiselabs import TortoiseLabs

tl = TortoiseLabs('nasonfish', 'api_key')
print(tl.vps.list_all())  # List all vps' and their info/
print(tl.vps.info(20))    # list the info for this specific vps
tl.support.ticket_new('My vps isn\'t working!', 'HELP!')  # create a support ticket. don't do this, this is a bad idea
print(tl.billing.invoice_list())   # check out your invoice list
```
