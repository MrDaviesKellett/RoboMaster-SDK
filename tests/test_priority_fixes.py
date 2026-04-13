import sys
import types
import unittest

if sys.version_info < (3, 14):
    raise unittest.SkipTest("Priority regression tests require Python 3.14+")

from multi_robomaster import multi_group
from multi_robomaster import multi_robot
from robomaster import camera
from robomaster import client
from robomaster import flight
from robomaster import gripper
from robomaster import robotic_arm


class PriorityFixTests(unittest.TestCase):

    def test_camera_base_methods_are_explicit(self):
        base_camera = object.__new__(camera.Camera)
        with self.assertRaises(NotImplementedError):
            camera.Camera.start_video_stream(base_camera)
        with self.assertRaises(NotImplementedError):
            camera.Camera.stop_video_stream(base_camera)

    def test_tello_camera_stop_uses_public_stop_video_stream(self):
        tello_camera = object.__new__(camera.TelloCamera)
        calls = []
        tello_camera._video_enable = True
        tello_camera.stop_video_stream = lambda: calls.append("stop_video_stream")
        tello_camera._liveview = types.SimpleNamespace(stop=lambda: calls.append("liveview_stop"))

        camera.TelloCamera.stop(tello_camera)

        self.assertEqual(calls, ["stop_video_stream", "liveview_stop"])

    def test_client_remote_addr_raises_runtime_error(self):
        text_client = object.__new__(client.Client)
        text_client._conn = None

        with self.assertRaises(RuntimeError):
            _ = text_client.remote_addr

    def test_rmgroup_play_sound_reports_success(self):
        robot_a = types.SimpleNamespace(play_sound=lambda sound_id, times: True)
        robot_b = types.SimpleNamespace(play_sound=lambda sound_id, times: True)
        group = multi_group.RMGroup([1, 2], {1: robot_a, 2: robot_b})

        self.assertTrue(group.play_sound(1))

    def test_rmgroup_play_sound_reports_partial_failure(self):
        robot_a = types.SimpleNamespace(play_sound=lambda sound_id, times: True)
        robot_b = types.SimpleNamespace(play_sound=lambda sound_id, times: False)
        group = multi_group.RMGroup([1, 2], {1: robot_a, 2: robot_b})

        self.assertFalse(group.play_sound(1))

    def test_group_and_multi_robot_base_hooks_are_explicit(self):
        robot_group = object.__new__(multi_group.RobotGroupBase)
        with self.assertRaises(NotImplementedError):
            multi_group.RobotGroupBase._scan_group_module(robot_group)

        multi_robot_base = multi_robot.MultiRobotBase()
        with self.assertRaises(NotImplementedError):
            multi_robot_base._scan_multi_robot()
        with self.assertRaises(NotImplementedError):
            multi_robot_base.build_group([])

    def test_multi_drone_host_mapping_uses_scalar_robot_ids(self):
        drones = multi_robot.MultiDrone()
        drones._robot_sn_dict = {
            "sn-a": ("192.168.10.2", 8889),
            "sn-b": ("192.168.10.3", 8889),
        }
        drones._get_sn = lambda timeout=0: drones._robot_sn_dict

        drones.number_id_to_all_drone()

        self.assertEqual(drones._robot_host_dict[("192.168.10.2", 8889)], 0)
        self.assertEqual(drones._robot_host_dict[("192.168.10.3", 8889)], 1)

    def test_flight_validates_direction_distance_and_speed(self):
        dispatcher = types.SimpleNamespace(sent_actions=[])
        dispatcher.send_action = dispatcher.sent_actions.append
        drone = types.SimpleNamespace(client=None, action_dispatcher=dispatcher)
        drone_flight = flight.Flight(drone)

        with self.assertRaises(ValueError):
            drone_flight.fly("diagonal", 20)
        with self.assertRaises(ValueError):
            drone_flight.fly(flight.FORWARD, 10)
        with self.assertRaises(ValueError):
            drone_flight.set_speed(9)
        with self.assertRaises(ValueError):
            drone_flight.rotate(361)

        action = drone_flight.fly(flight.FORWARD, 20, retry=False)
        self.assertIs(action, dispatcher.sent_actions[0])

    def test_gripper_and_robotic_arm_reset_delegate_to_safe_defaults(self):
        grip = object.__new__(gripper.Gripper)
        grip.pause = lambda: "paused"
        arm = object.__new__(robotic_arm.RoboticArm)
        arm.recenter = lambda: "recentered"

        self.assertEqual(gripper.Gripper.reset(grip), "paused")
        self.assertEqual(robotic_arm.RoboticArm.reset(arm), "recentered")


if __name__ == "__main__":
    unittest.main()
