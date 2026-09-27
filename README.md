# pon_gxh_tuzcsapfigyelo

Ez a kis beadandom ros2-ben. A lenyege h van ket node ami a tuzcsapok viznyomasat
 szimulálja és ellenorzi.

A szenzor_node.py random nyomas ertekeket general 2 es 5 bar kozott, ezt kuldi ki
 a /viznyomas topicba. A tipusa sensor_msgs/msg/FluidPressure.

A masik az ellenor_node.py, ez feliratkozik a topicra es figyeli hogy milyen
 adatok jonnek.
 Ha a nyomas lecsokken 3 bar ala akkor riaszt, amugy meg csak kiirja, hogy minden
 rendben van a halozattal.

Leforditani igy lehet a workspace gyokerebol:
colcon build --packages-select pon_gxh_tuzcsapfigyelo
aztan egy source install/setup.bash

Futtatni meg gkulon terminal ablakokban lehet oket ezekkel:
ros2 run pon_gxh_tuzcsapfigyelo szenzor
ros2 run pon_gxh_tuzcsapfigyelo ellenor
