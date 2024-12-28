import unittest
from common import GenvexNabtoCTS602, GenvexNabtoDatapointKey
from modelTester import modelTester

class CTS602WithNoQuirksTest(modelTester):    
    def setUp(self):
        self.loadedModel = GenvexNabtoCTS602(0)
        self.loadedModel.addDeviceQuirks() # Should not load any quirks.
        self.expectedName = "CTS 602 - Ukendt type"
        self.expectedManufacturer = "Nilan"

    def test_quirks_not_loaded(self):
        self.assertNotIn(GenvexNabtoDatapointKey.HOTWATER_TOP, self.loadedModel._datapoints)

class CTS602WithQuirksTest(modelTester):    
    def setUp(self):
        self.loadedModel = GenvexNabtoCTS602(12)
        self.loadedModel.addDeviceQuirks()
        self.expectedName = "CTS 602 - VP18cCompact"
        self.expectedManufacturer = "Nilan"

    def test_hotwater_temp_quirk_loaded(self):
        self.assertIn(GenvexNabtoDatapointKey.HOTWATER_TOP, self.loadedModel._datapoints)

class CTS602WithHPSQuirksTest(modelTester):    
    def setUp(self):
        self.loadedModel = GenvexNabtoCTS602(144)
        self.loadedModel.addDeviceQuirks()
        self.expectedName = "CTS 602 - Compact P AIR"
        self.expectedManufacturer = "Nilan"

    def test_hotwater_temp_quirk_loaded(self):
        self.assertIn(GenvexNabtoDatapointKey.HPS_HEATER_ACTIVE, self.loadedModel._datapoints)       
    

if __name__ == '__main__':
    unittest.main()