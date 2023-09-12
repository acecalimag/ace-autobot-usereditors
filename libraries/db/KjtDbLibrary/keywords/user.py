from libraries.db.KjtDbLibrary.dto.userdetails import UserDetails
from autocore.bases import DBLibraryComponent
from robot.api.deco import keyword

class Users(DBLibraryComponent):


    @keyword(tags=("kjt", "Users"))
    def query_user_details_from_user_table(self, uid: str, _: UserDetails = None) -> UserDetails:
        """Query the details of the user using the ``uid`` provided and return it as `UserDetails`"""
        query = """SELECT uid, username, name, isAdmin
                    FROM kjt.`user` 
                    where uid = %s;"""
        result = self.db.execute(query, (uid,))[0]
        details = UserDetails(
            uid=result['uid'], username=result['username'], name=result['name'], isAdmin=result['isAdmin']
        )
        self.logger.pretty_debug(data=details)
        return details
        