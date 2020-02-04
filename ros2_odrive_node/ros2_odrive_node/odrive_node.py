
import rclpy

from sensor_msgs.msg import JointState
from lifecycle_msgs.msg import State
from lifecycle_msgs.msg import Transition

from ros2_lifecycle_py.lifecycle import LifecycleNode


import odrive
import odrive.enums

class OdriveAxisNode(LifecycleNode):
    def __init__(self,
        odrive_axis,
        encoder_cpr = 2400,
        node_name = "odrive",
        motorloop_frequency_Hz = 240,
        publishloop_frequency_Hz = 60):

        super().__init__(node_name)

        self.odaxis = odrive_axis


        self.motor_timer =- self.create_timer(1.0/motorloop_frequency_Hz, self.update)
        self.publish_timer =- self.create_timer(1.0/publishloop_frequency_Hz, self.update)

    
    def motor_update(self):
        dt_s = self.updatetimer.time_since_last_call()
    
    def on_configure(self):
        return Transition.TRANSITION_CALLBACK_SUCCESS
    
    def on_activate(self):
        return Transition.TRANSITION_CALLBACK_SUCCESS

    def on_deactivate(self):
        self.odaxis.requested_state = odrive.enums.AXIS_STATE_IDLE

        while(self.odaxis.current_state != odrive.enums.AXIS_STATE_IDLE):
            pass
        return Transition.TRANSITION_CALLBACK_SUCCESS



def main():
    print('Hi from ros2_odrive.')


if __name__ == '__main__':
    main()
