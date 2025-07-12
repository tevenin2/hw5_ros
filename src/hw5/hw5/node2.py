from std_msgs.msg import Float64MultiArray
from geometry_msgs.msg import Twist
import rclpy
from rclpy.node import Node

class Node2(Node):
    def __init__(self):
        super().__init__('node2')
        self.subscription = self.create_subscription(Float64MultiArray, 'random_array', self.listener_callback, 10)
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)

    def listener_callback(self, msg):
        twist = Twist()
        twist.linear.x = msg.data[0]
        twist.angular.z = msg.data[1]
        self.publisher_.publish(twist)
        self.get_logger().info(f'[node2] Publishing Twist: linear.x={twist.linear.x}, angular.z={twist.angular.z}')

def main(args=None):
    rclpy.init(args=args)
    node = Node2()
    rclpy.spin(node)
    rclpy.shutdown()
