from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='package',    # Replace with your package name
            executable='talker',            
            name='minimal_publisher',
            parameters=[
                {'v': 1.0},
                {'d': 0.0}
            ]
        ),
        Node(
            package='package',    # Replace with your package name
            executable='relay',             
            name='relay_node'
        ),
    ])
