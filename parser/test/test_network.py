from parser.network import validateIP


def testAdress():

    assert validateIP("192.168.1.2/32") == True
    assert validateIP("192.168.1.2/33") == False
    assert validateIP("256.0.0.0/32") == False
    assert validateIP("-1.0.0.0/32") == False
    assert validateIP("0.0.0.0/-1") == False
    assert validateIP("0.0.0.0") == False
    assert validateIP("0.0.0/32") == False
    assert validateIP("0.0.0.0.0/32") == False

    