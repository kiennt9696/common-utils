import jwt
from common_utils.exception import InvalidToken


def encode_jwt(payload, private_key: str):
    encoded = jwt.encode(payload, private_key.encode(), algorithm="RS256")
    return encoded


def verify_token(token, public_key):
    try:
        data = jwt.decode(
            token,
            public_key.encode(),
            algorithms="RS256",
            options={"verify_aud": False},
        )
    except jwt.exceptions.InvalidSignatureError:
        raise InvalidToken(error_code=4011000)
    except jwt.exceptions.InvalidAudienceError:
        raise InvalidToken(error_code=4011001)
    except jwt.exceptions.ExpiredSignatureError:
        raise InvalidToken(error_code=4011002)
    except jwt.exceptions.DecodeError:
        raise InvalidToken(error_code=4011003)
    except Exception:
        raise InvalidToken()
    return data


def get_current_user(token, public_key: str) -> str:
    token = jwt.decode(
        token, public_key.encode(), algorithms="RS256", options={"verify_aud": False}
    )
    return token
