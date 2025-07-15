import os
import requests
from flask import jsonify

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}

def delete_bukti_setor(id):
    table = "bukti_setor"
    url = f"{SUPABASE_URL}/rest/v1/{table}?id=eq.{id}"

    response = requests.delete(url, headers=HEADERS)

    if response.status_code == 204:
        return jsonify(message="Bukti setor berhasil dihapus!"), 200
    elif response.status_code == 404:
        return jsonify(message="Data bukti setor tidak ditemukan"), 404
    else:
        print(f"[❌ ERROR delete_bukti_setor] {response.text}")
        return jsonify(message="Gagal menghapus bukti setor."), 500
