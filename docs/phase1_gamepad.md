# Phase 1: Gamepad Teleoperation

## Objective
This phase maps a physical USB gamepad (e.g., standard PC/console controller) to the `geometry_msgs/Twist` message format. It introduces hardware-in-the-loop control, parameter configuration via `.yaml`, and a mandatory safety deadman switch.



---

## 1. Hardware Pre-Flight Check
Before running any ROS 2 nodes, you must verify that your Linux environment successfully recognizes the physical USB controller.

1. Plug your gamepad into your computer.
2. **If using a Virtual Machine:** Ensure you have explicitly enabled USB passthrough for the controller in your VM software's top menu.
3. Open a terminal and run the hardware list command:
   ```bash
   ls /dev/input/js*
   ```
   * **Expected Output:** `/dev/input/js0` (or `js1`, `js2`, etc.)
   * **Error:** If it returns `No such file or directory`, your OS does not see the hardware. Stop here and fix your VM USB settings.

---

## 2. Prerequisites
Ensure your target simulation environment is listening to `/cmd_vel`. 
*(For local testing without Isaac Sim, run `ros2 run turtlesim turtlesim_node --ros-args --remap /turtle1/cmd_vel:=/cmd_vel`)*

---

## 3. Launch the Control Node
Open a new terminal, navigate to the workspace, source the installation, and launch the gamepad architecture:

```bash
# Navigate to the workspace
cd ~/isaacsim-surgical-teleop

# Source the ROS 2 overlay
source install/setup.bash

# Launch the gamepad node
ros2 launch haptic_teleop_core phase1_gamepad.launch.py
```
---

## 4. Customizing Controller Mappings
The default configuration (`gamepad_config.yaml`) is mapped for a standard Xbox controller. If you are using a different gamepad (like a PlayStation dual-shock), the physical buttons may map to different array indices in Linux.

To find your specific button mappings:
1. Open a new terminal and run: `ros2 topic echo /joy`
2. Press the button you want to use as your Deadman Switch (e.g., Left Bumper). 
3. Watch the `buttons: []` array on your screen. Count the position of the number that flips from `0` to `1` (remembering that the first number is index `0`).
4. Open `src/haptic_teleop_core/config/gamepad_config.yaml` and change the `enable_button` value to your new index. 
5. Rebuild the workspace (`colcon build`) to apply the changes.
---

## 5. Execution & Controls
The node translates specific joystick axes into velocities, governed by a safety switch. 

* **Safety Deadman Switch:** You **MUST** press and hold the **Left Bumper (LB)** for any commands to register. If released, the robot will immediately halt.
* **Translation (Forward/Reverse):** Left Joystick (Up/Down) controls linear X velocity.
* **Rotation (Yaw):** Left Joystick (Left/Right) controls angular Z velocity.

---

## 6. Hardware Troubleshooting Pipeline
If the node launches successfully but the robot does not move, isolate the failure point by opening a new terminal and running these diagnostics in order:

1. **Check Raw USB Data:** `ros2 topic echo /joy`
   * Move the joysticks. If arrays of numbers print to the screen, ROS 2 is successfully reading the hardware. If blank, check your USB connection.
2. **Check the Deadman Switch:** Keep `/joy` running and press the Left Bumper. Look at the `buttons:` array and verify that the 5th number in the list (index 4) flips from `0` to `1`.
3. **Check the Translation Layer:** `ros2 topic echo /cmd_vel`
   * Hold the Left Bumper and move the joystick. If you see velocity math happening here but the robot still isn't moving, the issue is in your simulation environment, not your controller.