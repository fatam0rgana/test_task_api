from hashlib import sha256
from uuid import uuid4


def data_to_hash(dictionary, keys_required, secret_key):
    """Generates hash from provided data"""
    sorted_data = [str(dictionary.get(key)) for key in sorted(keys_required)]
    result_data = ':'.join(sorted_data) + secret_key
    dictionary['sign'] = sha256(result_data.encode('utf-8')).hexdigest()
    return dictionary


def generate_uuid():
    """Generates unique value for shop_order"""
    return uuid4()


