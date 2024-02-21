# Importing built-in modules
import logging, getpass, os, sys, configparser
sys.dont_write_bytecode = True

# initiating logging
logger = logging.getLogger()
logging.basicConfig(
    filename = "logs/error.log",
    level = logging.ERROR,
    format = '%(asctime)s:%(levelname)s:%(name)s:%(message)s'
)

# Importing custom and 3rd-party module
try:
    from src.modules.ConfigHanlder import ConfigHanlder
except Exception as error:
    print("Error Occured!")
    print("Please check the log file for more details.")
    logger.exception(error)

def main():
    config: object = ConfigHanlder()
    print("AutoSeekOut Setup")
    print("Enter SeekOut Credentials")
    config.setLoginMail(input("Email address: "))
    password = getpass.getpass("Password: ")
    retyped = getpass.getpass("Retype the password: ")
    if (password == retyped):
        config.setLoginPassword(password)
        config.writeCredentialJson()
        print("Account Configured")

    # Debug
    # config.clearCredentialJson()

if __name__ == "__main__":
    main()
