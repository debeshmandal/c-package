from ctest import engine

def test_engine():
    assert engine.addNumbers(1, 2) == 3
    print(engine.vectorNorm(1., 2., 3.))
    return

if __name__ == '__main__':
    test_engine()