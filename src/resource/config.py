CONFIG = {
    "XING_API_URL": "https://www.xing.com/xing-one/api",

    "REQUEST_DATA": {
        "operationName": "getXingId",
        "variables": {
            "profileId": "NULL",
            "actionsFilter": [
                "ADD_CONTACT",
                "ADVERTISE_PROFILE",
                "BLOCK_USER",
                "BOOKMARK_USER",
                "CONFIRM_CONTACT",
                "EDIT_XING_ID",
                "FOLLOW",
                "INVITE_GROUP",
                "OPEN_INSIDER_COLLECTION",
                "OPEN_SETTINGS",
                "OPEN_XTM",
                "PRINT",
                "REPORT_PROFILE",
                "SEND_MESSAGE",
                "SHARE",
                "SHOW_CONTACT_DETAILS",
                "UNBLOCK_USER",
                "UNFOLLOW"
            ]
        },
        "query": "query getXingId($profileId: SlugOrID!, $actionsFilter: [AvailableAction!]) {\n  profileModules(id: $profileId) {\n    __typename\n    xingIdModule(actionsFilter: $actionsFilter) {\n      xingId {\n        status {\n          localizationValue\n          __typename\n        }\n        __typename\n      }\n      __typename\n      ...xingIdContactDetails\n      ...xingIdModuleCta\n    }\n  }\n}\n\nfragment xingIdContactDetails on XingIdModule {\n  contactDetails {\n    business {\n      address {\n        city\n        country {\n          countryCode\n          name: localizationValue\n          __typename\n        }\n        province {\n          id\n          canonicalName\n          name: localizationValue\n          __typename\n        }\n        street\n        zip\n        __typename\n      }\n      email\n      fax {\n        phoneNumber\n        __typename\n      }\n      mobile {\n        phoneNumber\n        __typename\n      }\n      phone {\n        phoneNumber\n        __typename\n      }\n      __typename\n    }\n    private {\n      address {\n        city\n        country {\n          countryCode\n          name: localizationValue\n          __typename\n        }\n        province {\n          id\n          canonicalName\n          name: localizationValue\n          __typename\n        }\n        street\n        zip\n        __typename\n      }\n      email\n      fax {\n        phoneNumber\n        __typename\n      }\n      mobile {\n        phoneNumber\n        __typename\n      }\n      phone {\n        phoneNumber\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment xingIdModuleCta on XingIdModule {\n  actions {\n    __typename\n    label\n  }\n  __typename\n}\n"
    },

    "REQUEST_HEADERS": {
        "content-type": "application/json",
        "Content-Length": "",
        "Cookie": ""
    }
}
