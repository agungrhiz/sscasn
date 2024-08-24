import requests
import pandas as pd


def fetch_data(kode_ref_pend):
    url = "https://api-sscasn.bkn.go.id/2024/portal/spf"
    headers = {"Origin": "https://sscasn.bkn.go.id"}
    offset = 0
    all_data = []

    while True:
        params = {"kode_ref_pend": kode_ref_pend, "offset": offset}
        response = requests.get(url, params=params, headers=headers)
        data = response.json().get("data", {}).get("data", [])
        all_data.extend(data)

        total_records = response.json().get("data", {}).get("meta", {}).get("total", 0)
        offset += 10

        if offset >= total_records:
            break

    return all_data


def save_to_excel(data, kode_ref_pend):
    df = pd.DataFrame(data)
    filename = f"data_formasi_{kode_ref_pend}.xlsx"

    # number formatting
    with pd.ExcelWriter(filename, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Data")
        worksheet = writer.sheets["Data"]

        for col in ["gaji_min", "gaji_max"]:
            if col in df.columns:
                col_idx = df.columns.get_loc(col) + 1
                for cell in worksheet.iter_cols(
                    min_col=col_idx,
                    max_col=col_idx,
                    min_row=2,
                    max_row=worksheet.max_row,
                ):
                    for item in cell:
                        try:
                            item.value = int(item.value)
                        except ValueError:
                            pass
                    item.number_format = "0"

        worksheet.auto_filter.ref = worksheet.dimensions

    print(f"Data saved to {filename}")


kode_ref_pend = 5109100  # modify to your kode_ref_pend
data = fetch_data(kode_ref_pend)
save_to_excel(data, kode_ref_pend)
