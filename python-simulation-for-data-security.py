# ============================================
# Nanotechnology Data Security Simulation
# ============================================

# Import required libraries
from cryptography.fernet import Fernet
import datetime
import os


# --------------------------------------------
# Step 1: Generate Nano Sensor Data
# --------------------------------------------
def generate_sensor_data():
    """
    Simulate nano sensor data generation
    """
    temperature = 36.5  # Example value (°C)
    pressure = 1.02     # Example value (atm)
    
    data = f"Temp:{temperature}, Pressure:{pressure}, Time:{datetime.datetime.now()}"
    
    print("\n[+] Sensor Data Generated:")
    print(data)
    
    return data.encode()  # Convert to bytes


# --------------------------------------------
# Step 2: Generate Encryption Key
# --------------------------------------------
def generate_key():
    """
    Generate and save encryption key
    """
    key = Fernet.generate_key()
    
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    
    print("\n[+] New Encryption Key Generated and Saved!")
    return key


# --------------------------------------------
# Step 3: Load Existing Key OR Generate New One
# --------------------------------------------
def load_or_generate_key():
    """
    Load existing key if available, otherwise generate a new one
    """
    if os.path.exists("secret.key"):
        print("\n[+] Loading Existing Key...")
        return open("secret.key", "rb").read()
    else:
        print("\n[+] No Key Found! Generating New Key...")
        return generate_key()


# --------------------------------------------
# Step 4: Encrypt Data
# --------------------------------------------
def encrypt_data(data, key):
    """
    Encrypt sensor data using Fernet (AES-based encryption)
    """
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data)
    
    print("\n[+] Data Encrypted Successfully!")
    print(encrypted_data)
    
    return encrypted_data


# --------------------------------------------
# Step 5: Store Encrypted Data Securely
# --------------------------------------------
def store_data(encrypted_data):
    """
    Store encrypted data into a binary file
    """
    with open("secure_data.bin", "wb") as file:
        file.write(encrypted_data)
    
    print("\n[+] Encrypted Data Stored Securely!")


# --------------------------------------------
# Step 6: Decrypt Data (Verification)
# --------------------------------------------
def decrypt_data(key):
    """
    Decrypt stored data to verify integrity
    """
    try:
        cipher = Fernet(key)
        
        with open("secure_data.bin", "rb") as file:
            encrypted_data = file.read()
        
        decrypted_data = cipher.decrypt(encrypted_data)
        
        print("\n[+] Data Decrypted Successfully!")
        print(decrypted_data.decode())

    except Exception as e:
        print("\n[!] Decryption Failed:", str(e))


# --------------------------------------------
# Main Program Execution
# --------------------------------------------
if __name__ == "__main__":
    
    print("===== Nanotechnology Data Security Simulation =====")
    
    # Step 1: Generate Data
    sensor_data = generate_sensor_data()
    
    # Step 2: Load or Generate Key
    key = load_or_generate_key()
    
    # Step 3: Encrypt Data
    encrypted = encrypt_data(sensor_data, key)
    
    # Step 4: Store Data Securely
    store_data(encrypted)
    
    # Step 5: Decrypt Data (Verification)
    decrypt_data(key)

    print("\n===== Process Completed Successfully =====")