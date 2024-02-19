from pyliteway.migrator import PyLiteWay


def dummy_test():
    test_val = "ttt"
    pyLiteWay = PyLiteWay(test_val)
    assert pyLiteWay.getPath() == test_val
