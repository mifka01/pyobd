# -*- coding: utf-8 -*-

########################################################################
#                                                                      #
# python-OBD: A python OBD-II serial module derived from pyobd         #
#                                                                      #
# Copyright 2004 Donour Sizemore (donour@uchicago.edu)                 #
# Copyright 2009 Secons Ltd. (www.obdtester.com)                       #
# Copyright 2009 Peter J. Creath                                       #
# Copyright 2016 Brendan Whitfield (brendan-w.com)                     #
#                                                                      #
########################################################################
#                                                                      #
# commands.py                                                          #
#                                                                      #
# This file is part of python-OBD (a derivative of pyOBD)              #
#                                                                      #
# python-OBD is free software: you can redistribute it and/or modify   #
# it under the terms of the GNU General Public License as published by #
# the Free Software Foundation, either version 2 of the License, or    #
# (at your option) any later version.                                  #
#                                                                      #
# python-OBD is distributed in the hope that it will be useful,        #
# but WITHOUT ANY WARRANTY; without even the implied warranty of       #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the        #
# GNU General Public License for more details.                         #
#                                                                      #
# You should have received a copy of the GNU General Public License    #
# along with python-OBD.  If not, see <http://www.gnu.org/licenses/>.  #
#                                                                      #
########################################################################

import logging

from .OBDCommand import OBDCommand
from .decoders import *
from .protocols import ECU

logger = logging.getLogger(__name__)

# flake8: noqa
'''
Define command tables
'''

# NOTE: the NAME field will be used as the dict key for that sensor
# NOTE: commands MUST be in PID order, one command per PID (for fast lookup using __mode1__[pid])

# see OBDCommand.py for descriptions & purposes for each of these fields

