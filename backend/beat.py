from backend.db import execute_query, fetch_all

# ═══════════════════════════════════════════════════════════════════════════
# BEATS
# ═══════════════════════════════════════════════════════════════════════════

def add_beat(beat_name, area, assigned_to):
    q = "INSERT INTO Beat (BeatName, Area, AssignedTo) VALUES (%s,%s,%s)"
    return execute_query(q, (beat_name, area, assigned_to if assigned_to else None))

def get_all_beats():
    q = """SELECT b.BeatID, b.BeatName, b.Area, s.Name AS AssignedOfficer
           FROM Beat b
           LEFT JOIN Staff s ON b.AssignedTo = s.StaffID
           ORDER BY b.BeatName"""
    return fetch_all(q)

def delete_beat(beat_id):
    return execute_query("DELETE FROM Beat WHERE BeatID = %s", (beat_id,))

# ═══════════════════════════════════════════════════════════════════════════
# BEAT BOOK (Register 9)
# ═══════════════════════════════════════════════════════════════════════════

def add_beat_record(beat_id, staff_id, date, activity_details, remarks):
    q = """INSERT INTO BeatBook (BeatID, StaffID, Date, ActivityDetails, Remarks)
           VALUES (%s,%s,%s,%s,%s)"""
    return execute_query(q, (beat_id, staff_id, date, activity_details, remarks))

def get_all_beat_records():
    q = """SELECT bb.BeatRecordID, b.BeatName, s.Name AS Officer,
                  bb.Date, bb.ActivityDetails, bb.Remarks
           FROM BeatBook bb
           JOIN Beat b  ON bb.BeatID  = b.BeatID
           JOIN Staff s ON bb.StaffID = s.StaffID
           ORDER BY bb.Date DESC"""
    return fetch_all(q)

def delete_beat_record(record_id):
    return execute_query("DELETE FROM BeatBook WHERE BeatRecordID = %s", (record_id,))