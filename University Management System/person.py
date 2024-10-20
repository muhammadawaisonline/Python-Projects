class Person:
    def __init__(self, whatsapp_number, name, age):
        self.whatsapp_number = whatsapp_number
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.__class__.__name__}(WhatsApp: {self.whatsapp_number}, Name: {self.name}, Age: {self.age})"
