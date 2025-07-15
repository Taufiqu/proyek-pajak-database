import os
import requests
from datetime import datetime
from decimal import Decimal

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
TABLE_MASUKAN = "ppn_masukan"
TABLE_KELUARAN = "ppn_keluaran"

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}

def save_invoice_data(data):
    jenis_pajak = data.get("klasifikasi") or "PPN_KELUARAN"
    table = TABLE_MASUKAN if jenis_pajak == "PPN_MASUKAN" else TABLE_KELUARAN

    # Validasi
    required_fields = [
        "no_faktur", "tanggal", "npwp_lawan_transaksi",
        "nama_lawan_transaksi", "keterangan", "dpp", "ppn"
    ]
    for field in required_fields:
        if not data.get(field):
            raise ValueError(f"Field '{field}' wajib diisi.")

    try:
        tanggal_obj = datetime.strptime(data["tanggal"], "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Format tanggal tidak valid. Gunakan YYYY-MM-DD.")

    bulan = data.get("bulan") or tanggal_obj.strftime("%B")

    # Cek duplikat berdasarkan no_faktur
    check_url = f"{SUPABASE_URL}/rest/v1/{table}?no_faktur=eq.{data['no_faktur']}"
    check_resp = requests.get(check_url, headers=HEADERS)
    if check_resp.status_code == 200 and check_resp.json():
        raise ValueError(f"Faktur '{data['no_faktur']}' sudah ada.")

    payload = {
        "bulan": bulan,
        "tanggal": tanggal_obj.isoformat(),
        "keterangan": data["keterangan"],
        "npwp_lawan_transaksi": data["npwp_lawan_transaksi"],
        "nama_lawan_transaksi": data["nama_lawan_transaksi"],
        "no_faktur": data["no_faktur"],
        "dpp": float(Decimal(str(data["dpp"]))),
        "ppn": float(Decimal(str(data["ppn"]))),
    }

    insert_url = f"{SUPABASE_URL}/rest/v1/{table}"
    response = requests.post(insert_url, headers=HEADERS, json=payload)

    if response.status_code >= 300:
        raise ValueError(f"Gagal menyimpan faktur: {response.text}")

    return response.json()
