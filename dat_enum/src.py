from enum import Enum

class Links(Enum):
    DOMEN_LINK = "https://demo.app.stack-it.ru/app/"
    AUTH_LINK = f"{DOMEN_LINK}graphql"
    RECORD_LINK = f"{DOMEN_LINK}stackgateway/demo/fl/kvpl"
