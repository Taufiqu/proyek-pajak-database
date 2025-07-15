import os
import requests
from flask import jsonify

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
}

def get_history():
    def fetch_data(jenis, table):
        url = f"{SUPABASE_URL}/rest/v1/{table}?select=id,no_faktur,nama_lawan_transaksi,tanggal"
        resp = requests.get(url, headers=HEADERS)

        if resp.status_code != 200:
            raise ValueError(f"Gagal fetch {jenis}: {resp.text}")

        return [
            {
                "id": row["id"],
                "jenis": jenis,
                "no_faktur": row["no_faktur"],
                "nama_lawan_transaksi": row["nama_lawan_transaksi"],
                "tanggal": row["tanggal"],
            }
            for row in resp.json()
        ]

    try:
        masukan = fetch_data("masukan", "ppn_masukan")
        keluaran = fetch_data("keluaran", "ppn_keluaran")
        return jsonify(masukan + keluaran), 200
    except Exception as e:
        print(f"[❌ ERROR /api/history] {e}")
        return jsonify(error=str(e)), 500
