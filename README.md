# Foreign-Born Population Visualization for Wyoming
(only in Wyoming for now, will add more states or complete US soon)

<p align="center">
  <img src=https://github.com/user-attachments/assets/67b31698-cad4-4708-8a86-2f40963d1fb0 alt="Wyoming Map" />
</p>

## Overview

This project visualizes the foreign-born population distribution across cities in Wyoming for the year 2023. It uses geospatial data visualization techniques to plot the foreign-born population in an interactive map, with city points scaled by population and colored based on the proportion of foreign-born citizens. The map is generated using Plotly and exported as an interactive HTML file.

## Features

- Filters the data for Wyoming cities and the year 2023.
- Retrieves latitude and longitude for each city using the Geopy geocoding API.
- Visualizes foreign-born population distribution on an interactive map.
- Customizes map style, zoom level, and appearance using Plotly.
- Exports the map as an interactive HTML file that can be shared or embedded.

## Technologies Used

- **Python**: Main programming language for data manipulation and visualization.
- **Pandas**: Used for data manipulation, cleaning, and filtering.
- **Plotly**: For creating interactive maps and visualizations.
- **Geopy**: For geocoding cities and retrieving latitude and longitude.
- **Jupyter Notebooks** (optional): For experimentation and testing (if applicable).

## Setup and Installation

### Prerequisites

- Python 3.x
- Required libraries: `pandas`, `plotly`, `geopy`

### Install Dependencies

Clone this repository and install the required dependencies using pip:

```bash
git clone https://github.com/yourusername/Foreign-Born-Population.git
cd Foreign-Born-Population
pip install -r requirements.txt
```
### Data File

The project requires the Foreign-Born Population.csv dataset, taken from [United States | Data USA](https://datausa.io/profile/geo/united-states).
Ensure that this file is present in the root directory of the project for it to function correctly.

### Run the Project

Once the environment is set up and the dataset is in place, run the following command to generate the interactive map:
```bash
python wyoming_population_map.py
```

This will create an interactive map saved as wyoming_population_map.html from where the screenshot was taken.
