# -*- coding: utf-8 -*-
"""Module for IQ Option buyV2 websocket chanel."""

from src.api.iqoption.ws.chanels.base import Base


class Buyv2(Base):
    """Class for IQ option buy websocket chanel."""
    # pylint: disable=too-few-public-methods

    name = "buyV2"

    def __call__(self, price, active, option, direction, exp_timestamp=None):
        """Method to send message to buyv2 websocket chanel.

        :param price: The buying price.
        :param active: The buying active.
        :param option: The buying option.
        :param direction: The buying direction.
        """
        expiration_timestamp = self.api.timesync.expiration_timestamp
        if exp_timestamp:
            expiration_timestamp = exp_timestamp

        data = {"price": price,
                "act": active,
                "exp": expiration_timestamp,
                "type": option,
                "direction": direction,
                "time": self.api.timesync.server_timestamp
                }

        self.send_websocket_request(self.name, data)
