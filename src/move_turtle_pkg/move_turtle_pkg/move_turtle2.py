import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist #다른 string과는 다름
from rclpy.qos import QoSProfile #qos 네임을 사용자가 지정할수 있도록 선언
import random
import math

class Move_turtle(Node):
  def __init__(self):
    super().__init__('move_turtle') #message_publisher에 노드명 정의
    self.qos_profile = QoSProfile(depth = 10) #qos 네임을 사용자가 지정

    self.move_turtle = self.create_publisher(Twist,"turtle1/cmd_vel",self.qos_profile) #create_publisher를 이용
    self.move_turtle2 = self.create_publisher(Twist,"turtle2/cmd_vel",self.qos_profile) #create_publisher를 이용
    self.move_turtle3 = self.create_publisher(Twist,"turtle3/cmd_vel",self.qos_profile) #create_publisher를 이용

    self.timer = self.create_timer(0.1,self.m_turtle)
    self.timer = self.create_timer(0.1,self.m_turtle2)
    self.timer = self.create_timer(0.1,self.m_turtle3)
    self.velocity = 0.0
    self.theata = 0.0

  def m_turtle(self):
    msg = Twist()

    msg.linear.x = 5.0
    msg.linear.y = 0.0
    msg.linear.z = 0.0

    msg.angular.x = 0.0
    msg.angular.y = 0.0
    msg.angular.z = self.velocity

    self.move_turtle.publish(msg)
    self.velocity += 0.08

    if self.velocity > 2.0:
      self.velocity = 0.0

  def m_turtle2(self):
      msg = Twist()

      msg.linear.x = 5.0
      msg.linear.y = 0.0
      msg.linear.z = 0.0

      msg.angular.x = 0.0
      msg.angular.y = 0.0
      msg.angular.z = self.velocity*5

      self.move_turtle2.publish(msg)
      self.velocity -= 0.08

      if self.velocity > 2.0:
        self.velocity = 0.0

  def m_turtle3(self):
      msg = Twist()

      msg.linear.x = 5.0 * math.sin(self.theata)
      msg.linear.y = 0.0
      msg.linear.z = 0.0

      msg.angular.x = 0.0
      msg.angular.y = 0.0
      msg.angular.z = self.velocity*5

      self.move_turtle3.publish(msg)
      self.velocity += 0.08
      self.theata += 0.1

      if self.velocity > 2.0:
        self.velocity = 0.0


def main(args = None): #메인은 거의 변하지 않는다... 거의 이대로 고정
  rclpy.init(args = args)
  node = Move_turtle()
  try:
    rclpy.spin(node)
  except KeyboardInterrupt: # 종료할때 대부분 사용
    node.get_logger().info("Keyboard interrupt")
  node.destroy_node()
  rclpy.shutdown()


if __name__ == "__main": #main 상태에서만 실행
  main()


