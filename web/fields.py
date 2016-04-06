import flask_wtf
from widgets import * #http://wtforms.readthedocs.org/en/latest/fields.html

class BreachField(CheckboxButtonField):
    col_md = 2
    col_sm = 4
    col_xs = 12

class Form(flask_wtf.Form):
    match_id = IntegerField('Match #', buttons=False)
    team_id = IntegerField('Team #', buttons=False)
    #Auton Section
    auton_balls = IntegerField('Auton balls possessed',buttons=False)
    auton_high = RadioField("Auton High Goal", choices=[('0','N/A'),('1','Missed'),('2','Scored')])
    auton_low = RadioField("Auton Low Goal", choices=[('0','N/A'),('1','Missed'),('2','Scored')])
    #Teleop Section
    high = IntegerField('Teleop High Goals:')
    high_miss = IntegerField('High Goals Missed:')
    low = IntegerField('Teleop Low Goals:')

    low_speed = RadioField('Teleop Low Goal Speed:', choices=[('-1', 'N/A'),('0','Slow'),('1','Medium'),('2','Fast')])
    
    fouls = IntegerField('Fouls:')
    tfouls = IntegerField('Technical Fouls:')
    defense = RadioField('Defense:',choices=[('-1','N/A'),('0','Bad'),('1','Mediocre'),('2','Good')])

    catch_truss = CheckboxButtonField('Truss')
    catch_ranged = CheckboxButtonField('Ranged')
    catch_human = CheckboxButtonField('From Human')
    result = RadioField("Match Result:", choices=[('2','Win'),('0', 'Loss'),('1', 'Tie')])
    comments = TextAreaField('', col_lg=12)
