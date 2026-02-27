# Medical Robotics Digital Twin: Simulation & Haptics

**Context:** Independent Research & Mercer X Lab Core Infrastructure  
**Status:** Architecture & Requirements Definition (Active Development)  
**Timeline:** Jan 2026 – May 2026  

## Project Overview
This repository contains the architecture and ROS2 packages for a high-fidelity digital twin focused on **surgical robotics**. Built using **NVIDIA Isaac Sim** and **ROS 2 Humble**, the primary objective is to create a safe, simulated testbed for medical teleoperation. This environment bridges the gap between theoretical kinematics and real-time hardware control, allowing for the rapid integration and testing of varied haptic feedback devices.

Because the system is designed with a highly modular hardware-agnostic architecture, the foundational hardware-integration phases (Phases 0–2) will be adopted as official educational robotics modules for the RPI Mercer XLab.

## Tech Stack
* **Simulation Environment:** NVIDIA Isaac Sim (Omniverse)
* **Middleware/Networking:** ROS 2 (Humble)
* **Languages:** Python, C++
* **Hardware Interfacing:** Standard Gamepad (XInput), Novint Falcon, 3D Systems Phantom Omni

## System Architecture & Development Roadmap
The development pipeline is structured to progressively scale from basic kinematic validation up to high-fidelity, 6-DOF force reflection.

### Phase 0: System Validation (Keyboard Teleoperation)
* **Objective:** Establish and verify the baseline network connection between the ROS 2 host and the Isaac Sim environment.
* **Mechanism:** Utilize standard `teleop_twist_keyboard` nodes to drive the digital twin's end-effector, ensuring the native inverse kinematics solvers (Lula) are functioning without hardware driver interference.

### Phase 1: Gamepad Integration (Xbox Controller)
* **Objective:** Introduce external USB hardware teleoperation.
* **Mechanism:** Map standard 2D joystick axes to the ROS 2 `/cmd_vel` topic utilizing the `joy` package. 
* **Implementation Note:** *The documentation and deployment of this phase currently serve as the highly scalable introductory robotics module for Mercer Lab students.*

### Phase 2: Low-Fidelity Haptics (Novint Falcon)
* **Objective:** Introduce 3-Degree-of-Freedom (DOF) spatial control.
* **Mechanism:** Resurrect legacy Novint Falcon drivers to interface with ROS 2, translating 3D Cartesian coordinates into spatial end-effector targets within the simulation.
* **Implementation Note:** *Serves as the advanced hardware module for the Mercer Lab curriculum.*

### Phase 3: High-Fidelity Surgical Simulation (Phantom Omni) 🌟
* **Objective:** Achieve 6-DOF teleoperation with active force reflection.
* **Mechanism:** Deploy the Phantom Omni within a simulated hospital room environment. This phase requires programming virtual fixtures (walls) and soft-body physics (veins/tissue) in Isaac Sim, actively calculating and feeding resistance data back to the user's hand via the Omni's haptic motors.
