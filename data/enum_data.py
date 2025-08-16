from enum import Enum


class InputField(str, Enum):
    EMAIL = "EMAIL"
    PASSWORD = "PASSWORD"


class MaskingPassword(str, Enum):
    MASKED = "password"
    UNMASKED = "text"
