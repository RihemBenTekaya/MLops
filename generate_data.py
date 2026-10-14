from pathlib import Path

import numpy as np
import pandas as pd


def main() -> None:
    rng = np.random.default_rng(42)
    n = 500

    data = pd.DataFrame(
        {
            "age": rng.integers(18, 70, size=n),
            "salaire": rng.integers(1200, 8000, size=n),
            "abonnement": rng.choice(["Basique", "Standard", "Premium"], size=n),
            "anciennete": rng.integers(0, 15, size=n),
            "consommation": rng.integers(0, 100, size=n),
        }
    )

    data["churn"] = (
        (data["consommation"] < 30) & (data["anciennete"] < 2)
    ).astype(int)

    output_path = Path(__file__).resolve().parent / "churn_data.csv"
    data.to_csv(output_path, index=False)

    print(data.head())
    print(f"Taux de churn : {data['churn'].mean():.1%}")


if __name__ == "__main__":
    main()