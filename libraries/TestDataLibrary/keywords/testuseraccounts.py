import random
from robot.api.deco import keyword
from autocore.bases import LibraryBase, LibraryComponentBase
from libraries.TestDataLibrary.dto.testuserdetails import TestUserAccount
from pabot import PabotLib
import configparser


class TestUserAccounts(LibraryComponentBase):
    
    def __init__(self, library: LibraryBase):
        super().__init__(library)
        self.pabotlib = PabotLib()
        self.test_account_parser = configparser.ConfigParser()
    
    @keyword(tags=("TestUserAccount",))
    def get_user_test_account(self, _: TestUserAccount = None) -> TestUserAccount:
        """Get user test account details and return it as an object of `TestUserAccount`.

        Notes:
        - When running test using pabot, be sure to include the --variable=PABOT:true  and the path to the .dat file using --resourcefile.
        - As much as possible, use pabot when running test remotely. If only 1 process is needed, still use pabot and --processes to 1.
        - Always release the acquired test account using `Release User Test Account`. If account was acquired on the test setup or at the test itself,
         it must be released at the test teardown. If account was acquired during suite setup, it must be released at the suite teardown. So that
         other process won't be left waiting for a test account to use.
        """
        if self.globals.is_pabot_lib_used:
            self.pabotlib.acquire_value_set()
            username = self.pabotlib.get_value_from_set('username')
            password = self.pabotlib.get_value_from_set('password')
            fullname = self.pabotlib.get_value_from_set('fullname')
            position = self.pabotlib.get_value_from_set('position')
        elif self.globals.creds_dir is not None:
            self.test_account_parser.read(self.globals.creds_dir)
            sections = self.test_account_parser.sections()
            if len(sections) == 0:
                raise Exception(
                    f"Test accounts not available for [{self.globals.env}] environment.")

            section = random.choice(sections)

            username = self.test_account_parser.get(
                section.upper(), "username")
            password = self.test_account_parser.get(
                section.upper(), "password")
            fullname = self.test_account_parser.get(
                section.upper(), "fullname")
            position = self.test_account_parser.get(
                section.upper(), "position")
        else:
            try:
                import properties
                test_accounts = properties.LOCAL_TEST_ACCOUNT.get(self.globals.env)
                username = test_accounts.get("username")
                password = test_accounts.get("password")
                fullname = test_accounts.get("fullname")
                position = test_accounts.get("position")
            except Exception:
                raise Exception("Cannot get test account.")

        details = TestUserAccount(
            username=username, password=password, fullname=fullname, position=position)
        self.logger.debug(details)
        return details

    @keyword(tags=("TestUserAccount",))
    def release_user_test_account(self):
        """Releases the acquired test account.
        Only takes effect if pabotlib was used. See `Get User Test Account`.
        """
        if self.globals.is_pabot_lib_used:
            self.pabotlib.release_value_set()