from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    
    # 1. Start the raw USB joystick reader
    joy_node = Node(
        package='joy',
        executable='joy_node',
        name='joy_node',
        parameters=[{'deadzone': 0.1}] 
    )

    # 2. Start the translator node with direct Python parameters
    teleop_node = Node(
        package='teleop_twist_joy',
        executable='teleop_node',
        name='teleop_twist_joy_node',
        # THIS DICTIONARY REPLACES THE YAML FILE COMPLETELY:
        parameters=[{
            'require_enable_button': True,
            'enable_button': 4,       # Left Bumper
            'axis_linear': {'x': 1},  # Left Stick Up/Down
            'scale_linear': {'x': 3.0},
            'axis_angular': {'yaw': 0}, # Left Stick Left/Right
            'scale_angular': {'yaw': 5.0}
        }],
        remappings=[('/cmd_vel', '/cmd_vel')] 
    )

    return LaunchDescription([
        joy_node,
        teleop_node
    ])