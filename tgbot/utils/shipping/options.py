from aiogram.types import ShippingOption, LabeledPrice

UA_NOVAPOSHTA_SHIPPING = ShippingOption(
    id="ua_nova",
    title="Delivery in Ukraine by Nova Poshta",
    prices=[
        LabeledPrice(
            label="Nova Poshta",
            amount=10000
        )
    ]
)

UA_SHIPPING = ShippingOption(
    id="ua",
    title="Delivery in Ukraine by Ukrposhta",
    prices=[
        LabeledPrice(
            label="Ukrposhta",
            amount=5000
        )
    ]
)

RO_SHIPPING = ShippingOption(
    id="ro",
    title="Delivery in Romania by Poshta Romana",
    prices=[
        LabeledPrice(
            label="Poshta Romana",
            amount=7000
        )
    ]
)

RO_NOVAPOSHTA_SHIPPING = ShippingOption(
    id="ro_nova",
    title="Delivery in Romania by Nova Poshta",
    prices=[
        LabeledPrice(
            label="Nova Poshta",
            amount=20000
        )
    ]
)

BG_SHIPPING = ShippingOption(
    id="bg",
    title="Delivery in Bulgaria",
    prices=[
        LabeledPrice(
            label="Delivery of Bulgaria",
            amount=12000
        )
    ]
)

FAST_SHIPPING = ShippingOption(
    id="capitals",
    title="Fast delivery in capitals",
    prices=[
        LabeledPrice(
            label="Fast delivery",
            amount=20000
        )
    ]
)