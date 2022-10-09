2Checkout Python SDK
=====================

This is the current 2Checkout Python SDK providing developers with a simple set of bindings to the 2Checkout 6.0 REST API, IPN and Convert Plus Signature API.

To use, clone or download a release and install (Or just import in your script.)_

```shell
cd 2checkout-python-sdk
sudo python setup.py install

```

Import in your script
```python
import twocheckout
```


Example Rest API Usage
-----------------

*Example Usage:*

```python
auth_params = {
    'merchant_code': 'YOUR_MERCHANT_CODE',
    'secret_key': 'YOUR_SECRET_KEY'
}

# order params ( when creating new orders use this JSON format (some fields are optional)
# to view what are the required or optional fields please read the our docs
order_params = {
  "Country": "us",
  "Currency": "USD",
  "CustomerIP": "91.220.121.21",
  "ExternalReference": "REST_API_AVANGTE",
  "Language": "en",
  "Source": "testAPI.com",
  "BillingDetails": {
    "Address1": "Test Address",
    "City": "LA",
    "State": "California",
    "CountryCode": "US",
    "Email": "testcustomer@2Checkout.com",
    "FirstName": "Customer",
    "LastName": "2Checkout",
    "Zip": "12345"
  },
  "Items": [
    {
      "Name": "Dynamic product",
      "Description": "Test description",
      "Quantity": 1,
      "IsDynamic": True,
      "Tangible": False,
      "PurchaseType": "PRODUCT",
      "CrossSell": {
        "CampaignCode": "CAMPAIGN_CODE",
        "ParentCode": "MASTER_PRODUCT_CODE"
      },
      "Price": {
        "Amount": 100,
        "Type": "CUSTOM"
      },
      "PriceOptions": [
        {
          "Name": "OPT1",
          "Options": [
            {
              "Name": "Name LR",
              "Value": "Value LR",
              "Surcharge": 7
            }
          ]
        }
      ],
      "RecurringOptions": {
        "CycleLength": 2,
        "CycleUnit": "DAY",
        "CycleAmount": 12.2,
        "ContractLength": 3,
        "ContractUnit": "DAY"
      }
    }
  ],
  "PaymentDetails": {
    "Type": "TEST",
    "CardType": "VISA",
    "Currency": "USD",
    "CustomerIP": "91.220.121.21",
    "PaymentMethod": {
      "CardNumber": "4111111111111111",
      "CardType": "VISA",
      "Vendor3DSReturnURL": "www.success.com",
      "Vendor3DSCancelURL": "www.fail.com",
      "ExpirationYear": "2044",
      "ExpirationMonth": "12",
      "CCID": "123",
      "HolderName": "John Doe",
      "RecurringEnabled": True,
      "HolderNameTime": 1,
      "CardNumberTime": 1
    }
  }
}
# # instantiate the object ( for auth)
order = twocheckout.order.Order(auth_params)
## creates a new order
new_order = order.create(order_params)
```


Example Convert Plus Signature Generation:
-----------------------

*Example Usage:*

```python
cplus = twocheckout.CplusSignature()
cplus.get_signature('YOUR_MERCHANT_ID', 'YOUR_SECRET_WORD', 'JSON_STRING_OF_PARAMETERS')
```


Example IPN Usage:
---------------------

*Example Usage:*

```python
ipn = twocheckout.ipn_helper.IpnHelper('YOUR_SECRET_KEY')
ipn_valid = ipn.is_valid(DICT_OF_IPN_PARAMTERS)
ipn_response = ipn.calculate_ipn_response(DICT_OF_IPN_PARAMTERS)
```


Errors:
------------------

A `TwocheckoutError` will be thrown for any library related errors. It is best to catch these errors so that they can be gracefully handled in your application.

