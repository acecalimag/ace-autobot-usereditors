
from robot.api.deco import keyword
from autocore.Database import Database
from datetime import datetime
import arrow

class AdherenceAdjustmentDB:

    def __init__(self, db: Database):
        self.__db = db

    @keyword
    def get_user_details_headers(self, username: str):
        """ TODO: Create a database query to retrieve the Agent's UID."""
        query = "SELECT u.username, um.position, ul.code, ul.location, um.workforceid, ut.name as team FROM kjt.usermeta AS um JOIN kjt.user AS u ON um.uid = u.uid JOIN kjt.userlocation AS ul ON um.lid = ul.lid JOIN kjt.userteam AS ut ON um.teamId = ut.utid  WHERE u.username = %s;"
         
        result = self.__db.execute(query, (username,))
        if result and len(result) > 0:
            row = result[0]
            return {
                'username': row['username'].upper(),
                'position': row['position'].upper(),
                'location_code': row['code'].upper(),
                'location': row['location'], 
                'workforceid': row['workforceid'],
                'team': row['team']
            }
        else:
            return None
    
    @keyword
    def get_user_details(self, username: str):
        """ TODO: Create a database query to retrieve the Agent's UID."""
        query = "SELECT u.username, um.position, ul.code, ul.location, um.workforceid, ut.name as team FROM kjt.usermeta AS um JOIN kjt.user AS u ON um.uid = u.uid JOIN kjt.userlocation AS ul ON um.lid = ul.lid JOIN kjt.userteam AS ut ON um.teamId = ut.utid  WHERE u.username = %s;"
         
        result = self.__db.execute(query, (username,))
        if result and len(result) > 0:
            row = result[0]
            return {
                'username': row['username'],
                'position': row['position'],
                'location_code': row['code'],
                'location': row['location'], 
                'workforceid': row['workforceid'],
                'team': row['team']
            }
        else:
            return None
        

    @keyword
    def get_dispute_details_db(self, udid: str):
        """ TODO: Create a database query to retrieve the dispute details"""
        query = "SELECT u.username, u.name, ud.status, ud.udid, ud.requestedstarttime, ud.requestedendtime, ud.currentstarttime, ud.currentendtime, ud.workhours, ud.reason, ud.createTime, ul.location, ut.name as Team, ud.currentactivitycode, ud.requestedactivitycode, ud.payhours, ud.reviewcomment, ud.internalnotes, ud.reviewedby, ud.reviewtime, ud.confirmtime FROM kjt.usermeta AS um JOIN kjt.user AS u ON um.uid = u.uid JOIN kjt.userlocation AS ul ON um.lid = ul.lid JOIN kjt.userteam AS ut ON um.teamId = ut.utid JOIN wfm.userdispute AS ud ON u.username = ud.username where ud.udid = %s;"
         
        result = self.__db.execute(query, (udid,))
        if result and len(result) > 0:
            row = result[0]
            # Full Name
            full_name = f"{row['name']} ({row['username']})"

            # # Current Time Range:
            # ctr_time_range = ""
            # if row['currentstarttime'] and row['currentendtime']:
            #     ctr_formatted_starttime = row['currentstarttime'].strftime("%b %d, %Y %I:%M %p")
            #     ctr_formatted_endtime = row['currentendtime'].strftime("%b %d, %Y %I:%M %p")
            #     ctr_time_range = f"{ctr_formatted_starttime} - {ctr_formatted_endtime}"


            # # Current Time Range:
            # ctr_time_range = ""
            # if row['currentstarttime'] and row['currentendtime']:
            #     ctr_formatted_starttime = row['currentstarttime'].strftime("%b %d, %Y %I:%M %p")
            #     ctr_formatted_endtime = row['currentendtime'].strftime("%b %d, %Y %I:%M %p")
                
            #     # Remove leading zero from hour if present
            #     ctr_formatted_starttime = ctr_formatted_starttime.replace(" 0", " ")
            #     ctr_formatted_endtime = ctr_formatted_endtime.replace(" 0", " ")
                
            #     ctr_time_range = f"{ctr_formatted_starttime} - {ctr_formatted_endtime}"
            

            # Current Time Range:
            ctr_time_range = ""
            if row['currentstarttime'] and row['currentendtime']:
                start_time = arrow.get(row['currentstarttime'])
                end_time = arrow.get(row['currentendtime'])

                ctr_formatted_starttime = start_time.format("MMM DD, YYYY h:mm A")
                ctr_formatted_endtime = end_time.format("MMM DD, YYYY h:mm A")

                ctr_time_range = f"{ctr_formatted_starttime} - {ctr_formatted_endtime}"



            # Requested Time Range:
            rtr_time_range = ""
            if row['requestedstarttime'] and row['requestedendtime']:
                start_time = arrow.get(row['requestedstarttime'])
                end_time = arrow.get(row['requestedendtime'])

                rtr_formatted_starttime = start_time.format("MMM DD, YYYY h:mm A")
                rtr_formatted_endtime = end_time.format("MMM DD, YYYY h:mm A")

                rtr_time_range = f"{rtr_formatted_starttime} - {rtr_formatted_endtime}"

            # Create Time
            ct_time = ""
            if row['createTime']:
                ct_time = arrow.get(row['createTime']).format("MMM DD, YYYY h:mm A")

            # Review Time
            review_time = ""
            if row['reviewtime']:
                review_time = arrow.get(row['reviewtime']).format("MMM DD, YYYY h:mm A")

            # Confirm Time
            confirm_time = ""
            if row['confirmtime']:
                confirm_time = arrow.get(row['confirmtime']).format("MMM DD, YYYY h:mm A")
            
            # Work Hours
            work_hours = row['workhours']
            if work_hours is None:
                work_hours = ''
            
            # Reason
            reason = row['reason']
            if reason is None:
                reason = ''
            
            # Location
            location = row['location']
            if location is None:
                location = ''
            
            # Current Activity
            currentactivity = row['currentactivitycode']
            if currentactivity is None:
                currentactivity = ''

            # Requested Activity
            requestedactivity = row['requestedactivitycode']
            if requestedactivity is None:
                requestedactivity = ''

            # Comment
            comment = row['reviewcomment']
            if comment is None:
                comment = ''

            # Internal Notes
            internalnotes = row['internalnotes']
            if internalnotes is None:
                internalnotes = ''

            # Reviewed By
            reviewedby = row['reviewedby']
            if reviewedby is None:
                reviewedby = ''

            # Team
            team = row['Team']
            if team is None:
                team = ''

            # Status
            status = row['status']
            if status is None:
                status = ''
            
            # Pay Hours
            pay_hours = row['payhours']
            if pay_hours is None:
                pay_hours = ''
            

            return {
                'Full Name': full_name,
                'Status': status.capitalize(),
                'Current Time Range': ctr_time_range,
                'Requested Time Range': rtr_time_range, 
                'Work Hours': work_hours,
                'Reason': reason,
                'Created At': ct_time,
                'Location': location,
                'Team': team,
                'Current Activity': currentactivity,
                'Requested Activity': requestedactivity,
                'Pay Hours': pay_hours,
                'Comment': comment,
                'Internal Notes': internalnotes,
                'Reviewed By': reviewedby,
                'Reviewed At': review_time,
                'Confirmed At': confirm_time,
                'UDID': row['udid']
            }
        else:
            return {}
            
        
        








    @keyword
    def get_user_team_db(self, tname: str):
        """ TODO: Create a database query to retrieve the User Team Details."""
        query = "SELECT ut.name as Team_Name, ut.description as Team_Description, u.name as Team_Lead, ul.code as Team_Location, ut.type as Team_Type, ut.status as Team_Status, ut.updateTime as Last_Updated FROM kjt.userteam AS ut JOIN kjt.user AS u ON ut.teamLead = u.uid JOIN kjt.userlocation AS ul ON ut.location = ul.lid WHERE ut.name = %s;"
        
        result = self.__db.execute(query, (tname,))
        if result and len(result) > 0:
            row = result[0]

            # Convert and format the Team Type
            team_type = row['Team_Type'].lower()
            formatted_team_type = team_type.replace('nonoperational', 'Non-Operational').title()

            return {
                'Team Name': row['Team_Name'],
                'Team Description': row['Team_Description'],
                'Team Lead': row['Team_Lead'],
                'Team Location': row['Team_Location'],
                'Team Type': formatted_team_type,
                'Team Status': row['Team_Status'].capitalize(),
                'Last Updated': row['Last_Updated']
            }
        else:
            return None
        


 



# QA_DB_CREDS = {
#     "host": "qa-db.letsdochinese.com",
#     "user": "qaauto",
#     "password": "8bbz9k",
#     "port": "3306"
# }
# db = Database(database="kjt", host=QA_DB_CREDS['host'], user=QA_DB_CREDS['user'], password=QA_DB_CREDS['password'],port=QA_DB_CREDS['port'])       
# t = Authority(db=db)
# t.query_name_from_authority_table(aid="df726970-c211-11eb-893a-0afcf0c3c7ed")