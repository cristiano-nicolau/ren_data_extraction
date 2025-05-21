# REN Data Extraction – Gas and Electricity Monthly Data (Portugal)

This project provides Python scripts to extract and organize monthly **gas** and **electricity** consumption and supply data from the **REN (Redes Energéticas Nacionais)** public API in Portugal. The data can be used for analysis, visualization, and reporting purposes.

## What This Does

- Extracts monthly gas and electricity data for each year from **2020 to 2024**.
- Gathers data using the official REN DataHub API.
- Structures the data into a clean `pandas.DataFrame`.
- Reshapes the data so that each row represents a `(year, month)` combination and each metric becomes a column (wide format).
- Data can be saved to `.csv` or used for further analysis/visualization.

---

## Electricity Data

The electricity data is collected from:
````
https://servicebus.ren.pt/datahubapi/electricity/ElectricityConsumptionSupplyMonthly
````


## 🔥 Gas Data

The gas data is collected from:
````
https://servicebus.ren.pt/datahubapi/gas/GasConsumptionSupplyMonthly
````

---

## Data Structure
The data is structured in a wide format, where each row corresponds to a specific year and month, and each column represents a different metric. This allows for easy analysis and visualization of the data.
The data is organized into two main sections: **Gas** and **Electricity**.

Metrics included in the electricity data are:
| Field                              | Description                                                        |
|-------------------------------------|--------------------------------------------------------------------|
| ano                                | Year of the data record                                            |
| mes                                | Month of the data record                                           |
| CONSUMO_ARMAZENAMENTO              | Consumption from storage sources                                   |
| BIOMASSA_OUTROS                    | Biomass from other sources                                         |
| CONSUMO_BOMBAGEM                   | Consumption for pumping (e.g., pumped hydro storage)               |
| INJECAO_BATERIAS                   | Energy injected into batteries                                     |
| CONSUMO_BATERIAS                   | Energy consumed from batteries                                     |
| CONSUMO                            | Total energy consumption                                           |
| BIOMASSA_COGERACAO                 | Biomass used in cogeneration                                       |
| EXPORTACAO                         | Energy exported                                                    |
| HIDRICA                            | Hydropower production                                              |
| IMPORTACAO                         | Energy imported                                                    |
| GAS_NATURAL_CICLO_COMBINADO        | Natural gas (combined cycle plants)                                |
| GAS_NATURAL_COGERACAO              | Natural gas used in cogeneration                                   |
| PRODUCAO_NAO_RENOVAVEL             | Non-renewable energy production                                    |
| GAS_NATURAL                        | Total natural gas energy production                                |
| OUTRA_TERMICA_COGERACAO            | Other thermal sources used in cogeneration                         |
| OUTRA_TERMICA_OUTROS               | Other thermal sources (miscellaneous)                              |
| OUTRA_TERMICA                      | Total other thermal energy production                              |
| PRODUCAO_ARMAZENAMENTO             | Energy produced from storage                                       |
| PRODUCAO_BOMBAGEM                  | Energy produced by pumping (e.g., pumped hydro storage)            |
| EOLICA                             | Wind power production                                              |
| ONDAS                              | Wave power production                                              |
| SOLAR                              | Solar power production                                             |
| PRODUCAO_TOTAL                     | Total energy production                                            |
| PRODUCAO_RENOVAVEL                 | Total renewable energy production                                  |
| SALDO_IMPORTADOR                   | Net importer balance (import - export)                             |
| BIOMASSA                           | Total biomass energy production                                    |


---
Metrics included in the gas data are:

| Field                | Description                                                      |
|----------------------|------------------------------------------------------------------|
| ano                  | Year of the data record                                          |
| mes                  | Month of the data record                                         |
| CLIENTES_AP          | Consumption by protected customers (clientes com acesso protegido)|
| MERCADO_CONVENCIONAL | Consumption in the conventional market                           |
| MERCADO_ELETRICO     | Consumption for electricity generation                           |
| REDE_DISTRIBUICAO    | Consumption via the distribution network                         |
| UAG                  | Consumption at Underground Gas Storage (Unidade de Armazenamento de Gás) |
| CONSUMO_TOTAL        | Total gas consumption                                            |

---

## Requirements
- Python 3.7+
- `pandas`
- `requests`


## Data Source
All data is sourced from the official REN DataHub API. The API provides a comprehensive set of endpoints for accessing various energy-related data in Portugal.
- [REN DataHub](https://datahub.ren.pt/pt/)
- [REN DataHub API Documentation](https://datahub.ren.pt/pt/instrucoes-api/)

## Usage
This repository contains Python scripts to extract and process the data. You can run the scripts directly or import them into your own projects.
The data belong to REN and is publicly available. Please refer to the [REN DataHub](https://datahub.ren.pt/pt/) for more information on data usage and licensing.



