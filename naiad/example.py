from naiad.core import MoistureFeedController
from contracts import contract


class ExampleMoistureFeedController(MoistureFeedController):
    @contract
    def feed(self, volume: float):
        MoistureFeedController.feed(self, volume)
        print('%s.feed(%f) has been called.' % (self.__class__, volume))
