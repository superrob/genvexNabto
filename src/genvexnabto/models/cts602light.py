from typing import Dict, List
from .basemodel import ( GenvexNabtoBaseModel, GenvexNabtoDatapointKey, GenvexNabtoDatapoint, GenvexNabtoSetpointKey, GenvexNabtoSetpoint )

class GenvexNabtoCTS602Light(GenvexNabtoBaseModel):
    def __init__(self, slaveDeviceModel):
        super().__init__(slaveDeviceModel)

        self._datapoints = {
            GenvexNabtoDatapointKey.TEMP_SUPPLY: GenvexNabtoDatapoint(obj=0, address=37, divider=100, offset=0),
            GenvexNabtoDatapointKey.TEMP_OUTSIDE: GenvexNabtoDatapoint(obj=0, address=38, divider=100, offset=0),
            GenvexNabtoDatapointKey.TEMP_EXHAUST: GenvexNabtoDatapoint(obj=0, address=33, divider=100, offset=0),
            GenvexNabtoDatapointKey.TEMP_EXTRACT: GenvexNabtoDatapoint(obj=0, address=34, divider=100, offset=0),
            GenvexNabtoDatapointKey.TEMP_HEATER: GenvexNabtoDatapoint(obj=0, address=39, divider=100, offset=0),
            GenvexNabtoDatapointKey.HUMIDITY: GenvexNabtoDatapoint(obj=0, address=51, divider=100, offset=0),
            GenvexNabtoDatapointKey.DUTYCYCLE_SUPPLY: GenvexNabtoDatapoint(obj=0, address=98, divider=1, offset=0),
            GenvexNabtoDatapointKey.DUTYCYCLE_EXTRACT: GenvexNabtoDatapoint(obj=0, address=99, divider=1, offset=0),
            GenvexNabtoDatapointKey.BYPASS_ACTIVE: GenvexNabtoDatapoint(obj=0, address=129, divider=1, offset=0),
            GenvexNabtoDatapointKey.CO2_LEVEL: GenvexNabtoDatapoint(obj=0, address=53, divider=1, offset=0),
            GenvexNabtoDatapointKey.FILTER_DAYS_LEFT: GenvexNabtoDatapoint(obj=0, address=101, divider=1, offset=0),
            GenvexNabtoDatapointKey.CONTROLSTATE_602: GenvexNabtoDatapoint(obj=0, address=85, divider=1, offset=0),
            GenvexNabtoDatapointKey.ALARM_CTS602NO1: GenvexNabtoDatapoint(obj=0, address=64, divider=1, offset=0),
            GenvexNabtoDatapointKey.ALARM_CTS602NO2: GenvexNabtoDatapoint(obj=0, address=67, divider=1, offset=0),
            GenvexNabtoDatapointKey.ALARM_CTS602NO3: GenvexNabtoDatapoint(obj=0, address=70, divider=1, offset=0)
        }

        self._setpoints = {
            GenvexNabtoSetpointKey.FAN_SPEED: GenvexNabtoSetpoint(read_obj=0, read_address=135, write_obj=0, write_address=135, divider=1, offset=0, min=0, max=4),
            GenvexNabtoSetpointKey.TEMP_SETPOINT: GenvexNabtoSetpoint(read_obj=0, read_address=136, write_obj=0, write_address=136, divider=100, offset=0, min=0, max=3000, step=0.5),
            GenvexNabtoSetpointKey.FILTER_RESET: GenvexNabtoSetpoint(read_obj=0, read_address=67, write_obj=0, write_address=67, divider=1, offset=0, min=0, max=1),            
            GenvexNabtoSetpointKey.FILTER_DAYS_SETTING: GenvexNabtoSetpoint(read_obj=0, read_address=153, write_obj=0, write_address=153, divider=1, offset=0, min=0, max=365, step=1)
        }

        self._defaultDatapointRequest = [
            GenvexNabtoDatapointKey.TEMP_SUPPLY,
            GenvexNabtoDatapointKey.TEMP_OUTSIDE,
            GenvexNabtoDatapointKey.TEMP_EXHAUST,
            GenvexNabtoDatapointKey.TEMP_EXTRACT,
            GenvexNabtoDatapointKey.HUMIDITY,
            GenvexNabtoDatapointKey.DUTYCYCLE_SUPPLY,
            GenvexNabtoDatapointKey.DUTYCYCLE_EXTRACT,
            GenvexNabtoDatapointKey.BYPASS_ACTIVE,
            GenvexNabtoDatapointKey.CO2_LEVEL,
            GenvexNabtoDatapointKey.FILTER_DAYS_LEFT,
            GenvexNabtoDatapointKey.CONTROLSTATE_602,
            GenvexNabtoDatapointKey.ALARM_CTS602NO1,
            GenvexNabtoDatapointKey.ALARM_CTS602NO2,
            GenvexNabtoDatapointKey.ALARM_CTS602NO3
        ]

        self._defaultSetpointRequest = [
            GenvexNabtoSetpointKey.FAN_SPEED,
            GenvexNabtoSetpointKey.TEMP_SETPOINT,
            GenvexNabtoSetpointKey.FILTER_DAYS_SETTING
        ]

    def getModelName(self):
        return "CTS 602light"
    
    def getManufacturer(self):
        return "Nilan"