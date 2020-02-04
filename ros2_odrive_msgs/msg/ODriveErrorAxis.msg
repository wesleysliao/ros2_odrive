uint32 ERROR_NONE = 0
uint32 ERROR_INVALID_STATE = 1 #<! an invalid state was requested
uint32 ERROR_DC_BUS_UNDER_VOLTAGE = 2
uint32 ERROR_DC_BUS_OVER_VOLTAGE = 4
uint32 ERROR_CURRENT_MEASUREMENT_TIMEOUT = 8
uint32 ERROR_BRAKE_RESISTOR_DISARMED = 16  #<! the brake resistor was unexpectedly disarmed
uint32 ERROR_MOTOR_DISARMED = 32 #<! the motor was unexpectedly disarmed
uint32 ERROR_MOTOR_FAILED = 64 # Go to motor.hpp for information, check odrvX.axisX.motor.error for error value 
uint32 ERROR_SENSORLESS_ESTIMATOR_FAILED = 128
uint32 ERROR_ENCODER_FAILED = 256 # Go to encoder.hpp for information, check odrvX.axisX.encoder.error for error value
uint32 ERROR_CONTROLLER_FAILED = 512 
uint32 ERROR_POS_CTRL_DURING_SENSORLESS = 1024
uint32 ERROR_WATCHDOG_TIMER_EXPIRED = 2048 

uint32 error
string label
