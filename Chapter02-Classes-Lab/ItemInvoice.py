class ItemInvoice:

    def __init__(self, item, description):
        self.__item = item
        self.__description = description

    @property
    def item(self):
        return self.__item

    @property
    def description(self):
        return self.__description

    @description.setter
    def descripton(self, description: str):
        self.__description = description


def main():
    invoice = ItemInvoice(100, "stereo system")
#    invoice.description = "a new description"
    print("Item quantity: " + str(invoice.item))
    print("Item description: " + invoice.description)

if __name__ == "__main__":
    main()
