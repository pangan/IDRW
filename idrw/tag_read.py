
import usb.control
from idrw.beep import beep
from idrw.utils import int_list_to_hex

from time import sleep

def read_tag(dev):
    BUFFER_SIZE = 256
    buff = [0x00] * BUFFER_SIZE

    # Set up payload for reading routing
    buff[0x00] = 0x01
    buff[0x06] = 0x08
    buff[0x08] = 0xaa
    buff[0x0a] = 0x03
    buff[0x0b] = 0x25
    buff[0x0e] = 0x26
    buff[0x0f] = 0xbb

    # Write to Feature Report 1
    ret = dev.ctrl_transfer(0x21, 0x09, 0x0301, 0, buff)
    if ret != BUFFER_SIZE:
    	raise ValueError('Communication Error.')

    # Read from Feature Report 2
    return dev.ctrl_transfer(0xa1, 0x01, 0x0302, 0, BUFFER_SIZE)





def array_to_hex_string(input):
    return ' '.join([hex(x) for x in input])

def get_customer_id_hex(input):
    return ' '.join([hex(x) for x in input[12:13]])

def get_tag_value_hex(input):
    return ' '.join([hex(x) for x in input[13:17]])

def get_customer_id_int(input):
    return input[12:13]

def get_tag_value_int(input):
    return input[13:17]

dev = usb.core.find(idVendor=0xffff, idProduct=0x0035)

try:
    while True:

        ret = read_tag(dev)
        sleep(0.5)
        if len(ret)>=18:
            beep(dev)

            customer_id = get_customer_id_int(ret)
            tag_value = get_tag_value_int(ret)
            print('----')
            print('customer id = {}'.format(int_list_to_hex(customer_id)))
            print('tag value = {}'.format(int_list_to_hex(tag_value)))

except KeyboardInterrupt as ex:
    exit(0)
