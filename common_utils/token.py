import jwt


def encode_jwt(payload, private_key: str):
    encoded = jwt.encode(payload, private_key.encode(), algorithm='RS256')
    return encoded
