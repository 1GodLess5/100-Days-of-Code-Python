def addNewCountry(countryName: str, numberOfVisits: int, visitedCities: list):
    global travelLog
    addDictionary = {
        "country": countryName,
        "visits": numberOfVisits,
        "cities": visitedCities
    }

    travelLog.append(addDictionary)

    return travelLog


travelLog = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
},
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

addNewCountry("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travelLog)
