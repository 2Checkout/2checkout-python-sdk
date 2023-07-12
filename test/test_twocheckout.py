# -*- coding: utf-8 -*-
import os
import sys
import datetime
import unittest
import logging
from freezegun import freeze_time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import twocheckout
from test import config

NOW = datetime.datetime.now()

auth_params = {
    'merchant_code': config.TWOCHECKOUT_TEST_MERCHANT_ID,
    'secret_key': config.TWOCHECKOUT_TEST_MERCHANT_SECRET_KEY,
}
order_transaction_id = '147288494'
order_get_test = {"meta": {"status": "success", "message": "ok"},
                  "body": {'RefNo': '147288494', 'OrderNo': 0, 'ExternalReference': 'REST_API_AVANGTE',
                           'ShopperRefNo': None,
                           'Status': 'PENDING', 'ApproveStatus': 'WAITING', 'VendorApproveStatus': 'OK',
                           'MerchantCode': config.TWOCHECKOUT_TEST_MERCHANT_ID, 'Language': 'en',
                           'OrderDate': '2021-03-19 11:49:50',
                           'FinishDate': None,
                           'Source': 'testAPI.com',
                           'Affiliate': {'AffiliateCode': None, 'AffiliateSource': None, 'AffiliateName': None,
                                         'AffiliateUrl': None},
                           'HasShipping': False,
                           'BillingDetails': {'FiscalCode': None, 'TaxOffice': None, 'Phone': None,
                                              'FirstName': 'Customer',
                                              'LastName': '2Checkout', 'Company': None,
                                              'Email': 'testcustomer@2Checkout.com',
                                              'Address1': 'Test Address', 'Address2': None, 'City': 'LA',
                                              'Zip': '12345',
                                              'CountryCode': 'us', 'State': 'California'},
                           'DeliveryDetails': {'Phone': None, 'FirstName': 'Customer', 'LastName': '2Checkout',
                                               'Company': None,
                                               'Email': 'testcustomer@2Checkout.com', 'Address1': 'Test Address',
                                               'Address2': None,
                                               'City': 'LA', 'Zip': '12345', 'CountryCode': 'us',
                                               'State': 'California'},
                           'PaymentDetails': {'Type': 'CC', 'Currency': 'usd',
                                              'PaymentMethod': {'Authorize3DS': None, 'Vendor3DSReturnURL': None,
                                                                'Vendor3DSCancelURL': None, 'FirstDigits': '4111',
                                                                'LastDigits': '1111', 'CardType': 'Visa',
                                                                'RecurringEnabled': True},
                                              'CustomerIP': '91.220.121.21'}, 'DeliveryInformation': {
                          'ShippingMethod': {'Code': None, 'TrackingUrl': None, 'TrackingNumber': None,
                                             'Comment': None}},
                           'CustomerDetails': None, 'Origin': 'API', 'AvangateCommission': 4.1, 'OrderFlow': 'REGULAR',
                           'GiftDetails': None, 'PODetails': None, 'ExtraInformation': None, 'PartnerCode': None,
                           'PartnerMargin': None, 'PartnerMarginPercent': None, 'ExtraMargin': None,
                           'ExtraMarginPercent': None,
                           'ExtraDiscount': None, 'ExtraDiscountPercent': None, 'LocalTime': None, 'TestOrder': False,
                           'FxRate': 1,
                           'FxMarkup': 0, 'PayoutCurrency': 'USD', 'DeliveryFinalized': False, 'Errors': None,
                           'Items': [{
                               'ProductDetails': {
                                   'Name': 'Dynamic product',
                                   'ShortDescription': 'Test description',
                                   'Tangible': False,
                                   'IsDynamic': True,
                                   'ExtraInfo': None,
                                   'RenewalStatus': False,
                                   'Subscriptions': None,
                                   'DeliveryInformation': {
                                       'Delivery': 'NO_DELIVERY',
                                       'DownloadFile': None,
                                       'DeliveryDescription': '',
                                       'CodesDescription': '',
                                       'Codes': []}},
                               'PriceOptions': [
                                   {
                                       'Code': 'OPT1_292',
                                       'Name': 'OPT1',
                                       'Required': True,
                                       'Options': [
                                           {
                                               'Name': 'Name LR',
                                               'Value': 'f7f4d3d5546e4f25e8dcdaf8301c34d6',
                                               'Surcharge': '7.00'}]}],
                               'Price': {
                                   'UnitNetPrice': 107,
                                   'UnitGrossPrice': 107,
                                   'UnitVAT': 0,
                                   'UnitDiscount': 0,
                                   'UnitNetDiscountedPrice': 107,
                                   'UnitGrossDiscountedPrice': 107,
                                   'UnitAffiliateCommission': 0,
                                   'ItemUnitNetPrice': 0,
                                   'ItemUnitGrossPrice': 0,
                                   'ItemNetPrice': 0,
                                   'ItemGrossPrice': 0,
                                   'VATPercent': 0,
                                   'HandlingFeeNetPrice': 0,
                                   'HandlingFeeGrossPrice': 0,
                                   'Currency': 'usd',
                                   'NetPrice': 107,
                                   'GrossPrice': 107,
                                   'NetDiscountedPrice': 107,
                                   'GrossDiscountedPrice': 107,
                                   'Discount': 0,
                                   'VAT': 0,
                                   'AffiliateCommission': 0},
                               'LineItemReference': '69057567c67d17d570523b4ea67fe8770fdbc5bd',
                               'PurchaseType': 'PRODUCT',
                               'ExternalReference': '',
                               'Quantity': 1,
                               'SKU': None,
                               'CrossSell': None,
                               'Trial': None,
                               'AdditionalFields': None,
                               'Promotion': None,
                               'RecurringOptions': None,
                               'SubscriptionStartDate': None,
                               'SubscriptionCustomSettings': None}],
                           'Promotions': [], 'AdditionalFields': None, 'Currency': 'usd', 'NetPrice': 107,
                           'GrossPrice': 107,
                           'NetDiscountedPrice': 107, 'GrossDiscountedPrice': 107, 'Discount': 0, 'VAT': 0,
                           'AffiliateCommission': 0,
                           'CustomParameters': None
                           }}
