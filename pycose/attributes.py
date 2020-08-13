from enum import IntEnum, unique


@unique
class CoseAlgorithm(IntEnum):
    ES512 = -36
    ES384 = -35
    ECDH_SS_A256KW = -34
    ECDH_SS_A192KW = -33
    ECDH_SS_A128KW = -32
    ECDH_ES_A256KW = -31
    ECDH_ES_A192KW = -30
    ECDH_ES_A128KW = -29
    ECDH_SS_HKDF_512 = -28
    ECDH_SS_HKDF_256 = -27
    ECDH_ES_HKDF_512 = -26
    ECDH_ES_HKDF_256 = -25
    DIRECT_HKDF_AES_256 = -13
    DIRECT_HKDF_SHA_128 = -12
    DIRECT_HKDF_SHA_512 = -11
    DIRECT_HKDF_SHA_256 = -10
    EDDSA = -8
    ES256 = -7
    DIRECT = -6
    A256KW = -5
    A192KW = -4
    A128KW = -3
    A128GCM = 1
    A192GCM = 2
    A256GCM = 3
    HMAC_256_64 = 4
    HMAC_256_256 = 5
    HMAC_384_384 = 6
    HMAC_512_512 = 7
    AES_CCM_16_64_128 = 10
    AES_CCM_16_64_256 = 11
    AES_CCM_64_64_128 = 12
    AES_CCM_64_64_256 = 13
    AES_MAC_128_64 = 14
    AES_MAC_256_64 = 15
    CHACHA20_POLY1305 = 24
    AES_MAC_128_128 = 25
    AES_MAC_256_128 = 26
    AES_CCM_16_128_128 = 30
    AES_CCM_16_128_256 = 31
    AES_CCM_64_128_128 = 32
    AES_CCM_64_128_256 = 33

    @classmethod
    def has_member(cls, item):
        return item in cls.__members__

    @classmethod
    def has_value(cls, value):
        return value in set(cls.__members__[attr] for attr in cls.__members__)
