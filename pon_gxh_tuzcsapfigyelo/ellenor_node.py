import rclpy
from rclpy.node import Node
from sensor_msgs.msg import FluidPressure

class UzemeltetoiEllenor(Node):
    def __init__(self):
        super().__init__('ellenor_node')
        self.elofizeto = self.create_subscription(FluidPressure, 'viznyomas', self.nyomas_vizsgalat, 10)
        self.get_logger().info('Üzemeltetői ellenőrzés aktív, hálózat figyelése...')

    def nyomas_vizsgalat(self, uzenet):
        aktualis_nyomas = uzenet.fluid_pressure
        if aktualis_nyomas < 3.0:
            self.get_logger().warning(f'RIASZTÁS! Alacsony nyomás a tűzcsapon: {aktualis_nyomas} bar!')
        else:
            self.get_logger().info(f'Hálózat rendben. Stabil nyomás: {aktualis_nyomas} bar.')

def main(args=None):
    rclpy.init(args=args)
    node = UzemeltetoiEllenor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
