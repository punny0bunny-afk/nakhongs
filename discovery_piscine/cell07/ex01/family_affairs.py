def find_the_redheads(family):
    return list(filter(lambda name: family[name] == "red", family))

def main():
    dupont_family = {
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red"
    }
    print(find_the_redheads(dupont_family))

if __name__ == "__main__":
    main()