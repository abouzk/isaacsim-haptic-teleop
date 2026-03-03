# Medical Robotics Digital Twin: Simulation & Haptics

**Context:** Independent Research & Mercer XLab Core Infrastructure
**Status:** Architecture & Requirements Definition (Active Development)
**Timeline:** Jan 2026 – May 2026

## Project Overview
This repository contains the architecture and ROS 2 packages for a high-fidelity digital twin focused on surgical robotics. Built using NVIDIA Isaac Sim and ROS 2 Humble, the primary objective is to create a safe, simulated testbed for medical teleoperation. This environment bridges the gap between theoretical kinematics and real-time hardware control, allowing for the rapid integration and testing of varied haptic feedback devices.

Because the system is designed with a highly modular, hardware-agnostic architecture, the foundational hardware-integration phases (Phases 0–2) will be adopted as official educational robotics modules for the RPI Mercer XLab.

## Tech Stack
* **Simulation Environment:** NVIDIA Isaac Sim (Omniverse)
* **Middleware/Networking:** ROS 2 (Humble)
* **Languages:** Python, C++
* **Hardware Interfacing:** Standard Gamepad (XInput), Novint Falcon, 3D Systems Phantom Omni

## System Architecture & Development Roadmap
The development pipeline is structured to progressively scale from basic kinematic validation up to high-fidelity, 6-DOF force reflection and biological simulation.

### Phase 0: System Validation (Keyboard Teleoperation)
* **Objective:** Establish and verify the baseline network connection between the ROS 2 host and the Isaac Sim environment.
* **Mechanism:** Utilize standard `teleop_twist_keyboard` nodes to drive the digital twin's end-effector, ensuring the native inverse kinematics solvers (Lula) are functioning without hardware driver interference.

### Phase 1: Gamepad Integration (Xbox Controller)
* **Objective:** Introduce external USB hardware teleoperation.
* **Mechanism:** Map standard 2D joystick axes to the ROS 2 `/cmd_vel` topic utilizing the `joy` package.
* **Implementation Note:** The documentation and deployment of this phase currently serve as the highly scalable introductory robotics module for Mercer Lab students.

### Phase 2: Low-Fidelity Haptics & Rigid Contacts (Novint Falcon)
* **Objective:** Introduce 3-Degree-of-Freedom (DOF) spatial control and establish the baseline force-reflection loop.
* **Mechanism:** Resurrect legacy Novint Falcon drivers to interface with ROS 2, translating 3D Cartesian coordinates into spatial end-effector targets. Program virtual fixtures (rigid walls) within Isaac Sim to calculate collision forces and publish resistance data back to the Falcon's motors.
* **Implementation Note:** Serves as the advanced hardware module for the Mercer Lab curriculum.

### Phase 3: High-Fidelity Kinematics (Phantom Omni)
* **Objective:** Achieve 6-DOF teleoperation. 
* **Mechanism:** Upgrade the hardware interface to the Phantom Omni. Update the ROS 2 control nodes to process full spatial and rotational data (Pitch, Yaw, Roll) to drive the surgical end-effector with complete articulation.

### Phase 4: Soft-Body Physics & Biological Simulation
* **Objective:** Introduce active, variable force reflection mimicking human tissue.
* **Mechanism:** Transition from rigid virtual walls to soft-body physics (veins/tissue) in Isaac Sim. Actively calculate elastic and dynamic resistance data based on tissue deformation and feed it back to the user's hand via the Omni's haptic motors.

### Phase 5: Surgical Environment & Bioscanners
* **Objective:** Finalize the hospital room digital twin data architecture.
* **Mechanism:** Deploy independent ROS 2 nodes that simulate and publish patient telemetry (e.g., heart rate, tissue density alerts). Integrate these data streams into a centralized interface used during the teleoperated surgery simulation.
