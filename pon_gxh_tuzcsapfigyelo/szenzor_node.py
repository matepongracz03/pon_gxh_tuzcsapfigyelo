import rclpy
from rclpy.node import Node
from sensor_msgs.msg import FluidPressure
import random

class TuzcsapSzenzor(Node):
    def __init__(self):
        # A node neve, ahogy a ROS rendszer látja majd
        super().__init__('tuzcsap_szenzor_node')
        
        # Létrehozunk egy adót (publisher), ami 'viznyomas' néven fog sugározni
        self.kiado = self.create_publisher(FluidPressure, 'viznyomas', 10)
        
        # Egy időzítő, ami másodpercenként (1.0) lefuttatja az adat_kuldes függvényt
        self.idozito = self.create_timer(1.0, self.adat_kuldes)
        
        # Kezdő üzenet a terminálba
        self.get_logger().info('Tűzcsap szenzor elindult, mérések küldése...')

    def adat_kuldes(self):
        # Létrehozunk egy üres, gyári nyomás-üzenetet
        uzenet = FluidPressure()
        
        # Generálunk egy véletlenszerű számot 2.0 és 5.0 bar között (2 tizedesjegyig)
        mert_ertek = round(random.uniform(2.0, 5.0), 2)
        
        # Beletesszük a mért értékünket az üzenet gyári 'fluid_pressure' fiókjába
        uzenet.fluid_pressure = mert_ertek
        
        # Kilőjük az üzenetet a hálózatba
        self.kiado.publish(uzenet)
        
        # Kiírjuk a képernyőre is, hogy lássuk működés közben
        self.get_logger().info(f'Kiküldött nyomás: {mert_ertek} bar')

def main(args=None):
    rclpy.init(args=args)
    node = TuzcsapSzenzor()
    rclpy.spin(node) # Ez tartja életben a programot, amíg le nem állítjuk
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
