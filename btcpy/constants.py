from decimal import Decimal


class Constants(object):

    _lookup = {'base58.prefixes': {'1': ('p2pkh', 'mainnet'),
                                   'm': ('p2pkh', 'testnet'),
                                   'n': ('p2pkh', 'testnet'),
                                   '3': ('p2sh', 'mainnet'),
                                   '2': ('p2sh', 'testnet')},
               'base58.raw_prefixes': {('mainnet', 'p2pkh'): bytearray(b'\x00'),
                                       ('testnet', 'p2pkh'): bytearray(b'\x6f'),
                                       ('mainnet', 'p2sh'): bytearray(b'\x05'),
                                       ('testnet', 'p2sh'): bytearray(b'\xc4')},
               'bech32.net_to_hrp': {'mainnet': 'bc',
                                     'testnet': 'tb'},
               'bech32.hrp_to_net': {'bc': 'mainnet',
                                     'tb': 'testnet'},
               'xkeys.prefixes': {'mainnet': ['x','z','y'], 'testnet': ['t','v','u']},
               'xpub.versions': {'mainnet': [b'\x04\x88\xb2\x1e',b'\x04\xb2\x47\x46',b'\x04\x9d\x7c\xb2'], 'testnet': [b'\x04\x35\x87\xcf',b'\x04\x5f\x1c\xf6',b'\x04\x4a\x52\x62']},
               'xprv.versions': {'mainnet': [b'\x04\x88\xad\xe4',b'\x04\xb2\x43\x0c',b'\x04\x9d\x78\x78'], 'testnet': [b'\x04\x35\x83\x94',b'\x04\x5f\x18\xbc',b'\x04\x4a\x4e\x28']},
               'xpub.prefixes': {'mainnet': ['xpub','zpub','ypub'], 'testnet': ['tpub','vpub','upub']},
               'xprv.prefixes': {'mainnet': ['xprv','zpriv','ypriv'], 'testnet': ['tprv','vpriv','upriv']},
               'wif.prefixes': {'mainnet': 0x80, 'testnet': 0xef},
               'from_unit': Decimal('1e-8'),
               'to_unit': Decimal('1e8')
               }

    @staticmethod
    def get(key):
        try:
            return Constants._lookup[key]
        except KeyError:
            raise ValueError('Unknown constant: {}'.format(key))
