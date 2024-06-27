import crypt

hashed_password = crypt.crypt("secret", "MS")
print(hashed_password)