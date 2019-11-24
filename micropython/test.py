
from atm90e32_u import ATM90e32
from app_error import NoMonitor, SysStatusError, NoMonitorNameError, NoWiFiError, NoDBidError, blink
import machine
import time


class MyTest:
    def __init__(self):
        self.led_red = machine.Pin(27, machine.Pin.OUT)
        self.led_green = machine.Pin(32, machine.Pin.OUT)
        # ***** atm90e32 CALIBRATION SETTINGS *****/

        lineFreq = 4485  # 4485 for 60 Hz (North America)
        # 389 for 50 hz (rest of the world)
        PGAGain = 21     # 21 for 100A (2x), 42 for >100A (4x)

        # VoltageGain = 42080  # 42080 - 9v AC transformer.
        VoltageGain = 37898  # What I calculated based on reading app notes on calibration
        # 32428 - 12v AC Transformer

        CurrentGainCT1 = 25368  # My calculation
        CurrentGainCT2 = 25368  # My calculation
        # CurrentGainCT1 = 25498  # 38695 - SCT-016 120A/40mA
        # CurrentGainCT2 = 25498  # 25498 - SCT-013-000 100A/50mA
        # 46539 - Magnalab 100A w/ built in burden resistor
        # *******************************************/
        try:
            # Get reading and then send reading.
            # Initializing the atm90e32 could throw an AppError if the energy monitor
            # is not communicating with the microcontroller.
            self.energy_sensor = ATM90e32(lineFreq, PGAGain,
                                          VoltageGain, CurrentGainCT1, 0, CurrentGainCT2)
            time.sleep(.5)
            # Maybe we don't have to initialize a second time...I found working with a
            # different atm90 that initializing twice was more robust than once.
            self.energy_sensor = ATM90e32(lineFreq, PGAGain,
                                          VoltageGain, CurrentGainCT1, 0, CurrentGainCT2)

            # We have an instance of the atm90e32.  Let's check if we get sensible readings
            sys0 = self.energy_sensor.sys_status0
            if (sys0 == 0xFFFF or sys0 == 0):
                raise OSError(SysStatusError().number,
                              SysStatusError().explanation)
        except OSError as e:
            blink(self.led_red, 4)
            print(e)
            print(e.args)
        else:
            blink(self.led_green, 2)

    def get_power(self):
        # Look at active power
        print(f'Total active power: {self.energy_sensor.total_active_power}')
        print(f'Active power on line A: {self.energy_sensor.active_power_A}')
        print(f'Active power on line C: {self.energy_sensor.active_power_C}')
        # Are the two readings close?
        print(
            f'Active Power A+C {self.energy_sensor.active_power_A+self.energy_sensor.active_power_C}')
        # Look at reactive power
        print(
            f'Total reactive power: {self.energy_sensor.total_reactive_power}')
        print(
            f'Reactive power on line A: {self.energy_sensor.reactive_power_A}')
        print(
            f'Reactive power on line C: {self.energy_sensor.reactive_power_C}')
        # Are the two readings close?
        print(
            f'Reactive Power A+C {self.energy_sensor.reactive_power_A+self.energy_sensor.reactive_power_C}')
