# 🧬 Role Replication (Frappe Custom App)

A lightweight Frappe app that cleanly backports the **Role Replication** functionality from [Frappe PR #26845](https://github.com/frappe/frappe/pull/26845) into **Frappe version 15** without modifying core framework code. Ideal for production environments needing latest features and long-term maintainability.

---

## 📌 Compatibility

- ✅ Designed for **Frappe v15**
- 🚫 Not tested on older versions
- 🛡️ Patch is idempotent — skips itself if already merged upstream

---

## ✨ Features

- Creates a new doctype **Role Replication**
- Backports upstream functionality with minimal overhead
- Ships with `.patch` and patch applier logic
- Clean, production-safe — core files untouched
- Auto-applies at migration, then gracefully exits if patch is no longer needed

---

## 🚀 Installation (Frappe v15)

> Replace `mysite` with your actual site name

1. **Clone the app into your bench:**
   ```bash
   cd ~/frappe-bench/apps
   git clone https://github.com/Tariquaf/role_replication.git

2. **Install the app on your site:**
   ```bash
   cd ~/frappe-bench
   bench --site mysite install-app role_replication

4. **Run the patch and apply migration:**
   ```bash
   bench update --patch
   bench migrate --site mysite

## 🧠 How It Works
This app uses a simple but powerful after_migrate hook to apply the upstream role replication patch:
- The patch from Frappe commit f06f30b64f lives at role_replication/patches/role_replication.patch
- The hook runner in role_replication/patches/apply_role_replication.py checks if the patch applies cleanly, and applies it to apps/frappe
- If the patch is already present (e.g. merged in upstream), the hook gracefully skips
No core repo pollution. No Git cherry-pick gymnastics. Just results.

