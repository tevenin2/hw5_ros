from geometry_msgs.msg import Twist
from std_msgs.msg import Bool
import rclpy
from rclpy.node import Node

class Node3(Node):
    def __init__(self):
        super().__init__('node3')
        self.subscription = self.create_subscription(Twist, 'cmd_vel', self.listener_callback, 10)
        self.publisher_ = self.create_publisher(Bool, 'flag', 10)

    def listener_callback(self, msg):
        flag_msg = Bool()
        flag_msg.data = msg.linear.x != 0.0
        self.publisher_.publish(flag_msg)
        self.get_logger().info(f'[node3] Received linear.x={msg.linear.x} → flag: {flag_msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = Node3()
    rclpy.spin(node)
    rclpy.shutdown()
