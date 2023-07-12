import hmac
from .error import TwocheckoutError
from datetime import datetime


# more information on calculating the IPN HASH signature can be found here
# https://knowledgecenter.2checkout.com/API-Integration/Webhooks/06Instant_Payment_Notification_(IPN)/Calculate-the-IPN-HASH-signature#PHP_Hash_Example
class IpnHelper:
    secret_key = None

    def __init__(self, secret):
        self.secret_key = secret

    # check if the received request is a valid one
    def is_valid(self, params):
        if self.secret_key is None:
            raise TwocheckoutError('SECRET KEY MISSING', 'You must pass the secret key to the constructor class')

        try:
            result = ''
            algorithm = self.__get_algorithm(params)
            receivedHash = self.__get_compare_hash(algorithm, params)
            for param in params:
                if param not in ["HASH", "SIGNATURE_SHA2_256", "SIGNATURE_SHA3_256"]:
                    var_type = type(params[param])
                    if var_type is list:
                        result += self.expand(params[param])
                    else:
                        size = str(len(params[param].lstrip()))
                        result += size + params[param].lstrip()
            try:
                calcHash = hmac.new(self.secret_key.encode(), result.encode(), algorithm).hexdigest()
                return receivedHash == calcHash
            except Exception as e:
                raise TwocheckoutError('Hash signatures do not match', e.args)

        except Exception as error:
            raise TwocheckoutError('Exception validating ipn signature', error.args)

    def calculate_ipn_response(self, params, date=None):
        if date == None:
            now = datetime.now()
            date = now.strftime('%Y%m%d%H%M%S')

        try:
            result = ''
            ipn_response = {'IPN_PID': [params['IPN_PID[]']],
                            'IPN_NAME': [params['IPN_PNAME[]']],
                            'IPN_DATE': params['IPN_DATE'],
                            'DATE': date}

            for param in ipn_response:
                if type(ipn_response[param]) is list:
                    result += self.__expand(ipn_response[param])
                else:
                    size = len(ipn_response[param])
                    result += str(size) + ipn_response[param]

            algorithm = self.__get_algorithm(params)
            signature = hmac.new(self.secret_key.encode(), result.encode(), algorithm).hexdigest()

            return self.__format_response(algorithm, date, signature)
        except Exception as e:
            raise TwocheckoutError('Exception generating ipn response', e.args)

    def __expand(self, val_list):
        result = ''
        for val in val_list:
            size = len(val.lstrip())
            result += str(size) + str(val.lstrip())
        return result
    
    def __get_algorithm(self, params):
      if 'SIGNATURE_SHA3_256' in params:
        return 'sha3_256'
      elif 'SIGNATURE_SHA2_256' in params:
        return 'sha256'
      else:
        return 'md5'

    def __get_compare_hash(self, algorithm, params):
        if algorithm == "sha3_256":
            return params['SIGNATURE_SHA3_256']
        elif algorithm == "sha256":
            return params['SIGNATURE_SHA2_256']
        else:
            return params['HASH']

    def __format_response(self, algorithm, date, signature):
        if algorithm == "md5":
            return '<EPAYMENT>' + date + '|' + signature + '</EPAYMENT>'
        else:
            return '<sig algo=\"' + algorithm +'\" date=\"' + date + '\">' + signature + '</sig>'
