import copy
countries = ["Brazil", "Croatia", "Mexico", "Cameroon",
            "Spain", "Netherlands", "Chile", "Australia",
            "Colombia", "Greece", "Cote d'Ivoire", "Japan",
            "Uruguay", "Costa Rica", "England", "Italy",
            "Switzerland", "Ecuador", "France", "Honduras",
            "Argentina", "Bosnia and Herzegovina", "Iran",
            "Nigeria", "Germany", "Portugal", "Ghana",
            "USA", "Belgium", "Algeria", "Russia",
            "Korea Republic"]

def search_count(key, country_list, get_list):
    result_count = 0
    for v in country_list:
        if key == "" or key[-1:] == v[0]:
            buff_list = copy.deepcopy(country_list)
            buff_list.remove(v)
            buff_get = copy.deepcopy(get_list)
            buff_get.append(v)
            count = search_count(v, buff_list, buff_get)
            if result_count < count:
                result_count = count
                print(get_list)

    if result_count != 0:
        return result_count

    return len(countries) - len(country_list)

        

def main():
    get_list = []
    country_list = [v.lower() for v in countries]
    print(search_count("" ,country_list, get_list))
            
if __name__ == "__main__":
    main()