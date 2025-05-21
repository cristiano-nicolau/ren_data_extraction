import requests
import pandas as pd
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

def fetch_gas_data(year: int, month: int) -> list:
    """
    Fetches gas consumption data from REN API for a given year and month.

    Args:
        year (int): The year for which to fetch data.
        month (int): The month for which to fetch data.

    Returns:
        list: A list of dictionaries with filtered gas data for the specified month and year.
    """
    url = (
        f"https://servicebus.ren.pt/datahubapi/gas/GasConsumptionSupplyMonthly"
        f"?culture=pt-PT&year={year}&month={month:02d}"
    )
    response = requests.get(url)
    if response.status_code != 200:
        logging.error(f"Error fetching data for {year}-{month:02d}: HTTP {response.status_code}")
        return []
    logging.info(f"Data fetched successfully for {year}-{month:02d}")
    json_data = response.json()
    filtered_types = [
        "CLIENTES_AP",
        "CONSUMO_TOTAL",
        "MERCADO_CONVENCIONAL",
        "MERCADO_ELETRICO",
        "REDE_DISTRIBUICAO",
        "UAG"
    ]
    result = []
    for item in json_data:
        if item['type'] in filtered_types:
            result.append({
                'ano': year,
                'mes': month,
                'tipo': item['type'],
                'acumulado_mensal': item['monthly_Accumulation']
            })
    return result

def collect_gas_data(start_year: int, end_year: int) -> pd.DataFrame:
    """
    Collects gas consumption data for a range of years and all months.

    Args:
        start_year (int): The starting year (inclusive).
        end_year (int): The ending year (inclusive).

    Returns:
        pd.DataFrame: A pandas DataFrame containing the collected gas data.
    """
    dados = []
    for ano in range(start_year, end_year + 1):
        for mes in range(1, 13):
            dados.extend(fetch_gas_data(ano, mes))
    df = pd.DataFrame(dados)
    df_pivot = df.pivot_table(
        index=['ano', 'mes'],
        columns='tipo',
        values='acumulado_mensal'
    ).reset_index()
    ordered_cols = [
        'ano', 'mes', 'CLIENTES_AP', 'MERCADO_CONVENCIONAL', 'MERCADO_ELETRICO',
        'REDE_DISTRIBUICAO', 'UAG', 'CONSUMO_TOTAL'
    ]
    df_pivot = df_pivot.reindex(columns=ordered_cols)
    logging.info("Gas data collected and pivoted successfully.")
    return df_pivot

def fetch_electricity_data(year: int, month: int) -> list:
    """
    Fetches electricity consumption and production data from REN API for a given year and month.

    Args:
        year (int): The year for which to fetch data.
        month (int): The month for which to fetch data.

    Returns:
        list: A list of dictionaries with filtered electricity data for the specified month and year.
    """
    url = (
        f"https://servicebus.ren.pt/datahubapi/electricity/ElectricityConsumptionSupplyMonthly"
        f"?culture=pt-PT&year={year}&month={month:02d}"
    )
    response = requests.get(url)
    if response.status_code != 200:
        logging.error(f"Error fetching data for {year}-{month:02d}: HTTP {response.status_code}")
        return []
    logging.info(f"Data fetched successfully for {year}-{month:02d}")

    json_data = response.json()
    filtered_types = [
        "CONSUMO_ARMAZENAMENTO",
        "BIOMASSA_OUTROS",
        "CONSUMO_BOMBAGEM",
        "INJECAO_BATERIAS",
        "CONSUMO_BATERIAS",
        "CONSUMO",
        "BIOMASSA_COGERACAO",
        "EXPORTACAO",
        "HIDRICA",
        "IMPORTACAO",
        "GAS_NATURAL_CICLO_COMBINADO",
        "GAS_NATURAL_COGERACAO",
        "PRODUCAO_NAO_RENOVAVEL",
        "GAS_NATURAL",
        "OUTRA_TERMICA_COGERACAO",
        "OUTRA_TERMICA_OUTROS",
        "OUTRA_TERMICA",
        "PRODUCAO_ARMAZENAMENTO",
        "PRODUCAO_BOMBAGEM",
        "EOLICA",
        "ONDAS",
        "SOLAR",
        "PRODUCAO_TOTAL",
        "PRODUCAO_RENOVAVEL",
        "SALDO_IMPORTADOR",
        "BIOMASSA"
    ]
    result = []
    for item in json_data:
        if item['type'] in filtered_types:
            result.append({
                'ano': year,
                'mes': month,
                'tipo': item['type'],
                'acumulado_mensal': item['monthly_Accumulation']
            })
    return result

def collect_electricity_data(start_year: int, end_year: int) -> pd.DataFrame:
    """
    Collects electricity consumption and production data for a range of years and all months.

    Args:
        start_year (int): The starting year (inclusive).
        end_year (int): The ending year (inclusive).

    Returns:
        pd.DataFrame: A pandas DataFrame containing the collected electricity data.
    """
    dados = []
    for ano in range(start_year, end_year + 1):
        for mes in range(1, 13):
            dados.extend(fetch_electricity_data(ano, mes))
    df = pd.DataFrame(dados)
    df_pivot = df.pivot_table(
        index=['ano', 'mes'],
        columns='tipo',
        values='acumulado_mensal'
    ).reset_index()
    ordered_cols = [
        'ano', 'mes', 'CONSUMO_ARMAZENAMENTO', 'BIOMASSA_OUTROS', 'CONSUMO_BOMBAGEM',
        'INJECAO_BATERIAS', 'CONSUMO_BATERIAS', 'CONSUMO', 'BIOMASSA_COGERACAO',
        'EXPORTACAO', 'HIDRICA', 'IMPORTACAO', 'GAS_NATURAL_CICLO_COMBINADO',
        'GAS_NATURAL_COGERACAO', 'PRODUCAO_NAO_RENOVAVEL', 'GAS_NATURAL',
        'OUTRA_TERMICA_COGERACAO', 'OUTRA_TERMICA_OUTROS', 'OUTRA_TERMICA',
        'PRODUCAO_ARMAZENAMENTO', 'PRODUCAO_BOMBAGEM', 'EOLICA', 'ONDAS',
        'SOLAR', 'PRODUCAO_TOTAL', 'PRODUCAO_RENOVAVEL', 'SALDO_IMPORTADOR', 'BIOMASSA'
    ]
    df_pivot = df_pivot.reindex(columns=ordered_cols)
    logging.info("Electricity data collected and pivoted successfully.")
    return df_pivot

def main():
    """
    Main function to collect gas data from 2020 to 2024 and display the first rows.
    """
    logging.info("Starting data collection...")
    logging.info("Collecting gas data...")
    df = collect_gas_data(2020, 2024)
    df.to_csv("gas_consumption_2020_2024_REN.csv", index=False)
    logging.info("Gas data collected and saved to consumo_gas_2020_2024_REN.csv")
    logging.info("Collecting electricity data...")
    df = collect_electricity_data(2020, 2024)
    df.to_csv("electricity_consumption_2020_2024_REN.csv", index=False)
    logging.info("Electricity data collected and saved to consumo_electricidade_2020_2024_REN.csv")
if __name__ == "__main__":
    main()

