import usb.core
import usb.control
from idrw.beep import beep

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

def get_customer_id(input):
    return ' '.join([hex(x) for x in input[12:13]])

def get_tag_value(input):
    return ' '.join([hex(x) for x in input[13:17]])





dev = usb.core.find(idVendor=0xffff, idProduct=0x0035)
ret = read_tag(dev)
beep(dev)
print (ret)
print (array_to_hex_string(ret))

customer_id = get_customer_id(ret)
tag_value = get_tag_value(ret)

print('customer id={}'.format(customer_id))
print('tag value={}'.format(tag_value))