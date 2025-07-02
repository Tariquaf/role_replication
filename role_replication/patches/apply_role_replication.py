import os
import subprocess
import frappe

def apply_patch():
    app_path = frappe.get_app_path('frappe')
    patch_file = os.path.join(os.path.dirname(__file__), 'role_replication.patch')

    # Skip if already applied
    if subprocess.run(['git', 'apply', '--check', patch_file], cwd=app_path).returncode != 0:
        return

    subprocess.check_call(['git', 'apply', patch_file], cwd=app_path)
