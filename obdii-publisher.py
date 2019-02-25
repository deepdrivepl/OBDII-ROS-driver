import obd
import time
import rospy
from std_msgs.msg import Float64


rospy.init_node('OBDII-ROS-driver', anonymous=True)

pubrpm = rospy.Publisher('rpm', Float64, queue_size=10)
pubspeed = rospy.Publisher('speed', Float64, queue_size=10)
pubthrottle = rospy.Publisher('throttle', Float64, queue_size=10)
pubrelthrot = rospy.Publisher('rel_throttle', Float64, queue_size=10)
pubaccd = rospy.Publisher('acc_pedal_d', Float64, queue_size=10)
pubacce = rospy.Publisher('acc_pedal_e', Float64, queue_size=10)
pubthrotact = rospy.Publisher('throttle_act', Float64, queue_size=10)
pubengine = rospy.Publisher('engine_load', Float64, queue_size=10)
pubpressure = rospy.Publisher('pressure', Float64, queue_size=10)
pubfuel = rospy.Publisher('fuel', Float64, queue_size=10)


def new_rpm(v):
    value = float(str(v).split(':')[-1].split(' ')[0])
    pubrpm.publish(value)
def new_speed(v):
    value = float(str(v).split(':')[-1].split(' ')[0])
    pubspeed.publish(value)
def new_relthrot(v):
    value = float(str(v).split(':')[-1].split(' ')[0])
    pubrelthrot.publish(value)
def new_throt(v):
    value = float(str(v).split(':')[-1].split(' ')[0])
    pubthrottle.publish(value)
def new_accd(v):
    value = float(str(v).split(':')[-1].split(' ')[0])
    pubaccd.publish(value)
def new_acce(v):
    value = float(str(v).split(':')[-1].split(' ')[0])
    pubacce.publish(value)
def new_throtact(v):
    value = float(str(v).split(':')[-1].split(' ')[0])
    pubthrotact.publish(value)
def new_engine(v):
    value = float(str(v).split(':')[-1].split(' ')[0])
    pubengine.publish(value)
def new_pressure(v):
    value = float(str(v).split(':')[-1].split(' ')[0])
    pubpressure.publish(value)
def new_fuel(v):
    value = float(str(v).split(':')[-1].split(' ')[0])
    pubfuel.publish(value)


if __name__ == '__main__':
    try:
        port = "/dev/ttyUSB0"

        connection = obd.Async(portstr=port)

        connection.watch(obd.commands.RPM, callback=new_rpm)
        connection.watch(obd.commands.SPEED, callback=new_speed)
        connection.watch(obd.commands.THROTTLE_POS, callback=new_throt)
        connection.watch(obd.commands.RELATIVE_THROTTLE_POS, callback=new_relthrot)
        connection.watch(obd.commands.ACCELERATOR_POS_D, callback=new_accd)
        connection.watch(obd.commands.ACCELERATOR_POS_E, callback=new_acce)
        connection.watch(obd.commands.THROTTLE_ACTUATOR, callback=new_throtact)
        connection.watch(obd.commands.ENGINE_LOAD, callback=new_engine)
        connection.watch(obd.commands.BAROMETRIC_PRESSURE, callback=new_pressure)
        connection.watch(obd.commands.FUEL_STATUS, callback=new_fuel)

        connection.start()

        rospy.spin()

        connection.stop()
    except rospy.ROSInterruptException:
        pass
