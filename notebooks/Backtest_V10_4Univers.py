# ---
# jupyter:
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Backtest_V10_4Univers — gabarit minimal
# Ce notebook est converti en .ipynb par Jupytext, puis exécuté par Papermill.

# %% tags=["parameters"]
EXECUTION_DAY = "first_business_day"  # ou "last_business_day"
DEPUIS = "2014-01"
JUSQUA = "2025-12"

# %%
print("Paramètres:", EXECUTION_DAY, DEPUIS, JUSQUA)

# %% [markdown]
# ## Calcul très minimal (fumée)
# Ici on mettra les imports réels, le chargement des données, etc.

# %%
import os, pandas as pd
os.makedirs("out", exist_ok=True)
pd.DataFrame({"ordre": ["EXEMPLE"], "montant": [800]}).to_csv(f"out/orders_{JUSQUA}.csv", index=False)
print("CSV d'ordres écrit:", f"out/orders_{JUSQUA}.csv")
