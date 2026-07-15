def build_profile(name, **details):
    print("Name:", name)

    for key, value in details.items():
        print(key, ":", value)


build_profile(
    "Sita",
    program="BSCS",
    semester=2,
    portfolio="www.portfolio.com"
)