from backend.db import execute_query, fetch_all

# ═══════════════════════════════════════════════════════════════════════════
# GOVERNMENT ASSETS (Register 16 Part B)
# ═══════════════════════════════════════════════════════════════════════════

def add_asset(property_type, description, quantity, issue_date, condition):
    q = """INSERT INTO GovtAssets (PropertyType, Description, Quantity, IssueDate, Condition)
           VALUES (%s,%s,%s,%s,%s)"""
    return execute_query(q, (property_type, description, quantity, issue_date, condition))

def get_all_assets():
    return fetch_all("SELECT * FROM GovtAssets ORDER BY PropertyType")

def delete_asset(property_id):
    return execute_query("DELETE FROM GovtAssets WHERE PropertyID = %s", (property_id,))

# ═══════════════════════════════════════════════════════════════════════════
# RECOVERED PROPERTY (Register 19)
# ═══════════════════════════════════════════════════════════════════════════

def add_recovered(fir_id, item_name, quantity, recovery_date, recovered_from, status):
    q = """INSERT INTO RecoveredProperty (FIRID, ItemName, Quantity, RecoveryDate,
                                          RecoveredFrom, Status)
           VALUES (%s,%s,%s,%s,%s,%s)"""
    return execute_query(q, (fir_id, item_name, quantity, recovery_date,
                              recovered_from, status))

def get_all_recovered():
    q = """SELECT r.RecoveryID, f.FIRNumber, r.ItemName, r.Quantity,
                  r.RecoveryDate, r.RecoveredFrom, r.Status
           FROM RecoveredProperty r
           JOIN FIR f ON r.FIRID = f.FIRID
           ORDER BY r.RecoveryDate DESC"""
    return fetch_all(q)

def delete_recovered(recovery_id):
    return execute_query("DELETE FROM RecoveredProperty WHERE RecoveryID = %s", (recovery_id,))