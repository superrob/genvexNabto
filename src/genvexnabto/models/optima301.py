from typing import Dict, List
from .basemodel import ( GenvexNabtoBaseModel, GenvexNabtoDatapointKey, GenvexNabtoDatapoint, GenvexNabtoSetpointKey, GenvexNabtoSetpoint )

class GenvexNabtoOptima301(GenvexNabtoBaseModel):
    def __init__(self, slaveDeviceModel):
        super().__init__(slaveDeviceModel)

        self._datapoints = {
            GenvexNabtoDatapointKey.TEMP_SUPPLY: GenvexNabtoDatapoint(address=0, divider=10, offset=-300), #T1
            GenvexNabtoDatapointKey.TEMP_OUTSIDE: GenvexNabtoDatapoint(address=2, divider=10, offset=-300), #T3
            GenvexNabtoDatapointKey.TEMP_EXHAUST: GenvexNabtoDatapoint(address=3, divider=10, offset=-300), #T4
            GenvexNabtoDatapointKey.TEMP_EXTRACT: GenvexNabtoDatapoint(address=6, divider=10, offset=-300), #T7
            GenvexNabtoDatapointKey.HUMIDITY: GenvexNabtoDatapoint(address=10),
            GenvexNabtoDatapointKey.DUTYCYCLE_SUPPLY: GenvexNabtoDatapoint(address=102),
            GenvexNabtoDatapointKey.DUTYCYCLE_EXTRACT: GenvexNabtoDatapoint(address=103),
            GenvexNabtoDatapointKey.RPM_SUPPLY: GenvexNabtoDatapoint(address=108),
            GenvexNabtoDatapointKey.RPM_EXTRACT: GenvexNabtoDatapoint(address=109),
            GenvexNabtoDatapointKey.BYPASS_ACTIVE: GenvexNabtoDatapoint(address=104)
        }

        self._setpoints = {
            GenvexNabtoSetpointKey.FAN_SPEED: GenvexNabtoSetpoint(read_address=100, write_address=100, min=0, max=4),
            GenvexNabtoSetpointKey.TEMP_SETPOINT: GenvexNabtoSetpoint(read_address=0, write_address=0, divider=10, offset=100, min=0, max=200, step=0.5),         
            GenvexNabtoSetpointKey.FILTER_RESET: GenvexNabtoSetpoint(read_address=105, write_address=105, min=0, max=1),
            GenvexNabtoSetpointKey.PREHEATING: GenvexNabtoSetpoint(read_address=20, write_address=20, min=0, max=1),         
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL1: GenvexNabtoSetpoint(read_address=6, write_address=6, min=0, max=100),
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL2: GenvexNabtoSetpoint(read_address=7, write_address=7, min=0, max=100),
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL3: GenvexNabtoSetpoint(read_address=8, write_address=8, min=0, max=100),
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL1: GenvexNabtoSetpoint(read_address=9, write_address=9, min=0, max=100),
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL2: GenvexNabtoSetpoint(read_address=10, write_address=10, min=0, max=100),
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL3: GenvexNabtoSetpoint(read_address=11, write_address=11, min=0, max=100),
            GenvexNabtoSetpointKey.COOLING_ENABLE: GenvexNabtoSetpoint(read_address=2, write_address=2, min=0, max=1),
            GenvexNabtoSetpointKey.COOLING_TEMPERATURE: GenvexNabtoSetpoint(read_address=1, write_address=1, min=30, max=100, step=0.1),
        }

    def getModelName(self):
        return "Optima 301"
    
    def getManufacturer(self):
        return "Genvex"

    def getDefaultDatapointRequest(self) -> List[GenvexNabtoDatapointKey]:
        return [
            GenvexNabtoDatapointKey.TEMP_SUPPLY,
            GenvexNabtoDatapointKey.TEMP_OUTSIDE,
            GenvexNabtoDatapointKey.TEMP_EXHAUST,
            GenvexNabtoDatapointKey.TEMP_EXTRACT,
            GenvexNabtoDatapointKey.HUMIDITY,
            GenvexNabtoDatapointKey.DUTYCYCLE_SUPPLY,
            GenvexNabtoDatapointKey.DUTYCYCLE_EXTRACT,
            GenvexNabtoDatapointKey.RPM_SUPPLY,            
            GenvexNabtoDatapointKey.RPM_EXTRACT,
            GenvexNabtoDatapointKey.BYPASS_ACTIVE
        ]
    
    def getDefaultSetpointRequest(self) -> List[GenvexNabtoSetpointKey]:
        return [
            GenvexNabtoSetpointKey.FAN_SPEED,
            GenvexNabtoSetpointKey.TEMP_SETPOINT,
            GenvexNabtoSetpointKey.PREHEATING,
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL1,
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL2,
            GenvexNabtoSetpointKey.SUPPLY_AIR_LEVEL3,
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL1,
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL2,
            GenvexNabtoSetpointKey.EXTRACT_AIR_LEVEL3,
            GenvexNabtoSetpointKey.COOLING_ENABLE,
            GenvexNabtoSetpointKey.COOLING_TEMPERATURE
        ]