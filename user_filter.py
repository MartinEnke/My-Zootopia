def user_filter(animals_data):
    '''Collects animal characteristics and filters them
    by user choice of skin type'''
    skin_types = set()
    for animal in animals_data:
        if "skin_type" in animal["characteristics"]:
            skin_types.add(animal["characteristics"]["skin_type"])

    while True:
        print("Available skin types:")
        for skin in sorted(skin_types):
            print(f"- {skin}")

        selected_skin_type = input("\nChoose a skin type or hit enter to show all: ").strip().lower()

        if selected_skin_type == "":
            filtered_animals = animals_data
            return filtered_animals

        elif selected_skin_type in ("fur", "hair", "scales"):
            filtered_animals = []
            for animal in animals_data:
                if "skin_type" in animal["characteristics"] and animal["characteristics"][
                    "skin_type"].lower() == selected_skin_type:
                    filtered_animals.append(animal)
            return filtered_animals

        else:
            print(f"Invalid Input, please choose from the list.\n")