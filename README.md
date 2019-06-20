# Botctolib

This is a script that you run with a cronjob every X hours that can check if a practician has available appointments and send you an email.

This is useful for practicians that have availabilities only when they post their new schedules, and disabled the "alert me" functionnality.

This will send you an email allowing you to book an appointment first !

You have to get the API link that gives availability by inspecting element on the practician's schedule, going to "network" tab and then changing the week. The link that appears with some Json should be pasted to follow the script's model.
