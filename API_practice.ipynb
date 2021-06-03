{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "362b8662",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a practice set of random latitude and longitude combinations.\n",
    "x = [25.12903645, 25.92017388, 26.62509167, -59.98969384, 37.30571269]\n",
    "y = [-67.59741259, 11.09532135, 74.84233102, -76.89176677, -61.13376282]\n",
    "coordinates = zip(x, y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "ba5d8475",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "25.12903645 -67.59741259\n",
      "25.92017388 11.09532135\n",
      "26.62509167 74.84233102\n",
      "-59.98969384 -76.89176677\n",
      "37.30571269 -61.13376282\n"
     ]
    }
   ],
   "source": [
    "# Use the tuple() function to display the latitude and longitude combinations.\n",
    "for coordinate in coordinates:\n",
    "    print(coordinate[0], coordinate[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "2faed489",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use the citipy module to determine city based on latitude and longitude.\n",
    "from citipy import citipy\n",
    "\n",
    "# Use the tuple() function to display the latitude and longitude combinations.\n",
    "for coordinate in coordinates:\n",
    "    print(citipy.nearest_city(coordinate[0], coordinate[1]).city_name,\n",
    "          citipy.nearest_city(coordinate[0], coordinate[1]).country_code)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "eb4991eb",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import the requests library.\n",
    "import requests\n",
    "\n",
    "# Import the API key.\n",
    "from config import weather_api_key"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aceec831",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Starting URL for Weather Map API Call. NEVER SAVE API KEY IN PLAIN TEXT OR IN OUTPUT\n",
    "url = \"http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=\" + weather_api_key\n",
    "print(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4295f866",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create an endpoint URL for a city.\n",
    "city_url = url + \"&q=\" + \"Boston\"\n",
    "print(city_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "523c93d8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Response [200]>"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Make a 'Get' request for the city weather.\n",
    "city_weather = requests.get(city_url)\n",
    "city_weather"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "2363619c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "200"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# The code output will be <Response [200]>, indicating a valid response. 404 is client error\n",
    "city_weather.status_code"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "54be4d4f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Response [404]>"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Create an endpoint URL for a city.\n",
    "# If we tried to get weather data from an unrecognized city,\n",
    "# or if the weather data for a city wasn't available, we would get a 404 response\n",
    "city_url = url + \"&q=\" + \"Bston\"\n",
    "city_weather = requests.get(city_url)\n",
    "city_weather"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "f5a1afcb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Response [200]>"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Create an endpoint URL for a city.\n",
    "city_url = url + \"&q=\" + \"Boston\"\n",
    "city_weather = requests.get(city_url)\n",
    "city_weather"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "5ba22a65",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'{\"coord\":{\"lon\":-71.0598,\"lat\":42.3584},\"weather\":[{\"id\":804,\"main\":\"Clouds\",\"description\":\"overcast clouds\",\"icon\":\"04n\"}],\"base\":\"stations\",\"main\":{\"temp\":63.37,\"feels_like\":63.09,\"temp_min\":57.34,\"temp_max\":67.77,\"pressure\":1021,\"humidity\":78},\"visibility\":10000,\"wind\":{\"speed\":3,\"deg\":174,\"gust\":11.99},\"clouds\":{\"all\":90},\"dt\":1622696702,\"sys\":{\"type\":2,\"id\":2013408,\"country\":\"US\",\"sunrise\":1622711353,\"sunset\":1622765760},\"timezone\":-14400,\"id\":4930956,\"name\":\"Boston\",\"cod\":200}'"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Get the text of the 'Get' request.\n",
    "# When we receive a valid response from the server,\n",
    "# we have to decide on the data format. The options are text, JSON, XML, or HTML format.\n",
    "city_weather.text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "adc671c5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'coord': {'lon': -71.0598, 'lat': 42.3584},\n",
       " 'weather': [{'id': 804,\n",
       "   'main': 'Clouds',\n",
       "   'description': 'overcast clouds',\n",
       "   'icon': '04n'}],\n",
       " 'base': 'stations',\n",
       " 'main': {'temp': 63.37,\n",
       "  'feels_like': 63.09,\n",
       "  'temp_min': 57.34,\n",
       "  'temp_max': 67.77,\n",
       "  'pressure': 1021,\n",
       "  'humidity': 78},\n",
       " 'visibility': 10000,\n",
       " 'wind': {'speed': 3, 'deg': 174, 'gust': 11.99},\n",
       " 'clouds': {'all': 90},\n",
       " 'dt': 1622696702,\n",
       " 'sys': {'type': 2,\n",
       "  'id': 2013408,\n",
       "  'country': 'US',\n",
       "  'sunrise': 1622711353,\n",
       "  'sunset': 1622765760},\n",
       " 'timezone': -14400,\n",
       " 'id': 4930956,\n",
       " 'name': 'Boston',\n",
       " 'cod': 200}"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Get the JSON text of the 'Get' request.\n",
    "city_weather.json()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "da86cb22",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "City Weather found.\n"
     ]
    }
   ],
   "source": [
    "# Create an endpoint URL for a city.\n",
    "city_url = url + \"&q=\" + \"Boston\"\n",
    "city_weather = requests.get(city_url)\n",
    "if city_weather.status_code == 200:\n",
    "    print(f\"City Weather found.\")\n",
    "else:\n",
    "    print(f\"City weather not found.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "b34731a5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "City weather not found.\n"
     ]
    }
   ],
   "source": [
    "# Create an endpoint URL for a city.\n",
    "city_url = url + \"&q=\" + \"Bston\"\n",
    "city_weather = requests.get(city_url)\n",
    "if city_weather.status_code == 200:\n",
    "    print(f\"City Weather found.\")\n",
    "else:\n",
    "    print(f\"City weather not found.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "92c588df",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "PythonData",
   "language": "python",
   "name": "pythondata"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
