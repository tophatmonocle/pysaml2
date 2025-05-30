__author__ = 'rolandh'

from pathutils import full_path


CONFIG = {
    "entityid": "urn:mace:example.com:saml:roland:sp",
    "name": "urn:mace:example.com:saml:roland:sp",
    "description": "My own SP",
    "service": {
        "sp": {
            "endpoints": {
                "assertion_consumer_service": [
                    "http://lingon.catalogix.se:8087/"],
            },
            "required_attributes": ["surName", "givenName", "mail"],
            "optional_attributes": ["title"],
            "idp": ["urn:mace:example.com:saml:roland:idp"],
        }
    },
    "debug": 1,
    "key_file": full_path("test.key"),
    "cert_file": full_path("test.pem"),
    # "xmlsec_binary" : None,
    "metadata": [{
        "class": "saml2_tophat.mdstore.MetaDataFile",
        "metadata": [(full_path("idp.xml"), ), (full_path("vo_metadata.xml"), )],
    }],
    "virtual_organization": {
        "urn:mace:example.com:it:tek": {
            "nameid_format": "urn:oid:1.3.6.1.4.1.1466.115.121.1.15-NameID",
            "common_identifier": "umuselin",
        }
    },
    "subject_data": full_path("subject_data.db"),
    "accepted_time_diff": 60,
    "attribute_map_dir": full_path("attributemaps"),
    "organization": {
        "name": ("AB Exempel", "se"),
        "display_name": ("AB Exempel", "se"),
        "url": "http://www.example.org",
    },
    "contact_person": [{
                           "given_name": "Roland",
                           "sur_name": "Hedberg",
                           "telephone_number": "+46 70 100 0000",
                           "email_address": ["tech@eample.com",
                                             "tech@example.org"],
                           "contact_type": "technical"
                       },
    ],
    "logger": {
        "syslog": {
            "address": ("localhost", 514),
            "facility": "local3",
            "socktype": "dgram",
        },
        "loglevel": "info",
    }
}
