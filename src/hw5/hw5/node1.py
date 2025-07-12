from std_msgs.msg import Float64MultiArray, Bool
import rclpy
from rclpy.node import Node
import random

class Node1(Node):
    def __init__(self):
        super().__init__('node1')
        self.publisher_ = self.create_publisher(Float64MultiArray, 'random_array', 10)
        self.subscription = self.create_subscription(Bool, 'flag', self.listener_callback, 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.flag = False

    def listener_callback(self, msg):
        self.flag = msg.data
        self.get_logger().info(f'[node1] flag received: {self.flag}')

    def timer_callback(self):
        msg = Float64MultiArray()
        msg.data = [random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)]
        self.publisher_.publish(msg)
        self.get_logger().info(f'[node1] Publishing: {msg.data}, flag={self.flag}')

def main(args=None):
    rclpy.init(args=args)
    node = Node1()
    rclpy.spin(node)
    rclpy.shutdown()
