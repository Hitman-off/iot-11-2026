from enum import Enum

class GovernmentType(Enum):
    DEMOCRACY = "DEMOCRACY"
    REPUBLIC = "REPUBLIC"
    MONARCHY = "MONARCHY"
    AUTOCRACY = "AUTOCRACY"
    OLIGARCHY = "OLIGARCHY"
    THEOCRACY = "THEOCRACY"

class Country:
    def __init__(self, name, capital, code, population, area, gdp,
                 government=GovernmentType.REPUBLIC):
        self._name = name
        self._capital = capital
        self._code = code
        self._population = population
        self._area = area
        self._gdp = gdp
        self._government = government

    def __del__(self):
        print(f"[Destructor] Country {self._name} removed")

    def get_name(self): return self._name
    def get_capital(self): return self._capital
    def get_code(self): return self._code
    def get_population(self): return self._population
    def get_area(self): return self._area
    def get_gdp(self): return self._gdp
    def get_government(self): return self._government

    def set_capital(self, value):
        self._capital = value

    def set_population(self, value):
        if value < 0:
            raise ValueError("Population cannot be negative")
        self._population = value

    def set_gdp(self, value):
        if value < 0:
            raise ValueError("GDP cannot be negative")
        self._gdp = value

    def get_density(self):
        return self._population / self._area

    def get_gdp_per_capita(self):
        return self._gdp * 1e9 / self._population

    def __str__(self):
        return (f"{self._name} ({self._code})  capital: {self._capital}  "
                f"population: {self._population:,}  area: {self._area:,} km2  "
                f"GDP: {self._gdp:,} billion  {self._government.value}")

    def print_info(self):
        print(self)

class Land:
    def __init__(self, name):
        self._name = name
        self._countries = []

    def __del__(self):
        print(f"[Destructor] Land {self._name} removed")

    def get_name(self): return self._name
    def get_countries(self): return list(self._countries)

    def add_country(self, country):
        if country not in self._countries:
            self._countries.append(country)

    def get_total_population(self):
        return sum(c.get_population() for c in self._countries)

    def __str__(self):
        return f"Land {self._name}: " + ", ".join(c.get_name() for c in self._countries)

    def print_info(self):
        print(self)

class Film:
    def __init__(self, title, release_date):
        self._title = title
        self._release_date = release_date

    def __del__(self):
        print(f"[Destructor] Film {self._title} removed")

    def get_title(self): return self._title
    def get_release_date(self): return self._release_date

    def __str__(self):
        year, month, day = self._release_date.split("-")
        return f"{self._title} ({day}.{month}.{year})"

    def print_info(self):
        print(self)

def calculate_population_density(countries):
    result = {c.get_name(): c.get_density() for c in countries}
    average = sum(c.get_population() for c in countries) / sum(c.get_area() for c in countries)
    return result, average

def sort_by_gdp(countries):
    return sorted(countries, key=lambda c: c.get_gdp(), reverse=True)

def print_top_by_gdp(countries, n=3):
    print(f"Top {n} countries by GDP")
    for place, c in enumerate(sort_by_gdp(countries)[:n], start=1):
        print(f"{place}. {c.get_name()}: {c.get_gdp():,} billion")

def choose_country(countries, allowed_governments, max_density, min_gdp_per_capita):
    suitable = [c for c in countries
                if c.get_government() in allowed_governments
                and c.get_density() <= max_density
                and c.get_gdp_per_capita() >= min_gdp_per_capita]
    return max(suitable, key=lambda c: c.get_gdp_per_capita()) if suitable else None

def sort_films_by_date(films):
    return sorted(films, key=lambda f: f.get_release_date())

def main():
    ukraine = Country("Ukraine", "Kyiv", "UA", 38_000_000, 603_550, 160, GovernmentType.REPUBLIC)
    poland = Country("Poland", "Warsaw", "PL", 36_800_000, 312_696, 810, GovernmentType.DEMOCRACY)
    germany = Country("Germany", "Berlin", "DE", 83_200_000, 357_022, 4200, GovernmentType.DEMOCRACY)
    france = Country("France", "Paris", "FR", 68_000_000, 551_695, 2900, GovernmentType.REPUBLIC)
    saudi = Country("Saudi Arabia", "Riyadh", "SA", 36_000_000, 2_149_690, 1070, GovernmentType.MONARCHY)
    china = Country("China", "Beijing", "CN", 1_410_000_000, 9_596_961, 17800, GovernmentType.AUTOCRACY)
    countries = [ukraine, poland, germany, france, saudi, china]
    
    print("All countries")
    for c in countries:
        c.print_info()

    europe = Land("Europe")
    for c in (ukraine, poland, germany, france):
        europe.add_country(c)
    europe.print_info()
    print(f"Population of Europe: {europe.get_total_population():,}")

    densities, avg = calculate_population_density(europe.get_countries())
    print("Population density (people per km2)")
    for name, d in densities.items():
        print(f"{name}: {d:.1f}")
    print(f"Average density: {avg:.1f}")

    print_top_by_gdp(countries)

    best = choose_country(countries, [GovernmentType.DEMOCRACY, GovernmentType.REPUBLIC], 300, 30_000)
    print("Chosen country")
    print(best if best else "No suitable country found")

    poland.set_population(37_000_000)
    print(f"New population of Poland: {poland.get_population():,}")

    films = [Film("Film A", "2015-06-12"),
             Film("Film B", "2001-03-05"),
             Film("Film C", "2022-11-30")]
    print("Films by release date (oldest first)")
    for film in sort_films_by_date(films):
        film.print_info()

lnd_1 = Land("fff" )
cnt_1 = Country("fff", "frfr", "FF", 50_000_000, 1000, 100, GovernmentType.THEOCRACY)
cnt_2 = Country("fdf", "frfr", "FFL", 70_000_000, 2000, 200, GovernmentType.AUTOCRACY)
cnt_3 = Country("fnf", "frfr", "FFH", 60_000_000, 3000, 300, GovernmentType.DEMOCRACY)
lnd_1.add_country(cnt_1)
lnd_1.add_country(cnt_2)
lnd_1.add_country(cnt_3)
lnd_1.print_info()
for country in lnd_1.get_countries():
    print(f" name = {country.get_name()} , population = {country.get_population()}")
    
print(f" name = {lnd_1.get_name()} , population = {lnd_1.get_total_population()}")









