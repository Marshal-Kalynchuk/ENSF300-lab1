from main import *

def test_eval():
    assert evaluate(['+', '/'],[1, 4, 2]) == 3, "Should be 3"
    assert evaluate(['+-', '-'],[7, 3, 2]) == 2, "Should be 2"
    assert evaluate(['*', '/'],[2, 2, 2]) == 2, "Should be 2"
    assert evaluate(['/', '-'],[6, 3, 1]) == 1, "Should be 1"
    assert evaluate(['/', '*'],[1, 2, 1]) == -0.5, "Should be -0.5"

if __name__ == "__main__":
    test_eval()
    print("Everything passed")