import rclpy
from rclpy.node import Node
from sensor_msgs.msg import FluidPressure
import random

class TuzcsapSzenzor(Node):
    def __init__(self):
        super().__init__('tuzcsap_szenzor_node')
        self.kiado = self.create_publisher(FluidPressure, 'viznyomas', 10)
        self.idozito = self.create_timer(1.0, self.adat_kuldes)
        self.get_logger().info('Tűzcsap szenzor elindult, mérések küldése...')

    def adat_kuldes(self):
        uzenet = FluidPressure()
        mert_ertek = round(random.uniform(2.0, 5.0), 2)
        uzenet.fluid_pressure = mert_ertek
        self.kiado.publish(uzenet)
        self.get_logger().info(f'Kiküldött nyomás: {mert_ertek} bar')

def main(args=None):
    rclpy.init(args=args)
    node = TuzcsapSzenzor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
