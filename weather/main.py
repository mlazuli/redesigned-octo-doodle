import typer
from rich import print

from api import get_current_weather
app = typer.Typer()

@app.command()
def current_weather(zipcode:int):
    print(f'Getting weather for {zipcode}')
    params = {
	"latitude": 52.52,
	"longitude": 13.41,
	"current": "temperature_2m",
	"forecast_days": 1
    }
    get_current_weather(weather_params=params)

if __name__ == '__main__':
    app()