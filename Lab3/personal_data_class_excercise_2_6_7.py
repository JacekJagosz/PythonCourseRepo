from dataclasses import dataclass, asdict
import json

# "Normal" implementation
# class PersonalData:
#     def __init__(self, first_name, last_name, home_address, zip_code, pesel):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.home_address = home_address
#         self.zip_code = zip_code
#         self.pesel = pesel
#
#     def to_json(self, filename):
#         with open(filename, 'w') as file: # if instead it should append, then change 'w' to 'a'
#             json.dump(self.__dict__, file)
#
#     @classmethod
#     def from_json(cls, filename):
#         with open(filename, 'r') as file:
#             data = json.load(file)
#         return cls(**data)

# Dataclass implementation
@dataclass
class PersonalData:
    first_name: str
    last_name: str
    home_address: str
    zip_code: str
    pesel: int

    def to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(asdict(self), file)

    @classmethod
    def from_json(cls, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        return cls(**data)

# Upper case decorator
class UppercaseDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        original_result = self.func(*args, **kwargs)
        uppercase_result = original_result.upper()
        return uppercase_result

@UppercaseDecorator
def print_name(personal_data):
    return personal_data.first_name


# Creating an instance of the class
person = PersonalData("Jan", "Kowalski", "Reymonta 21", "31-059", "1234567890")

# Writing the object to a JSON file
person.to_json("personal_data.json")

# Reading the JSON file and creating an instance of the class
new_person = PersonalData.from_json("personal_data.json")

print(new_person.first_name)
print(new_person.last_name)
print(new_person.home_address)
print(new_person.zip_code)
print(new_person.pesel)

print(f"Name converted to uppercase using a decorator: {print_name(new_person)}")