__mode1__ = [
    #                      name                             description                    cmd  bytes       decoder           ECU       fast
    OBDCommand("PIDS_A"                     , "Podporované PIDy [01-20]"                  , b"0100", 6, pid,                   ECU.ENGINE, True),
    OBDCommand("STATUS"                     , "Stav od vymazání DTC"               , b"0101", 6, status,                ECU.ENGINE, True),
    OBDCommand("FREEZE_DTC"                 , "DTC, který spustil zmrazení snímku"     , b"0102", 4, single_dtc,            ECU.ENGINE, True),
    OBDCommand("FUEL_STATUS"                , "Stav palivového systému"                      , b"0103", 4, fuel_status,           ECU.ENGINE, True),
    OBDCommand("ENGINE_LOAD"                , "Vypočtené zatížení motoru"                  , b"0104", 3, percent,               ECU.ENGINE, True),
    OBDCommand("COOLANT_TEMP"               , "Teplota chladicí kapaliny motoru"              , b"0105", 3, temp,                  ECU.ENGINE, True),
    OBDCommand("SHORT_FUEL_TRIM_1"          , "Krátkodobý trim paliva - banka 1"           , b"0106", 3, percent_centered,      ECU.ENGINE, True),
    OBDCommand("LONG_FUEL_TRIM_1"           , "Dlouhodobý trim paliva - banka 1"            , b"0107", 3, percent_centered,      ECU.ENGINE, True),
    OBDCommand("SHORT_FUEL_TRIM_2"          , "Krátkodobý trim paliva - banka 2"           , b"0108", 3, percent_centered,      ECU.ENGINE, True),
    OBDCommand("LONG_FUEL_TRIM_2"           , "Dlouhodobý trim paliva - banka 2"            , b"0109", 3, percent_centered,      ECU.ENGINE, True),
    OBDCommand("FUEL_PRESSURE"              , "Tlak paliva"                           , b"010A", 3, fuel_pressure,         ECU.ENGINE, True),
    OBDCommand("INTAKE_PRESSURE"            , "Tlak v sacím potrubí"                , b"010B", 3, pressure,              ECU.ENGINE, True),
    OBDCommand("RPM"                        , "Otáčky motoru"                              , b"010C", 4, uas(0x07),             ECU.ENGINE, True),
    OBDCommand("SPEED"                      , "Rychlost vozidla"                           , b"010D", 3, uas(0x09),             ECU.ENGINE, True),
    OBDCommand("TIMING_ADVANCE"             , "Předstih časování"                          , b"010E", 3, timing_advance,        ECU.ENGINE, True),
    OBDCommand("INTAKE_TEMP"                , "Teplota nasávaného vzduchu"                         , b"010F", 3, temp,                  ECU.ENGINE, True),
    OBDCommand("MAF"                        , "Průtok vzduchu (MAF)"                     , b"0110", 4, uas(0x27),             ECU.ENGINE, True),
    OBDCommand("THROTTLE_POS"               , "Poloha škrticí klapky"                       , b"0111", 3, percent,               ECU.ENGINE, True),
    OBDCommand("AIR_STATUS"                 , "Stav sekundárního vzduchu"                    , b"0112", 3, air_status,            ECU.ENGINE, True),
    OBDCommand("O2_SENSORS"                 , "Přítomnost senzorů O2"                      , b"0113", 3, o2_sensors,            ECU.ENGINE, True),
    OBDCommand("O2_B1S1"                    , "O2: Banka 1 - napětí senzoru 1"           , b"0114", 4, sensor_voltage,        ECU.ENGINE, True),
    OBDCommand("O2_B1S2"                    , "O2: Banka 1 - Senzor 2 Napětí"           , b"0115", 4, sensor_voltage,        ECU.ENGINE, True),
    OBDCommand("O2_B1S3"                    , "O2: Banka 1 - Senzor 3 Napětí"           , b"0116", 4, sensor_voltage,        ECU.ENGINE, True),
    OBDCommand("O2_B1S4"                    , "O2: Banka 1 - Senzor 4 Napětí"           , b"0117", 4, sensor_voltage,        ECU.ENGINE, True),
    OBDCommand("O2_B2S1"                    , "O2: Banka 2 - Napětí snímače 1"           , b"0118", 4, sensor_voltage,        ECU.ENGINE, True),
    OBDCommand("O2_B2S2"                    , "O2: Banka 2 - napětí senzoru 2"           , b"0119", 4, sensor_voltage,        ECU.ENGINE, True),
    OBDCommand("O2_B2S3"                    , "O2: Banka 2 - Senzor 3 Napětí"           , b"011A", 4, sensor_voltage,        ECU.ENGINE, True),
    OBDCommand("O2_B2S4"                    , "O2: Banka 2 - Senzor 4 Napětí"           , b"011B", 4, sensor_voltage,        ECU.ENGINE, True),
    OBDCommand("OBD_COMPLIANCE"             , "Soulad s normami OBD"                , b"011C", 3, obd_compliance,        ECU.ENGINE, True),
    OBDCommand("O2_SENSORS_ALT"             , "Přítomnost snímačů O2 (náhradní)"          , b"011D", 3, o2_sensors_alt,        ECU.ENGINE, True),
    OBDCommand("AUX_INPUT_STATUS"           , "Stav pomocného vstupu (odpojení napájení)" , b"011E", 3, aux_input_status,      ECU.ENGINE, True),
    OBDCommand("RUN_TIME"                   , "Doba chodu motoru"                         , b"011F", 4, uas(0x12),             ECU.ENGINE, True),

    #                      name                             description                    cmd  bytes       decoder           ECU       fast
    OBDCommand("PIDS_B"                     , "Supported PIDs [21-40]"                  , b"0120", 6, pid,                   ECU.ENGINE, True),
    OBDCommand("DISTANCE_W_MIL"             , "Ujetá vzdálenost s MIL"           , b"0121", 4, uas(0x25),             ECU.ENGINE, True),
    OBDCommand("FUEL_RAIL_PRESSURE_VAC"     , "Tlak v palivové liště (ve vztahu k podtlaku)" , b"0122", 4, uas(0x19),             ECU.ENGINE, True),
    OBDCommand("FUEL_RAIL_PRESSURE_DIRECT"  , "Tlak v palivové liště (přímé vstřikování)"      , b"0123", 4, uas(0x1B),             ECU.ENGINE, True),
    OBDCommand("O2_S1_WR_VOLTAGE"           , "02 Senzor 1 WR Lambda napětí"           , b"0124", 6, sensor_voltage_big,    ECU.ENGINE, True),
    OBDCommand("O2_S2_WR_VOLTAGE"           , "02 Senzor 2 WR Lambda napětí"           , b"0125", 6, sensor_voltage_big,    ECU.ENGINE, True),
    OBDCommand("O2_S3_WR_VOLTAGE"           , "02 Senzor 3 WR Lambda napětí"           , b"0126", 6, sensor_voltage_big,    ECU.ENGINE, True),
    OBDCommand("O2_S4_WR_VOLTAGE"           , "02 Senzor 4 WR Lambda napětí"           , b"0127", 6, sensor_voltage_big,    ECU.ENGINE, True),
    OBDCommand("O2_S5_WR_VOLTAGE"           , "02 Senzor 5 WR Lambda napětí"           , b"0128", 6, sensor_voltage_big,    ECU.ENGINE, True),
    OBDCommand("O2_S6_WR_VOLTAGE"           , "02 Senzor 6 WR Lambda napětí"           , b"0129", 6, sensor_voltage_big,    ECU.ENGINE, True),
    OBDCommand("O2_S7_WR_VOLTAGE"           , "02 Senzor 7 WR Lambda napětí"           , b"012A", 6, sensor_voltage_big,    ECU.ENGINE, True),
    OBDCommand("O2_S8_WR_VOLTAGE"           , "02 Senzor 8 WR Lambda napětí"           , b"012B", 6, sensor_voltage_big,    ECU.ENGINE, True),
    OBDCommand("COMMANDED_EGR"              , "Příkaz EGR"                           , b"012C", 3, percent,               ECU.ENGINE, True),
    OBDCommand("EGR_ERROR"                  , "Chyba EGR"                               , b"012D", 3, percent_centered,      ECU.ENGINE, True),
    OBDCommand("EVAPORATIVE_PURGE"          , "Příkaz k odpařování"             , b"012E", 3, percent,               ECU.ENGINE, True),
    OBDCommand("FUEL_LEVEL"                 , "Vstupní hladina paliva"                        , b"012F", 3, percent,               ECU.ENGINE, True),
    OBDCommand("WARMUPS_SINCE_DTC_CLEAR"    , "Počet zahřátí od vymazání kódů"  , b"0130", 3, uas(0x01),             ECU.ENGINE, True),
    OBDCommand("DISTANCE_SINCE_DTC_CLEAR"   , "Ujetá vzdálenost od vymazání kódů"   , b"0131", 4, uas(0x25),             ECU.ENGINE, True),
    OBDCommand("EVAP_VAPOR_PRESSURE"        , "Tlak par odpařovacího systému"       , b"0132", 4, evap_pressure,         ECU.ENGINE, True),
    OBDCommand("BAROMETRIC_PRESSURE"        , "Barometrický tlak"                     , b"0133", 3, pressure,              ECU.ENGINE, True),
    OBDCommand("O2_S1_WR_CURRENT"           , "02 Senzor 1 WR Lambda Current"           , b"0134", 6, current_centered,      ECU.ENGINE, True),
    OBDCommand("O2_S2_WR_CURRENT"           , "02 Senzor 2 WR Lambda Current"           , b"0135", 6, current_centered,      ECU.ENGINE, True),
    OBDCommand("O2_S3_WR_CURRENT"           , "02 Senzor 3 WR Lambda Current"           , b"0136", 6, current_centered,      ECU.ENGINE, True),
    OBDCommand("O2_S4_WR_CURRENT"           , "02 Senzor 4 WR Lambda Current"           , b"0137", 6, current_centered,      ECU.ENGINE, True),
    OBDCommand("O2_S5_WR_CURRENT"           , "02 Senzor 5 WR Lambda Current"           , b"0138", 6, current_centered,      ECU.ENGINE, True),
    OBDCommand("O2_S6_WR_CURRENT"           , "02 Senzor 6 WR Lambda Current"           , b"0139", 6, current_centered,      ECU.ENGINE, True),
    OBDCommand("O2_S7_WR_CURRENT"           , "02 Senzor 7 WR Lambda Current"           , b"013A", 6, current_centered,      ECU.ENGINE, True),
    OBDCommand("O2_S8_WR_CURRENT"           , "02 Senzor 8 WR Lambda proud"           , b"013B", 6, current_centered,      ECU.ENGINE, True),
    OBDCommand("CATALYST_TEMP_B1S1"         , "Teplota katalyzátoru: Banka 1 - Senzor 1" , b"013C", 4, uas(0x16),             ECU.ENGINE, True),
    OBDCommand("CATALYST_TEMP_B2S1"         , "Teplota katalyzátoru: Banka 2 - Senzor 1" , b"013D", 4, uas(0x16),             ECU.ENGINE, True),
    OBDCommand("CATALYST_TEMP_B1S2"         , "Teplota katalyzátoru: Banka 1 - Senzor 2" , b"013E", 4, uas(0x16),             ECU.ENGINE, True),
    OBDCommand("CATALYST_TEMP_B2S2"         , "Teplota katalyzátoru: Banka 2 - Senzor 2" , b"013F", 4, uas(0x16),             ECU.ENGINE, True),

    #                      name                             description                    cmd  bytes       decoder           ECU       fast
    OBDCommand("PIDS_C"                     , "Supported PIDs [41-60]"                  , b"0140", 6, pid,                   ECU.ENGINE, True),
    OBDCommand("STATUS_DRIVE_CYCLE"         , "Stav monitoru v tomto cyklu pohonu"         , b"0141", 6, status,                ECU.ENGINE, True),
    OBDCommand("CONTROL_MODULE_VOLTAGE"     , "Napětí řídicího modulu"                  , b"0142", 4, uas(0x0B),             ECU.ENGINE, True),
    OBDCommand("ABSOLUTE_LOAD"              , "Absolutní hodnota zatížení"                     , b"0143", 4, absolute_load,         ECU.ENGINE, True),
    OBDCommand("COMMANDED_EQUIV_RATIO"      , "Příkazový ekvivalentní poměr"             , b"0144", 4, uas(0x1E),             ECU.ENGINE, True),
    OBDCommand("RELATIVE_THROTTLE_POS"      , "Relativní poloha škrticí klapky"              , b"0145", 3, percent,               ECU.ENGINE, True),
    OBDCommand("AMBIANT_AIR_TEMP"           , "Teplota okolního vzduchu"                 , b"0146", 3, temp,                  ECU.ENGINE, True),
    OBDCommand("THROTTLE_POS_B"             , "Absolutní poloha škrticí klapky B"            , b"0147", 3, percent,               ECU.ENGINE, True),
    OBDCommand("THROTTLE_POS_C"             , "Absolutní poloha škrticí klapky C"            , b"0148", 3, percent,               ECU.ENGINE, True),
    OBDCommand("ACCELERATOR_POS_D"          , "Poloha pedálu akcelerátoru D"            , b"0149", 3, percent,               ECU.ENGINE, True),
    OBDCommand("ACCELERATOR_POS_E"          , "Poloha pedálu akcelerátoru E"            , b"014A", 3, percent,               ECU.ENGINE, True),
    OBDCommand("ACCELERATOR_POS_F"          , "Poloha pedálu akcelerátoru F"            , b"014B", 3, percent,               ECU.ENGINE, True),
    OBDCommand("THROTTLE_ACTUATOR"          , "Ovladač škrticí klapky s příkazem"             , b"014C", 3, percent,               ECU.ENGINE, True),
    OBDCommand("RUN_TIME_MIL"               , "Čas běhu se zapnutým MIL"                    , b"014D", 4, uas(0x34),             ECU.ENGINE, True),
    OBDCommand("TIME_SINCE_DTC_CLEARED"     , "Doba od vymazání chybových kódů"        , b"014E", 4, uas(0x34),             ECU.ENGINE, True),
    OBDCommand("MAX_VALUES"                 , "Různé maximální hodnoty"                      , b"014F", 6, drop,                  ECU.ENGINE, True), # todo: decode this
    OBDCommand("MAX_MAF"                    , "Maximální hodnota pro snímač hmotnostního průtoku vzduchu"  , b"0150", 6, max_maf,               ECU.ENGINE, True),
    OBDCommand("FUEL_TYPE"                  , "Typ paliva"                               , b"0151", 3, fuel_type,             ECU.ENGINE, True),
    OBDCommand("ETHANOL_PERCENT"            , "Etanolové palivo Procento"                    , b"0152", 3, percent,               ECU.ENGINE, True),
    OBDCommand("EVAP_VAPOR_PRESSURE_ABS"    , "Absolutní odpařovací systém Tlak par"     , b"0153", 4, abs_evap_pressure,     ECU.ENGINE, True),
    OBDCommand("EVAP_VAPOR_PRESSURE_ALT"    , "Tlak par v odpařovacím systému"              , b"0154", 4, evap_pressure_alt,     ECU.ENGINE, True),
    OBDCommand("SHORT_O2_TRIM_B1"           , "Krátkodobý sekundární trim O2 - banka 1"   , b"0155", 4, percent_centered,      ECU.ENGINE, True), # todo: decode seconds value for banks 3 and 4
    OBDCommand("LONG_O2_TRIM_B1"            , "Dlouhodobý sekundární trim O2 - banka 1"    , b"0156", 4, percent_centered,      ECU.ENGINE, True),
    OBDCommand("SHORT_O2_TRIM_B2"           , "Krátkodobý sekundární trim O2 - banka 2"   , b"0157", 4, percent_centered,      ECU.ENGINE, True),
    OBDCommand("LONG_O2_TRIM_B2"            , "Dlouhodobý sekundární trim O2 - banka 2"    , b"0158", 4, percent_centered,      ECU.ENGINE, True),
    OBDCommand("FUEL_RAIL_PRESSURE_ABS"     , "Tlak v palivové liště (absolutní)"           , b"0159", 4, uas(0x1B),             ECU.ENGINE, True),
    OBDCommand("RELATIVE_ACCEL_POS"         , "Relativní poloha pedálu plynu"     , b"015A", 3, percent,               ECU.ENGINE, True),
    OBDCommand("HYBRID_BATTERY_REMAINING"   , "Zbývající životnost hybridního akumulátoru"      , b"015B", 3, percent,               ECU.ENGINE, True),
    OBDCommand("OIL_TEMP"                   , "Teplota motorového oleje"                  , b"015C", 3, temp,                  ECU.ENGINE, True),
    OBDCommand("FUEL_INJECT_TIMING"         , "Časování vstřikování paliva"                   , b"015D", 4, inject_timing,         ECU.ENGINE, True),
    OBDCommand("FUEL_RATE"                  , "Množství paliva v motoru"                        , b"015E", 4, fuel_rate,             ECU.ENGINE, True),
    OBDCommand("EMISSION_REQ"               , "Navržené emisní požadavky"          , b"015F", 3, drop,                  ECU.ENGINE, True),
]

