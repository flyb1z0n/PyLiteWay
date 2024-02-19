from pyliteway.migrator import PyLiteWay

def test_dummy():
    test_val = "ttt"
    pyLiteWay = PyLiteWay(test_val)
    assert pyLiteWay.getPath() == test_val
