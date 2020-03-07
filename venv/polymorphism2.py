class India:
    def states(self):
        print(29)

    def currency(self):
        print("Rupee")


class Usa:
    def states(self):
        print(15)

    def currency(self):
        print("Dollar")


def main():
    ind_obj = India()
    usa_obj = Usa()

    for obj in (ind_obj, usa_obj):
        obj.states()
        obj.currency()


if __name__ == "__main__":
    main()
