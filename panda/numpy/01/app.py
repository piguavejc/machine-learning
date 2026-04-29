
from pathlib import Path
import pandas as pd
import numpy as np


class Processor:
    def __init__(self):
        self.dataset = None
        self.dataset_cleaned = None

    def load_data(self):
        dir = Path(__file__).parent
        self.dataset = pd.read_csv(
            dir / "../../dataset/Ciudades_Visitadas_Latinoamerica_2023.csv")
        return self.dataset

    def clean_data(self):
        df = self.dataset.copy()

        print("\nPoblación")
        print(df["Población"].mean())

        print("\nRedondeo de la población a millones:")
        print(np.round(df["Población"].mean(), 2))

        print("\nPoblación minima:")
        print(df["Población"].min())

        print("\nPoblación máxima:")
        print(df["Población"].max())

        self.dataset_cleaned = df
        return self.dataset_cleaned


if __name__ == "__main__":
    processor = Processor()
    processor.load_data()
    processor.clean_data()
