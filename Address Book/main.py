class AddressBook:
    def whole_address_book(self):
        try:
            with open('address_book.txt', 'r') as file:
                return [i.strip() for i in file.readlines()]
        except FileNotFoundError:
            with open('address_book.txt', 'w') as file:
                print("The Address Book is clear. Please add some People.")
                quit()

    def add(self, name, surname):
        name = name.capitalize();
        surname = surname.capitalize()
        mass = self.whole_address_book()
        if f"{name} {surname}" in mass:
            print(f"{name} {surname} already exists in the address book.")
        else:
            with open('address_book.txt', 'a') as file:
                file.write(f"{name} {surname}\n")
                print(f"{name} {surname}: successfully added to the address book.")

    def delete(self, name, surname):
        name = name.capitalize();
        surname = surname.capitalize()
        mass = self.whole_address_book()
        if f"{name} {surname}" in mass:
            mass.remove(f"{name} {surname}")
            with open('address_book.txt', 'w') as file:
                for i in mass:
                    file.write(i + "\n")
            print(f"{name} {surname} successfully deleted from the address book.")
        else:
            print(f"{name} {surname} doesn`t exists in the address book.")

    def edit(self, name, surname, edit_name, edit_surname):
        name = name.capitalize();
        surname = surname.capitalize()
        edit_name = edit_name.capitalize();
        edit_surname = edit_surname.capitalize()
        mass = self.whole_address_book()
        if name == edit_name and surname == edit_surname:
            print("They are the same.")
            quit()
        if f"{name} {surname}" not in mass:
            print(f"{name} {surname} doesn`t exists in the address book.")
        if f"{edit_name} {edit_surname}" in mass:
            print(f"{edit_name} {edit_surname} exists in the address book.")
        else:
            mass.insert(mass.index(f'{name} {surname}'), f"{edit_name} {edit_surname}")
            mass.pop(mass.index(f'{name} {surname}'))
            with open('address_book.txt', 'w') as file:
                for i in mass:
                    file.write(i + "\n")
            print(f"{name} {surname} successfully changed to {edit_name} {edit_surname} in the address book.")

    def find(self, name, surname):
        name = name.capitalize();
        surname = surname.capitalize()
        mass = self.whole_address_book()

        if (f"{name} {surname}") not in mass:
            print(f"{name} {surname} doesn`t exists in the address book.")
        else:
            print(f"{name} {surname} founded on row: {mass.index(f'{name} {surname}') + 1}")


    def help(self):
        print("And here are the commands: \n"
            "add(*name*, *surname*): add people to the address book.\n"
            "delete(*name*, *surname*): delete people to the address book.\n"
            "edit(*name*, *surname*, *edited_name*, *edited_surname*): edit people in the address book\n"
            "find(*name*, *surname*): find the people in the address book. (Returns the number of row.)")



