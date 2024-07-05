# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"ip_address": "ipAddress"})
class Locator(BaseModel):
    """Locator

    :param ip_address: ip_address, defaults to None
    :type ip_address: str, optional
    """

    def __init__(self, ip_address: str = None):
        if ip_address is not None:
            self.ip_address = ip_address


@JsonMap({})
class HierarchyFlightsNearestRequest(BaseModel):
    """HierarchyFlightsNearestRequest

    :param locale: locale, defaults to None
    :type locale: str, optional
    :param locator: locator, defaults to None
    :type locator: Locator, optional
    """

    def __init__(self, locale: str = None, locator: Locator = None):
        if locale is not None:
            self.locale = locale
        if locator is not None:
            self.locator = self._define_object(locator, Locator)
