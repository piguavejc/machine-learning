import pandas as pd
from pathlib import Path 


class Processor:
    def __init__(self):
        self.dataset = None
        self.dataset_store_one = None
        self.dataset_store_two = None
        self.dataset_cleaned = None

    def get_data(self):
        dir = Path(__file__).parent 
        print("-------",dir)
        self.dataset_store_one = pd.read_csv(dir / "../../dataset/Datos_Ventas_Tienda.csv")
        self.dataset_store_two = pd.read_csv(dir / "../../dataset/Datos_Ventas_Tienda2.csv")

        self.dataset = pd.concat([self.dataset_store_one, self.dataset_store_two], ignore_index=True)
        rows = len(self.dataset) 
        print("Rows:", rows)

    def clean_data(self):
        df = self.dataset.copy()

        print("Columnas con valores nulos:")
        print(df.isnull().sum())

        df["Fecha"] = pd.to_datetime(df["Fecha"], errors="coerce")
        df["Cantidad"] = df["Cantidad"].astype(int)
        df["Precio Unitario"] = df["Precio Unitario"].astype(float)
        df["Total Venta"] = df["Total Venta"].astype(float)

        df = df.sort_values(by="Total Venta", ascending=False)
        self.dataset_cleaned = df
        return self.dataset_cleaned
    
    def analysis(self):
        df = self.dataset_cleaned.copy()

        print("\n Cual es el producto mas vendido:")
        most_sold_product = df.groupby("Producto")["Cantidad"].sum().sort_values(ascending=False).head(1)
        print(most_sold_product)

        print("\n cual es el mes con mas ventas:")
        moths = []

        for f in df["Fecha"]:
            month = f.month
            moths.append(month)

        df["Mes"] = moths
        df = df.sort_values(by=["Total Venta", "Mes"], ascending=False)

        self.dataset_cleaned = df

        month_with_most_sales = df.groupby("Mes")["Total Venta"].sum().sort_values(ascending=False).head(1)
        print(month_with_most_sales)

        most_sold_product = df.groupby("Producto")["Total Venta"].sum().sort_values(ascending=False)

        return {
            "most_sold_product": most_sold_product,
            "month_with_most_sales": month_with_most_sales, 
            "sales_by_product": most_sold_product
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
    processor.export_data(result['most_sold_product'], file_name="most_sold_product.csv")
    processor.export_data(result['month_with_most_sales'], file_name="month_with_most_sales.csv")
    processor.export_data(result['sales_by_product'], file_name="sales_by_product.csv")
    print("Proceso completado")