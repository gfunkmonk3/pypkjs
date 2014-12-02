__author__ = 'katharine'

import PyV8 as v8
from console import Console
from performance import Performance
from timers import Timers
from localstorage import LocalStorage
from jsJSON import JSON
from pebble import Pebble
from xhr import xhr_factory


class PebbleKitJS(v8.JSClass):
    def __init__(self, group):
        self.console = Console()
        self.performance = Performance()
        self.localStorage = LocalStorage()
        self.JSON = JSON()
        self.Pebble = Pebble()
        self.XMLHttpRequest = xhr_factory(group)

        timer_impl = Timers(group)
        self.setTimeout = timer_impl.setTimeout
        self.clearTimeout = timer_impl.clearTimeout
        self.setInterval = timer_impl.setInterval
        self.clearInterval = timer_impl.clearInterval
