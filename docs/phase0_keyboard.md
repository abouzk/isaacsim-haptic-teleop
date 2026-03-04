# Phase 0: Keyboard Teleoperation

## Objective
This phase validates the ROS 2 network architecture and the base kinematic solver using a standard keyboard interface. It establishes the foundational `/cmd_vel` communication bridge before introducing complex external hardware.

---

## 1. Prerequisites
Ensure your target simulation environment is actively running and configured to listen to the standard velocity topic.

**For Production (Isaac Sim):**
1. Open your Isaac Sim environment.
2. Ensure the OmniGraph contains a `ROS 2 Subscribe Twist` node actively listening to the `/cmd_vel` topic.

**For Local Testing (Turtlesim):**
If you are validating the network locally without Isaac Sim, open a new terminal and run Turtlesim with the remapped topic:
```bash
ros2 run turtlesim turtlesim_node --ros-args --remap /turtle1/cmd_vel:=/cmd_vel
```

---

## 2. Launch the Control Node
Open a fresh terminal, navigate to the root of your workspace, source the installation files, and execute the Phase 0 launch file.

```bash
# 1. Navigate to the workspace
cd ~/isaacsim-surgical-teleop

# 2. Source the ROS 2 overlay
source install/setup.bash

# 3. Launch the keyboard node
ros2 launch haptic_teleop_core phase0_keyboard.launch.py
```

---

## 3. Execution & Controls
Once the launch file executes, a dedicated terminal window will open automatically. **You must click inside this new window for your keystrokes to register.**

Use the following keys to publish `geometry_msgs/Twist` messages to the digital twin:

* **Drive Linear/Angular:** Arrow Keys (or `I`, `J`, `L`, `,`)
* **Force Stop (E-Stop):** `K` (Instantly zeroes out all velocities)
* **Increase/Decrease Max Global Speed:** `Q` / `Z`
* **Increase/Decrease Linear Speed Only:** `W` / `X`
* **Increase/Decrease Angular Speed Only:** `E` / `C`

**Safe Shutdown:** To terminate the node, return to your primary terminal window and press `Ctrl+C` to gracefully kill the ROS 2 process.