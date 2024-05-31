from typing import Any

from aiogram import Router, F
from aiogram.filters.command import Command
from aiogram.handlers import MessageHandler, PreCheckoutQueryHandler, ShippingQueryHandler
from aiogram.types import LabeledPrice, Message

from tgbot.data.config import get_config
from tgbot.keyboards.payments.some_payment_inlinekeyboard import payment_keyboard
from tgbot.utils.multilingualism.langs import get_text
from tgbot.utils.shipping.options import UA_SHIPPING, RO_SHIPPING, BG_SHIPPING, FAST_SHIPPING, UA_NOVAPOSHTA_SHIPPING, \
    RO_NOVAPOSHTA_SHIPPING


class Payment(MessageHandler):
    async def handle(self) -> Any:
        config = get_config()
        price = 12345  # 123.45 uah
        vat_percent = .2  # If in your region Percent of VAT another, change it
        bonus_k = .1  # Can be like percent or some number

        await self.bot.send_invoice(
            chat_id=self.from_user.id,
            title="Some product",
            description="Description of your product",
            payload="Payment trough a bot",
            provider_token=config.payment.token,
            currency=config.payment.currency,
            prices=[
                LabeledPrice(
                    label="Price",
                    amount=price
                ),
                LabeledPrice(
                    label="VAT",
                    amount=round(price * vat_percent)  # Count VAT, multiply price to your VAT percent
                ),
                LabeledPrice(
                    label="Bonus",
                    amount=-round(price * bonus_k)  # Count Bonus size, it can be like a percent, or maybe some number. It's negative num!
                )
            ],
            max_tip_amount=round(price*.25),
            suggested_tip_amounts=[(price*.25//4) * k for k in range(1, 5)],
            start_parameter='some_deep_link',  # If it's None, then someone else can pay for user, if there is some deep_link, then he will start bot with deep link,
            provider_data=None,  # If payment provider needs some data for transaction, then with this parameter you can send it
            photo_url="some url with photo",  # Photo of the product, or your company logo, because it will be seen by user during payment
            photo_size=100,
            photo_width=800,
            photo_height=450,
            need_name=False,  # User will know that you take him privacy info
            need_phone_number=False,  # If you need user phone number
            need_email=False,
            need_shipping_address=False,  # If you need to deliver product by address
            send_phone_number_to_provider=False,  # If your provider needs phone number of client (Then set need_phone_number to True)
            send_email_to_provider=False,  # If your provider needs email of client (Then set need_email to True)
            is_flexible=True,  # If the final price depends on the delivery, then set it True
            disable_notification=False,
            protect_content=False,
            reply_to_message_id=None,  # If you want to reply to client after pay something, then set his id
            allow_sending_without_reply=True,
            reply_markup=payment_keyboard(),
            request_timeout=15
        )


class CheckShipping(ShippingQueryHandler):
    async def handle(self) -> Any:
        shipping_options = []
        country_code = self.update.shipping_query.shipping_address.country_code

        counties = ['UA', 'RO', 'BG']
        if not country_code in counties:
            await self.bot.send_message(
                chat_id=self.from_user.id,
                text="Unavailable country was chosen!"
            )

        if country_code == "UA":
            shipping_options.append(UA_SHIPPING)
            shipping_options.append(UA_NOVAPOSHTA_SHIPPING)
        elif country_code == "RO":
            shipping_options.append(RO_SHIPPING)
            shipping_options.append(RO_NOVAPOSHTA_SHIPPING)
        elif country_code == "BG":
            shipping_options.append(BG_SHIPPING)

        city = self.update.shipping_query.shipping_address.city
        cities = ["Kiev", "Bucharest", "Sofia"]
        if city in cities:
            shipping_options.append(FAST_SHIPPING)

        await self.bot.answer_shipping_query(
            shipping_query_id=self.update.shipping_query.id,
            ok=True,
            shipping_options=shipping_options,
            error_message="No shipping offer with your address("
        )


class PreCheckout(PreCheckoutQueryHandler):
    async def handle(self) -> Any:
        await self.bot.answer_pre_checkout_query(self.update.pre_checkout_query.id, ok=True)


async def successful_payment(message: Message):
    await message.answer(text=get_text(message.from_user.language_code, "successful_payment").format(
        first_name=message.from_user.first_name,
        total_amount=message.successful_payment.total_amount,
        currency=message.successful_payment.currency
    ))


def register(router: Router):
    router.message.register(Payment, Command(commands='pay'))
    router.shipping_query.register(CheckShipping)
    router.pre_checkout_query.register(PreCheckout)
    router.message.register(successful_payment, F.content_type.in_({"successful_payment"}))
