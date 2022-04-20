
from fastapi import FastAPI

from models.models import InputModel, OutputModel
from services.city import get_apartment_rent, get_city_list, get_city_score

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/search", status_code=200, response_model=list[OutputModel], tags=['city-list'])
async def search(raw_body: InputModel):
    app_rent = get_apartment_rent()
    del app_rent[0]

    input_dep = raw_body.department
    input_rent_m2 = int(raw_body.max_rent/raw_body.surface)

    city_list = get_city_list(input_dep)
    cities_selected = []

    for commune in city_list:
        city_name = commune.get('nom')
        commune_insee = commune.get('code')

        for item in app_rent:
            data = item[0].split(";")
            insee = data[1]
            avg_rent = data[7]

            if (commune_insee == insee) and int(avg_rent) <= input_rent_m2:
                city_ok = {
                    'city': city_name,
                    'avg_rent': avg_rent,
                    'postal_code': commune.get('codesPostaux'),
                    'population': commune.get('population'),
                    'score': get_city_score(city_name)
                }
                cities_selected.append(city_ok)

    return sorted(cities_selected, key=lambda d: (d['avg_rent'], -d['score']))
