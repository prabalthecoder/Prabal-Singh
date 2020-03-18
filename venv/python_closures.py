def p_m_m(my_str):
    def nested():
        print(my_str)
    return nested
b = p_m_m("hello")
b()
