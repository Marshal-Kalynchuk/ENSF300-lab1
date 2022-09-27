from main import *

def test_eval():
    print("Test 1 =", evaluate(['+', '/'],[1, 4, 2]))
    assert evaluate(['+', '/'],[1, 4, 2]) == 3, "Should be 3"
    print("Test 2 =", evaluate(['+', '/'],[1, 4, 2]))
    assert evaluate(['+', '-'],[7, 3, 2]) == 8, "Should be 8"
    print("Test 3 =", evaluate(['+', '/'],[1, 4, 2]))
    assert evaluate(['*', '/'],[2, 2, 2]) == 2, "Should be 2"
    print("Test 4 =", evaluate(['+', '/'],[1, 4, 2]))
    assert evaluate(['/', '-'],[6, 3, 1]) == 1, "Should be 1"
    print("Test 5 =", evaluate(['+', '/'],[1, 4, 2]))
    assert evaluate(['/', '*'],[1, 2, 1]) == 0, "Should be 0"

if __name__ == "__main__":
    test_eval()
    print("Everything passed")