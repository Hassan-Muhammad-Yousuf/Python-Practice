def case1():
    print("\n--- Case 1: No Exception ---")
    try:
        print("a")
        print("b")
        print("c")
        try:
            print("d")
            print("e")
            print("f")
        except ZeroDivisionError:
            print("g")
        finally:
            print("Inner finally running")
    except ValueError:
        print("h")
    finally:
        print("i")
        print("j")
    print("k")
    print("l")


def case2():
    print("\n--- Case 2: Exception at b, outer except matches ---")
    try:
        print("a")
        x = int("abc")  # ValueError
        print("c")
        try:
            print("d")
            print("e")
        except ZeroDivisionError:
            print("g")
        finally:
            print("Inner finally running")
    except ValueError:
        print("h")
    finally:
        print("i")
        print("j")
    print("k")
    print("l")


def case3():
    print("\n--- Case 3: Exception at b, outer except doesn't match ---")
    try:
        print("a")
        x = int("abc")  # ValueError
        print("c")
        try:
            print("d")
            print("e")
        except ZeroDivisionError:
            print("g")
        finally:
            print("Inner finally running")
    except ZeroDivisionError:
        print("h")
    finally:
        print("i")
        print("j")
    print("k")
    print("l")


def case4():
    print("\n--- Case 4: Exception at e, inner except matches ---")
    try:
        print("a")
        print("b")
        print("c")
        try:
            print("d")
            x = 10 / 0  # ZeroDivisionError
            print("f")
        except ZeroDivisionError:
            print("g")
        finally:
            print("Inner finally running")
    except ValueError:
        print("h")
    finally:
        print("i")
        print("j")
    print("k")
    print("l")


def case5():
    print("\n--- Case 5: Exception at e, inner except fails, outer except matches ---")
    try:
        print("a")
        print("b")
        print("c")
        try:
            print("d")
            x = int("abc")  # ValueError
            print("f")
        except ZeroDivisionError:
            print("g")
        finally:
            print("Inner finally running")
    except ValueError:
        print("h")
    finally:
        print("i")
        print("j")
    print("k")
    print("l")


def case6():
    print("\n--- Case 6: Exception at e, neither inner nor outer except matches ---")
    try:
        print("a")
        print("b")
        print("c")
        try:
            print("d")
            x = 10 / 0  # ZeroDivisionError
            print("f")
        except ValueError:
            print("g")
        finally:
            print("Inner finally running")
    except TypeError:
        print("h")
    finally:
        print("i")
        print("j")
    print("k")
    print("l")


def case7():
    print("\n--- Case 7: Exception at g, inner except matches ---")
    try:
        print("a")
        print("b")
        print("c")
        try:
            print("d")
            print("e")
            raise ZeroDivisionError("Error at g")  # Force an error at g
        except ZeroDivisionError:
            print("g")
        finally:
            print("Inner finally running")
    except ValueError:
        print("h")
    finally:
        print("i")
        print("j")
    print("k")
    print("l")


def case8():
    print("\n--- Case 8: Exception at g, inner except doesn't match ---")
    try:
        print("a")
        print("b")
        print("c")
        try:
            print("d")
            print("e")
            raise ValueError("Error at g")  # ValueError, but catching ZeroDivisionError
        except ZeroDivisionError:
            print("g")
        finally:
            print("Inner finally running")
    except TypeError:
        print("h")
    finally:
        print("i")
        print("j")
    print("k")
    print("l")


def case9():
    print("\n--- Case 9: Exception at h, outer except matches ---")
    try:
        print("a")
        print("b")
        print("c")
        try:
            print("d")
            print("e")
        except ZeroDivisionError:
            print("g")
        finally:
            print("Inner finally running")
    except ValueError:
        print("h")
        raise ZeroDivisionError  # Error inside h
    finally:
        print("i")
        print("j")
    print("k")
    print("l")


def case10():
    print("\n--- Case 10: Exception at h, outer except doesn't match ---")
    try:
        print("a")
        print("b")
        print("c")
        try:
            print("d")
            print("e")
        except ZeroDivisionError:
            print("g")
        finally:
            print("Inner finally running")
    except TypeError:
        print("h")
        raise ValueError  # Error inside h
    finally:
        print("i")
        print("j")
    print("k")
    print("l")


def case11():
    print("\n--- Case 11: Exception at i, outer except matches ---")
    try:
        print("a")
        print("b")
        print("c")
        try:
            print("d")
            print("e")
        except ZeroDivisionError:
            print("g")
        finally:
            raise ValueError  # error at i
    except ValueError:
        print("h")
    finally:
        print("i")
        print("j")
    print("k")
    print("l")


def case12():
    print("\n--- Case 12: Exception at i, outer except doesn't match ---")
    try:
        print("a")
        print("b")
        print("c")
        try:
            print("d")
            print("e")
        except ZeroDivisionError:
            print("g")
        finally:
            raise ValueError  # error at i
    except TypeError:
        print("h")
    finally:
        print("i")
        print("j")
    print("k")
    print("l")


def case13():
    print("\n--- Case 13: Exception at j ---")
    try:
        print("a")
        print("b")
        print("c")
        try:
            print("d")
            print("e")
        except ZeroDivisionError:
            print("g")
        finally:
            print("Inner finally running")
    except ValueError:
        print("h")
    finally:
        print("i")
        raise Exception("Exception at j")
    print("k")
    print("l")


def case14():
    print("\n--- Case 14: Exception at k ---")
    try:
        print("a")
        print("b")
        print("c")
        try:
            print("d")
            print("e")
        except ZeroDivisionError:
            print("g")
        finally:
            print("Inner finally running")
    except ValueError:
        print("h")
    finally:
        print("i")
        print("j")
    raise Exception("Exception at k")
    print("l")


# Running all cases one by one:
if __name__ == "__main__":
    cases = [case1, case2, case3, case4, case5, case6, case7, case8, case9, case10, case11, case12, case13, case14]
    for idx, func in enumerate(cases, start=1):
        try:
            func()
        except Exception as e:
            print(f"Error Occurred in Case {idx}: {e}")
        print("\n"+"-"*50+"\n")
