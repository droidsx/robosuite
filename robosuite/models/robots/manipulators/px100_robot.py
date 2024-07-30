import numpy as np

from robosuite.models.robots.manipulators.manipulator_model import ManipulatorModel
from robosuite.utils.mjcf_utils import xml_path_completion


# TODO: Note: you don't change the gripper on PX100, so we don't need to add a gripper to the robot
class UR5e(ManipulatorModel):
    """
    PX100 is a cheap and simple 4DOF robot arm by Trossen Robotics

    Args:
        idn (int or str): Number or some other unique identification string for this robot instance
    """

    def __init__(self, idn=0):
        super().__init__(xml_path_completion("robots/px100/robot.xml"), idn=idn)

    # TODO: 
    @property
    def default_mount(self):
        return "RethinkMount"

    # TODO: 
    @property
    def default_gripper(self):
        return "Robotiq85Gripper"
   
    # TODO: 
    @property
    def default_controller_config(self):
        return "default_ur5e"

    # TODO: 
    @property
    def init_qpos(self):
        return np.array([-0.470, -1.735, 2.480, -2.275, -1.590, -1.991])

    # TODO: 
    @property
    def base_xpos_offset(self):
        return {
            "bins": (-0.5, -0.1, 0),
            "empty": (-0.6, 0, 0),
            "table": lambda table_length: (-0.16 - table_length / 2, 0, 0),
        }

    # TODO: 
    @property
    def top_offset(self):
        return np.array((0, 0, 1.0))

    # TODO: 
    @property
    def _horizontal_radius(self):
        return 0.5

    # TODO: 
    @property
    def arm_type(self):
        return "single"