# mode 2 is the same as mode 1, but returns values from when the DTC occured
__mode2__ = []
for c in __mode1__:
    c = c.clone()
    c.command = b"02" + c.command[2:]  # change the mode: 0100 ---> 0200
    c.name = "DTC_" + c.name
    c.desc = "DTC " + c.desc
    if c.decode == pid:
        c.decode = drop  # Never send mode 02 pid requests (use mode 01 instead)
    __mode2__.append(c)

__mode3__ = [
    OBDCommand("GET_DTC", "Získat DTC", b"03", 100, dtc, ECU.ALL, False),
]

__mode4__ = [
    OBDCommand("CLEAR_DTC", "Vymazání DTC a zmrazení dat", b"04", 0, drop, ECU.ALL, False),
]

__mode6__ = [
    # Mode 06 calls PID's MID's (Monitor ID)
    # This is for CAN only
    #                      name                             description                            cmd     bytes       decoder           ECU        fast
    OBDCommand("MIDS_A"                      , "Supported MIDs [01-20]"                         , b"0600",   0, pid,                   ECU.ALL,     False),
    OBDCommand("MONITOR_O2_B1S1"             , "Monitor snímače O2 Banka 1 - Snímač 1"            , b"0601",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_O2_B1S2"             , "Monitor snímače O2 Banka 1 - Snímač 2"            , b"0602",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_O2_B1S3"             , "Monitor snímače O2 Banka 1 - Snímač 3"            , b"0603",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_O2_B1S4"             , "Monitor snímače O2 Banka 1 - Snímač 4"            , b"0604",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_O2_B2S1"             , "Monitor snímače O2 Banka 2 - Snímač 1"            , b"0605",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_O2_B2S2"             , "Monitor snímače O2 Banka 2 - Snímač 2"            , b"0606",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_O2_B2S3"             , "Monitor snímače O2 Banka 2 - Snímač 3"            , b"0607",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_O2_B2S4"             , "Monitor snímače O2 Banka 2 - Snímač 4"            , b"0608",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_O2_B3S1"             , "Monitor snímače O2 Banka 3 - Snímač 1"            , b"0609",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_O2_B3S2"             , "Monitor snímače O2 Banka 3 - Snímač 2"            , b"060A",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_O2_B3S3"             , "Monitor snímače O2 Banka 3 - Snímač 3"            , b"060B",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_O2_B3S4"             , "Monitor snímače O2 Banka 3 - Snímač 4"            , b"060C",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_O2_B4S1"             , "Monitor snímače O2 Banka 4 - Snímač 1"            , b"060D",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_O2_B4S2"             , "Monitor snímače O2 Banka 4 - Snímač 2"            , b"060E",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_O2_B4S3"             , "Monitor snímače O2 Banka 4 - Snímač 3"            , b"060F",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_O2_B4S4"             , "Monitor snímače O2 Banka 4 - Snímač 4"            , b"0610",   0, monitor,               ECU.ALL,     False),
] + ([None] * 15) + [ # 11 - 1F Reserved
    OBDCommand("MIDS_B"                      , "Supported MIDs [21-40]"                         , b"0620",   0, pid,                   ECU.ALL,     False),
    OBDCommand("MONITOR_CATALYST_B1"         , "Catalyst Monitor Bank 1"                        , b"0621",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_CATALYST_B2"         , "Catalyst Monitor Bank 2"                        , b"0622",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_CATALYST_B3"         , "Catalyst Monitor Bank 3"                        , b"0623",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_CATALYST_B4"         , "Catalyst Monitor Bank 4"                        , b"0624",   0, monitor,               ECU.ALL,     False),
] + ([None] * 12) + [ # 25 - 30 Reserved
    OBDCommand("MONITOR_EGR_B1"              , "Monitor EGR Banka 1"                             , b"0631",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_EGR_B2"              , "Monitor EGR Banka 2"                             , b"0632",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_EGR_B3"              , "Monitor EGR Banka 3"                             , b"0633",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_EGR_B4"              , "Monitor EGR Banka 4"                             , b"0634",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_VVT_B1"              , "VVT Monitor Bank 1"                             , b"0635",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_VVT_B2"              , "VVT Monitor Bank 2"                             , b"0636",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_VVT_B3"              , "VVT Monitor Bank 3"                             , b"0637",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_VVT_B4"              , "VVT Monitor Bank 4"                             , b"0638",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_EVAP_150"            , "EVAP Monitor (Cap Off / 0.150\")"               , b"0639",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_EVAP_090"            , "EVAP Monitor (0.090\")"                         , b"063A",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_EVAP_040"            , "EVAP Monitor (0.040\")"                         , b"063B",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_EVAP_020"            , "EVAP Monitor (0.020\")"                         , b"063C",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_PURGE_FLOW"          , "Monitor průtoku proplachování"                             , b"063D",   0, monitor,               ECU.ALL,     False),
] + ([None] * 2) + [ # 3E - 3F Reserved
    OBDCommand("MIDS_C"                      , "Supported MIDs [41-60]"                         , b"0640",   0, pid,                   ECU.ALL,     False),
    OBDCommand("MONITOR_O2_HEATER_B1S1"      , "Monitor ohřevu snímače O2 Banka 1 - Snímač 1"     , b"0641",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_O2_HEATER_B1S2"      , "Monitor ohřevu snímače O2 Banka 1 - Snímač 2"     , b"0642",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_O2_HEATER_B1S3"      , "Monitor ohřevu snímače O2 Banka 1 - Snímač 3"     , b"0643",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_O2_HEATER_B1S4"      , "Monitor ohřevu snímače O2 Banka 1 - Snímač 4"     , b"0644",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_O2_HEATER_B2S1"      , "Monitor ohřevu snímače O2 Banka 2 - Snímač 1"     , b"0645",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_O2_HEATER_B2S2"      , "Monitor ohřevu snímače O2 Banka 2 - Snímač 2"     , b"0646",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_O2_HEATER_B2S3"      , "Monitor ohřevu snímače O2 Banka 2 - Snímač 3"     , b"0647",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_O2_HEATER_B2S4"      , "Monitor ohřevu snímače O2 Banka 2 - Snímač 4"     , b"0648",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_O2_HEATER_B3S1"      , "Monitor ohřevu snímače O2 Banka 3 - Snímač 1"     , b"0649",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_O2_HEATER_B3S2"      , "Monitor ohřevu snímače O2 Banka 3 - Snímač 2"     , b"064A",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_O2_HEATER_B3S3"      , "Monitor ohřevu snímače O2 Banka 3 - Snímač 3"     , b"064B",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_O2_HEATER_B3S4"      , "Monitor ohřevu snímače O2 Banka 3 - Snímač 4"     , b"064C",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_O2_HEATER_B4S1"      , "Monitor ohřevu snímače O2 Banka 4 - Snímač 1"     , b"064D",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_O2_HEATER_B4S2"      , "Monitor ohřevu snímače O2 Banka 4 - Snímač 2"     , b"064E",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_O2_HEATER_B4S3"      , "Monitor ohřevu snímače O2 Banka 4 - Snímač 3"     , b"064F",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_O2_HEATER_B4S4"      , "Monitor ohřevu snímače O2 Banka 4 - Snímač 4"     , b"0650",   0, monitor,               ECU.ALL,     False),
] + ([None] * 15) + [ # 51 - 5F Reserved
    OBDCommand("MIDS_D"                      , "Supported MIDs [61-80]"                         , b"0660",   0, pid,                   ECU.ALL,     False),
    OBDCommand("MONITOR_HEATED_CATALYST_B1"  , "Vyhřívaný monitor katalyzátoru Banka 1"                 , b"0661",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_HEATED_CATALYST_B2"  , "Vyhřívaný katalyzátor Monitor Bank 2"                 , b"0662",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_HEATED_CATALYST_B3"  , "Vyhřívaný katalyzátor Monitor Bank 3"                 , b"0663",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_HEATED_CATALYST_B4"  , "Vyhřívaný monitor katalyzátoru Banka 4"                 , b"0664",   0, monitor,               ECU.ALL,     False),
] + ([None] * 12) + [ # 65 - 70 Reserved
    OBDCommand("MONITOR_SECONDARY_AIR_1"     , "Sekundární monitor vzduchu 1"                        , b"0671",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_SECONDARY_AIR_2"     , "Sekundární monitor vzduchu 2"                        , b"0672",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_SECONDARY_AIR_3"     , "Sekundární monitor vzduchu 3"                        , b"0673",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_SECONDARY_AIR_4"     , "Sekundární monitor vzduchu 4"                        , b"0674",   0, monitor,               ECU.ALL,     False),
] + ([None] * 11) + [ # 75 - 7F Reserved
    OBDCommand("MIDS_E"                      , "Supported MIDs [81-A0]"                         , b"0680",   0, pid,                   ECU.ALL,     False),
    OBDCommand("MONITOR_FUEL_SYSTEM_B1"      , "Monitor palivového systému Banka 1"                     , b"0681",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_FUEL_SYSTEM_B2"      , "Monitor palivového systému Banka 2"                     , b"0682",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_FUEL_SYSTEM_B3"      , "Monitor palivového systému Banka 3"                     , b"0683",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_FUEL_SYSTEM_B4"      , "Monitor palivového systému Banka 4"                     , b"0684",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_BOOST_PRESSURE_B1"   , "Monitor regulace tlaku zvyšování tlaku Banka 1"          , b"0685",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_BOOST_PRESSURE_B2"   , "Monitor regulace tlaku zvyšování tlaku Banka 1"          , b"0686",   0, monitor,               ECU.ALL,     False),
] + ([None] * 9) + [ # 87 - 8F Reserved
    OBDCommand("MONITOR_NOX_ABSORBER_B1"     , "Monitor absorbéru NOx Banka 1"                    , b"0690",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_NOX_ABSORBER_B2"     , "Monitor absorbéru NOx Banka 2"                    , b"0691",   0, monitor,               ECU.ALL,     False),
] + ([None] * 6) + [ # 92 - 97 Reserved
    OBDCommand("MONITOR_NOX_CATALYST_B1"     , "Monitor katalyzátoru NOx Banka 1"                    , b"0698",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_NOX_CATALYST_B2"     , "Monitor katalyzátoru NOx Banka 2"                    , b"0699",   0, monitor,               ECU.ALL,     False),
] + ([None] * 6) + [ # 9A - 9F Reserved
    OBDCommand("MIDS_F"                      , "Supported MIDs [A1-C0]"                         , b"06A0",   0, pid,                   ECU.ALL,     False),
    OBDCommand("MONITOR_MISFIRE_GENERAL"     , "Misfire Monitor Obecné údaje"                   , b"06A1",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_MISFIRE_CYLINDER_1"  , "Údaje o chybném zážehu válce 1"                        , b"06A2",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_MISFIRE_CYLINDER_2"  , "Údaje o chybném zážehu válce 2"                        , b"06A3",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_MISFIRE_CYLINDER_3"  , "Údaje o chybném zážehu válce 3"                        , b"06A4",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_MISFIRE_CYLINDER_4"  , "Údaje o nesprávném zapálení válce 4"                        , b"06A5",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_MISFIRE_CYLINDER_5"  , "Údaje o chybném zážehu válce 5"                        , b"06A6",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_MISFIRE_CYLINDER_6"  , "Údaje o nesprávném zapálení válce 6"                        , b"06A7",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_MISFIRE_CYLINDER_7"  , "Údaje o chybném zážehu válce 7"                        , b"06A8",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_MISFIRE_CYLINDER_8"  , "Údaje o nesprávném zapálení válce 8"                        , b"06A9",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_MISFIRE_CYLINDER_9"  , "Údaje o chybném zážehu válce 9"                        , b"06AA",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_MISFIRE_CYLINDER_10" , "Údaje o chybném zážehu válce 10"                       , b"06AB",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_MISFIRE_CYLINDER_11" , "Údaje o nesprávném zážehu válce 11"                       , b"06AC",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_MISFIRE_CYLINDER_12" , "Údaje o chybném zážehu válce 12"                       , b"06AD",   0, monitor,               ECU.ALL,     False),
] + ([None] * 2) + [ # AE - AF Reserved
    OBDCommand("MONITOR_PM_FILTER_B1"        , "Monitor filtru PM Banka 1"                       , b"06B0",   0, monitor,               ECU.ALL,     False),
    OBDCommand("MONITOR_PM_FILTER_B2"        , "Monitor filtru PM Banka 2"                       , b"06B1",   0, monitor,               ECU.ALL,     False),
]

__mode7__ = [
    OBDCommand("GET_CURRENT_DTC", "Získání DTC z aktuálního/posledního jízdního cyklu", b"07", 0, dtc, ECU.ALL, False),
]


__mode9__ = [
    #                      name                             description                            cmd     bytes       decoder       ECU        fast
    OBDCommand("PIDS_9A"                    , "Supported PIDs [01-20]"                            , b"0900",  7, pid,                ECU.ALL,     True),
    OBDCommand("VIN_MESSAGE_COUNT"          , "Počet zpráv VIN"                                 , b"0901",  3, count,              ECU.ENGINE,  True),
    OBDCommand("VIN"                        , "Vehicle Identification Number"                     , b"0902", 22, encoded_string(17), ECU.ENGINE,  True),
    OBDCommand("CALIBRATION_ID_MESSAGE_COUNT","Počet kalibračních ID zpráv pro PID 04"           , b"0903",  3, count,              ECU.ALL,     True),
    OBDCommand("CALIBRATION_ID"             , "Calibration ID"                                    , b"0904", 18, encoded_string(16), ECU.ALL,     True),
    OBDCommand("CVN_MESSAGE_COUNT"          , "Počet zpráv CVN pro PID 06"                      , b"0905",  3, count,              ECU.ALL,     True),
    OBDCommand("CVN"                        , "Kalibrační ověřovací čísla"                  , b"0906", 10, cvn,                ECU.ALL,     True),

#
# NOTE: The following are untested
#
#    OBDCommand("PERF_TRACKING_MESSAGE_COUNT", "Performance tracking message count"                , b"0907",  3, count,              ECU.ALL,     True),
#    OBDCommand("PERF_TRACKING_SPARK"        , "In-use performance tracking (spark ignition)"      , b"0908",  4, raw_string,         ECU.ALL,     True),
#    OBDCommand("ECU_NAME_MESSAGE_COUNT"     , "ECU Name Message Count for PID 0A"                 , b"0909",  3, count,              ECU.ALL,     True),
#    OBDCommand("ECU_NAME"                   , "ECU Name"                                          , b"090a", 20, raw_string,         ECU.ALL,     True),
#    OBDCommand("PERF_TRACKING_COMPRESSION"  , "In-use performance tracking (compression ignition)", b"090b",  4, raw_string,         ECU.ALL,     True),
]

__misc__ = [
    OBDCommand("ELM_VERSION", "Řetězec verze ELM327", b"ATI", 0, raw_string, ECU.UNKNOWN, False),
    OBDCommand("ELM_VOLTAGE", "Napětí detekované adaptérem OBD-II", b"ATRV", 0, elm_voltage, ECU.UNKNOWN, False),
]

"""
Assemble the command tables by mode, and allow access by name
"""


class Commands():
    def __init__(self):

        # allow commands to be accessed by mode and PID
        self.modes = [
            [],
            __mode1__,
            __mode2__,
            __mode3__,
            __mode4__,
            [],
            __mode6__,
            __mode7__,
            [],
            __mode9__,
        ]

        # allow commands to be accessed by name
        for m in self.modes:
            for c in m:
                if c is not None:
                    self.__dict__[c.name] = c

        for c in __misc__:
            self.__dict__[c.name] = c

    def __getitem__(self, key):
        """
            commands can be accessed by name, or by mode/pid

            obd.commands.RPM
            obd.commands["RPM"]
            obd.commands[1][12] # mode 1, PID 12 (RPM)
        """

        try:
            basestring
        except NameError:
            basestring = str

        if isinstance(key, int):
            return self.modes[key]
        elif isinstance(key, basestring):
            return self.__dict__[key]
        else:
            logger.warning("OBD commands can only be retrieved by PID value or dict name")

    def __len__(self):
        """ returns the number of commands supported by python-OBD """
        return sum([len(mode) for mode in self.modes])

    def __contains__(self, name):
        """ calls has_name(s) """
        return self.has_name(name)

    def base_commands(self):
        """
            returns the list of commands that should always be
            supported by the ELM327
        """
        return [
            self.PIDS_A,
            self.PIDS_9A,
            self.MIDS_A,
            self.GET_DTC,
            self.CLEAR_DTC,
            self.GET_CURRENT_DTC,
            self.ELM_VERSION,
            self.ELM_VOLTAGE,
        ]

    def pid_getters(self):
        """ returns a list of PID GET commands """
        getters = []
        for mode in self.modes:
            getters += [cmd for cmd in mode if (cmd and cmd.decode == pid)]
        return getters

    def has_command(self, c):
        """ checks for existance of a command by OBDCommand object """
        return c in self.__dict__.values()

    def has_name(self, name):
        """ checks for existance of a command by name """
        # isupper() rejects all the normal properties
        return name.isupper() and name in self.__dict__

    def has_pid(self, mode, pid):
        """ checks for existance of a command by int mode and int pid """
        if (mode < 0) or (pid < 0):
            return False
        if mode >= len(self.modes):
            return False
        if pid >= len(self.modes[mode]):
            return False

        # make sure that the command isn't reserved
        return self.modes[mode][pid] is not None


# export this object
commands = Commands()
