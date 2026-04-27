import pandas as pd
from pathlib import Path 


class Processor:
    def __init__(self):
        self.dataset = None
        self.dataset_cleaned = None

    def get_data(self):
        dir = Path(__file__).parent 
        print("-------",dir)
        self.dataset = pd.read_csv(dir / "../../dataset/medallas.csv")
        rows = len(self.dataset) 
        print("Rows:", rows)

    def clean_data(self):
        df = self.dataset.copy()

        print("Columnas con valores nulos:")
        print(df.isnull().sum())

        df["Oro"] = df["Oro"].fillna(0)
        df["Plata"] = df["Plata"].fillna(0)
        df["Bronce"] = df["Bronce"].fillna(0)


        print("Columnas con valores nulos después de la limpieza:")
        print(df.isnull().sum())

        print("Agregar el tipado a las columnas de medallas:")
        df["Oro"] = df["Oro"].astype(int)
        df["Plata"] = df["Plata"].astype(int)
        df["Bronce"] = df["Bronce"].astype(int)

        print("Tipos de datos después de la limpieza:")
        print(df.dtypes)

        df = df.sort_values(by="Total", ascending=False)
        self.dataset_cleaned = df

        print("Dataset limpio:")
        print(self.dataset_cleaned.head())
        return self.dataset_cleaned
    
    def analysis(self):
        df = self.dataset_cleaned.copy()
        top_5 = df.head(5)

        print("Top 5 países con más medallas:")
        print(top_5[["Pais", "Total"]])

        print("Paises con mas de 10 medallas:")
        more_than_10 = df[df["Total"] > 10]
        print(more_than_10[["Pais", "Total"]])

        return {
            "top_5": top_5[["Pais", "Total"]],
            "more_than_10": more_than_10[["Pais", "Total"]]
        }
    
    def export_data(self,data,file_name="medallas_cleaned.csv"):
        dir = Path(__file__).parent 
        data.reset_index().to_csv(dir / f"../../result/{file_name}.csv", index=False)
        print("Dataset limpio exportado a medallas_cleaned.csv")

if __name__ == "__main__":
    processor = Processor()
    processor.get_data()
    processor.clean_data()
    result = processor.analysis()
    processor.export_data(result['top_5'], file_name="top_5_medallas.csv")
    processor.export_data(result['more_than_10'], file_name="medallas_mas_de_10.csv")