order_params_test = {
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
json_encoded_convert_plus_parameters = '{"merchant":"' \
                                       + config.TWOCHECKOUT_TEST_MERCHANT_ID \
                                       + '","dynamic":1,"src":"DJANGO",' \
                                         '"return-url":"https:\/\/google.com",' \
                                         '"return-type":"redirect",' \
                                         '"expiration":1617189603,"order-ext-ref":292,' \
                                         '"customer-ext-ref":"example@example.com",' \
                                         '"currency":"GBP","test":"1","language":"en",' \
                                         '"prod":"test site","price":"71.03","qty":"1",' \
                                         '"type":"PRODUCT","tangible":"0",' \
                                         '"ship-name":"John Doe","ship-country":"US",' \
                                         '"ship-state":"AL",' \
                                         '"ship-email":"example@example.com",' \
                                         '"ship-address":"Example","ship-address2":"",' \
                                         '"ship-city":"Example","name":"John Doe",' \
                                         '"phone":"756852919","country":"US","state":"AL",' \
                                         '"email":"example@example.com",' \
                                         '"address":"Example","address2":"",' \
                                         '"city":"Example","zip":"35242","company-name":""} '

ipn_payload = {
    'GIFT_ORDER': '0',
    'SALEDATE': '2023-06-09 15:26:18',
    'PAYMENTDATE': '2023-06-09 15:31:18',
    'REFNO': '211153389',
    'REFNOEXT': 'REST_API_AVANGTE',
    'SHOPPER_REFERENCE_NUMBER': '',
    'ORDERNO': '25430',
    'ORDERSTATUS': 'COMPLETE',
    'PAYMETHOD': 'Visa/MasterCard',
    'PAYMETHOD_CODE': 'CCVISAMC',
    'FIRSTNAME': 'Customer',
    'LASTNAME': '2Checkout',
    'COMPANY': '',
    'REGISTRATIONNUMBER': '',
    'FISCALCODE': '',
    'TAX_OFFICE': '',
    'CBANKNAME': '',
    'CBANKACCOUNT': '',
    'ADDRESS1': 'Test Address',
    'ADDRESS2': '',
    'CITY': 'LA',
    'STATE': 'DF',
    'ZIPCODE': '70403-900',
    'COUNTRY': 'United States of America',
    'COUNTRY_CODE': 'us',
    'PHONE': '556133127400',
    'FAX': '',
    'CUSTOMEREMAIL': 'customer@2Checkout.com',
    'FIRSTNAME_D': 'Customer',
    'LASTNAME_D': '2Checkout',
    'COMPANY_D': '',
    'ADDRESS1_D': 'Test Address',
    'ADDRESS2_D': '',
    'CITY_D': 'LA',
    'STATE_D': 'DF',
    'ZIPCODE_D': '70403-900',
    'COUNTRY_D': 'United States of America',
    'COUNTRY_D_CODE': 'us',
    'PHONE_D': '556133127400',
    'EMAIL_D': 'customer@2Checkout.com',
    'IPADDRESS': '91.220.121.21',
    'IPCOUNTRY': 'Romania',
    'COMPLETE_DATE': '2023-06-09 15:31:23',
    'TIMEZONE_OFFSET': 'GMT+03:00',
    'CURRENCY': 'RON',
    'LANGUAGE': 'en',
    'ORDERFLOW': 'REGULAR',
    'IPN_PID[]': '40898000',
    'IPN_PNAME[]': 'Dynamic product',
    'IPN_PCODE[]': '',
    'IPN_EXTERNAL_REFERENCE[]': '',
    'IPN_INFO[]': '',
    'IPN_QTY[]': '1',
    'IPN_PRICE[]': '0.01',
    'IPN_VAT[]': '0.00',
    'IPN_VAT_RATE[]': '0.0000',
    'IPN_VER[]': '1',
    'IPN_DISCOUNT[]': '0.00',
    'IPN_PROMOTION_CATEGORY[]': '',
    'IPN_PROMONAME[]': '',
    'IPN_PROMOCODE[]': '',
    'IPN_ORDER_COSTS[]': '0',
    'IPN_SKU[]': '',
    'IPN_PARTNER_CODE': '',
    'IPN_PGROUP[]': '0',
    'IPN_PGROUP_NAME[]': '',
    'MESSAGE_ID': '254514574331',
    'MESSAGE_TYPE': 'COMPLETE',
    'IPN_LICENSE_PROD[]': '40898000',
    'IPN_LICENSE_TYPE[]': 'REGULAR',
    'IPN_LICENSE_REF[]': 'XRILXB9ZI3',
    'IPN_LICENSE_EXP[]': '9999-12-31 23:59:59',
    'IPN_LICENSE_START[]': '2023-06-09 15:31:18',
    'IPN_LICENSE_LIFETIME[]': 'YES',
    'IPN_LICENSE_ADDITIONAL_INFO[]': '',
    'IPN_DELIVEREDCODES[]': '',
    'IPN_DOWNLOAD_LINK': '',
    'IPN_TOTAL[]': '0.01',
    'IPN_TOTALGENERAL': '0.01',
    'IPN_SHIPPING': '0.00',
    'IPN_SHIPPING_TAX': '0.00',
    'AVANGATE_CUSTOMER_REFERENCE': '756227060',
    'EXTERNAL_CUSTOMER_REFERENCE': 'IOUER',
    'IPN_PARTNER_MARGIN_PERCENT': '0.00',
    'IPN_PARTNER_MARGIN': '0.00',
    'IPN_EXTRA_MARGIN': '0.00',
    'IPN_EXTRA_DISCOUNT': '0.00',
    'IPN_COUPON_DISCOUNT': '0.00',
    'IPN_LINK_SOURCE': 'testAPI.com',
    'IPN_COMMISSION': '2.7678',
    'REFUND_TYPE': '',
    'CHARGEBACK_RESOLUTION': 'NONE',
    'CHARGEBACK_REASON_CODE': '',
    'TEST_ORDER': '0',
    'IPN_ORDER_ORIGIN': 'API',
    'FRAUD_STATUS': 'APPROVED',
    'CARD_TYPE': 'mastercard',
    'CARD_LAST_DIGITS': '5547',
    'CARD_EXPIRATION_DATE': '05/27',
    'GATEWAY_RESPONSE': 'Approved',
    'IPN_DATE': '20230621183208',
    'FX_RATE': '0.20810660205937',
    'FX_MARKUP': '4',
    'PAYABLE_AMOUNT': '-0.57',
    'PAYOUT_CURRENCY': 'USD',
    'VENDOR_CODE': '250111206876',
    'PROPOSAL_ID': '',
    'HASH': 'c9dab0c182b551b1e5d2cc9c17d72c8a',
    'SIGNATURE_SHA2_256': '4e1987e54ba070da5dcb583251b71a221c64b41e7bf4d9156938ece4d536a00e',
    'SIGNATURE_SHA3_256': '9a4deae5e3479adcbecb7b1f8202ab86e3d3ff415b5add9c40737f1a01b400fc'
}


class CplusTestCase(unittest.TestCase):
    def setUp(self) -> None:
        super(CplusTestCase, self).setUp()


class CplusSignatureTest(CplusTestCase):
    cplus = None

    def setUp(self):
        super(CplusSignatureTest, self).setUp()
        self.cplus = twocheckout.CplusSignature()

    def test_1_get_signature_without_token_expiration(self):
        self.assertEqual(64, len(self.cplus.get_signature(
            config.TWOCHECKOUT_TEST_MERCHANT_ID,
            config.TWOCHECKOUT_TEST_BUYLINK_SECRET_WORD,
            json_encoded_convert_plus_parameters)))

    def test_2_get_signature_with_token_expiration(self):
        self.assertEqual(64, len(self.cplus.get_signature(
            config.TWOCHECKOUT_TEST_MERCHANT_ID,
            config.TWOCHECKOUT_TEST_BUYLINK_SECRET_WORD,
            json_encoded_convert_plus_parameters,
            1000)))


class ApiTestCase(unittest.TestCase):
    def setUp(self) -> None:
        super(ApiTestCase, self).setUp()


class OrderTest(ApiTestCase):
    order = None

    # setup auth headers
    def setUp(self):
        super(OrderTest, self).setUp()
        self.order = twocheckout.Order(auth_params)

    # Get order test
    def test_1_order_get(self):
        response = self.order.get(order_transaction_id)
        self.assertEqual(order_transaction_id, response['body']['RefNo'])

    # Create order test
    def test_2_order_create(self):
        self.assertEqual('REST_API_AVANGTE', self.order.create(order_params_test)['body']['ExternalReference'])


class IpnHelperTestCase(unittest.TestCase):
    ipn = None

    def setUp(self):
        super(IpnHelperTestCase, self).setUp()
        self.ipn = twocheckout.IpnHelper(config.TWOCHECKOUT_TEST_MERCHANT_SECRET_KEY)

    def test_1_ipn_sha3(self):
        params = ipn_payload.copy()

        self.assertEqual(True, self.ipn.is_valid(params))
    
    def test_2_ipn_sha2(self):
        params = ipn_payload.copy()
        if 'SIGNATURE_SHA3_256' in params:
            del params['SIGNATURE_SHA3_256']

        self.assertEqual(True, self.ipn.is_valid(params))
    
    def test_3_ipn_md5(self):
        params = ipn_payload.copy()
        if 'SIGNATURE_SHA3_256' in params:
            del params['SIGNATURE_SHA3_256']
        if 'SIGNATURE_SHA2_256' in params:
            del params['SIGNATURE_SHA2_256']

        self.assertEqual(True, self.ipn.is_valid(params))

    @freeze_time("Jan 1st, 2023")
    def test_4_ipn_calculate_response_sha3(self):
        params = ipn_payload.copy()
        date = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        expected = '<sig algo="sha3_256" date="' + date + '">8bfa5029589981a1f959cfb0f95fb16f1f270237bed4af3531ab2c162bf0d48c</sig>'
        received = self.ipn.calculate_ipn_response(params, date)
        
        self.assertEqual(expected, received)

    @freeze_time("Jan 1st, 2023")
    def test_5_ipn_calculate_response_sha2(self):
        params = ipn_payload.copy()
        if 'SIGNATURE_SHA3_256' in params:
            del params['SIGNATURE_SHA3_256']
        date = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        expected = '<sig algo="sha256" date="' + date + '">e2594e0b3054b5d21c9ea8be18356f1ac43f5ca6bb66473556f6beb49880adf9</sig>'
        received = self.ipn.calculate_ipn_response(params, date)
        
        self.assertEqual(expected, received)

    @freeze_time("Jan 1st, 2023")
    def test_6_ipn_calculate_response_md5(self):
        params = ipn_payload.copy()
        if 'SIGNATURE_SHA3_256' in params:
            del params['SIGNATURE_SHA3_256']
        if 'SIGNATURE_SHA2_256' in params:
            del params['SIGNATURE_SHA2_256']
        date = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        expected = '<EPAYMENT>' + date + '|8e8147a440040b520239d304735c2ef4</EPAYMENT>'
        received = self.ipn.calculate_ipn_response(params, date)
        
        self.assertEqual(expected, received)
