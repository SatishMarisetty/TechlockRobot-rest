from pyrogram import Client

from TechlockRobot import API_ID, API_HASH, TOKEN


session_name = TOKEN.split(":")[0]
client = Client("AQCHpHiYZ-V6UxDlI_3Yr2tKRjvQO0jn-QDHMLsztcNnNMbaVRsE_-Y7HQUl2fErgN-S3wxq-p4I1ofvVDcM_5DfKJNMVYyaYnYR2SoTXF9USnBIu7Xx7DFkaMVCq5XPefY8LvqfV9D9EiMWiycIrAn-gGZcp9gtyR5JabFy1e4ZMR67vHR3xS7_sQj5jDvdRumMHLPmj_P2FQQtzSUwWrPhfZ-W-9phpNSga7ntrBDNducjradgNy5-wjKs5GSfzrLo00VsUKI-_aua2uOVtZEgYSnqdoj324kSxMXYh2J-_a2TcrbX64iV8njfjQc57ONYSqXXVCL7nFy6hgCbOF1sZdlAaAA", API_ID, API_HASH)
run = client.run
