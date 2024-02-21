# Imports
import sys, json, configparser
sys.dont_write_bytecode = True

"""
    Config class does the following
    1. stores login credentials in json.
    2. installs necessary modules to the tool.
    3. create config file.
"""
class ConfigHanlder:
    def __init_(self):
        # Private Attributes
        self.__loginMail: str = None
        self.__loginPassword: str = None
        self.__isconfigured: bool = False

        # Public Attributes
        self.majorPythonVersion: int = None
        self.minorPythonVersion: int = None

    def setLoginMail(self, loginMail: str) -> None:
        self.__loginMail = loginMail

    def setLoginPassword(self, loginPassword: str) -> None:
        self.__loginPassword = loginPassword

    def getPythonVersion(self) -> list:
        self.majorPythonVersion = sys.implementation.version.major
        self.minorPythonVersion = sys.implementation.version.minor
        return [self.majorPythonVersion, self.minorPythonVersion]

    def writeCredentialJson(self) -> None:
        with open("config/.credentials.json", 'w+') as file:
            json.dump(
                {
                    "loginMail": self.__loginMail,
                    "loginPassword": self.__loginPassword
                }, file, indent=4
            )
        self.__isconfigured = True

    def clearCredentialJson(self) -> None:
        with open("config/.credentials.json", "w+") as file:
            json.dump(
                {
                    "loginMail": None,
                    "loginPassword": None
                }, file, indent=4
            )
        self.__isconfigured = False

    def writeConfigFile(self) -> None:
        if (self.__isconfigured == True):
            configparser.
