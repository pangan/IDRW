
from idrw.beep import beep
import struct

import usb.control

from idrw.beep import beep


def array_to_hex_string(input):
    return ' '.join([hex(x) for x in input])

def write_tag(dev, cid, uid):
    BUFFER_SIZE = 256
    buff = [0x00] * BUFFER_SIZE

    # Setup payload for writing routine
    buff[0x00] = 0x01
    buff[0x06] = 0x08
    buff[0x08] = 0xaa
    buff[0x0a] = 0x03
    buff[0x0b] = 0x89
    buff[0x0c] = 0x05
    buff[0x0d] = 0x01
    buff[0x0e] = 0x8e
    buff[0x0f] = 0xbb

    # Write to Feature Report 1
    ret_value = dev.ctrl_transfer(0x21, 0x09, 0x0301, 0, buff)
    if ret_value != BUFFER_SIZE:
        raise ValueError('Communication Error.')

    # Read from Feature Report 2
    ret = dev.ctrl_transfer(0xa1, 0x01, 0x0302, 0, BUFFER_SIZE)
    print (array_to_hex_string(ret))

    buff = [0x00] * BUFFER_SIZE

    # python 2
    # id_data = [cid] + [ord(x) for x in list(struct.pack('>I', uid))]
    # python 3
    id_data = [cid] + list(struct.pack('>I', uid))
    print ('id data: ' + array_to_hex_string(id_data))

    # Payload containing uid and customer_id
    buff[0x00] = 0x01
    buff[0x06] = 0x1f
    buff[0x08] = 0xaa
    buff[0x0a] = 0x1a
    buff[0x0b] = 0x21
    buff[0x0d] = 0x01
    buff[0x0e] = 0x01
    buff[0x0f] = 0x02
    buff[0x10] = id_data[0]
    buff[0x11] = id_data[1]
    buff[0x12] = id_data[2]
    buff[0x13] = id_data[3]
    buff[0x14] = id_data[4]
    buff[0x15] = 0x80
    buff[0x25] = 0xfb
    buff[0x26] = 0xbb

    dev.ctrl_transfer(0x21, 0x09, 0x0301, 0, buff)

    # Read from Feature Report 2
    ret = dev.ctrl_transfer(0xa1, 0x01, 0x0302, 0, BUFFER_SIZE)
    print (array_to_hex_string(ret))

    return ret

dev = usb.core.find(idVendor=0xffff, idProduct=0x0035)

ret = write_tag(dev, 1, 129346688)
beep(dev)
print (array_to_hex_string(ret))