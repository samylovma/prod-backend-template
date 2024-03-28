__all__ = (
    "hash_password",
    "check_password",
)

import bcrypt


def hash_password(password: str) -> bytes:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def check_password(password: str, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(password=password.encode(), hashed_password=hashed_password)
