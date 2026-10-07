def array_of_names(namebook):
    full_names = []
    for first, last in namebook.items():
        full_name = f"{first.capitalize()} {last.capitalize()}"
        full_names.append(full_name)
    return full_names

def main():
    persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
    }
    print(array_of_names(persons))

if __name__ == "__main__":
    main()